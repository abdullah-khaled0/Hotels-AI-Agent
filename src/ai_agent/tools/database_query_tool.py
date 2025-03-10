from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from website.models.database import db
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

class DatabaseQueryToolInput(BaseModel):
    """Input schema for the Database Query Tool."""
    table_name: str = Field(..., description="Name of the table to interact with (e.g., 'Reservations', 'Rooms')")
    operation_type: str = Field(..., description="Type of operation to execute ('find', 'create', 'update', 'delete')")
    filter_key: str = Field(None, description="Column name to filter on (used for 'find', 'update', 'delete')")
    filter_value: str = Field(None, description="Value to match for the filter_key")
    data: dict = Field(None, description="Data for 'create' or 'update' operations as a dictionary")

class DatabaseQueryTool(BaseTool):
    name: str = "Database Query Tool"
    description: str = (
        "Handles database operations across all tables. "
        "Supports finding, creating, updating, and deleting records."
    )
    args_schema: Type[BaseModel] = DatabaseQueryToolInput

    def _execute_query(self, sql_query: str, params: dict) -> str:
        """Executes SQL queries and returns the result."""
        try:
            with db.engine.connect() as connection:
                # Begin a transaction
                with connection.begin():
                    result = connection.execute(text(sql_query), params)
                    if sql_query.strip().lower().startswith("select"):
                        rows = result.fetchall()
                        return "\n".join(str(row) for row in rows) if rows else "No records found."
                    return "Operation completed successfully."
        except SQLAlchemyError as e:
            return f"Query execution error: {str(e)}"

    def _run(
        self,
        table_name: str,
        operation_type: str,
        filter_key: str = None,
        filter_value: str = None,
        data: dict = None,
    ) -> str:
        """Executes the specified database operation."""
        operation_type = operation_type.lower()
        # Input validation
        if operation_type == "find" and (not filter_key or not filter_value):
            return "Error: 'filter_key' and 'filter_value' are required for 'find' operation."
        elif operation_type == "create" and not data:
            return "Error: 'data' is required for 'create' operation."
        elif operation_type == "update" and (not filter_key or not filter_value or not data):
            return "Error: 'filter_key', 'filter_value', and 'data' are required for 'update' operation."
        elif operation_type == "delete" and (not filter_key or not filter_value):
            return "Error: 'filter_key' and 'filter_value' are required for 'delete' operation."
        elif operation_type not in {"find", "create", "update", "delete"}:
            return "Error: Invalid operation type. Use 'find', 'create', 'update', or 'delete'."

        # Execute the operation
        try:
            if operation_type == "find":
                sql_query = f"SELECT * FROM {table_name} WHERE {filter_key} = :filter_value;"
                return self._execute_query(sql_query, {"filter_value": filter_value})

            elif operation_type == "create":
                columns = ", ".join(data.keys())
                values = ", ".join(f":{key}" for key in data.keys())
                sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values}) RETURNING *;"
                result = self._execute_query(sql_query, data)
                if "Query execution error" in result:
                    return result
                return f"Record created: {result}"

            elif operation_type == "update":
                updates = ", ".join(f"{key} = :{key}" for key in data.keys())
                sql_query = f"UPDATE {table_name} SET {updates} WHERE {filter_key} = :filter_value RETURNING *;"
                return self._execute_query(sql_query, {**data, "filter_value": filter_value})

            elif operation_type == "delete":
                sql_query = f"DELETE FROM {table_name} WHERE {filter_key} = :filter_value RETURNING *;"
                return self._execute_query(sql_query, {"filter_value": filter_value})

        except Exception as e:
            return f"Database operation error: {str(e)}"

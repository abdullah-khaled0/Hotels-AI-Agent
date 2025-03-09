from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from website.models.database import db
from sqlalchemy import text  # Import text for safe SQL query execution

# Input schema for SQLQueryExecutorTool
class SQLQueryExecutorToolInput(BaseModel):
    """Input schema for SQLQueryExecutorTool."""
    sql_query: str = Field(..., description="The SQL query to execute.")

class SQLQueryExecutorTool(BaseTool):
    name: str = "SQL Query Executor"
    description: str = (
        "This tool executes SQL queries on the PostgreSQL database using Flask-SQLAlchemy. "
        "It takes a raw SQL query as input and returns the results."
    )
    args_schema: Type[BaseModel] = SQLQueryExecutorToolInput

    def _run(self, sql_query: str) -> str:
        try:
            # Use a connection to execute the SQL query
            with db.engine.connect() as connection:
                # Use text() to safely execute the SQL query
                result = connection.execute(text(sql_query))
                # Fetch and format the results
                rows = result.fetchall()
                if not rows:
                    return "No results found."
                # Convert rows to a readable string
                return "\n".join([str(row) for row in rows])
        except Exception as e:
            # Handle any errors that occur during the query execution
            return f"An error occurred while executing the query: {e}"
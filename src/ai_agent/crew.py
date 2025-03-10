import os
from crewai import LLM, Agent, Crew, Process, Task
from ai_agent.tools.database_query_tool import DatabaseQueryTool
from ai_agent.tools.sql_query_executor_tool import SQLQueryExecutorTool

from crewai.memory import ShortTermMemory
from crewai.memory.storage.rag_storage import RAGStorage



google_api_key = os.getenv("GEMINI_API_KEY")
llm = LLM(model="gemini/gemini-2.0-flash", temperature=0, api_key=google_api_key)

storage_path = os.getenv("CREWAI_STORAGE_DIR")

# Define Database Agent
sql_agent = Agent(
    role="SQL Agent",
    goal="Handle database-related queries and tasks across all tables, including calculating totals for reservations.",
    backstory=(
        "You are an expert in managing and querying relational databases. "
        "You can find, create, update, and delete records in tables such as Hotels, Rooms, Guests, Reservations, Staff, Payments, Services, and RoomServices. "
        "You are also skilled at calculating totals, such as reservation prices, by fetching necessary data like room prices."
    ),
    llm=llm,
    tools=[DatabaseQueryTool(), SQLQueryExecutorTool()],
    verbose=True
)

# Define Database Task with enhanced instructions
sql_task = Task(
    description=(
        "Handle database-related queries and tasks based on the user's request: {query}. "
        "Use the provided database schema:\n\n{schema}\n\n"
        "User my guest_id if needed:1"
        "to ensure the query is accurate and valid. "
        "Specify the table name, operation type ('find', 'create', 'update', 'delete'), and required parameters. "
        "Use the 'Database Query Tool' to execute operations like inserting, updating, or deleting records. "
        "Use the 'SQL Query Executor Tool' to run raw SQL queries when additional data retrieval is needed, such as fetching room prices. "
        "Check for missing parameters and report them clearly if any are absent. "
        "\n\n"
        "For 'create' operations involving reservations:\n"
        "1. If the query involves creating a reservation (e.g., 'Create a reservation with guest_id 456, room_id 201, date 2025-03-15'), "
        "   use the 'SQL Query Executor Tool' to fetch the room price from the 'Rooms' table using the provided room_id. "
        "2. Calculate the total price based on the room price (assume a single-night stay unless duration is specified). "
        "3. Use the 'Database Query Tool' to insert the reservation into the 'Reservations' table, including the calculated total_price. "
        "   Ensure the data includes at least: guest_id, room_id, date, and total_price. "
        "Dont add the ids of Tables in the Final Answer."
        "Return the results in a user-friendly format, including confirmation of the insertion and the total price."
        "Respond in a pro style and tone."
    ),
    expected_output=(
        "Pro answer based on the query results, or a message listing missing parameters."
    ),
    agent=sql_agent,
)

# Define Crew
crew = Crew(
    agents=[sql_agent],
    tasks=[sql_task],
    verbose=True,
    process=Process.sequential,
    # memory = True,
    # embedder= {
    #             "provider": "google",
    #             "config": {
    #                 "api_key": google_api_key,
    #                 "model": 'models/text-embedding-004'
    #             }
    #             },
    # short_term_memory = ShortTermMemory(
    #     storage = RAGStorage(
    #             embedder_config= {
    #                         "provider": "google",
    #                         "config": {
    #                             "api_key": google_api_key,
    #                             "model": 'models/text-embedding-004'
    #                         }
    #                 },
    #             type="short_term",
    #             path="{storage_path}/memory.db".format(storage_path=storage_path)
    #         )
    #     ),
)


def run(input):
    # Validate input for required fields and check for missing parameters
    required_fields = ["query", "schema"]
    missing_params = [field for field in required_fields if field not in input or not input[field]]
    
    if missing_params:
        return f"Error: Missing required parameters: {', '.join(missing_params)}. Please provide all necessary inputs."
    
    # Kick off the crew with the validated input
    result = crew.kickoff(inputs=input)
    return result
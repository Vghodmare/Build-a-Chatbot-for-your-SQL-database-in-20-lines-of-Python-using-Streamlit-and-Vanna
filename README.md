# Build-a-Chatbot-for-your-SQL-database-in-20-lines-of-Python-using-Streamlit-and-Vanna

Overview
This guide demonstrates how to create a simple yet powerful chatbot using Streamlit and Vanna to interact with an SQLite database. The chatbot can convert natural language questions into SQL queries, execute them, and display the results both as a table and a chart. The entire setup is achieved in just 20 lines of Python code.

1. How It Works
Importing Required Libraries:

Streamlit: Provides the user interface for the chatbot.

Vanna: Uses an LLM (Large Language Model) to convert natural language questions into SQL queries.

2. Setting Up Vanna:

API Key: Set your Vanna API key.

Model Selection: Set the Vanna Retrieval Augmentation Model to "chinook," which includes metadata for the SQLite database.

Database Connection: Connect to the SQLite database using the provided URL.

3. User Interaction:

Text Input: A text box allows users to input their natural language questions.

SQL Generation: Vanna generates the corresponding SQL query based on the user's question.

Query Execution: The generated SQL query is executed against the database.

Result Display: The results are displayed as a table and a chart using Streamlit.

import streamlit as st
from functools import lru_cache
from vanna.remote import VannaDefault

# Initialize VannaDefault outside of cached functions
vn = None

@st.cache_resource
def setup_vanna():
    global vn
    # Initialize VannaDefault with API key and model name
    api_key = "11a6e155c86e446d8e40fab49867fcd9"
    vanna_model_name = "Chinook"
    vn = VannaDefault(model=vanna_model_name, api_key=api_key)
    
    # Connect to the SQLite database
    try:
        vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")
        st.write("Connected to the SQLite database successfully.")
    except Exception as e:
        st.error(f"Failed to connect to the SQLite database: {e}")
        st.stop()  # Stop execution if connection fails
    
    return vn

@lru_cache(maxsize=None)
def generate_questions_cached():
    global vn
    if vn is None:
        vn = setup_vanna()  # Ensure vn is initialized if not already

    try:
        training_data = vn.get_training_data()
        st.write("Training data:", training_data)  # Log training_data
        if training_data is None:
            st.error("Training data is None. Please check the API response.")
            return []
        if not hasattr(training_data, "questions"):
            st.error("Training data does not have 'questions' attribute.")
            st.write("Training data contents:", training_data)
            return []
        st.write("Training data retrieved successfully.")
        return training_data.questions
    except Exception as e:
        st.error(f"An error occurred while retrieving training data: {e}")
        return []

@lru_cache(maxsize=None)
def generate_sql_cached(question: str):
    global vn
    if vn is None:
        vn = setup_vanna()  # Ensure vn is initialized if not already

    try:
        sql = vn.generate_sql(question=question, allow_llm_to_see_data=True)
        if sql is None:
            st.error("Failed to generate SQL for the question.")
            st.write("Question asked:", question)
        return sql
    except Exception as e:
        st.error(f"An error occurred while generating SQL: {e}")
        return None

@lru_cache(maxsize=None)
def is_sql_valid_cached(sql: str):
    global vn
    if vn is None:
        vn = setup_vanna()  # Ensure vn is initialized if not already

    try:
        return vn.is_sql_valid(sql=sql)
    except Exception as e:
        st.error(f"An error occurred while checking SQL validity: {e}")
        return False

@lru_cache(maxsize=None)
def run_sql_cached(sql: str):
    global vn
    if vn is None:
        vn = setup_vanna()  # Ensure vn is initialized if not already

    try:
        return vn.run_sql(sql=sql)
    except Exception as e:
        st.error(f"An error occurred while running SQL: {e}")
        return None

@lru_cache(maxsize=None)
def should_generate_chart_cached(question, sql, df):
    global vn
    if vn is None:
        vn = setup_vanna()  # Ensure vn is initialized if not already

    try:
        return vn.should_generate_chart(df=df)
    except Exception as e:
        st.error(f"An error occurred while determining if a chart should be generated: {e}")
        return False

@lru_cache(maxsize=None)
def generate_plotly_code_cached(question, sql, df):
    global vn
    if vn is None:
        vn = setup_vanna()  # Ensure vn is initialized if not already

    try:
        code = vn.generate_plotly_code(question=question, sql=sql, df=df)
        return code
    except Exception as e:
        st.error(f"An error occurred while generating Plotly code: {e}")
        return ""

@lru_cache(maxsize=None)
def generate_plot_cached(code, df):
    global vn
    if vn is None:
        vn = setup_vanna()  # Ensure vn is initialized if not already

    try:
        return vn.get_plotly_figure(plotly_code=code, df=df)
    except Exception as e:
        st.error(f"An error occurred while generating the plot: {e}")
        return None

@lru_cache(maxsize=None)
def generate_followup_cached(question, sql, df):
    global vn
    if vn is None:
        vn = setup_vanna()  # Ensure vn is initialized if not already

    try:
        return vn.generate_followup_questions(question=question, sql=sql, df=df)
    except Exception as e:
        st.error(f"An error occurred while generating follow-up questions: {e}")
        return []

@lru_cache(maxsize=None)
def generate_summary_cached(question, df):
    global vn
    if vn is None:
        vn = setup_vanna()  # Ensure vn is initialized if not already

    try:
        return vn.generate_summary(question=question, df=df)
    except Exception as e:
        st.error(f"An error occurred while generating summary: {e}")
        return ""










import streamlit as st
import pandas as pd
from database import init_db, run_query, get_schema
from llm_chain import generate_sql

# Initialize DB
init_db()

# Page config
st.set_page_config(page_title="Text-to-SQL App", page_icon="🧠", layout="wide")

st.title("🧠 Text-to-SQL App")
st.markdown("Ask questions in plain English — get SQL answers instantly.")

# Show schema in sidebar
with st.sidebar:
    st.subheader("📋 Database Schema")
    schema = get_schema()
    st.code(schema, language="sql")
    st.markdown("---")
    st.markdown("**Sample Questions:**")
    st.markdown("- Who earns the most?")
    st.markdown("- List all employees in Engineering")
    st.markdown("- What's the average salary by department?")

# Main input
user_question = st.text_input("💬 Ask your question:", placeholder="e.g. Show me all employees hired after 2021")

if st.button("Generate & Run SQL") and user_question:
    with st.spinner("Thinking..."):
        
        # Generate SQL
        sql_query = generate_sql(user_question, schema)
        
        st.subheader("📝 Generated SQL")
        st.code(sql_query, language="sql")
        
        # Run query
        columns, rows, error = run_query(sql_query)
        
        if error:
            st.error(f"SQL Error: {error}")
        else:
            st.subheader("📊 Results")
            if rows:
                df = pd.DataFrame(rows, columns=columns)
                st.dataframe(df, use_container_width=True)
                st.success(f"✅ {len(rows)} row(s) returned")
            else:
                st.info("Query ran successfully but returned no results.")

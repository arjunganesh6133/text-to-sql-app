from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

def generate_sql(user_question: str, schema: str) -> str:
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

    prompt = ChatPromptTemplate.from_template("""
You are an expert SQL assistant. Given the database schema below, write a valid SQLite SQL query to answer the user's question.

Database Schema:
{schema}

Rules:
- Return ONLY the SQL query, no explanation
- Use correct SQLite syntax
- Do not include markdown or backticks

User Question: {question}
SQL Query:
""")

    chain = prompt | llm
    response = chain.invoke({"schema": schema, "question": user_question})
    return response.content.strip()
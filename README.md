# 🧠 Text-to-SQL App

An end-to-end AI application where users type a question 
in plain English and the LLM writes and executes the SQL 
query to find the answer.

Real applications.
1. 🏥 Hospital Management
   "Show me all patients admitted this week with fever"
   "Which doctor has the most appointments today?"
   "List all medicines running low in stock"
2. 🛒 E-Commerce Business
   "Which product has the highest return rate?"
   "Show me all orders that are pending for more than 3 days"
   "What is total revenue generated this month?"
3. 🏦 Banking & Finance
  "Show all transactions above 50000 in last 7 days"
  "Which customers have not logged in for 6 months?"
  "List accounts with negative balance"
5. 🎓 College/University System
   "Which students have attendance below 75%?"
   "Show me top 10 scorers in Mathematics"
   "List all students who haven't paid fees"
6. 📦 Inventory & Warehouse
    "Which items are out of stock?"
    "Show products that haven't been sold in 30 days"
    "What is total inventory value in warehouse 2?"
   

## Tech Stack
- Python
- LangChain
- Streamlit
- SQLite
- Groq (LLaMA 3.3)

## How to Run
1. Clone the repo
2. Create a virtual environment → `python -m venv venv`
3. Activate it → `venv\Scripts\activate`
4. Install dependencies → `python -m pip install -r requirements.txt`
5. Add your Groq API key in `.env` → `GROQ_API_KEY=your_key`
6. Run → `streamlit run app.py`

## Features
- Natural language to SQL conversion
- Real-time query execution
- Schema-aware responses

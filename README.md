# Text-To-SQL-LLM-App-Along-With-Querying-SQL-Database-Using-Google-Gemini

This project is a simple Text-to-SQL application using Google Gemini Pro to generate SQL queries from natural language questions. It then executes those queries on a SQLite database (student.db) and displays the results using Streamlit.

🚀 Features
Convert natural language questions to SQL queries using Gemini Pro.

Perform SQL operations on a SQLite database (student.db).

Display results using an interactive Streamlit interface.

![](Images/SQL_querying.png)


## Sample Questions
  - Provide the average marks of all students?
  - Provide the average marks of all students class wise?
  - Provide the student name with second highest marks?
  - Provide the student name with second highest marks class wise?
  
## Project Structure

- sql.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- sqllite.py: database, table creation, inserting, record display
- .env: Configuration file for storing your Google API key.

Example:

Input: Provide the average marks of all students

Generated SQL: SELECT AVG(MARKS) FROM STUDENT;

Output: Average Marks: 72.2

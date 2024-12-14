# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## My Streamlit App
![Screenshot 2024-12-14 170430](https://github.com/user-attachments/assets/ecaf61d7-aa60-4efa-9d37-f52e2d113c49)

## Skills Gained
- **Integrating Mysql with python**
- **Using Streamlit to design frontend and making HTTP calls from frontent to backend**
- **Used FastAPI as backend to run server**
- **Managing HTTP requests with PostMan API**

## Project Explanation

- These are the steps I followed in my project.
- **Integrated MySQl with python**: Created a set of functions which is used for CRUD operations
- **


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/siddu28/Expense-Tracking-system.git
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```

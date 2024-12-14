# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.
The goal of this project is to develop a system that allows users to view expenses through bar charts by entering a specific date, as well as manage the database by adding, updating, or deleting records through seamless SQL integration with Python.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## My Streamlit App
![Screenshot 2024-12-14 170430](https://github.com/user-attachments/assets/ecaf61d7-aa60-4efa-9d37-f52e2d113c49)

## A Demo Video
https://github.com/user-attachments/assets/09ee725b-2733-4920-9e47-12c1f8b107ae

## Skills Gained
- **Integrating Mysql with python**
- **Using Streamlit to design frontend and making HTTP calls from frontent to backend**
- **Used FastAPI as backend to run server**
- **Managing HTTP requests with PostMan API**

## Project Explanation

- These are the steps I followed in my project.
- **Integrated MySQl with python**: Created a set of functions which is used for CRUD operations.
- **Setting up API Endpoints**: Used FastAPI instead of Flask bacause it has nice documentation and auto debugging process.
- **Added logging**: Used Logging to track our process, if there is any issue or error we can catch it using these logs.
- **Verified the API calls through POSTMAN**: Used postman to check responce given by 'GET' and 'POST' request.
- **Frontend Development using Streamlit**: In streamlit I used API endpoints to call backend and get the responce from FastAPI backend.


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

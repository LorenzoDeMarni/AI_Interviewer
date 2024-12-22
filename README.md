# AI Interview Questions Generator

This project generates tailored interview questions based on user-provided job details and resumes. Below are the steps to set up and run the project on your system using WSL (Windows Subsystem for Linux).

---

## Prerequisites

Ensure you have the following installed on your system:
1. **Python** (3.10 or newer)
2. **Node.js** (16.x or newer) and **npm** (Node Package Manager)
3. **WSL** (Windows Subsystem for Linux)
4. A modern web browser

---

## Project Structure

- `backend/`: Contains the backend server code (Python).
- `frontend/`: Contains the frontend React app.
- `venv/`: The virtual environment for Python dependencies (excluded from Git).
- `.env`: Contains environment variables (like API keys).

---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/LorenzoDeMarni/AI_Interviewer.git
cd AI_Interviewer
```

---

### 2. Setting Up the Backend

1. **Navigate to the `backend/` directory:**
   ```bash
   cd backend
   ```

2. **Activate the Python virtual environment:**
   - If the virtual environment already exists:
     ```bash
     source venv/bin/activate
     ```
   - If the virtual environment does not exist, create it:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install backend dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Open the `.env` file in the `backend` folder.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

5. **Start the backend server:**
   ```bash
   python app.py
   ```

   The backend server should now be running at `http://127.0.0.1:5000`.

---

### 3. Setting Up the Frontend

1. **Navigate to the `frontend/` directory:**
   ```bash
   cd ../frontend
   ```

2. **Install frontend dependencies:**
   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```

   The frontend app should now open in your default browser at `http://localhost:3000`.

---

### 4. Running the Full Application

- **Frontend**: Available at `http://localhost:3000`.
- **Backend**: Running at `http://127.0.0.1:5000`.

When the frontend form is submitted, it communicates with the backend API to generate interview questions.

---

## Common Issues

1. **Backend Errors**:
   - Ensure your virtual environment is activated before running the server.
   - Double-check that the OpenAI API key is set correctly in the `.env` file.

2. **Frontend Errors**:
   - Ensure all dependencies are installed using `npm install`.
   - If the React server fails, try restarting it with `npm start`.

3. **Permission Errors**:
   - If you encounter file access issues, ensure WSL has proper permissions and the required tools installed.

---

## Closing Notes

To stop the servers:
- For the backend, exit the Python virtual environment:
  ```bash
  deactivate
  ```
- For the frontend, stop the React server by pressing `CTRL+C` in the terminal.

---


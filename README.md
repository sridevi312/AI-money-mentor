#  AI Money Mentor

AI Money Mentor is an intelligent financial assistant that helps users manage their money effectively. It provides personalized savings plans, investment suggestions, and AI-powered financial advice.

---

## Problem Statement

In India, more than 95% of people lack proper financial planning. Most rely on guesswork or expensive financial advisors. This leads to poor savings habits and weak financial decisions.

---

##  Solution

AI Money Mentor solves this problem by:

- Analyzing user income and expenses
- Generating a financial health score
- Providing savings and investment suggestions
- Offering AI-powered financial advice through chat

---

##  Features

- Financial Health Score
- Savings & Investment Suggestions
- AI Chat Assistant
- Simple Web Interface

---

##  System Architecture

![Architecture Diagram](architecture.png)

### Explanation
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/1e36770c-ebe9-4361-9b82-b61eb9e0d755" />


The system consists of three main components:

1. **Frontend**
   - Built using HTML and JavaScript
   - Takes user input (salary, expenses)
   - Displays results and chatbot responses

2. **Backend**
   - Built using Flask (Python)
   - Processes user data
   - Calculates financial score and savings
   - Communicates with AI model

3. **AI Layer**
   - Uses Google Gemini API
   - Generates financial advice
   - Responds to user queries

### Workflow

User → Frontend → Backend → AI Model → Backend → Frontend → User

---

##  Tech Stack

- Frontend: HTML, JavaScript  
- Backend: Python (Flask)  
- AI: Google Gemini API  
- Tools: VS Code, GitHub  

---

##  Demo Flow

<img width="939" height="412" alt="image" src="https://github.com/user-attachments/assets/a463a712-82b7-4e20-9c9c-e5e6a14753ab" />


1. Enter salary and expenses  
2. Click "Analyze"  
3. View financial score and suggestions  
4. Ask questions using AI chatbot  

---

## Impact

- Helps users increase savings by 20–30%  
- Provides simple financial guidance  
- Reduces dependency on costly advisors  

---



```bash
git clone https://github.com/your-username/ai-money-mentor.git
cd ai-money-mentor

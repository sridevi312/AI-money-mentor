from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

#  Add your Gemini API key here
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")


#  Finance Logic
def analyze_finance(salary, expenses):
    savings = salary - expenses
    savings_percent = (savings / salary) * 100 if salary > 0 else 0

    if savings_percent >= 30:
        score = 90
    elif savings_percent >= 20:
        score = 70
    else:
        score = 50

    return {
        "savings": savings,
        "score": score,
        "suggestion": f"Try saving ₹{int(savings*0.5)} and invest ₹{int(savings*0.3)} monthly."
    }


#  Home Page
@app.route('/')
def home():
    return render_template("index.html")


#  Analyze Route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    salary = float(data['salary'])
    expenses = float(data['expenses'])

    result = analyze_finance(salary, expenses)
    return jsonify(result)


#  Chat Route (GEMINI FREE)
@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message']

    try:
        response = model.generate_content(
            f"You are a financial advisor. Give simple advice.\nUser: {user_msg}"
        )

        reply = response.text
        return jsonify({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "Error: " + str(e)})


#  Run App
if __name__ == '__main__':
    app.run(debug=True)

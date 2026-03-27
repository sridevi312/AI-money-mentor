from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 💰 Finance Logic
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


# 🤖 Smart Offline AI
def ai_reply(message):
    msg = message.lower()

    if "save" in msg:
        return "Start by following 50-30-20 rule: 50% needs, 30% wants, 20% savings. Reduce unnecessary expenses."

    elif "invest" in msg:
        return "Invest in SIPs, mutual funds, and diversify your portfolio. Start with low-risk funds."

    elif "tax" in msg:
        return "Use Section 80C, 80D for tax savings. Invest in ELSS, PPF, or insurance."

    elif "buy" in msg:
        return "Before buying, check if it fits your budget. Avoid spending more than 30% of your savings."

    elif "plan" in msg:
        return "Create a monthly budget, track expenses, save at least 20%, and invest regularly."

    elif "loan" in msg:
        return "Avoid high-interest loans. Keep EMI below 30% of your income."

    else:
        return "Track your expenses, save regularly, and invest wisely. Ask about saving, investing, or tax."


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    salary = float(data['salary'])
    expenses = float(data['expenses'])
    return jsonify(analyze_finance(salary, expenses))


@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message']
    reply = ai_reply(user_msg)
    return jsonify({"reply": reply})


if __name__ == '__main__':
    app.run(debug=True)
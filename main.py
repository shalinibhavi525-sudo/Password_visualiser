from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Password strength estimator function
def estimate_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Use special characters (!@# etc).")

    # Estimating time to crack (simple simulation)
    time_to_crack = {
        1: "Instantly cracked 😟",
        2: "Few seconds 😬",
        3: "Minutes 😕",
        4: "Several hours 😐",
        5: "Years 🤯 Strong password!"
    }

    return score, remarks, time_to_crack.get(score, "Very weak")

@app.route("/", methods=["GET", "POST"])
def home():
    strength = None
    tips = []
    result = None

    if request.method == "POST":
        password = request.form["password"]
        strength, tips, result = estimate_strength(password)

    return render_template("index.html", strength=strength, tips=tips, result=result)

if __name__ == "__main__":
    app.run(debug=True)

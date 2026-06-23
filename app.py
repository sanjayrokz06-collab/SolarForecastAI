import pandas as pd
from predict import predict_live
from flask import Flask, render_template, request, redirect, url_for, session
from utils.charts import (
    create_weather_chart,
    create_temperature_chart,
    create_dni_chart,
    create_power_chart
)
from report import generate_report
from flask import send_file
from database import create_database, save_prediction, get_history
# ----------------------------------
# Flask App Configuration
# ----------------------------------
app = Flask(__name__)
create_database()
app.secret_key = "solarforecast123"

# ----------------------------------
# Login Credentials
# ----------------------------------
USERNAME = "sanjay"
PASSWORD = "12345"

# ----------------------------------
# Home Route
# ----------------------------------
@app.route("/")
def home():
    return redirect(url_for("login"))

# ----------------------------------
# Login Route
# ----------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:

            session["user"] = username
            return redirect(url_for("dashboard"))

        else:

            return render_template(
                "login.html",
                error="Invalid Username or Password"
            )

    return render_template("login.html")

# ----------------------------------
# Dashboard
# ----------------------------------
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    result = predict_live()
    save_prediction(result)

    weather_chart = create_weather_chart(result)
    temperature_chart = create_temperature_chart(result)
    dni_chart = create_dni_chart(result)
    power_chart = create_power_chart(result)

    return render_template(
        "dashboard.html",
        result=result,
        weather_chart=weather_chart,
        temperature_chart=temperature_chart,
        dni_chart=dni_chart,
        power_chart=power_chart
    )

# ----------------------------------
# Forecast Page
# ---------------------------------
@app.route("/forecast")
def forecast():

    if "user" not in session:
        return redirect(url_for("login"))

    result = predict_live()

    weather_chart = create_weather_chart(result)
    temperature_chart = create_temperature_chart(result)
    dni_chart = create_dni_chart(result)
    power_chart = create_power_chart(result)

    return render_template(
        "forecast.html",
        result=result,
        weather_chart=weather_chart,
        temperature_chart=temperature_chart,
        dni_chart=dni_chart,
        power_chart=power_chart
    )
# ----------------------------------
# Analytics Page
# ----------------------------------
@app.route("/analytics")
def analytics():

    if "user" not in session:
        return redirect(url_for("login"))

    result = predict_live()

    return render_template(
        "analytics.html",
        result=result
    )

# ----------------------------------
# Research Page
# ----------------------------------
@app.route("/research")
def research():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("research.html")

# ----------------------------------
# About Page
# ----------------------------------
@app.route("/about")
def about():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("about.html")


@app.route("/download_report")
def download_report():

    if "user" not in session:
        return redirect(url_for("login"))

    result = predict_live()

    pdf = generate_report(result)

    return send_file(
        pdf,
        as_attachment=True
    )

# ----------------------------------
# Logout
# ----------------------------------
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("login"))

# ----------------------------------
# Run App
# ----------------------------------
if __name__ == "__main__":
    app.run(debug=True)
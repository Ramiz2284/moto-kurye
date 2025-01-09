from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    # Редиректим на русский по умолчанию
    return redirect(url_for("index_ru"))

@app.route("/ru")
def index_ru():
    return render_template("index_ru.html")

@app.route("/tr")
def index_tr():
    return render_template("index_tr.html")

if __name__ == "__main__":
    app.run(debug=True)

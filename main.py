from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    f = open("templates/database.txt", "r")

    return render_template("home.html", jobs=[jobs.split(", ") for jobs in f.readlines()], company_name="Humarr")


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/index')
# Landing Page and Possible Link to Login Page?
def index():
    return {}


@app.route("/login")
# Login Page and Password Setting?
def login():
    return {}


@app.route("/home")
# Home Page with Chat?
def home():
    return {}

if __name__ == '__main__':
    app.run(debug=True)

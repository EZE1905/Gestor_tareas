from flask import Flask,redirect,render_template

app = Flask(__name__)
app.secret_key = 'super_secret_key' # Necesario para sesiones

@app.route("/")
def home():
    return "hola  flask"

if __name__ == "__main__":
    app.run(debug=True)
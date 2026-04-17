from flask import Flask,redirect,render_template,url_for
from mgestor_tareas import leer_tareas

app = Flask(__name__)
app.secret_key = 'super_secret_key' # Necesario para sesiones

tareas = leer_tareas()

@app.route("/")
def home():
    return render_template("layout.html", tareas = tareas)

if __name__ == "__main__":
    app.run(debug=True)
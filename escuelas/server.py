from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicia():
    return "Hello World"

@app.route('/mapa')
def verMapa():
    return render_template("mapa.html")

if __name__ == "__main__":
    app.run()
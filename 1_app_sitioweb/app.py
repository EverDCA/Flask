from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app= Flask(__name__)
Bootstrap(app)

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

if __name__ == '__main__':
    app.run(debug=True)
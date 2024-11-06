#Se Importa Flask desde flasjk
from flask import Flask
#se crea una instancia de la clase Flask __name__
app = Flask(__name__)
# Este es un decorador que define una ruta
# corresponde a la página principal de la app
@app.route("/" )
# Cuando alguien visite app (por ejemplo, http://localhost:5000/),
# la función hello() será ejecutada
def hello():
    return "<h1>Hello, World Flask !</hl>"
# Solo se ejecute si el
# arranca la aplicación
if __name__ == '__main__':
    app.run(debug=True,port=5000)
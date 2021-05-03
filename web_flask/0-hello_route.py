from flask import Flask
app = Flask(__name__) #una instancia de la clase, flask sabra donde buscar plantillas

@app.route('/', strict_slashes=False) # route le dice a flask que URL desencadenara la funcion
def hello():
    return 'Hello HBNB!'

from flask import Flask
from controlador.tarea_controlador import tarea_bp

app = Flask(__name__)
app.register_blueprint(tarea_bp)

if __name__ == "__main__":
    app.run(debug=True)

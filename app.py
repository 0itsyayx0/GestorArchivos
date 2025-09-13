from flask import Flask
from controllers.archivo_controller import gestor_archivos

app = Flask(__name__)
app.register_blueprint(gestor_archivos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
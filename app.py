from flask import Flask, render_template, request
from games.pierre_feuille_ciseau import pfc_bp
from games.nombre_dor import nombre_dor_bp

app = Flask(__name__)
app.register_blueprint(pfc_bp)
app.register_blueprint(nombre_dor_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Blueprint, render_template
from games import nombre_dor

nombre_dor_bp = Blueprint(
    'nombre_dor', 
    __name__, 
    template_folder='templates'
)

@nombre_dor_bp.route('/game_nombre_dor')
def game_nombre_dor():
    return render_template('nombre_dor.html')
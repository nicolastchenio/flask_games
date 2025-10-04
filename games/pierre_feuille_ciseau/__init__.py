from flask import Blueprint, render_template
from games import pierre_feuille_ciseau

pfc_bp = Blueprint(
    'pfc', 
    __name__, 
    template_folder='templates'
)

@pfc_bp.route('/game_pfc')
def game_pfc():
    return render_template('pierre_feuille_ciseau.html')
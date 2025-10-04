from flask import Blueprint, render_template, request
from .models.PierreFeuilleCiseau import PierreFeuilleCiseau

pfc_bp = Blueprint(
    'pfc', 
    __name__, 
    template_folder='templates'
)

# @pfc_bp.route('/game_pfc')
# def game_pfc():
#     return render_template('pierre_feuille_ciseau.html')

# on instancie le jeu
play_pfc = PierreFeuilleCiseau()

@pfc_bp.route('/game_pfc')
def game_pfc():
    return render_template("pierre_feuille_ciseau.html", result=None)

@pfc_bp.route("/play", methods=["POST"])
def play():
    choix = request.form.get("choix")
    result = play_pfc.play_round(choix)
    return render_template("pierre_feuille_ciseau.html", result=result)
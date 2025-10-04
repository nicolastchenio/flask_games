import random

class PierreFeuilleCiseau:
    CHOISE_LIST = ["pierre", "feuille", "ciseaux"]
    GAME_ROUNDS = 3
     
    def __init__(self):
        self.score_player = 0
        self.score_ia = 0

    # @staticmethod
    # def verif_choise(choise):
    #     mapping = {"p": "pierre", "f": "feuille", "c": "ciseaux"}
    #     return mapping.get(choise)

    @staticmethod
    def verif_player_win(choise_player, choise_ia):
        if choise_player == choise_ia:
            return None
        elif (choise_player == "pierre" and choise_ia == "ciseaux") \
            or (choise_player == "feuille" and choise_ia == "pierre") \
            or (choise_player == "ciseaux" and choise_ia == "feuille"):
            return True
        else:
            return False

    def play_round(self, choise_player):
        choise_ia = random.choice(self.CHOISE_LIST)
        player_win = self.verif_player_win(choise_player, choise_ia)
        if player_win is True:
            self.score_player += 1
        elif player_win is False:
            self.score_ia += 1
        return {
            "choix_joueur": choise_player,
            "choix_ia": choise_ia,
            "resultat": player_win,
            "score_joueur": self.score_player,
            "score_ia": self.score_ia
        }

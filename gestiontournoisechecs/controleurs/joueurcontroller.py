from gestiontournoisechecs.modeles.joueur import Joueur
from gestiontournoisechecs.json.config import PATH_JSONFILE_JOUEUR
import json


class JoueurController:
    @staticmethod
    def save_joueurs(list_joueurs):
        with open(PATH_JSONFILE_JOUEUR, "w", encoding="utf-8") as file:
            list_dict_joueurs = [joueur.to_dict() for joueur in list_joueurs]
            json.dump(list_dict_joueurs, file, indent=4)

    @staticmethod
    def load_joueurs():
        with open(PATH_JSONFILE_JOUEUR, "r", encoding="utf-8") as file:
            list_joueurs = [Joueur().from_json(dict) for dict in json.load(file)]
            return list_joueurs


if __name__ == "__main__":
    joueur = [Joueur(prenom="benjamin"), Joueur()]
    JoueurController.save_joueurs(joueur)
    print("ok")

    list_joueurs = JoueurController.load_joueurs()
    joueur_bis = list_joueurs[0]
    print(joueur_bis.prenom, joueur_bis.nom_famille)

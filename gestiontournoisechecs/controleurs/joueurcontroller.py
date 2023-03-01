from gestiontournoisechecs.modeles.joueur import Joueur
from gestiontournoisechecs.json.config import PATH_JSONFILE_JOUEUR
import json


class JoueurController:
    def __init__(self) -> None:
        self.load_joueurs()

    def save_edits(self) -> None:
        with open(PATH_JSONFILE_JOUEUR, "w", encoding="utf-8") as file:
            list_dict_joueurs = [joueur.to_dict() for joueur in self._all_joueurs]
            json.dump(list_dict_joueurs, file, indent=4)

    def load_joueurs(self) -> None:
        try:
            with open(PATH_JSONFILE_JOUEUR, "r", encoding="utf-8") as file:
                self._all_joueurs = [
                    Joueur().from_json(dict) for dict in json.load(file)
                ]
        except FileNotFoundError:
            self._all_joueurs = []
            self.save_edits()

    # GET /joueurs
    def get_joueurs(self) -> list:
        list_joueurs = {joueur.to_dict() for joueur in self._all_joueurs}
        return list_joueurs

    def get_joueurs_id(self) -> set:
        return {joueur.id_fede for joueur in self._all_joueurs}

    def get_joueurs_index(self, id_searched):
        for index, joueur in enumerate(self._all_joueurs):
            if joueur.id_fede == id_searched:
                return index
        return None

    # GET /joueurs/<id>
    def get_joueur(self, id):
        index = self.get_joueurs_index(id)
        if index is not None:
            return self._all_joueurs[index].to_dict()
        return None

    # PUT /joueurs/<id>
    def put_joueur(self, id, dict_data):
        index = self.get_joueurs_index(id)
        joueur = Joueur().from_json(dict_data)
        if index is not None:
            self._all_joueurs[index] = joueur
        else:
            self._all_joueurs.append(joueur)
        self.save_edits()


if __name__ == "__main__":
    controller = JoueurController()

    # controller._all_joueurs = [
    #     Joueur(id_fede="AB12345", prenom="benjamin", nom_famille="Bourdon"),
    #     Joueur(id_fede="HG87538", prenom="benjamin", nom_famille="Mouton"),
    #     Joueur(id_fede="PL07483", prenom="muriel", nom_famille="Bourdon")
    # ]
    # controller.save_joueurs()
    # print("ok")

    data = {"id_fede": "PJ84483", "prenom": "astrid", "nom_famille": "Bourdon"}
    controller.put_joueur(data["id_fede"], data)

    # joueur_bis = controller.get_joueur("AB12345")
    # print(joueur_bis['prenom'], joueur_bis['nom_famille'])

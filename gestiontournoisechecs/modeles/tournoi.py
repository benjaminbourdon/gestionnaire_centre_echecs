from datetime import date

DEFAUT_NB_TOURS = 4


class Tournoi:
    """Représente un tournoi d'échecs"""

    def __init__(
        self,
        nom=None,
        descriptif="",
        lieu=None,
        date_debut=None,
        date_fin=None,
        nbtours=DEFAUT_NB_TOURS,
        idtour_actuel=0,
        liste_tours=None,
        liste_participants=None,
    ) -> None:

        self.nom = nom
        self.descriptif = descriptif
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nbtours = nbtours
        self.idtour_actuel = idtour_actuel
        self.liste_tours = liste_tours
        self.liste_participants = liste_participants

        if self.date_debut == None:
            self.date_debut = date.today()
        if self.nom == None:
            self.nom = f"Tournoi du {self.date_debut:%d/%m/%y}"
        if self.liste_tours == None:
            self.liste_tours = []
        if self.liste_participants == None:
            self.liste_participants = []


if __name__ == "__main__":
    tournoi = Tournoi()
    print(tournoi.nom)

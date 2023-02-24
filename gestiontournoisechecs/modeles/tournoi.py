from datetime import date
from gestiontournoisechecs.modeles.participant import Participant
from gestiontournoisechecs.modeles.tour import Tour


DEFAUT_NB_TOURS = 4


class Tournoi:
    """Represent a chess tournament"""

    def __init__(
        self,
        nom=None,
        descriptif="",
        lieu=None,
        date_debut=None,
        date_fin=None,
        nbtours=None,
        idtour_actuel=None,
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

        if self.liste_tours is None:
            self.liste_tours = []
        if self.liste_participants is None:
            self.liste_participants = []

    @staticmethod
    def new_tournoi(
        nom=None,
        descriptif="",
        lieu=None,
        nbtours=DEFAUT_NB_TOURS,
    ):
        date_debut = date.today()
        if nom is None:
            nom = f"Tournoi du {date_debut:%d/%m/%y}"

        idtour_actuel = 0  # Idtour is 0 while there's no Tour started

        tournoi = Tournoi(
            nom=nom,
            descriptif=descriptif,
            lieu=lieu,
            nbtours=nbtours,
            idtour_actuel=idtour_actuel,
        )
        tournoi.new_tour()
        return tournoi

    def new_tour(self):
        # Verify that the last round is completed (or this is the first)
        # and the number of round isn't reached
        if not (self.liste_tours) or (
            self.liste_tours[-1].iscompleted() and
            self.idtour_actuel < self.nbtours
        ):
            self.idtour_actuel += 1
            fresh_tour = Tour.new_tour(f"Round {self.idtour_actuel}")
            self.liste_tours.append(fresh_tour)

    def add_tour(self, tour) -> None:
        if issubclass(tour, Tour):
            self.liste_tours.append(tour)

    def add_participant(self, participant) -> None:
        if issubclass(participant, Participant):
            self.liste_participants.append(participant)
        else:
            raise Exception   # Préciser le type d'exception

    def get_nb_participants(self) -> int:
        return len(self.liste_participants)

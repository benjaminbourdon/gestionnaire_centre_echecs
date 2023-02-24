from gestiontournoisechecs.modeles.tournoi import Tournoi
from gestiontournoisechecs.modeles.joueur import Joueur


class Participant(Joueur):
    """Represent a participant in a chess tournament"""

    def __init__(self, tournoi: Tournoi, **kwargs):
        """Initialize Participant

        Args:
            tournoi (Tournoi): tournnament in wich the player is participating
            (à compléter)
        """
        self.tournoi = tournoi
        self.score = self.get_score()
        super().__init__(**kwargs)

    def get_score(self):
        return 0

    def from_joueur(tournoi: Tournoi, joueur: Joueur):
        pass
        # À implementer

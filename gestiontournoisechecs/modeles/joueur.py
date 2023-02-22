from collections import UserDict
from datetime import date
from gestiontournoisechecs.modeles.tournoi import Tournoi


class Joueur(UserDict):
    """Represents a chess player

    Attributes:
        nom_famille : a string containing player's family name.
        prenom : a string containing player's surname.
        date_naissance : a datetime.date object containing player's day of birth.
        id_fede  : a string containing player's id from chess federation."""

    def __init__(
        self,
        nom_famille: str = None,
        prenom: str = None,
        date_naissance: date = None,
        id_fede: str = None,
    ) -> None:
        """Initialize Joueur

        Args:
            nom_famille (str, optional): player's name. Defaults to None.
            prenom (str, optional): player's surname. Defaults to None.
            date_naissance (datetime.date, optional): player's day of birth. Defaults to None.
            id_fede (str, optional): player's federal id (2 letters follow by 5 numbers). Defaults to None.
        """
        dict = {
            "nom_famille": nom_famille,
            "prenom": prenom,
            "date_naissance": date_naissance,
            "id_fede": id_fede,
        }
        super().__init__(dict)


class Participant(Joueur):
    """Represent a participant in a chess tournament"""

    def __init__(self, tournoi: Tournoi, **kwargs):
        """Initialize Participant

        Args:
            tournoi (Tournoi): tournnament in wich the player is participating
        """
        self.tournoi = tournoi
        self.score = self.get_score()
        super().__init__(**kwargs)
        
    def get_score(self):
        return 0
    
    def from_joueur(tournoi:Tournoi,joueur:Joueur):
        pass 
        #À implementer


if __name__ == "__main__":
    joueur = Participant(Tournoi(), nom_famille="Bourdon")
    print(joueur.__doc__)

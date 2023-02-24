from datetime import date


class Joueur:
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
        self.nom_famille = nom_famille
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.id_fede = id_fede

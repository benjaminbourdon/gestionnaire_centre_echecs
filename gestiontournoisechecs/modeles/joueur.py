class Joueur:
    """Représente un joueur d'échec du club"""

    attributs = ("nom_famille", "prenom", "date_naissance", "id_fede")

    def __init__(self, **kwargs):
        for key in self.attributs:
            value = kwargs.get(key, None)
            setattr(self, key, value)


class Participant(Joueur):
    pass

from datetime import datetime


class Tour:
    """Represent a round in a chess tournament"""

    def __init__(
        self, nom: str = None, debut: datetime = None, fin: datetime = None
    ) -> None:
        self.nom = nom
        self.debut = debut
        self.fin = fin

    def add_match(self) -> None:
        pass

    def iscompleted(self) -> bool:
        # Ajouter d'autres conditions : matchs finis
        if isinstance(self.fin, datetime):
            return True
        return False

    def start_tour(self) -> None:
        self.debut = datetime.now()

    def end_tour(self) -> None:
        self.fin = datetime.now()

    @staticmethod
    def new_tour(nom):
        tour = Tour(nom=nom)
        tour.start_tour()
        return tour

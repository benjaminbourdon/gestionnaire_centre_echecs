class Match(tuple):
    __slots__ = ()

    SCORE_WIN = 1
    SCORE_TIE = 0.5
    SCORE_LOSE = 0

    def winner(self, winner_id: int) -> None:
        pass

    def is_finished(self) -> None:
        pass

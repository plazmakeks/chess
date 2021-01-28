from typing import List

import requests
from stockfish import Stockfish

from chess_cheater.game import Game
from chess_cheater.prediction import Prediction


class Predictor:
    def __init__(self):
        self.stockfish = Stockfish("/usr/games/stockfish")

    def get_games(self, player: str) -> List[Game]:
        url = f"https://api.chess.com/pub/player/{player}/games"
        result: List[Game] = []
        response = requests.get(url=url)
        if response.status_code == 200:
            try:
                data = response.json()
                result = [Game(**record) for record in data["games"]]
            except Exception:
                return []
        return result

    def get_predictions(self, player: str) -> List[Prediction]:
        games = self.get_games(player=player)
        result: List[Prediction] = []
        for game in games:
            self.stockfish.set_fen_position(game.fen)
            result.append(
                Prediction(
                    game=game.url,
                    opponent=game.white if player in game.black else game.black,
                    best_move=self.stockfish.get_best_move(),
                )
            )
        return result

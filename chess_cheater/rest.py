from fastapi import FastAPI, Depends

from chess_cheater.predictor import Predictor

app = FastAPI()


@app.get("/best_moves")
async def best_moves(player: str, predictor: Predictor = Depends(Predictor)):
    return predictor.get_predictions(player=player)
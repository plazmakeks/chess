from pydantic import BaseModel, constr


class Prediction(BaseModel):
    game: constr(min_length=1)
    opponent: constr(min_length=1)
    best_move: constr(min_length=1)
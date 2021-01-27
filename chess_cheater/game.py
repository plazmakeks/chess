from pydantic import BaseModel, constr


class Game(BaseModel):
    white: constr(min_length=1)
    black: constr(min_length=1)
    url: constr(min_length=1)
    fen: constr(min_length=1)

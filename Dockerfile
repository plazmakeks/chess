FROM python:3.6.9-slim-buster

RUN apt update && apt install -y stockfish curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="/root/.poetry/bin:${PATH}"

RUN mkdir -p /app/chess-cheater
COPY pyproject.toml /app/chess-cheater
COPY chess_cheater /app/chess-cheater/chess_cheater

RUN cd /app/chess-cheater && poetry install -n

EXPOSE 8080

WORKDIR /app/chess-cheater
CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "chess_cheater.rest:app"]
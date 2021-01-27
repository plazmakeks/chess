# chess
Predict best moves for chess.com 

# Run on host
[Install poetry](https://python-poetry.org/docs/#installation)
```
apt install stockfish

poetry run python -m chess_cheater.cli <cheater name>
```

# Run in docker
```
docker build -f Dockerfile -t cc .
docker run --rm cc
```
[Happy cheating](http://127.0.0.1/docs)
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
docker build -t cc .
docker run  -p 8080:8080 --rm cc
```
[Happy cheating](http://127.0.0.1:8080/docs)

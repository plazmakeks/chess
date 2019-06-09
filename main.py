import httpcall
import data.games
import stockfish
import sys

username = 'myusername'

if len(sys.argv) < 2:
    print('Please provide user name as arg1: $ python3 main.py myusername')
else:
    username = sys.argv[1]

print('Retrieving best moved for player', username)

json = httpcall.getGames(username)
games = data.games.Games(json).games

sf = stockfish.Stockfish()

for game in games:
    sf.set_fen_position(game.fen)
    print('Best move for game', game.url, 'against', game.white if username in game.black else game.black, 'is', sf.get_best_move())
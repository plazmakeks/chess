import argparse

from chess_cheater.predictor import Predictor

parser = argparse.ArgumentParser(description="Chess cheater")
parser.add_argument("pos_arg", type=str, help="the cheaters name")

if __name__ == "__main__":
    args = parser.parse_args()
    cheater = args.pos_arg
    for prediction in Predictor().get_predictions(cheater):
        print(
            f"best move in game {prediction.game} vs {prediction.opponent}: {prediction.best_move}"
        )

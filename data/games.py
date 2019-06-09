class Game:
    def __init__(self, json):
        self.white = json['white']
        self.black = json['black']
        self.url = json['url']
        self.fen = json['fen']
        self.pgn  = json['pgn']
        self.turn = json['turn']
        self.move_by = json['move_by']
        if 'draw_offer' in json:
            self.draw_offer = json['draw_offer']
        self.last_activity = json['last_activity']
        self.start_time = json['start_time']
        self.time_control = json['time_control']
        self.time_class = json['time_class']
        self.rules = json['rules']
        if 'tournament' in json:
            self.tournament = json['tournament']
        if 'match' in json:
            self.match = json['match']
        self.rated = json['rated']



class Games:
    #json is supposed to be an array of game objects
    def __init__(self, json):
        self.games = []
        for game in json['games']:
            self.games.append(Game(game))


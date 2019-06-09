import urllib.request
import json

baseUrl = 'https://api.chess.com/pub/'
header = {'Content-type': 'application/json'}

def getGames(player):
    url = baseUrl + 'player/' + player + '/games'
    req = urllib.request.Request(url=url, headers=header, method='GET')
    res = urllib.request.urlopen(req)
    if res.status != 200:
        print('failed calling')
        return
    data = json.loads(res.read().decode('utf-8'))
    return data
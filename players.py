import requests
from bs4 import BeautifulSoup


teams = []
urls = []
players = []

def getTeams(teams, urls):
    rec = "http://espn.go.com/nba/teams"
    r = requests.get(rec)
    soup = BeautifulSoup(r.text)
    links = soup.select("h5 a")
    for team in links:
        teams.append(team.text)
        urls.append(team['href'])

def getPlayers(teams, urls):
    baseURL = "http://espn.go.com/nba/team/roster/_/name/"
    prefix1 = ""
    prefix2 = ""
    parts = []
    '''url == team. '''
    for url in urls:
        parts = url.split("/")
        prefix1 = parts[-2]
        prefix2 = parts[-1]
        rec = baseURL + prefix1 + "/" + prefix2
        print("getting " + rec)
        r = requests.get(rec)
        print(r)
        soup = BeautifulSoup(r.text)
        rawPlayers = soup.select("tr")
        ''' rawPlayers is the current teams players data with a lot of noise. rawPlayer is the same only for one player '''
        for rawPlayer in rawPlayers:
            player = []
            ''' every el is an attribute of the current player - number, name, position, age, height, weight, school'''
            for el in rawPlayer:
                player.append(el.text)
            players.append(player)
        
getTeams(teams = teams, urls = urls)
getPlayers(teams, urls)

def getResult():
    return players
    
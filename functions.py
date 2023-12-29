import requests
import secret

def levelCheck(summonerName):
    r = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={secret.APIKEY}')

    if r.status_code != 200:
        return "That wasn't it"        

    formattedData = r.json()

    level = formattedData.get("summonerLevel")

    if level > 100:
        return "You're a low level"
    else:
        return "You're not a low level"

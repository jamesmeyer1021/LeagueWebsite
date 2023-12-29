import requests
import secret

#function to check the level of the Summoner
def levelCheck(summonerName):
    print(summonerName)
    r = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={secret.APIKEY}')
    print(r.text)
    if r.status_code != 200:
        return "That wasn't it"        
    
    formattedData = r.json()
    level = formattedData.get("summonerLevel")

    if level > 100:
        return "You're not a low level"
    else:
        return "You're a low level"

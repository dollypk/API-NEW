
import requests, json

def AnimeOngoing():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/anime2/ongoing",headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))
    
def AnimeList():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/anime2/list",headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

AnimeOngoing()

import requests, json

def oneCakRandom():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/1cak",headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

oneCakRandom()

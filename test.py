import requests
import json
import sys

def main():
    log = requests.get("https://logs.tf/api/v1/log/1000")
    logjson = json.loads(log.content)
    players = logjson.get("players")
    print(players)

main()

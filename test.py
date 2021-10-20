import requests
import json
import sys

def main():
    #log = requests.get("https://logs.tf/api/v1/log/1000")
    #logjson = json.loads(log.content)
    #players = logjson.get("players")
    #print(players)

    url = 'http://logs.tf/upload'
    fp = "/Users/jray1/Downloads/test.log"

    #just seeing how this shit works
    files = {'logfile': open(fp, 'rb').read(), 
            'title': 'test',
            'map': 'bagellol',
            'key': '76561198002965000#89090c88335a1f17',
            }
    response = requests.post(url, files=files, data=files, verify=False)
    data = response.json()
    print(data.get("error"))



main()

import requests
import json

BASEURL = 'http://192.168.2.19/'


def on():
    requests.get(BASEURL + 'relay/0?turn=on')


def off():
    requests.get(BASEURL + 'relay/0?turn=off')


def getpower():
    data = json.loads(requests.get(BASEURL + 'status').text)
    power = data['meters'][0]['power']
    print('power = ' + str(power))
    return power

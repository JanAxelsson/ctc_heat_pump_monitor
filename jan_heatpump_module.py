import requests
import json

HEAT_WIRE = 'http://192.168.2.19/'

def query_ctc_menu(url, pos, description):
    headers = {'Content-Type': 'application/x-www-form-urlencoded', }
    data = '-1,-1'
    response = requests.post(url, headers=headers, data=data)

    response_items = response.text.replace('\r', '').split('|')  # Replace CR with ''
    print(description + ' = ' + str( float(response_items[pos]) / 10) )


def shelly_plug_s_on_off(value): # value = 'on' or 'off'
    requests.get( HEAT_WIRE + 'relay/0?turn=' + value)


def shelly_plug_s_getpower():
    data = json.loads( requests.get( HEAT_WIRE + 'status').text)
    power = data['meters'][0]['power']
    print('power = ' + str(power) )

import requests
import time

BASEURL = 'http://192.168.2.3'

DRIFTINFO = BASEURL + '/click/glob;menu;1;0;112;113'  # First level Drift info on CTC GIS 212 display
DRIFTINFO_PUMP = BASEURL + '/click/glob;menu;1;0;111'  # submenu on CTC GIS 212 display
DRIFTINFO_VV_O_EL = BASEURL + '/click/glob;menu;1;0;110'  # submenu on CTC GIS 212 display

def print(a): # NOTE : override print.  Comment out to print output for all functions
    return

def query_ctc_menu(url, pos, description, output):

    headers = {'Content-Type': 'application/x-www-form-urlencoded', }
    data = '-1,-1'
    response = requests.post(url, headers=headers, data=data, timeout = 10)

    response_items = response.text.replace('\r', '').split('|')  # Replace CR with ''
    if output:
        print(description + ' = ' + str( float(response_items[pos]) / 10) )

    answer = str( float(response_items[pos]) / 10 )

    return answer

def compressor_status():
    status_value = query_ctc_menu(DRIFTINFO_PUMP, 64, 'Compressor status', False) # Divided by 10
    if str(status_value) == '1.4' :
        print('Compressor status = off')
        return 'off'

    if str(status_value)  == '1.5' :
        print('Compressor status = disabled')
        return 'disabled'

    if str(status_value)  == '0.1' :
        print('Compressor status = on')
        return 'on'

    return 'unknown'

def heat_system():
    status_value = query_ctc_menu(DRIFTINFO_VV_O_EL, 59, 'VS/VV', False) # Divided by 10
    if str(status_value) == '0.5' :
        print('Heating = VS')
        return 'VS'

    if str(status_value)  == '0.6' :
        print('Heating = VV')
        return 'VV'

    return 'unknown'

def compressor_rpm():
    return query_ctc_menu(DRIFTINFO_PUMP, 65, 'Compressor RPM', True)

def radiator_return():
    return query_ctc_menu(DRIFTINFO_PUMP, 75, 'Radiator return', True)

def radiator_out():
    return query_ctc_menu(DRIFTINFO_PUMP, 76, 'Radiator out', True)

def outdoor_temp():
    return query_ctc_menu(DRIFTINFO, 32, 'Outdoor temp', True)

def warm_water_percent():
    return query_ctc_menu(DRIFTINFO, 58, 'Warm water %', True)

def brine_in():
    return query_ctc_menu(DRIFTINFO, 37, 'Brine in', True)

def brine_out():
    return query_ctc_menu(DRIFTINFO, 38, 'Brine out', True)


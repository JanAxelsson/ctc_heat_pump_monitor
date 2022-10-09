import jan_heatpump_module as ctc
import traceback
import time
import datetime

LOGFILE = "/var/log/ctc_log.txt"  # On mac : sudo touch, and, sudo chmod a+w
DELAY = 60

EOL = '\n'
TAB = '\t'
header = 'time        ' + TAB + \
    'date          ' + TAB + \
    'out_T' + TAB + \
    'VS/VV' + TAB + \
    'status' + TAB + \
    'rpm' + TAB +  \
    'rad_ret' + TAB + \
    'rad_out' + TAB + \
    'brineIn' + TAB + \
    'brineUt' + TAB + \
    'brineDt' + TAB + \
    'bri/rpm'

f = open( LOGFILE, "a", buffering=1)
f.write(header + EOL)

while True:
    try:
        time.sleep(DELAY)

        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        time_now = now.strftime("%H:%M:%S")

        status = ctc.compressor_status()
        rpm = ctc.compressor_rpm()
        heater = ctc.heat_system()
        radiator_return = ctc.radiator_return()
        rad_out = ctc.radiator_out()
        outdoor_temp = ctc.outdoor_temp()
        warm_water = ctc.warm_water_percent()
        brine_in = ctc.brine_in()
        brine_out = ctc.brine_out()
        brine_dT = "{:6.4f}".format(  float(brine_out) - float(brine_in) )

        brineDTOverRPM = '0'
        if float(rpm) > 10:
            brineDTOverRPM = "{:6.4f}".format(  -100 * ( float(brine_out) - float(brine_in) ) / float(rpm) )


        data = time_now + TAB + \
            date + TAB + \
            outdoor_temp + TAB + \
            heater + TAB + \
            status + TAB + \
            rpm + TAB + \
            radiator_return + TAB + \
            rad_out + TAB + \
            brine_in + TAB + \
            brine_out + TAB + \
            brine_dT + TAB + \
            brineDTOverRPM + EOL
        f.write( data)

    except Exception as e:
        print('error')
        print(e)
        traceback.print_exc()


f.close()



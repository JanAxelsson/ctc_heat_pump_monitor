import jan_heatpump_module as ctc
import jan_shelly_module as plug
import traceback
import time
import datetime
#
# NOTES:
#
# AUTO OFF
#   Web browser to BASEURL (from jan_shelly_module.py).
#   Set Timer AUTOOFF to time to run heater after it has become lower than THRESHOLD level
#   I have it set to 1800 seconds = 30 minutes.
#
# HEAT WIRE THRESHOLD
THRESHOLD = 6                       # Threshold on delta brine relative fractional rpm;  deltaBrine / ( rpm / maxRpm)
#
# LOG FREQUENCY
DELAY = 60                          # Must be above approximately 20 seconds
#
# LOG FILE
LOGFILE = "/var/log/ctc_log.txt"    # Prepare : sudo touch, and, sudo chmod a+w

#
# CODE
#

EOL = '\n'
TAB = '\t'
header = 'time        ' + TAB + \
    'date          ' + TAB + \
    'out_T' + TAB + \
    '|' + TAB + \
    'VS/VV' + TAB + \
    'status' + TAB + \
    'rpm' + TAB +  \
    'vp_ret' + TAB + \
    'vp_out' + TAB + \
    '|' + TAB + \
    'brineIn' + TAB + \
    'brineUt' + TAB + \
    'brineDt' + TAB + \
    '|' + TAB + \
    'bri/rpm' + TAB + \
    'P_wire'

f = open( LOGFILE, "a", buffering=1)
f.write(header + EOL)

while True:
    try:
        #
        # Cycle menus (idea, that all data is updated)
        #
        ctc.top()
        time.sleep(2)

        ctc.click_top_to_next_window()
        time.sleep(2)
        ctc.click_next_to_warm_water_window()
        time.sleep(2)

        ctc.click_second_to_heat_pump_window()
        time.sleep(2)

        ctc.top()
        time.sleep(2)

        #
        # Read data
        #
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        time_now = now.strftime("%H:%M:%S")

        status = ctc.compressor_status()
        rpm = ctc.compressor_rpm()
        heater = ctc.heat_system()
        heatpump_return = ctc.heatpump_return()
        heatpump_out = ctc.heatpump_out()
        outdoor_temp = ctc.outdoor_temp()
        warm_water = ctc.warm_water_percent()
        brine_in = ctc.brine_in()
        brine_out = ctc.brine_out()
        brine_dT = "{:6.1f}".format(  float(brine_out) - float(brine_in) )

        wire_power = "{:6.0f}".format( plug.getpower())

        # Delta brine relative fractional rpm
        MAXRPM = 100;
        brineDTOverRPM = '0'
        if float(rpm) > 10:
            brineDTOverRPMvalue =  -MAXRPM * ( float(brine_out) - float(brine_in) ) / float(rpm)
            brineDTOverRPM = "{:6.2f}".format(brineDTOverRPMvalue)

        #
        # Heater
        #
        if brineDTOverRPMvalue > THRESHOLD:
            plug.on()

        if brineDTOverRPMvalue < THRESHOLD:
            plug.off()

        #
        # Log data
        #

        data = time_now + TAB + \
               date + TAB + \
               outdoor_temp + TAB + \
               '|' + TAB + \
               heater + TAB + \
               status + TAB + \
               rpm + TAB + \
               heatpump_return + TAB + \
               heatpump_out + TAB + \
               '|' + TAB + \
               brine_in + TAB + \
               brine_out + TAB + \
               brine_dT + TAB + \
               '|' + TAB + \
               brineDTOverRPM + TAB + \
               wire_power + EOL
        f.write( data)



    except Exception as e:
        print('error')
        print(e)
        traceback.print_exc()


    time.sleep(DELAY - 10)    # Subtract 10 s for delay due to above menu cycling

f.close()



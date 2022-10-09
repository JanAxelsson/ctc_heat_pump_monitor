import time
import jan_heatpump_module as ctc
import jan_shelly_module as plug

status = ctc.compressor_status()
rpm = ctc.compressor_rpm()
radiator_return = ctc.radiator_return()
rad_out = ctc.radiator_out()
outdoor_temp = ctc.outdoor_temp()
warm_water = ctc.warm_water_percent()
brine_in = ctc.brine_in()
brine_out = ctc.brine_out()

print(status)


import time
import jan_heatpump_module as ctc
import jan_shelly_module as plug

ctc.compressor_status()
ctc.compressor_rpm()
ctc.radiator_return()
ctc.radiator_out()
ctc.outdoor_temp()
ctc.warm_water_percent()
ctc.brine_in()
ctc.brine_out()

# ON
plug.on()
time.sleep(5)
plug.getpower()


# OFF
plug.off()
time.sleep(1)
plug.getpower()

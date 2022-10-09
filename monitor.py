import time
import jan_heatpump_module

query_ctc_menu = jan_heatpump_module.query_ctc_menu
shelly_plug_s_on_off = jan_heatpump_module.shelly_plug_s_on_off
shelly_plug_s_getpower = jan_heatpump_module.shelly_plug_s_getpower

DRIFTINFO = 'http://192.168.2.3/click/glob;menu;1;0;112;113'  # First level Drift info on CTC GIS 212 display
DRIFTINFO_PUMP = 'http://192.168.2.3/click/glob;menu;1;0;111'  # submenu on CTC GIS 212 display
DRIFTINFO_VV_O_EL = 'http://192.168.2.3/click/glob;menu;1;0;110'  # submenu on CTC GIS 212 display





query_ctc_menu(DRIFTINFO_PUMP, 64, 'Compressor status')
query_ctc_menu(DRIFTINFO_PUMP, 65, 'Compressor RPM')
query_ctc_menu(DRIFTINFO_PUMP, 75, 'Radiator return')
query_ctc_menu(DRIFTINFO_PUMP, 76, 'Radiator out')
query_ctc_menu(DRIFTINFO, 32, 'Outdoor temp')
query_ctc_menu(DRIFTINFO, 58, 'Warm water %')
query_ctc_menu(DRIFTINFO, 37, 'Brine in')
query_ctc_menu(DRIFTINFO, 38, 'Brine out')

# ON
shelly_plug_s_on_off('on')
time.sleep(5)
shelly_plug_s_getpower()
time.sleep(5)
shelly_plug_s_getpower()
time.sleep(5)
shelly_plug_s_getpower()
time.sleep(5)
shelly_plug_s_getpower()
time.sleep(5)
shelly_plug_s_getpower()
time.sleep(5)
shelly_plug_s_getpower()
time.sleep(5)
shelly_plug_s_getpower()
time.sleep(5)
shelly_plug_s_getpower()
time.sleep(5)
shelly_plug_s_getpower()
time.sleep(5)

# OFF
shelly_plug_s_on_off('off')
time.sleep(1)
shelly_plug_s_getpower()

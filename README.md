ctc_heat_pump_monitor
=====================

monitor and allow for heating wire when brine tubes are squeezed

 

background
----------

After the installation of a CTC 612, the company managed to freeze the whole
partially, so that the brine flow was restricted.There is research that suggests
that this is due to the bore hole freezing at two levels, and the liquid water
in between will eventually freeze and expand at the cost of squeezing the brine
leads. This happens in bore holes that have a long distance down to rock. One
suggested solution is to put a heat wire into the part of the bore hole that is
above solid rock. In my case, I have installed a 27 m head wire

 

this code
---------

the program `ctc_monitor.py` writes CTC 612 data to file `/var/log/ctc_log.txt`.
The module `jan_heatpump_module.py` contains the communication code, and a hard
coded URL to the heat-pump

`ctc_monitor.py` also monitors the power to the wire, controlled by a "Shelly
Plug S". The module `jan_shelly_module.py` contains the communication code, and
a hard coded URL for the power plug.

*NOTE:* work in progress

 

install
-------

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Systemd service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cd ~/ctc_heat_pump_monitor
sudo cp ctc_logger.service /etc/systemd/system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sudo chmod 644 /etc/systemd/system/ctc_logger.service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Auto start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sudo systemctl enable ctc_logger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

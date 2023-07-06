# This script aimed to automate data collection using bluetooth connectivity for experiments but DISTO did not allow direct connection for data retirval.  

import serial
import time
from openpyxl import Workbook
import statistics

from mac_alerts import alerts


port = "/dev/tty.wchusbserial110"  # Replace with the correct port name
uart = serial.Serial(port, 9600, timeout=1)
while True:              
    sensorValue = uart.read(12)
    dat = sensorValue[1:5]

    #dat = int(dat,10)
    
    try:
        dat = int(dat,10)
        #print(dat)
    except ValueError:
        #uart.close()
        continue 

    val = dat-104

    print(val)

    # if(val == 9895):
    #     alerts.play_warning()

    val = 0

   # time.sleep(1)

## Abandoning this scirpt because play_warning() function adds delay 
# which does not allow ultrasonic sensor to collect new data and the sensor throws back old data that is present in its cache. 

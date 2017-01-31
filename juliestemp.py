import Adafruit_BMP.BMP085 as BMP085
import datetime

sensor = BMP085.BMP085()
fd = open('/home/pi/Weather_station/adafruit_readings', 'a')

temp_value = sensor.read_temperature()
pressure_value = sensor.read_pressure()/100.00
time_value = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")	

fd.write('{0}, {1:0.2f}, {2:0.2f} \n'.format(time_value, temp_value, pressure_value))

fd.close()

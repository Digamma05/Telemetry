# scp -r ./main.py pi@raspberrypi.local:~/ADXL343

import time
import math
import board
import adafruit_adxl34x

i2c = board.I2C()
accelerometer = adafruit_adxl34x.ADXL343(i2c)

# time
t = 0.01
# input from accelerometer
a = accelerometer.acceleration
# velocity
v = [0, 0, 0]

sample = 1000
cal = [0, 0, 0]

def calibrate():
  for _ in range(sample):
    # refresh data from accelerometer
    a = accelerometer.acceleration

    cal = [
      (cal[0] + a[0]) / sample,
      (cal[1] + a[1]) / sample,
      (cal[2] + a[2]) / sample
    ]
  print(cal)
    
def run():
  while True:
    # refresh data from accelerometer
    a = accelerometer.acceleration

    v = [
      v[0]+(a[0]-cal[0])*t,
      v[1]+(a[1]-cal[1])*t,
      v[2]+(a[2]-cal[2])*t
    ]
    
    print(v)
    # speed (scalar quantity for v)
    s = math.sqrt((v[0]**2)+(v[1]**2)+(v[2]**2))
    print(s)
    time.sleep(t)
    
def main():
  calibrate()
  run()
  
if __name__ == '__main__':
  main()

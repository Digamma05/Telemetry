# scp -r ./main.py pi@raspberrypi.local:~/ADXL343

import time
import board
import adafruit_adxl34x

i2c = board.I2C()
accelerometer = adafruit_adxl34x.ADXL343(i2c)

t = 0.01 # time
a = accelerometer.acceleration # input from accelerometer
v = [0, 0, 0] # final velocity
u = [0, 0, 0] # initial velocity
run = 1

x = 0
sample = 1000
cal = [0, 0, 0]

while x != sample:
  cal = [
    (cal[0] + a[0]) / sample,
    (cal[1] + a[1]) / sample,
    (cal[2] + a[2]) / sample
  ]
  x = x + 1
  print(cal)

while run == 1:
  v = [
    u[0]+(a[0]-cal[0])*t,
    u[1]+(a[1]-cal[1])*t,
    u[2]+(a[2]-cal[2])*t
  ]
  u = v
  print(v)
  time.sleep(t)
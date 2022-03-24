# scp ./main.py pi@raspberrypi.local:~/ADXL343
# or
# scp -r $(pwd) pi@raspberrypi.local:~/ADXL343

import time
import math
import board
import adafruit_adxl34x
from server import start_server

i2c = board.I2C()
accelerometer = adafruit_adxl34x.ADXL343(i2c)

# delta time
dt = 0.1
# velocity
v = [0, 0, 0]

sample = 100


def calibrate():
    cal = [0, 0, 0]
    for _ in range(sample):
        # refresh data from accelerometer
        a = accelerometer.acceleration

        cal = [
            (cal[0] + a[0]),
            (cal[1] + a[1]),
            (cal[2] + a[2])
        ]
        print(cal)
    cal = [
        cal[0] / sample,
        cal[1] / sample,
        cal[2] / sample
    ]
    print(cal)
    return cal


def run(cal):
    global v
    while True:
        # refresh data from accelerometer
        a = accelerometer.acceleration

        v = [
            v[0] + (a[0] - cal[0]) * dt,
            v[1] + (a[1] - cal[1]) * dt,
            v[2] + (a[2] - cal[2]) * dt
        ]

        print(v)
        # speed (scalar quantity for v)
        s = math.sqrt((v[0] ** 2) + (v[1] ** 2) + (v[2] ** 2))
        print(s)
        time.sleep(dt)


def main():
    cal = calibrate()
    start_server(4506, lambda: v)
    run(cal)


if __name__ == '__main__':
    main()

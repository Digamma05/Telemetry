import time
import random

t = 0.01 # time
a = random.randint(-4, 4) # input from accelerometer
ao = random.uniform(-1, 1) # input from accelerometer when still
v = 0 # final velocity
u = 0 # initial velocity
run = 1
x = 0
sample = 1000
cal = 0

while x != sample:
  cal = cal + ao
  ao = random.uniform(-1, 1)
  x = x + 1
cal = cal / sample
print(cal)

while run == 1:
  v = u+(a-cal)*t
  u = v
  print(v)
  time.sleep(t)
  a = random.randint(-5000, 5000)
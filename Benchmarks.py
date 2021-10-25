import os
from time import time
with open('file.txt','w') as f:
  f.write("Score per 20 processes")

print("This program Will tell you the Cpu Benchmark score of Your Device Please Wait 30s-45s Depending on The Processor")
def timereps(reps, func):
    start = time()
    for i in range(0, reps):
        func()
    end = time()
    return (end - start) / reps
y = 0
x=1
for x in range(20):
  listdir_time = timereps(10000, lambda: os.listdir('/'))
  #print("This device is running %d commands per second" % (1 / listdir_time))
  with open('file.txt','a') as f:
    f.write(f"\n {1 / listdir_time} Processes in {x} Interval ")
  x = x+1
  y = y + 1/listdir_time

print(f"the Cpu benchmark Score For This Device is {round(y)}, A text File is Saved of Every Process Score")
a = input("How Did you like This Program (Y/N)")

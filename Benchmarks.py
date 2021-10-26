import os
from time import time
from tkinter import *
import shutil
import threading

def start_submit_thread(event):
    global submit_thread
    submit_thread = threading.Thread(target=run)
    submit_thread.start()
    window.after(20, check_submit_thread)

def check_submit_thread():
    if submit_thread.is_alive():
        window.after(20, check_submit_thread)




  
def run():
  with open('file.txt','w') as f:
    f.write("Score per 20 processes")
  t1.delete('1.0', END)
  t1.insert(END,"Please Wait 30s-45s Depending on The Processor")
  y = 0
  x=1
  for x in range(20):
    
    t2.delete('1.0', END)
    t2.insert(END,f"Running Code {x*5}% done")
    start = time()
    for i in range(0, 10000):
        os.listdir('/')
    end = time()
    listdir_time = (end - start) / 10000
    #print("This device is running %d commands per second" % (1 / listdir_time))zzz
    with open('file.txt','a') as f:
      f.write(f"\n {1 / listdir_time} Processes in {x} Interval ")
    y = y + 1/listdir_time
   
    x = x+1    
    with open('file.txt','a') as f:
      f.write(f"\n {round(y)} is the final Score of all the 20 Intervals ")
  t2.delete('1.0', END)
  t2.insert(END,f"{round(y)} is your score")
  t1.delete('1.0', END)
  t1.insert(END,"Detailed information is in the Notepad File Attached")

#print(f"the Cpu benchmark Score For This Device is {round(y)}, A text File is Saved of Every Process Score")


window = Tk()
window.title('Benchmark')
window.iconphoto(False,PhotoImage(file='c://Users/jasja/OneDrive/Desktop/Benchmarksgit/Benchmark.png'))

t1 = Text(window,height=1,width=52)
t1.grid(row=0,column=0,columnspan=3)
t1.insert(END,"This Program tells you The Benchmark of your device")

l1 = Label(window,text="Click this Button to know Your Score",height=1,width=30)
l1.grid(row=1,column=0)

b1 = Button(window,text="Calculate",width=12,command=lambda:start_submit_thread(None))
b1.grid(row=1,column=1)


l1 = Label(window,text="Your Score of Device",height=1,width=40)
l1.grid(row=2,column=0,columnspan=2)

t2=Text(window,height=1,width=40)
t2.grid(row=2,column=1,columnspan=2)


window.mainloop()

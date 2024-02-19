from progress.bar import ChargingBar
from progress.bar import Bar
import time
import random
import os

a = 0

while 0<1:

    time.sleep(3)
    bar = Bar('Processing', max=20)

    while a<20:
        track = random.randint(1,100000)
        if track == 2:
            a = a+1
            time.sleep(0.3)
            


            bar.next()
        
    bar.finish()
    #os.system("cls")

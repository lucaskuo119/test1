from progress.bar import ChargingBar
from progress.bar import Bar
import time
import random
import os



while 0<1:
    a = 0
    time.sleep(1)
    bar = ChargingBar('Processing', max=20)

    while a<20:
        track = random.randint(1,100000)
        if track == 2:
            a = a+1
            time.sleep(0.1)
            


            bar.next()
        
    bar.finish()
    os.system("cls")
    time.sleep(1)

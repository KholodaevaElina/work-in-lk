import RPi.GPIO as GPIO
import time


GPIO.setmode (GPIO.BCM)
#GPIO.setup (24, GPIO.OUT)
#GPIO.output (24, 1)
#time.sleep(1)
#GPIO.output(24,0)
#GPIO.cleanup (24)

array_cvetodiodov = [24,25,8,7,12,16,20,21]

GPIO.setup (array_cvetodiodov, GPIO.OUT)

def lightUp (ledNumber, period):
    GPIO.output (array_cvetodiodov[ledNumber], 1)
    time.sleep (period)
    GPIO.output (array_cvetodiodov[ledNumber],0)



def blink (ledNumber, blinkCount, blinkPeriod):
    count = 0
    while count < blinkCount:
         GPIO.output (array_cvetodiodov[ledNumber], 1)
         time.sleep (blinkPeriod)
         GPIO.output (array_cvetodiodov[ledNumber], 0)
         time.sleep (blinkPeriod)
         count += 1

def runningLight (count, period):
    my_count = 0
    my_count_round = 0
    
    while my_count_round < count:
        while my_count < 8:
             GPIO.output (array_cvetodiodov[my_count], 1)
             time.sleep (period)
             GPIO.output (array_cvetodiodov[my_count], 0)
             my_count += 1
        my_count_round += 1


def runningDark (count, period):
    GPIO.output (array_cvetodiodov, 1)

    my_count_round = 0
    my_count = 0

    while my_count_round < count:
         while my_count < 8:
             GPIO.output (array_cvetodiodov[my_count], 0)
             time.sleep (period)
             GPIO.output (array_cvetodiodov[my_count], 1)
             my_count += 1
         my_count_round += 1
         my_count = 0
        
def decToBinList (decNumber):
    rezult = []

    while decNumber > 0:
        rezult.insert (0, decNumber % 2) 
        decNumber = decNumber // 2
    
    while len (rezult) < 8:
        rezult.insert (0, 0)

    return rezult

def runningPattern (pattern, direction):
    GPIO.output (array_cvetodiodov, 0)
    arr = decToBinList (pattern)
    array = [0] * 8

    for t in range (0, 9):
        for i in range (0, 8):
            array [i] = arr [(i + t*direction) % 8]
        for j in range (0, 8):
            if array [7 - j] == 1:
                GPIO.output (array_cvetodiodov, 1)
        time.sleep (1)
        GPIO.output (array_cvetodiodov, 0)









   

#lightUp (2,1)
#blink (0, 2, 1)
#runningLight (2, 1)
#runningDark (2, 1)
print (decToBinList (133))
#runningPattern (3, 2)
GPIO.cleanup (array_cvetodiodov)



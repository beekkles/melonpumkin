import random
import time


flyingMachineTick = 10 #tarda 10 ticks para cada bloque

gameTick = 0
testPeriodHours = 10
testPeriodSeconds = testPeriodHours * 3600
testPeriodTicks = testPeriodSeconds * 20 + 30

assertNum = 1986

def blockTicked(n):
    rNum1 = random.randint(0, 4095)
    rNum2 = random.randint(0, 4095)
    rNum3 = random.randint(0, 4095)

    if assertNum == rNum1 or assertNum == rNum2 or assertNum == rNum3:
        return True
    return False


trues,falses = 0,0

while gameTick < testPeriodTicks:
    if blockTicked(assertNum):
        trues+=1
    else:
        falses+=1
        
    gameTick += 1
    print(gameTick,testPeriodTicks)

print(trues/(trues+falses))
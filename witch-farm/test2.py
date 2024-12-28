'''
2 ticks para que se active
5 por cada paso del agua, hay 7, son 35 ticks
intermedio...
2 para que se desactive
35 para que se vaya el agua

74+intermedio, vemos con 74 primero y ya
'''
#inactive = 74

import random
import matplotlib.pyplot as plt

def initialize_layers():
    return [[[False] * 9 for _ in range(7)] for _ in range(3)]

def initialize_mobcap():
    return [0, 0, 0]

heightMap = 72
max_mobcap = 70
layers = initialize_layers()
mobcap = initialize_mobcap()

testPeriodHours = 10
testPeriodSeconds = testPeriodHours * 3600
testPeriodTicks = testPeriodSeconds * 20

#no lo necesitaremos pq la idea es 24-32 bloques
#despawn = 1/800

def generate_mobs(layers, heightMap):
    global mobcap
    if sum(mobcap) >= max_mobcap:
        return
    
    for _ in range(3):
        layer_index = random.randint(0, len(layers) - 1)
        layer = layers[layer_index]
        i = random.randint(0, len(layer) - 1)
        j = random.randint(0, len(layer[i]) - 1)

        if random.randint(1, heightMap) == 1:
            if layer[i][j] == False:
                layer[i][j] = True

                mobcap[layer_index] += 1

                for _ in range(random.randint(0, 3)):
                    offset_i = i + random.randint(-5, 5)
                    offset_j = j + random.randint(-5, 5)
                    if 0 <= offset_i < len(layer) and 0 <= offset_j < len(layer[i]):
                        layer[offset_i][offset_j] = True
                        mobcap[layer_index] += 1

def test_farm(clock):
    global mobcap
    global layers
    res = 0
    tick = 0
    while tick < testPeriodTicks:
        if tick % clock == 0:
            res += sum(mobcap)
            tick = tick + 74 + 200
            mobcap = initialize_mobcap()
            layers = initialize_layers()

        generate_mobs(layers, heightMap)

        tick = tick + 1

    return res/testPeriodHours

clocks = range(1000, 2000 + 1, 2)
results = []

for clock in clocks:
    res = test_farm(clock)
    results.append(res)

plt.plot(clocks, results)
plt.xlabel('Clock Interval')
plt.ylabel('Avg. Witch\'s per Hour')
plt.title('Farm Efficiency vs Clock Interval')
plt.show()

max_result = max(results)
max_clock = clocks[results.index(max_result)]
print(max_clock/20, max_result)


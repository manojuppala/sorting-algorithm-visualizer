import time


def opt_bubble(data, drawData, timeTick):
    for _ in range(len(data)-1):
        swapped=False
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped=True
                drawData(data, ['green' if x == j or x == j +1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
        if not swapped:
            break    
    drawData(data, ['green' for x in range(len(data))])

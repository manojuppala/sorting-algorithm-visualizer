import time


def selection(data, drawData, timeTick):
    sort = 0
    mini_pos = 0
    while(sort != (len(data)-1)):
        mini = data[sort]
        for i in range(sort, len(data)):
            if(mini > data[i]):
                mini = data[i]
                mini_pos = i
        data[mini_pos], data[sort] = data[sort], data[mini_pos]
        sort += 1
        drawData(
            data, ['green' if x < sort else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])

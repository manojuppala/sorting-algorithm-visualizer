import time

def opt_bubble(data, drawData, timeTick,changetext):
    swap=0
    compare=0
    complexity='O(n^2)'
    for _ in range(len(data)-1):
        swapped=False
        for j in range(len(data)-1):
            compare+=1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped=True
                swap+=1
                changetext(swap, compare,complexity)
                drawData(data, ['green' if x == j or x == j +1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
            changetext(swap, compare,complexity)
        if not swapped:
            break    
    drawData(data, ['green' for x in range(len(data))])

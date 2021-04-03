import time

def heapify(data, n, i,drawData,timeTick):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and data[i] < data[l]:
        largest = l
 
    if r < n and data[largest] < data[r]:
        largest = r
  
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        drawData(data, ['green' if x == i or x == largest else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        heapify(data, n, largest,drawData,timeTick)
  
  
def heapsort(data,drawData,timeTick):
    n = len(data)
  
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(data, n, i,drawData,timeTick)
  
    for i in range(n-1, 0, -1):
        # Swap
        data[i], data[0] = data[0], data[i]
        drawData(data, ['green' if x == i or x == 0 else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        # Heapify root element
        heapify(data, i, 0,drawData,timeTick)
    drawData(data, ['green' for x in range(len(data))])
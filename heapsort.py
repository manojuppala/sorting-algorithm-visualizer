import time
swap=0
compare=0
complexity='O(nlog(n))'
def heapify(data, n, i,drawData,timeTick,changetext):
    global swap
    global compare
    global complexity
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and data[i] < data[l]:
        largest = l
        compare+=1
        changetext(swap, compare,complexity)
 
    if r < n and data[largest] < data[r]:
        largest = r
        compare+=1
        changetext(swap, compare,complexity)
  
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        compare+=1
        swap+=1
        changetext(swap, compare,complexity)
        drawData(data, ['green' if x == i or x == largest else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        heapify(data, n, largest,drawData,timeTick,changetext)
  
  
def heapsort(data,drawData,timeTick,changetext):
    global swap
    global compare
    global complexity
    n = len(data)
  
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(data, n, i,drawData,timeTick,changetext)
  
    for i in range(n-1, 0, -1):
        # Swap
        data[i], data[0] = data[0], data[i]
        swap+=1
        changetext(swap, compare,complexity)
        drawData(data, ['green' if x == i or x == 0 else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        # Heapify root element
        heapify(data, i, 0,drawData,timeTick,changetext)
    drawData(data, ['green' for x in range(len(data))])
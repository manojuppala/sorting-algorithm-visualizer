import time


def insertionSort(data,drawData,timeTick,changetext):
    swap=0
    compare=0
    complexity='O(n^2)'
    for i in range(1,len(data)):
        cur=data[i]
        j=i-1
        compare+=1
        changetext(swap, compare,complexity)
        while j >=0 and cur < data[j]:
            data[j+1]=data[j]
            swap+=1
            changetext(swap, compare,complexity)
            j-=1
        data[j+1]=cur
        drawData(data, ['green' if x < i else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
    
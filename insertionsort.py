import time


def insertionSort(data,drawData,timeTick):
    for i in range(1,len(data)):
        cur=data[i]
        j=i-1
        while j >=0 and cur < data[j]:
            data[j+1]=data[j]
            j-=1
        data[j+1]=cur
        drawData(
            data, ['green' if x < i else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
    
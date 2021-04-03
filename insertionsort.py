import time


def insertionSort(data,drawData,timeTick):
    for i in range(1,len(data)):
        cur=data[i]
        j=i-1
        while j >=0 and cur < data[j]:
            drawData(data ,getcolor(len(data),i,j))
            time.sleep(timeTick)

            data[j+1]=data[j]
            j-=1
        data[j+1]=cur
        time.sleep(timeTick)
    

def getcolor(length , cur,j_s):
    colorArray=[]
    for i in range(length):
        if i==cur:
            colorArray.append('pink')
        elif i==j_s:
            colorArray.append('cyan')
        elif i < cur:
            colorArray.append('green')

        else :
            colorArray.append('white')

    return colorArray
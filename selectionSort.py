import time


def selection(data, drawData, timeTick):
        for i in range(0,len(data)):
            min_pos=i
            for j in range(i+1,len(data)):
                if data[j]< data[min_pos]:
                  min_pos=j
            drawData(data,getcolor(len(data),i,min_pos ,i))
            time.sleep(timeTick)
            data[min_pos],data[i]=data[i],data[min_pos]
            drawData(data,getcolor(len(data),min_pos,i,i))
            time.sleep(timeTick)

                
          

            # drawData(
            # data, ['green' if x <= i else 'white' for x in range(len(data))])
            time.sleep(timeTick)


def getcolor(length,x,y,static):
    colorArray=[]
    for i in range(length):
        if i==x:
            colorArray.append('yellow')
        elif i==y:
            colorArray.append('pink')
        elif i < static:
            colorArray.append('green')
        else:
            colorArray.append('white')
    return colorArray
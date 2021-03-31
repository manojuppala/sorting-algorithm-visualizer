import time


def selection(data, drawData, timeTick):
        for i in range(0,len(data)-1):
            min_pos=i
            for j in range(i+1,len(data)):
                if data[j]< data[min_pos]:
                  min_pos=j
            data[min_pos],data[i]=data[i],data[min_pos]
                
          

            drawData(
            data, ['green' if x < i else 'red' for x in range(len(data))])
            time.sleep(timeTick)
        drawData(data, ['green' for x in range(len(data))])

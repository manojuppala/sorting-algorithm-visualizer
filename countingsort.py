import time

def countingSort(data,drawData,timeTick):

	output = [0 for i in range(len(data))]
	count = [0 for i in range(max(data)+1)]
	for i in data:
		count[i] += 1
	#counting the elements having distinct values
	for i in range(1,max(data)):
		count[i] += count[i-1]

	for i in range(len(data)):
		output[count[data[i]-1]] = data[i]
		count[data[i]-1] -= 1
		drawData(output, ['green' if x == i else 'red' for x in range(len(output))])
		time.sleep(timeTick)
	drawData(output, ['green' for x in range(len(output))])
	
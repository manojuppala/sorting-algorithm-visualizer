import time

def countingSort(data, exp1,drawData,timeTick):
	n = len(data)
	output = [0] * (n)
	count = [0] * (10)

	for i in range(0, n):
		index = (data[i] / exp1)
		count[int(index % 10)] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	i = n - 1
	while i >= 0:
		index = (data[i] / exp1)
		output[count[int(index % 10)] - 1] = data[i]
		count[int(index % 10)] -= 1
		i -= 1

	i = 0
	for i in range(0, len(data)):
		data[i] = output[i]
		drawData(data, ['green' if x == i or x == i +1 else 'red' for x in range(len(data))])
		time.sleep(timeTick)

# Method to do Radix Sort
def radixSort(data,drawData,timeTick):
	max1 = max(data)
	exp = 1
	while max1 / exp > 0:
		countingSort(data, exp,drawData,timeTick)
		exp *= 10
	drawData(data, ['green' for x in range(len(data))])
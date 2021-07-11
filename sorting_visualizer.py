from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
from selectionSort import selection
from insertionsort import insertionSort
from optimized_bubble import opt_bubble
from heapsort import heapsort
from radixsort import radixSort
from countingsort import countingSort
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

# variables
selected_alg = StringVar()
data = []
reset_data = []
var1 = IntVar()

# function

def drawData(data, colorArray):
	canvas.delete("all")
	c_height = 380
	c_width = 680
	x_width = c_width / (len(data) + 1)
	offset = 30
	spacing = 10
	normalizedData = [i / max(data) for i in data]
	for i, height in enumerate(normalizedData):
		# top left
		x0 = i * x_width + offset + spacing
		y0 = c_height - height * 340
		# bottom right
		x1 = (i + 1) * x_width + offset
		y1 = c_height

		canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
		canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
	
	root.update_idletasks()

def changetext(swap,compare,complexity):
	l1.config(text=("Complexity:"+complexity+"    Swaps:"+str(swap)+"    Compares:"+str(compare)))

def Reset():
	global reset_data
	global data
	data=reset_data[:]
	drawData(data, ['red' for x in range(len(data))])
	changetext(0,0,"O()")

def Generate():
	global data
	global reset_data
	global var1
	minVal = int(minEntry.get())
	maxVal = int(maxEntry.get())
	size = int(sizeEntry.get())
	data = []
	if(var1.get() == 0):
		if (maxVal-minVal+1 < size  ):
			messagebox.showwarning('Warning','Differnce of Max Value and Min Value is smaller than the Data Size')
			return
		else:
			 for _ in range(size):
				 v=random.randrange(minVal,minVal+1)
				 while v in data:  
					 v=random.randrange(minVal,maxVal+1)
				 data.append(v)
	elif(var1.get() == 1):
		for _ in range(size):
			data.append(random.randrange(minVal, maxVal+1))
	reset_data=data[:]
	drawData(data, ['red' for x in range(len(data))])  # ['red', 'red' ,....]

def StartAlgorithm():
	global data
	if not data:
		return

	if algMenu.get() == 'Quick Sort':
		quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
		drawData(data, ['green' for x in range(len(data))])

	elif algMenu.get() == 'Bubble Sort':
		bubble_sort(data, drawData, speedScale.get(),changetext)
	
	elif algMenu.get() == 'Optimized Bubble':
		opt_bubble(data, drawData, speedScale.get(),changetext)

	elif algMenu.get() == 'Merge Sort':
		merge_sort(data, drawData, speedScale.get())

	elif algMenu.get() == 'Selection Sort':
		selection(data, drawData, speedScale.get())

	elif algMenu.get() == 'Insertion Sort':
		insertionSort(data, drawData, speedScale.get(),changetext)

	elif algMenu.get() == 'Heap Sort':
		heapsort(data, drawData, speedScale.get(),changetext)

	elif algMenu.get() == 'Radix Sort':
		radixSort(data, drawData, speedScale.get())
	
	elif algMenu.get() == 'Counting Sort':
		countingSort(data, drawData, speedScale.get())



# frame / base lauout
UI_frame = Frame(root, width=700, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=0, pady=0)

canvas = Canvas(root, width=710, height=380, bg='white')
canvas.grid(row=1, column=0, padx=0, pady=0)

l1=Label(root, text="start the sorting algorithm!!!",bg='black',fg='white')          
l1.grid(row=2, column=0, padx=0, pady=0)

# User Interface Area
# Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(
	row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=[
					   'Bubble Sort','Optimized Bubble', 'Quick Sort', 'Merge Sort', 'Selection Sort', 'Insertion Sort','Heap Sort','Radix Sort','Counting Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2,
				   resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm,
	   bg='red').grid(row=0, column=3, padx=(5,0), pady=5)
Checkbutton(UI_frame, text='duplicates',variable=var1, onvalue=1, offvalue=0,command=Generate).grid(row=0, column=4, padx=(0,5), pady=5)

# Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=35, resolution=1,orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=1, to=11, resolution=1,
				 orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100,length=200, resolution=1,
				 orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=0, pady=5)

Button(UI_frame, text="Generate", command=Generate,
	   bg='white').grid(row=1, column=3, padx=5, pady=5)
Button(UI_frame, text="Reset", command=Reset,
	   bg='white').grid(row=1, column=4, padx=5, pady=5)

root.mainloop()

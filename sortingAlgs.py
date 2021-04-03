from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
from selectionSort import selection
from insertionsort import insertionSort
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

# variables
selected_alg = StringVar()
data = []

# function


def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 450
    c_width = 800
    x_width = c_width / (len(data) + 3)
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


def Generate():
    global data
    data.clear()

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    if (maxVal-minVal < size  ):
        messagebox.showwarning('Warning','Differnce of Max Value and Min Value is smaller than the Data Size') # needed condition otherwise , result in infinite while loop later
        return 


    for _ in range(size):
        v=random.randrange(minVal,minVal+1)
        while v in data: # needed loop to not add duplicates in the list . 
            v=random.randrange(minVal,maxVal+1)
        
        data.append(v)

    drawData(data, ['red' for x in range(len(data))])  # ['red', 'red' ,....]


def StartAlgorithm():
    global data
    if not data:
        return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())

    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Selection Sort':
        selection(data, drawData, speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        insertionSort(data, drawData, speedScale.get())

    drawData(data, ['green' for x in range(len(data))])


# frame / base lauout
UI_frame = Frame(root, width=800, height=300, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=800, height=450, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface Area
# Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=[
                       'Bubble Sort', 'Quick Sort', 'Merge Sort', 'Selection Sort', 'Insertion Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2,
                   resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm,
       bg='red').grid(row=0, column=3, padx=5, pady=5)

# Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1,
                  orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1,
                 orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1,
                 orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate,
       bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()

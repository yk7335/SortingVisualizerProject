import random
from tkinter import*
from tkinter import ttk
from BubbleSort import*
from QuickSort import*
from MergeSort import*

base = Tk()
base.title("Sorting Visualizer") # header of the window
base.maxsize(1200,1200) # max width and height
base['bg'] = '#49A' # background color

# variables
algorithmColorCoding = StringVar()
seleted_algorithm = StringVar()
data = []
global i
i = 4
# drawing the arrays
def drawData(data, colorArray):
    canvas.delete("all")
    canvasHeight = 380
    canvasWidth = 600
    BarGraphWidth = canvasWidth / (len(data) + 1)
    offset = 30
    spacingBetweenBars = 5
    normalizeDataForBetterFit = [i/max(data) for i in data]
    for i, height in enumerate(normalizeDataForBetterFit):
        #calculating top left corner
        TopLeftCornerX = i * BarGraphWidth + offset + spacingBetweenBars
        TopLeftCornerY = canvasHeight - height * 360
        # bottom right corner
        BottomRightCornerX = (i+1) * BarGraphWidth + offset
        BottomRightCornerY = canvasHeight
        ## creating rectangles
        canvas.create_rectangle(TopLeftCornerX, TopLeftCornerY, BottomRightCornerX, BottomRightCornerY, fill = colorArray[i])
        # writing the value of the array
        canvas.create_text(TopLeftCornerX+2, TopLeftCornerY + 2, anchor = SW, text = str(data[i]), fill="yellow")
    base.update_idletasks()
# making the sorting function
def Generate():
    global data

    try:
        MinValue = int(MinEntry.get())
    except:
        MinValue = 1
    try:
        MaxValue = int(MaxEntry.get())
    except:
        MaxValue = 10
    try:
        size = int(sizeEntry.get())
    except:
        size = 10

    data = []
    for _ in range(size):
        data.append(random.randrange(MinValue, MaxValue + 1))

    drawData(data, ['pink' for x in range(len(data))])



def StartAlgorithm():
    global data
    if not data: return

    if(algorithmMenu.get() == 'Quick Sort'):
        QuickSort(data, 0, len(data)-1, drawData, speedScale.get())
    elif(algorithmMenu.get() == 'Bubble Sort'):
        BubbleSort(data, drawData, speedScale.get())
    elif(algorithmMenu.get() == 'Merge Sort'):
        mergesort(data, drawData, speedScale.get())
    drawData(data, ['green' for x in range(len(data))])


# making three diferent frames

# user interphase where the user will change the arrays
User_Interpahse_Frame = Frame(base, width = 600, height = 200, bg='light blue')
User_Interpahse_Frame.grid(row = 0, column = 0, padx = 10, pady = 5)

# where the result will be changed i.e. the arrays out putted and being sorted.
canvas = Canvas(base, width=650, height = 380, bg='black')
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

# where the index of color coding will be
ColorCodingCanvas = Canvas(base, width = 100, height = 100, bg='light blue')
ColorCodingCanvas.grid(row = 2, column = 0, padx = 10, pady = 5)

# User interface Frame
# Row 0
Label(User_Interpahse_Frame, text="Choice of Algorithm: ", bg='light blue').grid(row = 0, column = 0, sticky = W)
algorithmMenu = ttk.Combobox(User_Interpahse_Frame, textvariable= seleted_algorithm, values = ['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algorithmMenu.grid(row = 0, column = 1, padx = 5, pady = 5)
algorithmMenu.current(0)
speedScale = Scale(User_Interpahse_Frame, from_ = 2.0, to = .1, length = 200, digits = 2, resolution = 0.1, orient = HORIZONTAL, label = "Select Speed of Algorithm (sec)")
speedScale.grid(row = 0, column = 2, padx = 5, pady = 5)
Button(User_Interpahse_Frame, text = "Start", command = StartAlgorithm, bg = 'yellow').grid(row = 0, column = 3, padx = 5, pady = 5)

# Row 1
sizeEntry = Scale(User_Interpahse_Frame, from_ = 3, to = 50, resolution = 1, orient = HORIZONTAL, label = "Array Size:")
sizeEntry.grid(row = 1, column = 0)

MinEntry = Scale(User_Interpahse_Frame, from_ = 0, to = 1000, resolution = 1, orient = HORIZONTAL, label = "Min Value: ")
MinEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

MaxEntry = Scale(User_Interpahse_Frame, from_ = 10, to = 1000, resolution = 1, orient = HORIZONTAL, label = "Max Value:")
MaxEntry.grid(row = 1, column = 2, padx = 5, pady = 5)

Button(User_Interpahse_Frame, text = "Create Arrays", command = Generate, bg = 'yellow').grid(row = 1, column = 3, padx = 5, pady = 5)

# Row 4
textSample = "Bubble Sort: Pink = Default Color   Red = Numbers being Compared    Green = Finished Array \n " \
             "\n Quick Sort: Gray = Default / Blue = highest index / Pink = Correct Position / Red = Border / Yellow = Current Index / Green = Comparing to Swap"
Label1 = Label(ColorCodingCanvas, text=textSample, bg='light blue').grid(row=2, column=0, sticky=W)



base.mainloop()
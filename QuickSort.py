import time
def GetPivot(data, low, high):
    return (high+low)//2

def partition(data, low, high, drawdata, timeTick):
    border = low
    PivotIndx = GetPivot(data, low, high)
    PivotValue = data[PivotIndx]
    drawdata(data, getColorArray(len(data), low, high, border, border))
    time.sleep(timeTick)
    data[PivotIndx], data[low] = data[low], data[PivotIndx] # makes our pivot value the left most value


    for i in range(low, high+1):
        if data[i] < PivotValue:
            drawdata(data, getColorArray(len(data), low, high, border, i, True))
            time.sleep(timeTick)
            border+=1
            data[i], data[border] = data[border], data[i]
        drawdata(data, getColorArray(len(data), low, high, border, i))
        time.sleep(timeTick)

    drawdata(data, getColorArray(len(data), low, high, border, low, True))
    time.sleep(timeTick)
    data[low], data[border] = data[border], data[low]
    return border

def QuickSort(data, low, high, drawData, timeTick):
    if low < high:
        p = partition(data, low, high, drawData, timeTick)
        QuickSort(data, low, p - 1 , drawData, timeTick)
        QuickSort(data, p + 1, high, drawData, timeTick)


def getColorArray(dataLen, low, high, border, CurrentIdx, isSwapping = False):
    CollorArray = []
    for i in range(dataLen):
        if i >= low and i <= high:
            CollorArray.append('gray')
        else:
            CollorArray.append("pink")
        if i == high:
            CollorArray[i] = 'blue'
        elif i == border:
            CollorArray[i] = 'red'
        elif i == CurrentIdx:
            CollorArray[i] = 'yellow'
        if isSwapping:
            if i == border or i == CurrentIdx:
                CollorArray[i] = 'green'
    return CollorArray
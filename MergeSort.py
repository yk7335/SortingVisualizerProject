import time

def mergesort(array, drawData, timeTick):
    if len(array) > 1:
        middle = len(array) // 2
        LArray = array[:middle] # making lefft side of array equal to the left array
        RArray = array[middle:] # making the right side of array equal to right array

        mergesort(LArray, drawData, timeTick)
        mergesort(RArray, drawData, timeTick)

        i = j = k = 0
        while i < len(LArray) and j < len(RArray):
            if LArray[i] < RArray[j]:
                array[k] = LArray[i]
                i += 1
            else:
                array[k] = RArray[j]
                j += 1
            k += 1

        while i < len(LArray):
            array[k] = LArray[i]
            i += 1
            k += 1

        while j < len(RArray):
            array[k] = RArray[j]
            j += 1
            k += 1

def ShiftArray(arr,n):

    if not len(arr)%2:
       i = int(len(arr)/2)
    else:
        i = int(len(arr)/2)+1
    arr[i: i] = [n]
    return arr

print(ShiftArray([2,4,6,8,9,11],10))



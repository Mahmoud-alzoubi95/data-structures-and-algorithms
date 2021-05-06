

def ShiftArray(arr,num):

  newarr = []
  i=0

  while i<len(arr):

    if arr[i]<num and arr[i+1]>num:
      newarr.append(arr[i])
      newarr.append(num)
    else:
      newarr.append(arr[i])
    i+=1
  return newarr

print(ShiftArray([2,4,6,8],5))


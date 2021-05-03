def ShiftArray(arr,num):
  newarr = []
  i=0

  while i<len(arr):

    if arr[i]<num and arr[i+1]>num:
      newList.append(arr[i])
      newList.append(num)
    else:
      newList.append(arr[i])
    i+=1
  return newarr


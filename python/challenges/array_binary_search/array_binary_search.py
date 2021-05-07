
def binary_search(input_list,num):
    srart = 0
    length_list = len(input_list) - 1
    midpoint = 0

    while srart <= length_list:

        midpoint = (length_list + srart) // 2

        # Check if num is present at midpoint
        if input_list[midpoint] < num:
            srart = midpoint + 1

        # If num is greater, ignore left half
        elif input_list[midpoint] > num:
            length_list = midpoint - 1

        # If num is smaller, ignore right half
        else:
            return midpoint

    # If we reach here, then the element was not present
    return -1

# input_list=[4,8,15,16,23,42]
# num=15
# print(BinarySearch(input_list,num))

## Challenge Summary
Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1).Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1).

## Challenge Description
input: two linked list output: 1 linked list merged (zipped) in pair form

## Approach & Efficiency
pass two nodes from two linked list the nmerge it as one linked list

## whiteBoard

<img src="../../../../assets/ch08.png">

## solution
```
List1 = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> NULL"
List2 = "{ 6 } -> { 7 } -> { 8 } -> { 9 } -> { 10 } -> NULL"
def zipLists(list1,list2):
    if not list1:
        return list2
    elif not list2:
        return list1
    zip_list=Linked_list()
    current1=list1
    current1=current1.head
    current2=list2.head
    while current1 or current2:
        if current1:
            zip_list.append_node(current1.data)
            current1=current1.next
        if current2:
            zip_list.append_node(current2.data)
            current2=current2.next
    return zip_list


a= zipLists(list1,list2)
print(a)

output:
{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 8 } -> { 9 } -> { 10 } -> NULL

```



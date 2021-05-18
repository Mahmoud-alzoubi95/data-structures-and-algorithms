# from python.challenges.Data_Structures.linked_list.linked_list import Node,Linked_list
from linked_list import Node,Linked_list

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

if __name__=='__main__':
    list1=Linked_list()
    list2=Linked_list()
    list1.append_node("1")
    list1.append_node("3")
    list1.append_node("5")
    list1.append_node("7")
    list2.append_node("2")
    list2.append_node("4")
    list2.append_node("6")
    list2.append_node("8")
    list2.append_node("9")
    list2.append_node("10")

    a=zipLists(list1,list2)
    print(a)

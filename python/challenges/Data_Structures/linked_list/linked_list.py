# Define Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# use a magic method so when you print node you see it's value
    def __str__(self):
        return f"{self.data}"

# Define linked list


class Linked_list:

  # Constructor
    def __init__(self):
        self.head = None

  # define your insert method
    def insert_node(self, data=None):
        new_node = Node(data)
    # Once we have a head
        if self.head:
            new_node.next = self.head  # set our current pointer to the head
        # Assign new_node to current.next
        self.head = new_node

    def append_node(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insertBefore(self,data,new_data):
        new_node = Node(new_data)
        before = self.head
        if not before.data == data:
            old=before
            while before:
                if before.data == data:
                    new_node.next = before
                    old.next = new_node
                    return
                else:
                    old = before
                    before = before.next

    def insertAfter(self,prev_node, data):
        new_node = Node(data)
        before=self.head
        if prev_node:
            while before:
                if before.data==prev_node:
                    new_node.next=before.next
                    before.next=new_node
                    return
                before=before.next




# Define a method called includes which takes any value as an argument and returns a boolean result
# depending on whether that value exists as a Node’s value somewhere within the list.

    def includes(self,data):
        current=self.head
        while current:
            if data==current.data:
                print("True")
                return True
            else:
                current=current.next
        print("False")
        return False


    def kth_from_the_end(self, k):
        current = self.head
        count = 0

        if k < 0 :
            print("wrong value")
            return "wrong value"

        while current.next:
            current = current.next
            count += 1

        if k >= count:
            print("out of the index")
            return "out of the index"

        current = self.head

        for j in range(count - k):
            current = current.next
        print(current.data)
        return current.data




    def __str__(self):
        """ Returns a string representaiton of the linked list
            1 -> 3 -> 4 -> Null
        """
        # step 0 - create a new empty string
        list_data = ""
        # step 1 iterate over each node
        current = self.head
        while current:
        # step 2 - insert each data to the string
            list_data += "{ %s } -> " %(current.data,)
        # step 2b:  move to the next item
            current = current.next
        list_data += "NULL"
        # step 3 - return the final string
        return list_data




# Print the Nodes
if __name__ == "__main__":
  linked = Linked_list()
#   linked.insert_node()
  linked.insert_node(27)
  linked.insert_node("Alzoubi")
  linked.insert_node("Mahmoud")
#   linked.append_node("hassan")
#   linked.append_node("ahmad")
#   linked.insertBefore(27,"khaled")
#   linked.insertAfter(27,"khaled")
  linked.kth_from_the_end(5)
  print(linked)
#   print(linked.includes("khaled"),linked.includes("Mahmoud"),linked.includes(27))




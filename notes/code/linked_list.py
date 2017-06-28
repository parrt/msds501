# Hmm.... python classes are not so clear.
class LinkedList:
    pass

class Node:
    def __str__(self):
        return str(self.value)

names = LinkedList()
names.head = None

def add(llist,x):
    newnode = Node()
    newnode.value = x
    newnode.next = llist.head
    llist.head = newnode

def printlist(llist):
    p = llist.head
    while p is not None:
        print p
        p = p.next

add(names, "ter")
add(names, "mary")
printlist(names)

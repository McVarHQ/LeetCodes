class Node:
    def __init__(self, x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self, x):
        new_node=Node(x)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=new_node

    def printList(self):
        curr=self.head
        while(curr!=None):
            print(curr.data, end= ' ')
            curr=curr.next
        print()

def reverse(node):
    curr = node
    temp = None
    while(curr!=None):
        new_node = Node(curr.data)
        new_node.next=temp
        temp=new_node
        curr=curr.next

    return temp

def palindrome(l):
    fp = l.head
    sp = l.head

    while(fp.next!=None and fp.next.next!=None):
        fp=fp.next.next
        sp=sp.next

    curr1=l.head
    curr2=sp.next
    sp.next=None

    curr2 = reverse(curr2)

    while(curr2!=None):
        print(curr1.data, curr2.data)
        if curr1.data!=curr2.data:
            return 'false'

        curr1 = curr1.next
        curr2 = curr2.next

    return 'true'

def main():
    llist=LinkedList()
    n = int(input())

    for i in list(map(int, input().split()))[:n]:
        llist.add(i)

    llist.printList()

    print(palindrome(llist))

if __name__=='__main__':
    main()

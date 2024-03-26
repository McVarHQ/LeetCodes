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

def check(arr):
    if arr==[]:
        return False
    return True

def sortK(arr, n):
    slist=LinkedList()
    curr=[i.head for i in arr]

    while(check(curr)):
        checkMin=[]
        for i in curr:
            if i!=None:
                checkMin.append(i.data)

        minElt=min(checkMin)
        minInd=checkMin.index(min(checkMin))

        slist.add(minElt)
        curr[minInd]=curr[minInd].next
        if curr[minInd]==None:
            curr.pop(minInd)

    return slist

k = int(input())
arr = [LinkedList() for i in range(k)]

for i in range(k):
    n = int(input())
    for j in list(map(int, input().split()))[:n]:
        arr[i].add(j)

sortedLinkedList = sortK(arr, n)
sortedLinkedList.printList()

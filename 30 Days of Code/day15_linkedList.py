# Day 15: Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        if head is None:  # If the list is empty, the new node becomes the head
            return new_node
        else:
            current = head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Append the new node at the end
            return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
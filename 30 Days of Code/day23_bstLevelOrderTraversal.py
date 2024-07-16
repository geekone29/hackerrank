# Day 23: BST Level-Order Tranversal

# Define a Node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the node with the given data
        self.next = None  # Initialize the next pointer to None

# Define a Solution class that contains methods to manipulate the linked list
class Solution: 
    def insert(self, head, data):
        # Create a new node with the given data
        p = Node(data)
        
        # If the linked list is empty, set the new node as the head
        if head == None:
            head = p
        # If the linked list has only one node, set the new node as the next node
        elif head.next == None:
            head.next = p
        else:
            # Traverse the list to find the last node
            start = head
            while start.next != None:
                start = start.next
            # Set the new node as the next node of the last node
            start.next = p
        
        # Return the head of the list
        return head  
    
    def display(self, head):
        # Start from the head and traverse the list
        current = head
        while current:
            # Print the data of each node
            print(current.data, end=' ')
            # Move to the next node
            current = current.next

    def removeDuplicates(self, head):
        # If the list is empty, return the head
        if head is None:
            return head

        # Use a set to store unique values from the linked list
        unique_values = set()
        unique_values.add(head.data)  # Add the data of the head node to the set

        current = head
        # Traverse the linked list
        while current.next:
            # If the next node's data is a duplicate, skip the next node
            if current.next.data in unique_values:
                current.next = current.next.next
            else:
                # If the next node's data is unique, add it to the set and move to the next node
                unique_values.add(current.next.data)
                current = current.next

        # Return the head of the modified list
        return head

# Create an instance of the Solution class
mylist = Solution()

# Read the number of elements to insert
T = int(input())

# Initialize the head of the list to None
head = None

# Insert each element into the linked list
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)    

# Remove duplicates from the linked list
head = mylist.removeDuplicates(head)

# Display the elements of the modified linked list
mylist.display(head)

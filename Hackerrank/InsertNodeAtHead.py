# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtHead(llist, data):
    # Write your code here
    newest = SinglyLinkedListNode(data)
    if(llist != None):
        newest.next = llist
    return newest 

#MAIN

#INPUT
#n [1-1000]
#list[i] [1-1000]

#Call insertNodeAtHead

#OUTPUT
#complete list read from head

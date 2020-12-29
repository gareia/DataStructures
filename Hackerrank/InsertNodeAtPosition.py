#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    
    if(position == 0):
        newest = SinglyLinkedListNode(data)
        if(head):
            newest.next = head
        return newest
    else: #position >= 1
        current = head
        while(position > 1):
            current = current.next
            position -= 1   
        newest = SinglyLinkedListNode(data)
        if(current.next):
            newest.next = current.next
        current.next = newest
        return head

#MAIN

#input:
#n [1-1000]
#data [1-1000]
#position [1-n]

#Call insertNodeAtPosition

#output: nodes list
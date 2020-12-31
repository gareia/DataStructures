
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(head, position):
    if(head):
        if(position==0):
            head = head.next
        else:
            current = head
            while(position>1 and current.next):
                current = current.next
                position -= 1
            if(position==1 and current.next):
                current.next = current.next.next
    return head
	
#MAIN
#input
#n [1-1000] number of elements in the linked list (integer)
#list[i] [1-1000] node data value (integer)
#position last line (integer)

#output
#reference to the head
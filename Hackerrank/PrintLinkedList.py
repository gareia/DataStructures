def printLinkedList(head):
    print(head.data)
    if(head.next != None):
        printLinkedList(head.next)
    pass
	
#MAIN
#INPUT n [1-1000]
#list[i] [1-1000]
#call printLinkedList(head)


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        
        first = self.head
        if first:
                new_element.next = first.next
                self.head = new_element
        else:
            self.head = new_element
        
        pass

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        
        first = self.head 
        if first:     
            self.head = first.next
            return first
                
        pass

class Stack(object):
    
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        
        current = self.ll.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
            #print "added like a next "+ str(new_element.value)
        else:
            self.ll.head = new_element
            #print "added to head " + str(new_element.value)
        pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        
        current = self.ll.head
        if current: #min 1 elem
            if current.next == None: #solo 1
                aux = Element(current.value)
                self.ll.head = None
                return aux
                
            while current.next and current.next.next: #si no existe .next.next borra defrente
                current = current.next
            #print "Numero a borrar " + str(current.next.value)
            aux = Element(current.next.value)
            current.next = None
            return aux
        pass
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value
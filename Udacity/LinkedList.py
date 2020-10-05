
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
          
  def get_position(self, position):
    current = self.head
    
    while(position > 1):
      if(current.next == None):
        return None
      current = current.next
      position -= 1
    
    return current

  def insert(self, new_element, position):
    #Assuming position is valid
    current = self.head
    
    while(position > 2):
      if(current.next == None):
        return
      current = current.next
      position -= 1
        
    if(current.next):
      new_element.next = current.next
    
    if(position == 1):
      self.head = new_element
    else:
      current.next = new_element
    
    pass


  def delete(self, value):
      current = self.head
      
      if(current == None):
        return
      
      if(current.value == value):
        self.head = current.next
        current = None
        return
      
      #si es q son >= 2 elem
      while(current.next):
        if(current.next.value == value):
          aux = current.next
          current.next = aux.next
          aux = None
          return
        else:
          current = current.next
      pass

# Test cases
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value

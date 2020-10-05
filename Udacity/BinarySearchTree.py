class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if(self.root):
            self.bst_insert(new_val, self.root)
        pass

    def bst_insert(self, new_val, curr_node):
        
        if(new_val <= curr_node.value):
            #print(str(new_val)+"es menor q "+str(curr_node.value))
            if(curr_node.left == None):
                #print("insertado "+str(new_val))
                curr_node.left = Node(new_val)
            else: #curr_node.left
                self.bst_insert(new_val, curr_node.left)
        else: #new_val > curr_node.value
            #print(str(new_val)+"es mayor q "+str(curr_node.value))
            if(curr_node.right == None):
                #print("insertado "+str(new_val))
                curr_node.right = Node(new_val)
            else: #curr_node.right
                self.bst_insert(new_val, curr_node.right)
            

    def search(self, find_val):
        if(self.root):
            return self.bst_search(find_val, self.root)
        return False
        
    def bst_search(self, find_val, curr_node):
        
        if(curr_node):
            if(curr_node.value == find_val):
                return True
            elif(curr_node.value <= find_val):
                return self.bst_search(find_val, curr_node.left)
            else: #curr_node.value > find_val
                return self.bst_search(find_val, curr_node.right)
        else:
            return False
        
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
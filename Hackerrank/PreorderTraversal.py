"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    print(preOrderHelper(root))

def preOrderHelper(root):
    if(root):
        result = str(root.info) + " "
        #print(result)
        result += preOrderHelper(root.left)
        result += preOrderHelper(root.right)
        return result 
    return ""
	
#MAIN
#input
#n[1-500] nodes in the tree

#output
#inline space-separated string tree's preorder traversal
from Trees.Tree import BinaryTree
from Trees.Node import Node

def in_order(root):
        """this function loops through the first tree and stores the value of each node in the hashmap dict as a key and the value and returns the dict in the end"""
        if root == None : return {} 
        hashmap ={}
        def recursive (root):
           if root.right : recursive(root.left)
           hashmap[root.value] = root.value
           if root.right : recursive(root.right)
        recursive(root)   
        return hashmap

def tree_intersection (rootone, roottwo):
      """this function calls the in order function and store the returnedd value in varible called hashmap then declare a dict to store the intersect node values in it after looping through the sconed tree using the function declared inside it  the return the intersection_node dict as a list after using the .keys method """
      hashmap = in_order(rootone)
      intersection_node = {}
      if roottwo.value in hashmap:
           intersection_node[roottwo.value] = roottwo.value
      def recursive (root):
           """this function loops through the sconed tree to find the intersected nodes by checking if its inside the hashmap dict """
           if root.left :
                if root.left.value in hashmap:
                    intersection_node[root.left.value] = root.left.value
                recursive(root.left)
           if root.right : 
                if root.right.value in hashmap:
                    intersection_node[root.right.value] = root.right.value
                recursive(root.right)
      recursive(roottwo)
      return intersection_node.keys()    



# tree = BinaryTree()

# node1 = Node(150)
# tree.root = node1

# node2 = Node(100)
# tree.root.left = node2

# node3 = Node(250)
# tree.root.right = node3

# node4 = Node(75)
# tree.root.left.left = node4

# node5 = Node(160)
# tree.root.left.right = node5

# node6 = Node(200)
# tree.root.right.left = node6

# node20 = Node(350)
# tree.root.right.right = node20




# tree2 = BinaryTree()

# node7 = Node(42)
# tree2.root = node7

# node8 = Node(100)
# tree2.root.left = node8

# node9 = Node(600)
# tree2.root.right = node9

# node10 = Node(15)
# tree2.root.left.left = node10

# node11 = Node(160)
# tree2.root.left.right = node11

# node12 = Node(200)
# tree2.root.right.left = node12

# node13 = Node(350)
# tree2.root.right.right = node13


# print(tree_intersection(tree.root, tree2.root))
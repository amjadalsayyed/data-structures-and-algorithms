from Trees.Node import Node
from Stacks_and_queues.Queue import Queue

class BinaryTree:
    """This Class creeate a tree where you can add nodes as leaf to it using root.left and root.right
    also there is three fuction that can help you put the values in order, pre order and post order
    
    """
    def __init__(self):
        self.root = None
        self.max= None
    def pre_order (self,root):
        """
        in this function we loop over the tree elements using recusive function 
        to sort the values in alist according to DFS pre order method
        """
        if self.root == None : return []
        list=[]
        def recursive (root):
            list.append(root.value)
            if root.left : recursive(root.left)
            if root.right : recursive(root.right)
        recursive(root)    
        return list
    
    def in_order(self,root):
        """
        in this function we loop over the tree elements using recusive function 
        to sort the values in alist according to DFS in order method
        """
        if self.root == None : return [] 
        list =[]
        def recursive (root):
           if root.left : recursive(root.left)
           list.append(root.value)
           if root.right : recursive(root.right)
        recursive(root)   
        return list
    
    def post_order(self,root):
        """
        in this function we loop over the tree elements using recusive function 
        to sort the values in alist according to DFS post order method
        """
        if self.root == None : return []
        list=[]
        def recursive (root):
             if root.left : recursive(root.left)
             if root.right : recursive(root.right)
             list.append(root.value)
        recursive(root)     
        return list
    
    def find_maximum_value(self): 
         """
         in this function we loop over the tree elements using recusive function to compare every value 
         inside the tree with the max value and assign it to max if its bigger
         """
         if self.root is None : return "Empty Tree!" 
         if self.max is None : self.max = self.root.value    
         def find_max (root):
              if root.left: find_max(root.left)
              if root.right: find_max(root.right)
              if root.value > self.max:
                    self.max = root.value
              
         find_max(self.root)
         return self.max 
           
        
              
         

class BinarySearchTree(BinaryTree):
     """
     this class is an extend from the binary tree class where it has two fuctions to one to add nodes to the tree dinamicly while keeping it binary 
     and the other is to find if the value exeist in the tree or not 
     """
     def __init__(self):
          super().__init__()

     def add(self,value):
          if self.root == None: self.root = Node(value)               
          else: self.add_recursion(self.root,value)         
     def add_recursion(self,root,value):          
          if root.value == value: print('value already exists')
          elif root.value > value:
               if root.left: self.add_recursion(root.left,value)        
               else: root.left = Node(value)                   
          elif root.value < value:
               if root.right: self.add_recursion(root.right,value)
               else: root.right = Node(value)

     def contain(self,value):
          if self.root is None : return "Empty Tree!"
          if self.root.value == value: return True      
          current = self.root
          while True:
               if current is None: return False    
               elif current.value > value: current = current.left    
               elif current.value < value: current = current.right
               else: return True   


def  breadth_first(tree):
     """
     this function takes a tree as an arguments the add the root to the queue then enter a loop with a condtion that keep looping until the queue is empty 
     inside the loop it dequeue from the queue and store the returned node from the dequeue and push it into the list thhen check if it has a left node add it to the queue and if it has a right value add it to the queue 
     after the loop ends it return the list 
     """
     if tree.root is None: return "Empty Tree!"
     list = []
     queue = Queue()
     queue.enqueue(tree.root)
     while queue.is_empty() is False:
          node = queue.dequeue()
          list.append(node.value)
          if node.left : queue.enqueue(node.left)
          if node.right : queue.enqueue(node.right)
     return list     



           

if __name__ == "__main__":
        tree = BinaryTree()

        node1 = Node(-3)
        tree.root = node1

        node2 = Node(-4)
        tree.root.left = node2

        node3 = Node(-23)
        tree.root.right = node3

        node4 = Node(-56)
        tree.root.left.left = node4

        node5 = Node(-210)
        tree.root.left.right = node5

        node6 = Node(-90)
        tree.root.right.left = node6
     #    tree.add(10)
     #    tree.add(4)
     #    tree.add(3)
     #    tree.add(13)
     #    tree.add(11)
     #    # tree.add(11)
     #    tree.add(9)
     #    tree.add(19)
     #    tree.add(1353)
     #    tree.add(1911)
     #    tree.add(193)
     #    tree.add(191)

        print(breadth_first(tree))
     #    print(tree.in_order(tree.root))
     #    print(tree.in_order(tree.root))
     #    print(tree.contain(22))
     #    print(tree.contain(3))



















    #  def contain(self,value,root=None):
    #     #   if self.root.value == value:
    #     #        return True
    #     #   else:
    #     #      return self.contain_r(self.root,value)
    
    #     if not root :
            
    #         root = self.root
    #         if root.value == value:
    #            return True
    #         if root.value > value:
    #            if root.left is None:
    #                return False
    #            return self.contain(root.left, value)
    #         if root.value < value:
    #             if root.right is None :
    #                 return False
    #             return self.contain(root.right, value)

    #  def contain_r(self,root,value):
    #      if root.value > value :
    #        if root.left.value is None :
    #            return False
    #        elif root.left.value == value:
    #             return True
    #        else:
    #             return self.contain_r(self.root.left,value)
    #      if root.value < value:
    #         if root.right.value is None :
    #            return False
    #         elif root.right.value == value:
    #             return True
    #         else:
    #            return self.contain_r(self.root.right,value)
         
    #      return False      
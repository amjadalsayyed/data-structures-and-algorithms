from Trees.Node import Node

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order (self,root):
        if self.root == None : return []
        list=[]
        def recursive (root):
            list.append(root.value)
            if root.left : recursive(root.left)
            if root.right : recursive(root.right)
        recursive(root)    
        return list
    
    def in_order(self,root):
        if self.root == None : return [] 
        list =[]
        def recursive (root):
           if root.left : recursive(root.left)
           list.append(root.value)
           if root.right : recursive(root.right)
        recursive(root)   
        return list
    
    def post_order(self,root):
        if self.root == None : return []
        list=[]
        def recursive (root):
             if root.left : recursive(root.left)
             if root.right : recursive(root.right)
             list.append(root.value)
        recursive(root)     
        return list

class BinarySearchTree(BinaryTree):
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
                    
           

if __name__ == "__main__":
        tree = BinarySearchTree()

        # node1 = Node("A")
        # tree.root = node1

        # node2 = Node("B")
        # tree.root.left = node2

        # node3 = Node("C")
        # tree.root.right = node3

        # node4 = Node("D")
        # tree.root.left.left = node4

        # node5 = Node("E")
        # tree.root.left.right = node5

        # node6 = Node("F")
        # tree.root.right.left = node6
        tree.add(10)
        tree.add(4)
        tree.add(3)
        tree.add(13)
        tree.add(11)
        # tree.add(11)
        tree.add(9)
        tree.add(19)
        tree.add(1353)
        tree.add(1911)
        tree.add(193)
        tree.add(191)

        print(tree.pre_order(tree.root))
        print(tree.in_order(tree.root))
        print(tree.in_order(tree.root))
        print(tree.contain(22))
        print(tree.contain(3))



















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
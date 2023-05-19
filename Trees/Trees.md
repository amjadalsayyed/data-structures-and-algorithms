# Stacks and Queues

> - create a Stack and Queue classes

## Whiteboard Process

## pre_order

![CC15](./CC15_1.jpg)

## in_order

![CC15](./CC15_2.jpg)

## post_order

![CC15](./CC15_3.jpg)

## Add nodes

![CC15](./CC15_4.jpg)

## Contain

![CC15](./CC15_5.jpg)

## Approach & Efficiency

> - Time --> O(log n) , O(n) check whiteboard for more info
> - space -->O(1) , O(n) check whiteboard for more info

## Solution

```python
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
```

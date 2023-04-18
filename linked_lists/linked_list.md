# Linked List

> - create a Linked list class that insert into the beginning

## Whiteboard Process

### insert

![CC5](./cc5.png)

### append

![CC6](./cc6-1.png)

### insert before

![CC6](./cc6-2.png)

### insert after

![CC6](./cc6-3.png)

### kthFromEnd

![CC7](./cc7.png)

## Approach & Efficiency

> - Time --> O(1) for some of them you can check the white board
> - Time --> O(n) for some of them you can check the white board
> - space -->O(1)

## Solution

```class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    count = 0

    def insert (self,value):
           """
           this function add the new node to the beggining of the list as the head of the list
           """
           node = Node(value)
           LinkedList.count +=1
           if self.head == None:
                self.head = node
           else:
                node.next = self.head
                self.head = node

    def includes (self,key):
         """
         this function check if the list have the key in it
         """

         temp = self.head
         if temp is None:
              return False
         while temp is not None:
              if temp.value == key:
                   return True
              temp = temp.next
         if temp is None:
              return False

    def append(self,value):
        """
        This function add a node to the end of the linked list
        """
        LinkedList.count +=1
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node




    def insert_after(self,target,value):
         """
         this function insert a node with the given value after the target value if it exists in the linked list
         """
         LinkedList.count +=1
         if self.includes(target):
            node = Node(value)
            if self.head == None :
              self.insert(value)

            else:
              currnet = self.head
              while currnet.value is not target:
                   currnet = currnet.next
              target = currnet
              node.next = target.next
              target.next = node
         else:
             print("this target value does not exists")


    def insert_before(self,target,value):
         """
         this function insert a node with the given value before the target value if it exists in the linked list
         """
         LinkedList.count +=1
         if self.includes(target):
            node = Node(value)
            if self.head == None or self.head.value == target:
              self.insert(value)

            else:
              currnet = self.head
              while currnet.next.value is not target:
                   currnet = currnet.next
              target = currnet
              node.next = target.next
              target.next = node
         else:
             print("this target value does not exists")

    def kthFromEnd(self,k):
        if self.head is None:
            return "Error : the linked list is empty"
        elif k >= LinkedList.count:
            return "Error : Your input can't be more than the length"
        elif k < 0 :
            return "Error : only positive numbers are accepted!"
        elif LinkedList.count == 1:
            return self.head.value
        else:
         pointer_one = self.head
         pointer_two = self.head

         for i in range(k):
            pointer_two = pointer_two.next

         while pointer_two.next is not None:
           pointer_one = pointer_one.next
           pointer_two = pointer_two.next

         return pointer_one.value





    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} -> '
                current = current.next

            output += " Null"
        return output
```

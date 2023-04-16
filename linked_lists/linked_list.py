class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert (self,value):
           """
           this function add the new node to the beggining of the list as the head of the list 
           """
           node = Node(value) 
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
             

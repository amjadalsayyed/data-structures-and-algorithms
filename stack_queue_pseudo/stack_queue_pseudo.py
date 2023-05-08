from Stacks_and_queues.Stack import Stack

class PseudoQueue:
    """
    this queue is using two stack to implement it self and add to the queue and de queue from it  
    """
    def __init__(self):
       self.inbox = Stack()
       self.outbox = Stack()

    def enqueue(self,value):
         self.inbox.push(value)

    def dequeue(self):
         if self.inbox.is_empty() and self.outbox.is_empty():
              return "Pseude Queue is Empty!"
         if self.outbox.is_empty() and not self.inbox.is_empty():
                  inbox_size = self.inbox.get_size()
                  for x in range(inbox_size):
                        self.outbox.push(self.inbox.pop())
                  return self.outbox.pop()
         if not self.outbox.is_empty():             
               return self.outbox.pop()
                
                        
ll = PseudoQueue()

ll.enqueue(1)
ll.enqueue(2)
ll.enqueue(3)

ll.enqueue(4)
# print(ll.dequeue())
# print(ll.dequeue())

print(ll.inbox)

         
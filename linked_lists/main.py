from linked_list import LinkedList

is_palindrome = LinkedList.is_palindrome

if __name__ == '__main__':
      linked_list = LinkedList()
      linked_list_2 = LinkedList()

      linked_list.insert('A')
      linked_list.insert('B')
      linked_list.insert('C')
      # linked_list.append('D')


      linked_list_2.insert('1')
      linked_list_2.insert('2')
      linked_list_2.insert('3')
      linked_list_2.insert('2')
      linked_list_2.insert('1')
      # linked_list_2.insert('4')
      print(linked_list_2)
      # linked_list_2.revers()
     
      
      # print(is_palindrome(linked_list_2))
      # print(linked_list.count)

      # print(linked_list.kthFromEnd(4))

      # linked_list_3 = LinkedList()
      # # linked_list_3.zip_list(linked_list,linked_list_2)
      # print(linked_list_3.zip_list(linked_list,linked_list_2))


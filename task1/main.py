from linked_list import LinkedList
llist = LinkedList()

# Вставляємо вузли
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)


print("Зв'язний список 1:")
llist.print_list()


print("\nЗв'язний список 1 після реверсу:")
llist.reverse_list()
llist.print_list()

llist.merge_sort()
print("\nЗв'язний список 1 після сортування:")
llist.print_list()

llist2 = LinkedList()

# Вставляємо вузли список 2
llist2.insert_at_beginning(101)
llist2.insert_at_beginning(1)
llist2.insert_at_beginning(31)
llist2.insert_at_end(51)
llist2.insert_at_end(61)
llist2.insert_at_end(99)
llist2.insert_at_end(100)

llist2.merge_sort()

print("\nЗв'язний список 2 після сортування:")
llist2.print_list()

llist3 = LinkedList.merge_lists(llist, llist2)

print("\nЗв'язний список 3 після об'єднання:") 
llist3.print_list()
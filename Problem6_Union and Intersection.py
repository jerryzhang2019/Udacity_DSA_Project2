
# coding: utf-8

# In[4]:


#Problem6: Union and Intersection
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None
 
    def get_prev_node(self, ref_node): 
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    def duplicate(self): 
        copy = LinkedList()
        current = self.head
        while current:
            node = Node(current.data)
            copy.append(node)
            current = current.next
        return copy
 
    def append(self, new_node): 
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
 
    def remove(self, node): 
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
 
    def display(self): 
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
            
def remove_duplicates(llist): 
    current1 = llist.head
    while current1:
        current2 = current1.next
        data = current1.data
        while current2:
            temp = current2
            current2 = current2.next
            if temp.data == data:
                llist.remove(temp)
        current1 = current1.next
 
 
def union(llist1, llist2): 
    if llist1.head is None:
        union = llist2.duplicate()
        remove_duplicates(union)
        return union
    if llist2.head is None:
        union = llist1.duplicate()
        remove_duplicates(union)
        return union
 
    union = llist1.duplicate()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next
    llist2_copy = llist2.duplicate()
    last_node.next = llist2_copy.head
    remove_duplicates(union)
 
    return union 
 
def intersection(llist1, llist2): 
    if (llist1.head is None or llist2.head is None):
        return LinkedList()
 
    intersection = LinkedList()
    current1 = llist1.head
    while current1:
        current2 = llist2.head
        data = current1.data
        while current2:
            if current2.data == data:
                node = Node(data)
                intersection.append(node)
                break
            current2 = current2.next
        current1 = current1.next
    remove_duplicates(intersection)
 
    return intersection 
 
# Test Case1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,2,3,4,5]
element_2 = [3,4,5,6,7]

for i in element_1:
    node = Node(int(i))
    linked_list_1.append(node)

for i in element_2:
    node = Node(int(i))
    linked_list_2.append(node)
    
print('The union as below:')
union(linked_list_1, linked_list_2).display()
print()

print('The intersection as below: ')
intersection(linked_list_1, linked_list_2).display()
print()

#Test Case2        
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3,2,4,35,6,65,6,4,3,23]
element_4 = [3,1,7,8,9,11,21,1]

for i in element_3:
    node = Node(int(i))
    linked_list_3.append(node)
    
for  i in element_4:
    node = Node(int(i))
    linked_list_4.append(node)
    
print('The union as below:')
union(linked_list_3, linked_list_4).display()
print()
print('The intersection as below:')
intersection(linked_list_3, linked_list_4).display()
print()

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [0,2,3,4]
element_6 = [1,2,3,5,7,9]

for i in element_5:
    node = Node(int(i))
    linked_list_5.append(node)
    
for  i in element_6:
    node = Node(int(i))
    linked_list_6.append(node)
    
print('The union as below:')
union(linked_list_5, linked_list_6).display()
print()
print('The intersection as below:')
intersection(linked_list_5, linked_list_6).display()
print()


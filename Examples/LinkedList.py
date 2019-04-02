class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def show(self):
        linked_list = []
        current = self.head
        current_position = 1
        if self.head:
            while current:
                linked_list.append(current.value)
                current = current.next
                current_position += 1
        return linked_list

    def append(self, new_element):
        """Appending object at the end of linked list"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Getting object at position N"""
        current = self.head
        current_position = 1
        if current_position < 1:
            return None
        while current and current_position != position:
            current = current.next
            current_position += 1
        if current_position == position:
            return current
        else:
            return None

    def insert(self, new_element, position):
        """Inserting value at position N"""
        current_position = 1
        current = self.head
        if position > 1:
            while current and current_position < position:
                if current_position == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                current_position += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete first object with value N"""
        pre_element = None
        current = self.head
        while current.value != value and current.next:
            pre_element = current
            current = current.next

        if current.value == value:
            if pre_element:
                pre_element.next = current.next
            else:
                self.head = current.next

    def insert_first(self, new_element):
        """Insert new element as the head of the LinkedList"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """Delete the first (head) element in the LinkedList as return it"""
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test insert_first
ll.insert_first(e4)

# Print linked list
print(ll.show())

# Test delete_first
ll.delete_first()
print(ll.show())

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e5, 3)
print(ll.show())

# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(5)
print(ll.show())

# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print(self):
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


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
print(ll.print())

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
print(ll.print())

# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
print(ll.print())

# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)

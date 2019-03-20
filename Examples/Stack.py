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


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)
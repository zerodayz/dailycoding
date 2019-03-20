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


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        pass

    def pop(self):
        pass

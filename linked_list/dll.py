"""
Have the implementation of Double Linked List in Python
"""


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        next_item = None
        prev_item = None
        if self.next:
            next_item = self.next.data

        if self.prev:
            prev_item = self.prev.data

        return f"Data => {self.data}"


class DoublyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def print_dll(self):
        current = self.head

        while current.next is not None:
            print(current, current.next, current.prev)
            current = current.next

        print(current, current.next, current.prev)

    def insert_at_beginning(self, data):
        new_node = Node(data, None, None)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data, None, None)
        if self.head:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next

            last_node.next = new_node
            new_node.prev = last_node

        else:
            self.head = new_node

    def insert_at_pos(self, index, data):

        new_node = Node(data)

        current_idx = 0
        current_node = self.head

        while current_idx < index and current_node.next is not None:
            current_node = current_node.next
            current_idx += 1

        if current_idx == index:
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next = new_node

    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next
            self.head.prev = None


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(22)
    dll.insert_at_beginning(33)
    dll.insert_at_beginning(66)
    dll.print_dll()
    print("--")
    dll.insert_at_end(44)
    dll.print_dll()
    print("--")
    dll.insert_at_pos(0, 333)
    dll.print_dll()
    print("--")
    dll.delete_at_beginning()
    dll.print_dll()

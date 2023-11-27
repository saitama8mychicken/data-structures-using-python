"""
Here we will have  implementation of Single Linked List and its related operations
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_linked_list(self):
        current = self.head
        while current.next is not None:
            print(current.data, current.next)
            current = current.next

        print(current.data, current.next)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head

        self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        new_node = Node(data)
        last_node.next = new_node
        self.length += 1

    def insert_at_position(self, data, pos):
        if pos > self.length:
            raise ValueError("Index out of Range")

        new_node = Node(data)
        current = self.head
        current_pos = 0
        while current.next is not None:
            if current_pos == pos:
                break
            current = current.next
            current_pos += 1

        new_node.next = current.next
        current.next = new_node

    def delete_from_beginning(self):
        current = self.head

        # check if something exists in head
        if current is not None:
            next_current = current.next
            self.head = next_current

    def delete_from_end(self):
        last_node = self.head
        last_previous_node = last_node

        if last_node.next is not None:
            last_node = last_node.next

        while last_node.next is not None:
            last_node = last_node.next
            last_previous_node = last_previous_node.next

        if last_previous_node == last_node:
            self.head = None
        else:
            last_previous_node.next = None


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(22)
    ll.insert_at_beginning(34)
    ll.insert_at_beginning(23)
    ll.insert_at_end(33)
    ll.insert_at_end(38)
    # ll.delete_from_beginning()
    ll.print_linked_list()
    print("Trying Insertion at a pos")
    ll.insert_at_position(232, 2)
    ll.print_linked_list()

"""
Here we will have  implementation of Circular Linked List and its related operations
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:

    def __init__(self, head=None):
        self.head = head

    def print_element(self):

        current = self.head
        print()
        if current:
            print(current.data)
            while current.next is not self.head:
                current = current.next
                print(current.data)
        print()

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next

            last_node.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            new_node.next = self.head

    def insert_at_end(self, data):
        new_node = Node(data)

        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next

        last_node.next = new_node
        new_node.next = self.head

    def delete_at_end(self):
        required_node = self.head

        while required_node.next.next != self.head:
            required_node = required_node.next

        if required_node == self.head:
            self.head = None
        else:
            required_node.next = self.head



    def delete_at_beginning(self):

        last_node = self.head

        while last_node.next != self.head:
            last_node = last_node.next

        if last_node == self.head:
            self.head = None
        else:
            last_node.next = self.head.next
            self.head = last_node.next


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.print_element()
    cll.insert_at_beginning(5)
    cll.print_element()
    cll.insert_at_beginning(33)
    cll.print_element()

    cll.insert_at_beginning(383)
    cll.print_element()

    cll.insert_at_end(393)
    cll.print_element()

    cll.delete_at_beginning()
    cll.print_element()

    cll.delete_at_end()
    cll.print_element()

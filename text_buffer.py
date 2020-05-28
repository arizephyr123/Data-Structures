
from doubly_linked_list import DoublyLinkedList
import sys

sys.path.append('./doubly_linked_list')


class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __str__(self):
        string_to_return = ''

        node = self.storage.head
        while node is not None:
            string_to_return += node.value
            node = node.next

        return string_to_return

    def join(self, other_buffer):
        # link tail of this buffer to the head of the other buffer
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail

        # point our tail to the other new tail
        # huh??? what goes here

        pass

    def append(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_tail(char)

    def prepend(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_head(char)

    def delete_from_front(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_head(_)

    def delete_from_back(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_tail(_)

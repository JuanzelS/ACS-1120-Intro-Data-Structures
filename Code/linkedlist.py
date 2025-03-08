class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because we need to traverse all n nodes to count them."""
        count = 0  # O(1) to initialize the counter
        node = self.head  # O(1) to start at the head
        while node is not None:  # O(n) loop
            count += 1  # O(1) to increment counter
            node = node.next  # O(1) to move to the next node
        return count  # O(1) to return the final count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) because we can directly append at the tail in constant time."""
        new_node = Node(item)  # O(1) to create a new node
        if self.is_empty():  # O(1) to check if the list is empty
            self.head = new_node  # O(1) to set head to new node
            self.tail = new_node  # O(1) to set tail to new node
        else:
            self.tail.next = new_node  # O(1) to link the current tail to the new node
            self.tail = new_node  # O(1) to update the tail

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because we can prepend the node in constant time."""
        new_node = Node(item)  # O(1) to create a new node
        if self.is_empty():  # O(1) to check if the list is empty
            self.head = new_node  # O(1) to set head to new node
            self.tail = new_node  # O(1) to set tail to new node
        else:
            new_node.next = self.head  # O(1) to link new node to the current head
            self.head = new_node  # O(1) to update the head

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        Best case running time: O(1) if the first node matches the matcher.
        Worst case running time: O(n) if the item is at the end or not present."""
        node = self.head  # O(1) to start from the head
        while node is not None:  # O(n) loop
            if node.data == matcher:  # O(1) to check if the node data matches
                return node.data  # O(1) to return the found item
            node = node.next  # O(1) to move to the next node
        return None  # O(1) to return None if not found

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if the item is the head.
        Worst case running time: O(n) if the item is at the end or not found."""
        node = self.head  # O(1) to start from the head
        prev_node = None  # O(1) to initialize previous node
        while node is not None:  # O(n) loop
            if node.data == item:  # O(1) to check if the node data matches
                if prev_node is None:  # O(1) to check if it's the head node
                    self.head = node.next  # O(1) to update head to next node
                else:
                    prev_node.next = node.next  # O(1) to update previous node to skip current node
                if node.next is None:  # O(1) to check if it's the tail
                    self.tail = prev_node  # O(1) to update tail to the previous node
                return  # O(1) to return after deleting
            prev_node = node  # O(1) to update previous node
            node = node.next  # O(1) to move to the next node
        raise ValueError(f'Item not found: {item}')  # O(1) to raise an error if not found


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

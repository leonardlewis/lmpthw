class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        if self.begin == self.end == None:
            self.begin = self.end = DoubleLinkedListNode(obj, None, None)

        elif self.begin == self.end != None:
            self.end = DoubleLinkedListNode(obj, None, self.begin)
            self.begin = DoubleLinkedListNode(self.begin.value, self.end, None)

        else:
            x = self.end
            self.end = DoubleLinkedListNode(obj, None, x)
            x.next = self.end

    def pop(self):
        """Removes the last item and returns it."""
        if self.begin == None:
            return None

        elif self.begin == self.end:
            node = self.begin
            self.end = self.begin = None

            return node.value

        else:
            node = self.begin
            while node.next != self.end:
                node = node.next
            self.end = node
            return node.next.value

    def shift(self, obj):
        """Actually just another name for push."""
        if self.begin == self.end == None:
            self.begin = self.end = DoubleLinkedListNode(obj, None, None)

        elif self.begin == self.end != None:
            self.end = DoubleLinkedListNode(obj, None, self.begin)
            self.begin = DoubleLinkedListNode(self.begin.value, self.end, None)

        else:
            x = self.end
            self.end = DoubleLinkedListNode(obj, None, x)
            x.next = self.end

    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        if self.begin == self.end == None:
            return None

        elif self.begin == self.end != None:
            x = self.begin
            self.begin = self.end = None
            return x.value

        else:
            x = self.begin
            self.begin = self.begin.next

            return x.value


    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly inside remove().
        It should take a node, and detach it from the list, whether the node is
        at the front, end, or in the middle."""
        # if the node is at the end
        if self.end = node:
            self.pop()

        # elif it's at the beginning
        elif self.begin = node:
            # call unshift
            self.unshift()
        #else it's in the middle
        else:
            # skip over it
            # save node.prev, node.next
            prev = node.prev
            next = node.next
            # set prev.next to saved next
            node.prev.next = next
            # set next.prev to saved prev
            node.next.prev = prev


    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

        if self.begin.value == obj:
            self.begin = self.begin.next
            self.begin.prev = None

        elif self.end.value == obj:
            self.end = self.end.prev
            self.end.next = None

        else:
            node = self.begin
            while node.value != obj:
                node = node.next
            node.prev.next = node.next
            node.next.prev = node.prev

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin and self.begin.value or None

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.last and self.last.value or None

    def count(self):
        """Counts the number of elements in the list."""

        count = 0
        x = self.begin

        if self.begin == self.end == None:
            return 0

        elif self.begin == self.end:
            return 1

        else:
            while x:
                count += 1
                x = x.next

            return count

    def get(self, index):
        """Get the value at index."""
        count = 0
        x = self.begin

        while count != index:
            x = x.next
            count += 1

        return x.value

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""

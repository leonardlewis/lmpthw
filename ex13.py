class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""

        if self.begin == None:
            self.begin = SingleLinkedListNode(obj, None)
            self.end = self.begin

        elif self.begin != None and self.begin == self.end:
            new_item = SingleLinkedListNode(obj, None)
            y = self.begin

            self.begin = SingleLinkedListNode(y.value, new_item)
            self.end = new_item

        else:
            new_item = SingleLinkedListNode(obj, None)
            self.end.next = new_item
            self.end = new_item

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
        """Another name for push."""
        if self.begin == None:
            self.begin = SingleLinkedListNode(obj, None)
            self.end = self.begin

        elif self.begin != None and self.begin == self.end:
            new_item = SingleLinkedListNode(obj, None)
            y = self.begin

            self.begin = SingleLinkedListNode(y.value, new_item)
            self.end = new_item

        else:
            new_item = SingleLinkedListNode(obj, None)
            self.end.next = new_item
            self.end = new_item

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin == None:
            return None

        elif self.begin == self.end != None:
            node = self.begin
            self.begin = self.end = node.next

            return node.value

        else:
            node = self.begin
            self.begin = node.next

            return node.value


    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        counter = 0

        if node.value == obj:
            self.begin = node.next
        else:
            while node != self.end:
                if node.next.value == obj and node.next == self.end:
                    self.end = node
                    counter += 1
                elif node.next == obj and node.next != self.end:
                    node.next = node.next.next.value
                else:
                    node = node.next
                    counter += 1

        return counter

    def first(self):
        """Returns a *reference* to the first item, does not remove."""

    def last(self):
        """Returns a reference to the last item, does not remove."""

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
        """Gets the value at index."""
        count = 0
        x = self.begin

        if count == index:
            return self.begin.value

        else:
            while count != index:
                count += 1
                x = x.next
            return x.value

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        mark = mark.lower()
        node = self.begin

        if mark[:6] == "before":
            while node.value.lower() != mark[7:]:
                print(node.value)
                node = node.next
        elif mark[:5] == "after":
            while node.value.lower() != mark[6:]:
                node = node.next
            node = node.next
            while node:
                print(node.value)
                node = node.next
        else:
            pass

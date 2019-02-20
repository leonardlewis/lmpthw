class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class Stack(object):
    def __init__(self):
        self.top = None
        self.bottom = None

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        if self.bottom == self.top == None:
            self.bottom = self.top = StackNode(obj, None)

        elif self.bottom == self.top != None:
            self.top = StackNode(obj, None)
            self.bottom.next = self.top

        else:
            x = self.top
            self.top = StackNode(obj, None)
            x.next = self.top

    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        if self.top == None:
            return None

        else:
            x = self.bottom
            y = self.top
            while x.next != self.top:
                x = x.next
            self.top = x
            self.top.next = None

            return y.value

    def top(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.top and self.top.value or None

    def count(self):
        """Counts the number of elements in the stack."""
        count = 0
        x = self.bottom

        if self.bottom == self.top == None:
            return 0

        elif self.bottom == self.top:
            return 1

        else:
            while x:
                count += 1
                x = x.next

            return count

    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the stack."""

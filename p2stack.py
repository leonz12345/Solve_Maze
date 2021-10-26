"""
Math 560
Project 2
Fall 2021

p2stack.py

Partner 1: Leon Zhang
Partner 2: Casper Hsiao
Date: Oct 26th 2021
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        # Return True if the number of element in the stack is equal to
        # the length of stack. Return False otherwise.
        return self.numElems == len(self.stack)

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        # Return True if the number of element in the stack is 0.
        # Return False otherwise.
        return self.numElems == 0

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        # Initialize new stack of size twice the original
        new_stack = [None for x in range(0, 2*len(self.stack))]
        # Append all elements from the original stack to the new one
        for i in range(self.numElems):
            new_stack[i] = self.stack[i]
        # Update the stack to the new one
        self.stack = new_stack
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        # If the stack is full, resize
        if self.isFull():
            self.resize()
        # Increment top
        self.top += 1
        # Push the value to the top of the stack
        self.stack[self.top] = val
        # Update number of element by one
        self.numElems += 1
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        # If stack is empty, do nothing and return None
        if self.numElems == 0:
            return None
        # Pop the top element
        else:
            # Get the top element
            val = self.stack[self.top]
            # Set the top to be None
            self.stack[self.top] = None
            # Update top and number of element
            self.top -= 1
            self.numElems -= 1
            return val

# For testing purpose
def main():
    stack = Stack()
    append = [x for x in range(20)]
    for val in append:
        stack.push(val)
    for _ in range(len(append)):
        print(stack.pop())
    print(stack)

if __name__ == "__main__":
    main()
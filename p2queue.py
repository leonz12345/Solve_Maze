"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1:
Partner 2:
Date:
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        # Return True if the number of element in the queue is equal to
        # the length of queue. Return False otherwise.
        return self.numElems == len(self.queue)

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        # Return True if the number of element in the queue is 0.
        # Return False otherwise.
        return self.numElems == 0

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        # Initialize new queue of size twice the original
        new_queue = [None for x in range(0, 2*len(self.queue))]
        # Append all elements from the original queue to the new one
        for i in range(self.numElems):
            new_queue[i] = self.queue[i]
        # Update the queue to the new one
        self.queue = new_queue
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        # If the queue is full, resize
        if self.isFull():
            self.resize()
        # Increment top
        self.rear += 1
        # Push the value to the back of the queue
        self.queue[self.rear] = val
        # Update number of element by one
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        # If queue is empty, do nothing and return None
        if self.isEmpty():
            return None
        # Pop the front element
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
    queue = Queue()
    append = [x for x in range(20)]
    for val in append:
        queue.push(val)
    for _ in range(len(append)):
        print(queue.pop())
    print(queue)

if __name__ == "__main__":
    main()

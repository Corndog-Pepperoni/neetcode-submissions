class MinStack:

    def __init__(self):
        # Create a regular stack and a stack that keeps track of the minimums
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Append the value into the regular stack
        self.stack.append(val)

        # Append the new minimum into the min stack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # Pop both stacks; you're essentially rolling back to the previous state of the two
        # stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Get the top of the stack using a -1 index
        return self.stack[-1]

    def getMin(self) -> int:
        # Get the current (most recent) min by using a -1 index for the min stack
        return self.minStack[-1]

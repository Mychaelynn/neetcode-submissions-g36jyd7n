class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Determine the new minimum to record
        if not self.min_stack:
            # If it's the first item, it IS the minimum
            self.min_stack.append(val)
        else:
            # Push the smaller of (current value) OR (previous minimum)
            current_min = self.min_stack[-1]
            if val < current_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(current_min)

    def pop(self) -> None:
        # Since we push to both every time, we must pop from both every time
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
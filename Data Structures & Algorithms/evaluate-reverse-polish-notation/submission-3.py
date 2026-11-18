class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            # All the operator if statements essentially consolidate data in the stack
            # ex: 2 and 3 are in the stack and a + operator is met -> 2 + 3 = 6
            # (two elements become one)
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # stack.append(stack.pop() - stack.pop()) poses issue of subtracting the last
                # element of the stack by the first element as opposed to the other way around
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                # stack.append(stack.pop() / stack.pop()) poses issue of dividing the last
                # element of the stack by the first element as opposed to the other way around
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            # Add numbers to the stack until an operator is reached
            else:
                stack.append(int(c))
        
        return stack[0]
class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize stack
        stack = []

        # Create dict of closings with openings
        CloseToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        # For every char in the str
        for c in s:
            # If we have reached a closing
            if c in CloseToOpen:
                # Check if there is still data in the stack
                # Check if the last element of the stack (LIFO) is equal to the current char's opening val
                if stack and stack[-1] == CloseToOpen[c]:
                    # If there is a match, remove the last element from the stack (LIFO)
                    stack.pop()
                # An empty stack indicates all openings have their closings and the current char is an
                # extra closing with no opening
                # A mismatched last element of the stack with the current char's opening val indicates
                # That the current char does not correspond to its opening's proper position
                else:
                    return False
            # If the char is an opening
            else:
                stack.append(c)
        
        # An empty stack means all openings have closings
        # Otherwise, there is an opening(s) with no closing(s)
        return not stack

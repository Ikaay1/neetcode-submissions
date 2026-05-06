class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token in "+*/-":
                smaller = stack.pop()
                bigger = stack.pop()
                if token in "+":
                    stack.append(bigger + smaller)
                elif token in "-":
                    stack.append(bigger - smaller)
                elif token in "*":
                    stack.append(bigger * smaller)
                else:
                    stack.append(int(bigger / smaller))
            else:
                stack.append(int(token))
        
        return stack[-1]
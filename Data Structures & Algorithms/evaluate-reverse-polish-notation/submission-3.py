class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            #add if no operator 
            if i not in operators:
                stack.append(i)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                match i:
                    case '+':
                        stack.append(a+b)
                    case '-':
                        stack.append(b-a)
                    case '*':
                        stack.append(a*b)
                    case '/':
                        stack.append(b/a)
        return int(stack[-1])
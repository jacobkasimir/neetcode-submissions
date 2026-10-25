class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '{', '[']
        for i in s:
            if len(stack)>0: 
                match stack[-1]:
                    case '(':
                        if i == ')':
                            stack.pop()
                        elif i in left:
                            stack.append(i)
                        else:
                            return False
                    case '{':
                        if i == '}':
                            stack.pop()
                        elif i in left:
                            stack.append(i)
                        else:
                            return False
                    case '[':
                        if i == ']':
                            stack.pop()
                        elif i in left:
                            stack.append(i)
                        else:
                            return False
            else:
                stack.append(i)
        return True if not stack else False
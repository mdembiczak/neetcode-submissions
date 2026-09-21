class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            elif len(stack) == 0 or c != stack.pop():
                return False
        return not stack
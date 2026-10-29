class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            # 1. Push opening brackets to the stack
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            
            # 2. Check closing brackets (Must ensure stack is NOT empty first)
            elif s[i] == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()  # Pop instead of setting to None
                
            elif s[i] == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
                
            elif s[i] == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
                
        # 3. Valid only if no unmatched opening brackets are left
        return len(stack) == 0

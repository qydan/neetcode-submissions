class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parantheses = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in parantheses.keys():
                if stack and stack[-1] == parantheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
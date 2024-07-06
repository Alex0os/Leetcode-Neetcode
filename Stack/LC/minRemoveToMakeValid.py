class Solution(object):
    def minRemoveToMakeValid(self, s):
        # El patron es ir sacando los parentesis que no son validos.
        # Parentesis abiertos sin cerrar, parentesis cerrados sin abrir

        # Esta es la solución eficiente
        s = list(s)
        stack = []  # stack[str]
        for i, char in enumerate(s):
            if stack and stack[-1][1] + char == "()":
                stack.pop()
                continue
            if char == ")" or char == "(":
                stack.append((i, char))
                continue

        return_string = ""
        for i, char in enumerate(s):
            if stack and (i, char) == stack[0]:
                stack.pop(0)
                continue
            return_string += char

        return return_string




print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
print(Solution().minRemoveToMakeValid("a)b(c)d"))
print(Solution().minRemoveToMakeValid("))(("))

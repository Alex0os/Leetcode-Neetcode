class Solution(object):
    def isValid(self, s):
        closers = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if stack and char in closers and closers[char] == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(char)


        return True if len(stack) == 0 else False

print(Solution().isValid("()"))

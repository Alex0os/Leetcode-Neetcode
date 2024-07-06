class Solution(object
    def minLength(self, s):
        stack = []

        for char in s:
            if stack and (stack[-1] + char == "AB" or stack[-1] + char == "CD"):
                stack.pop() 
                continue

            stack.append(char)

        return len(stack)

# Me demore 5 minutos en hacer este ejercicio


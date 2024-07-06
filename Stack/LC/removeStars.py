# Me tomo 2 minutos resolver este problema. Aunque realmente no deberia
# considerarse un problema de nivel medio
class Solution(object):
    def removeStars(self, s):
        stack = []

        for char in s:
            if stack and char == "*":
                stack.pop()
                continue
            stack.append(char)

        return "".join(stack)

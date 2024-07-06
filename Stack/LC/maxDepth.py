# Dada una cadena que contiene elementos dentro de parentesis, hay que retornar
# la cantidad mas grande de parentesis anidados, es decir, hay que encontrar el
# elemento que lo rodean la mayor cantidad de parentesis al mismo tiempo y
# luego devolver la cantidad de parentesis lo rodean

class Solution(object):
    def maxDepth(self, s):
        stack = []
        max_nest = 0

        for char in s:
            if char == "(":
                stack.append(char)

            if stack and char == ")":
                max_nest = max(max_nest, len(stack))
                stack.pop()

        return max_nest


print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))

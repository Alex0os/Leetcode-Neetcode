# La explicación es simple, tomas un parentesis y guardas su indice, en el
# momento en el cual encuentres su par que cierra el parentesis, entonces
# volteas la sección de la cadena la cual cubre los parentesis, y luego sigues
# hasta que hayas recorrido toda la lista derivada de la cadena, volteando cada
# sección

# Me tomo como una hora poder hacer este problema, no estaba tan serio
# intentando la verdad debo confesar, fallo mio

class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        s = list(s)

        for i, char in enumerate(s):
            if stack and stack[-1][1] + char == "()":
                s[stack[-1][0] + 1: i] = s[stack[-1][0] + 1: i][::-1]
                stack.pop()
                continue

            if char == "(":
                stack.append((i, char))

        return "".join([char for char in s if char.isalpha()])


print(Solution().reverseParentheses("(abcd)"))
print(Solution().reverseParentheses("(u(love)i)"))
print(Solution().reverseParentheses("(ed(et(oc))el)"))

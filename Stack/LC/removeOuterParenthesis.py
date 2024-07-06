# Me tomo 12 minutos entender el problema

# Me tomo una hora resolverlo

# En vez de agregar un parentesis al stack cuando se encuentra un parentesis de
# apertura, deberia comprobar primero si ya existe un parentesis de apertura
# dentro del stack, si es asi, entonces se debe agregar tanto al stack como a
# la cadena, solamente se debe agregar el de cerrado si al encontrarse este
# parentesis de cerrado y sacar su parentesis correspondiento, el stack queda
# al menos un elemento, de caso contrario, entonces este parentesis de
# cerradura es el parentesis externo

class Solution(object):
    def removeOuterParentheses(self, s):
        stack = []
        outermost_removed = ""

        for i in range(len(s)):
            char = s[i]
            if stack and char == "(":
                stack.append(char)
                outermost_removed += char
                continue

            if char == ")":
                stack.pop()
                if stack:
                    print(f"En la iteración {i}, se agregara un parentesis cerrado al resultado")
                    outermost_removed += char
                    # continue
                    # ^
                    # |
                    # Esto creaba un error debido a que cuando el
                    # stack quedaba vacio, no se saltaba a la siguiente
                    # iteración, si no que seguia con la función hasta llegar a
                    # la ultima linea del bucle en donde se agregaba el
                    # parentesis cerrado
                continue

            stack.append(char)

        return outermost_removed


print(Solution().removeOuterParentheses("(()())(())"))

# Lo que se me esta ocurriendo es ir resgistrando la profundidad (de anidados)
# en la cual nos encontramos en ese momento, esta profundidad sera un numero
# entero no negativo, la cual se usara para indicar cuantas veces se tiene que
# duplicar el valor el cual se obtiene cuando se encuentra un par de parentesis
# validos

# Me demore 25 minutos

class Solution(object):
    def scoreOfParentheses(self, s):
        depth = []
        stack = []
        score = 0

        for char in s: 

            if not stack and char == ")":
                depth.pop()
                continue
            elif stack and char == ")": 
                stack.pop()
                score += 1 * (2 ** len(depth))
                continue 
            elif stack and char == "(":  
                depth.append(stack.pop(0))
                stack.append(char)
                continue
            
            stack.append(char)

        return score
        


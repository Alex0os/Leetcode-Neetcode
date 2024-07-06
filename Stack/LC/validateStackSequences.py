# Si el primero de los que se ponen al final de la pila es igual al primero que
# se saca, entonces ambos se sacan de sus respectivos arrays, en caso
# contrario, entonces se toma el siguiente de los que se colocan en la cima del
# stack para ver si cumple, si en algun mommento ambos son diferentes y no
# quedan elementos a pushear, entonces no puede ser resultado de una secuencia,
# de lo contrario, cuando no quede ninguno en ambos, entonces se eliminan

# Me tomo 30 minutos poder completar esto

# Aunque no estoy totalmente seguro de como logre encontrar la solución.
# Me explico, el enunciado anterior es el procedimiento que queria pasar a
# codigo, y el concepto funciono. Lo que ahora me queda en duda es porque
# funciono ahora que en vez de usar el bucle while mientras hubiera elementos
# en "popped" siendo que cuando use "pushed" como condicional del bucle, esto
# no funciono

# Una idea era que, cuando se cumpla la condición, entonces eventualmente todos
# los elementos de popped seran eliminados, y se saldra del bucle while, en
# cambio, si en algun momento se acaban los elementos de "pushed" y el ultimo
# elemento empujado no encaja con el siguiente elemento a sacar del stack
# (popped[0]), entonces la condición no se cumple

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []

        while popped:
            if not pushed and stack[-1] != popped[0]:
                return False

            if stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
                continue

            stack.append(pushed.pop(0))

        return True






print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))

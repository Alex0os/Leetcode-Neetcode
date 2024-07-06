# Me demore 15 minutos en resolver este problema

# La intuición es, cada vez que hagamos una iteración dentro del bucle while,
# lo primero que estaremos haciendo es un "Push" al stack, queriendo pushear al
# final de la pila el elemento de el flujo de numeros que toca en esa
# iteración, luego, vemos si ese numero es igual al primer numero de el array
# de enteros, indicando que es un numero que corresponde para crear un
# equivalente al mismo array de numeros.

# Si es asi, entonces se elminina ese numero de el array de enteros original,
# ya que ahora estaremos buscando el siguiente.

# De caso contrario, entonces este numero no nos sirve, por lo tanto lo
# "eliminamos de la copia", lo cual se representa con un pop

# Al final del bucle, simplemente indicamos que pasamos al siguiente numero,
# para que en la siguiente iteración, se haga el mismo proceso sobre este
# numero a continuación

class Solution(object):
    def buildArray(self, target, n):
        stack = []
        i = 1
        while True:
            stack.append("Push")
            if i == target[0]:
                target.pop(0)
            else:
                stack.append("Pop")
            i += 1

            if len(target) == 0:
                return stack

class Solution:
    def finalPrices(self, prices):
        stack = []
        for i, p in enumerate(prices):
            print(stack, prices)
            while stack and prices[stack[-1]] >= p:
                prices[stack.pop()] -= p
            stack.append(i)
        return prices


Solution().finalPrices([8, 4, 6, 2, 3])


# No pude completarla, esta solución es parte de las que encontre, y es la
# unica que vi que hacia uso de un stack

# Mañana quiero volver a ver esta idea, mencionar también que este problema usa
# un stack mononotico, no un stack normal

# Realmente no es que sea un problema dificil de entender, pero es que la
# implementación del stack en este problema se va un poco fuera de lo
# convencional. En vez de guardar los precios dentro del stack, guardas los
# indices de los precios, y por cada iteración compruebas si el ultimo indice
# apunta a un precio el cual sea mayor o igual al precio que tomaste durante
# esa iteración.

# De ser asi, entonces usas un bucle while el cual vaya recorriendo el stack
# desde el final hacia atras, sacando los indices los cuales apuntan a valores
# mayores o iguales a el que se tomo en esa iteración, y cuando sacas uno,
# aprovechas para poder acceder a ese valor y aplicarle el descuento
# (precios[i] - p if precios[i] >= p). Y luego, independiente si habia o no un
# indice que apuntaba a un valor mayor, agregas el indice del valor de esa
# iteración al stack, y repites el proceso

# El uso de indices en vez de los valores es util si lo piensas, en casos donde
# realmente no te interesan todos los valores, si no que hacer modificaciones
# segun valores que le siguen a los valores que ya recorriste

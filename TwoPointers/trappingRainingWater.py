# El algoritmo es una busqueda con dos punteros, en la cual se inicializa en un
# numero, y se busca otro numero el cual sea igual o mayor a
# este, luego se multiplica el area entre el numero que sea menor entre estos 2
# (el mismo numero si ambos son iguales) y luego se le restan
# todos los numeros los cuales esten entremedio de este

# Una aproximación que promete ser correcta es inicializar 2 puntos y hacer lo
# mismo que la anterior, tomar el elemento que esta en el
# puntero izquierdo, compararlo con el cual esta en el puntero derecho y luego
# calcular la cantidad de agua. Ahora, la diferencia radica es

# que si en algun momento se encuentra algun elemento el cual sea el mas grande
# y ya no hayan mas elementos cuyo valor sea comparable para
# poder hacer el calculo de cuanta agua existe entre este elemento (al cual
# apunta el puntero izquierdo), entonces se pasa al siguiente
# elemento del elemento actual al cual apunta el puntero izquierdo

# Solución con complejidad espacial de O(n) (O(3n) que se trunca a O(n)) y
# complejidad temporal de O(n), (Que igual se trunca a (O(3n))

class Solution(object):
    def trap(self, height):
        max_left_value = 0
        max_right_value = 0

        max_left = []
        max_right = []

        total = 0

        for num in height:
            if num > max_left_value:
                max_left.append(max_left_value)
                max_left_value = num
            else:
                max_left.append(max_left_value)

        for num in height[::-1]:
            if num > max_right_value:
                max_right.append(max_right_value)
                max_right_value = num
            else:
                max_right.append(max_right_value)

        print(max_left)
        max_right = max_right[::-1]
        print(max_right)

        for i in range(len(height)):
            min_max = min(max_left[i], max_right[i])

            amount_water = min_max - height[i]
            if amount_water <= 0:
                continue

            total += amount_water

        return total



solution = Solution()

print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print("\n")
print(solution.trap([0,2,0]))

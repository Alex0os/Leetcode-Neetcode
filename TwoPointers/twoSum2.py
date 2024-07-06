class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            right_num = numbers[right]
            left_num = numbers[left]

            if right_num + left_num == target:
                return [left + 1, right + 1]

            if right_num + left_num > target:
                right -= 1
            else:
                left += 1
        else:
            return "No se ha encontrado solución"

# Fue bastante aburrido no poder hacerlo yo mismo sin poder entender como funciona el problema, pero tratare de dar la explicación

# La intuición era que, en un caso de fuerza bruta, realmente lo unico que se podría hacer es una iteración por cada numero de el array que
# se tome, lo cual haria que la complejidad temporal fuera igual a el cuadrado de el tamaño de la lista de entrada.

# Para poder realizar una busqueda con 2 punteros la cual se haga en una complejidad temporal lineal, lo que se debe de hacer es que,
# teniendo en cuenta de que la lista esta ordenada en orden ascendente, eso permite que haya momentos en los cuales, la suma de los valores
# de los extremos sea mayor o menor que el numero buscado, con lo cual se puede aprovechar esta caracteristica para ir viendo si se debe de
# avanzar hacia la derecha o si se debe avanzar hacia la izquierda con el puntero en el extremo de el array contrario al sentido al cual se
# busca moverse. Y con ello se llegara en algun momento a un par de numeros el cual den el numero objetivo, pudiendo asi devolver sus
# indices. De ser el caso contrario, solo quedaria retornar un valor que indique que no se ha encontrado una solución en el array

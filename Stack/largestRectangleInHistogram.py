'''Se otorga una array "heights" de enteros el cual representa un histograma
dode la anchura de cada barra (entero dentro del array) es 1. Regresa el area
del rectangulo mas grande que haya'''


# Nota 1: Cuando estas recorriendo el histograma, puede suceder que el elemento
# en el cual estas sea menor al anterior. Esto indica que el anterior no puede
# seguir produciendo areas validas debido a que el elemento en el cual te
# encuentras actualmente sera el valor el cual sera considerado al momento de
# calcular el area

'''
Se recorre el array y se agregan elementos al stack.

Cuando el elemento que se agrega es menor al ultimo elemento en el stack,
entonces se inicia un proceso en el cual se eliminaran del stack todos los
elementos que sean mayores al elemento que se va a colocar en el stack, hasta
llegar a un elemento en el stack el cual sea menor o igual a este elemento que
se va a agregar. Luego, se reemplazan las posiciones de los elementos
eliminados del stack con valores iguales al elemento que se va a agregar

Durante esta secuencia de eliminación de elementos, se debe hacer el calculo de
las areas de los elementos que se van agregando, cada vez que se elimina el
elemento, se calcula el area de este elemento multiplicando el valor del
elemento por la diferencia entre el indice del elemento y el elemento que se va
a agregar al stack.

'''

# Esta solución no supera todos los casos
class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for height in enumerate(heights):
            while stack and stack[-1][-1] > height[1]:
                i_last_element = stack[-1][0]
                value_last_element = stack[-1][1]

                area = value_last_element * (height[0] - i_last_element)
                if max_area < area:
                    max_area = area


                stack.pop()

            stack.append(height)

        # Computar todas las areas que se pueden hacer con los elementos del
        # stack

        for element in stack[::-1]:
            area = element[1] * (len(heights) - element[0])
            if area > max_area:
                max_area = area

        return max_area


class Solution1(object):
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([2, 4]))

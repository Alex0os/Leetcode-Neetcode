# En este problema, se toma un array de numeros en donde cada numero representa una altura determinada. La tarea es encontrar 2 alturas las
# cuales multiplicadas por la distancia entre ellas den el maximo numero posible. Estas seran las "dimensiones" del contenedor de agua
# (De ahí el nombre del probleam)

# Hagamos lo siguiente, recorramos el array de izquierda a derecha ordenando de mayor a menor y luego hagamoslo de derecha a izquierda

# Inicializar 2 punteros a los bordes del array, luego multiplicar el area (distancia entre los 2 puntos por el menor entre ambos) y guardar
# el resultado, luego hacer que el puntero avance segun cual de los 2 elementos sea menor. (Si son iguales, aumentar puntero izquierdo)

# La razon por la cual este algoritmo no funciona es debido a que no considera los casos en los que luego de encontrar un numero grande no
# se encuentren mas numeros que sean del mismo tamaño o mayor que el mismo
# 

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1

        results = []

        while left < right:
            left_val = height[left]
            right_val = height[right]

            print(left_val, right_val)


            area = (right - left) * min(left_val, right_val)
            results.append(area)

            if left_val == right_val:
                left += 1
                continue

            bigger = max(left_val, right_val)

            if bigger == left_val:
                right -= 1
                continue
            elif bigger == right_val:
                left += 1
                continue

        return max(results), results



solution = Solution()

print(solution.maxArea([1,8,6,2,5,4,8,3,7]))


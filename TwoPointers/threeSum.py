# Se usan 3 referencias a variables o variables para mantener registro de información necesiaria como indices.

# Podria almacenar todos los pares de valores que se encuentran
# Entonces. ¿Cómo soluciono este problema?

# Lo primero que se me ocurre es ordenar el array, para poder generar un proceso el cual vaya reduciendo el tamaño del array que necesito
# recorrer para encontrar las tripletas de numeros.

# Cuando tenga el array ordenado, puedo irlo recorriendo desde sus 2 extremos, y aqui es donde el proceso toma lugar, ya que para que
# funcione el algoritmo, puedo ir tomando cada numero que esta en el extremo de los numeros menores, y luego de eso recorrer el array con 2
# punteros los cuales vayan buscando el par de numeros que sumado al numeros del extremo de los menores de 0, y cuando los encuentre,
# colocar la posición de los punteros en el extremo de los mayores en la posicion de el numero menor en el par de numeros en el extremo de
# los mayores, ya que el siguiente numero que le siga, no tendra la posibilidad de encontrar un par que le corresponda en la sección ya
# recorrida, ya que cualquier resultado de la suma seria mayor a cero en todas las tripletas que se puedan dar en ese rango

# Los numeros se deben ordenar debido a que cuando lo este resolviendo como resolvi 2 sums, va a haber momentos en donde la suma de
# los 2 numeros a los cuales apuntan los punteros den mas o menos que el numero fijado, y desde alli voy a querer aumentar o
# disminuir el valor de la suma de estos (que en este caso solo se puede lograr haciendo que el puntero izquierdo avance o que el
# derecho retroceda)

# Vaya mierda de boilerplate, mañana veremos una solución la cual sea mucho mas aceptable

class Solution(object):
    def threeSum(self, nums):

        resultados = []

        nums = sorted(nums)

        for i, x in enumerate(nums):


            right = len(nums) - 1
            left = i + 1

            while left < right:
                result_two_ptrs = nums[left] + nums[right]

                if (result_two_ptrs + x) == 0:
                    agregado = [x, nums[left], nums[right]]
                    if agregado not in resultados:
                        resultados.append(agregado)

                        left += 1
                        continue
                    else:
                        left += 1
                        continue
                elif (result_two_ptrs + x) < 0:
                    left += 1
                elif (result_two_ptrs + x) > 0:
                    right -= 1

            if (i == len(nums) - 1):
                break

        return resultados



solution = Solution()

print(solution.threeSum([0, 0, 0, 0]))

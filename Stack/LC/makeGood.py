# La razon por la cual los condicionales tienden a ser de esta manera:
# "if stack and (...)"
# Es debido a que para luego poder revisar el ultimo elemento del stack,
# primero el stack debe de estar lleno, asi no se causan errores que pueden
# interrumpir el codigo

# Me tomo 10 minutos poder hacer esta solución
# Mas que nada son varias condiciones que se tienen que tener en cuenta antes
# de sacar un elemento de un stack, ya que primero que todo los caracteres
# adyacentes tienen que ser diferentes para luego ver si alguno de los dos
# equivale a la version mayuscula o minuscula del otro, ya que debido a la
# naturaleza de los metodos ".upper()" y ".lower()", si estos son iguales,
# entonces la condición se cumplira y se sacaran esos caracteres del stack
# aunque realmente no cumplan la condición que hace que los 2 deban ser
# eliminados de la cadena

class Solution(object):
    def makeGood(self, s):
        stack = []

        for char in s:
            if stack and char != stack[-1] and (char.upper() == stack[-1] or char.lower() == stack[-1]):
                stack.pop()
                continue
            stack.append(char)

        return "".join(stack)

# Quiero hacer un ejercicio mas de stacks que sea facil y luego de eso tratar
# con medios, mientras estudio el concepto de el stack monotono

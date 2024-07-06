# Me tomo 3 minutos completar este problema
# El problema se basa en devolver una cantidad, esta cantidad es la cantidad de
# veces que se debe retroceder en un sistema de archivos para volver a la
# carpeta en donde comenzo el registro (llamada Main).

# El codigo es bastante auto-explicatorio, asi que simplemente lo dejare aqui
# para poder dar a vasto de lo que se trata el problema (franco, franco,
# franco)

class Solution(object):
    def minOperations(self, logs):
        stack = []

        for op in logs:
            if op == "./":
                continue
            elif op == "../":
                if not stack:
                    continue
                stack.pop()
            else:
                stack.append(op)

        return len(stack)
        



class Solution(object):
    # Esto es fuerza bruta
    def dailyT1(self, temperatures):
        answers = []

        for i in range(len(temperatures)):
            if i == len(temperatures) - 1:
                answers.append(0)
                break
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    answers.append(j - i)
                    break

                if j == len(temperatures) - 1:
                    answers.append(0)
                    break

        return answers

    '''No funciona porque no tomas los casos en los que, luego de encontrar una
    temperatura, no encuentras una temperatura mayor a esta, pero si encuentras
    temperaturas que son mayores a los que le siguen a ese numero 

    Ej:
        75, 72, 69, 74

    En este caso, tendras el recuento de los dias entre las temperaturas que
    van desde el 72 hasta el 74, pero no tendras forma de comprobar los dias
    entre el 75

    '''

    # Tiene que ser asi debido a que si la lista esta vacia y se hace con
    # los valores se insertan con "insert()", entonces habra problemas
    # debido a como el metodo mueve los elementos dentro de la lista cuando
    # intenta insertar un elemento en un indice el cual ya tiene un
    # elemento
    def dailyTemperatures(self, temperatures):
        answers = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                days_between = i - stack[-1][0]
                value = stack.pop(-1)
                answers[value[0]] = days_between


            stack.append((i, temp))

        return answers






print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(Solution().dailyTemperatures([30, 40, 50, 60]))
print(Solution().dailyTemperatures([30, 60, 90]))

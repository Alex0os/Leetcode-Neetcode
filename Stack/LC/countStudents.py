# El proceso se hara mientras el estudiante que este al final no llegue a la
# fila, el estudiante al final de la fila a considerar cambia siempre y cuando
# un estudiante saque un sandwich

# La falla esta en que al hacer lo que se dice en el enunciado anterior,
# realmente no se cambia cual es el ultimo el elemento de la lista

class Solution(object):
    def countStudents(self, students, sandwiches):
        students = list(enumerate(students))

        # El uso de una lista para ir agregando a los estudiantes los cuales
        # han ido al final de la fila permite que en el momento en el cual
        # exista un bucle en el cual ningun momento un estudiante tome el
        # sandwich en la parte superior del stack, se pueda comprobar si ya se
        # intentaron todos los estudiantes desde el ultimo sandwich que se
        # tomo, condición representada con la linea -->
        # "if students_stack == # students:", y si es asi, entonces se devuelve
        # el tamaño de la cola de estudiantes, indicando que esos fueron los
        # que no pudieron comer sandwich

        students_stack = []

        while True:
            if students[0][1] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)

                if len(students) == 0:
                    return 0
                students_stack = []
            else:
                element = students.pop(0)
                students.append(element)
                students_stack.append(element)

            if students_stack == students:
                return len(students_stack)





print(Solution().countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))
print(Solution().countStudents([1, 1, 0, 0], [0, 1, 0, 1]))

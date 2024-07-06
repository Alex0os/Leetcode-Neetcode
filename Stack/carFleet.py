'''
position = list[int] --> len(n)
speed = list[int] --> len(n)

speed[i] and position[i] belongs to the i"th" car

if a car reach a car ahead of it, then the car will slow down matching the
speed of the car ahead of it

El problema se vasa en que en una sola carretera, hay autos recorriendola a una
cierta velocidad comenzando en una cierta posición (position y speed), la tarea
cuando una cantidad "n" va viajando a una velocidad hasta llegar a destino,
entonces se dice que una flota a llegado a destino, el objetivo es retornar la
cantidad total de flotas que llegan a destino (considerese 1 también una flota)

'''
# No tengo idea de como aproximarme a este problema asi que supongo que
# simplemente voy a ver el video

# Una cosa que he notado en los problemas que tienen numeros los cuales se
# buscan que se relacionen con cierto valor, es que normalmente la solución se
# basan en valor a relacionar con cada numero

# Entonces, la aproximación es tomar todas las posiciones iniciales y
# velocidades y organizarlas desde la que esta mas cerca del objetivo hasta la
# que esta mas lejos (de mayor a menor), luego calcular cuanto se va a demorar
# en llegar el auto al objetivo, que se calcula restando el objetivo con la
# posición del auto y luego dividiendo el resultado por la velocidad, luego
# se avanza hacia el siguiente y auto y se hace el mismo calculo, donde si el
# resultado es el mismo o menor al anterior, eso querra decir que llegara en el
# mismo momento o antes, lo cual segun las reglas del problema, hara que ambos
# conformen una flota

class Solution(object):
    def carFleet(self, target, position, speed):

        # La razon por la cual el tamaño del stack es el equivalente a cuantas
        # flotas llegan al objetivo es porque en cada iteración en donde se
        # cumple la condición donde hay mas de 2 elementos en el stack y en
        # donde el ultimo tiempo que se agrego es menor o igual al penultimo
        # (lo que quiere decir que el auto mas atras alcanza al ultimo), se
        # elimina el tiempo del auto que alcanzo al ultimo, haciendo que al
        # final este llege con el ultimo auto, es decir, que sea una flota,
        # cuando sea el caso contrario, es decir que el ultimo tiempo agregado
        # sea mayor, entonces ese auto no se convertira en parte de la flota,
        # por lo cual a partir de este se creara una nueva flota hasta que se
        # encuentre un tiempo mayor
        stack = []

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        for pos, sp in pairs:
            t = (target - pos) / sp
            stack.append(t)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))

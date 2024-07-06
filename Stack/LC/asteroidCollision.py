# Llevo como 30 minutos en este problema

# El "else" luego de un bucle while realmente fue util. Y tiene
# bastante sentido, ya que solamente necesitamos sacara asteroides
# del stack si el ultimo asteroide registrado va a la derecha (es
# positivo) y el que viene va a la izquierda (es negativo), con eso
# en mente, cuelquier otro caso en el que se pueda pensar, como que
# el ultimo asteroide del que se tiene registro va a la izquierda y
# el siguiente va a la derecha, o que ambos asteroides vayan en la
# misma dirección, significara que no habra ninguna colisión, y por
# lo tanto el asteroide se puede añadir al registro (el "stack")

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for ast in asteroids:
            while stack and (stack[-1] > 0 and ast < 0):
                if abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break

                if stack[-1] + ast < 0:
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(ast)

        return stack



print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([-2, -1, 1, 2]))


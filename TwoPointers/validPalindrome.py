# Aunque este sea resoluble facilmente con tecnicas intuituvas y herramientas otorgadas por Python, vamos a resolver esto con el algoritmo
# de 2 punteros.

class Solution(object):
    def isPalindrome(self, s: str):
        # Hay 3 consideraciones las cuales deben estar presentes dentro de el recorrido de el bucle
        # 1. No se deben comparar elementos numericos
        # 2. No se deben comparar elementos no alfabeticos
        # 3. Los caracteres a compararse no deben de ser mayusculas

        # Se define la variable que recorre desde el final
        right = len(s) - 1
        left = 0

        while left < right:
            right_char = s[right].upper()
            left_char = s[left].upper()

            if not left_char.isalnum():
                left += 1
                continue
            if not right_char.isalnum():
                right -= 1
                continue

            if right_char != left_char:
                return False
            else:
                left += 1
                right -= 1


        return True

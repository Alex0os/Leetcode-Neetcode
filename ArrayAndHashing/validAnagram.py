'''Dada 2 cadenas, "s" y "t", devuelve "True" si "t" es un anagrama de "s" y "False" si no es asi'''
from collections import defaultdict

class Solution1(object):
    def isAnagram(self, s, t):
        count_s = defaultdict(bool)

        for char in s:
            count_s[char] += 1

        for char in t:
            count_s[char] -= 1

        for value in count_s.values():
            if value != 0:
                return False

        return True


class Solution():
    def isAnagram(self, s, t):
        count = {}
        words_size = len(s)

        i = 0

        while i < words_size:
            s_char = s[i]
            t_char = t[i]

            if s_char in count and t_char in count:
                count[s_char] += 1
                count[t_char] -= 1
            elif s_char not in count and t_char in count:
                count[s_char] = 1
                count[t_char] -= 1
            elif s_char in count and t_char not in count:
                count[s_char] += 1
                count[t_char] = -1
            else:
                count[s_char] = 1
                count[t_char] = -1

            i += 1

        return count


print(Solution().isAnagram("racecar", "carrace"))
print(Solution().isAnagram("jar", "jam"))





'''
2 palabras son anagramas unas de otras si cumplen 2 condiciones:
    1.- Tienen la misma cantidad de caracteres unicos
    2.- Tienen la misma cantidad de cada caracter unico que poseen

Con esto en mente, simplemente es una suma de cancelación, tomaremos cada caracter unico en "s" como una clave dentro de un diccionario
(que en este caso hemos llamado "count_s"), donde el valor de esta clave sera la cantidad de veces que este caracter unico se repite,
luego de eso, se hace lo mismo con "t", pero esta vez, cada vez que encontremos un caracter unico en "t", buscaremos el item
correspondiente a este caracter dentro del diccionario y luego de eso restaremos en 1 el valor de este item. Si ambas palabras son
anagramas, los valores de cada item deberian ser 0 (debido a la segunda condición mencionada anteriormente), en caso de que algun valor no
sea 0, entonces estas palabras no son anagramas
'''

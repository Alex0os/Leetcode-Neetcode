'''Dado un array de enteros "nums", devuelve "true" si cualquiera de los valores aparece al menos 2 veces en el array, devuelve "false" si
sucede lo contrario'''

from collections import defaultdict

class Solution(object):
    def containsDuplicate(self, nums):
        exist_in_array = defaultdict(bool)

        for num in nums:
            if exist_in_array[num]:
                return True

        return False


'''Idea simple: Usando un mapa hash, cuando este numero no exista dentro de el mapa hash, entonces, lo usaremos como una clave cuyo
    valor sera true, y asi en el momento que este numero si exista dentro del mapa hash, entonces este nos devolvera un valor que
    confirme que este numero se repite en el array en una complejidad lineal de O(1), ya que el algoritmo de hasheo de los diccionarios
    de Python manejan bien las colisiones'''

class Solution1():
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = set()

        for num in nums:
            if num in hashmap:
                return True
            hashmap.add(num)

        return False

Solution1

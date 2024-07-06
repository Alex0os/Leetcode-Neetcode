'''Dado un array de enteros "nums" y un entero "target", devuelve los indices de 2 numeros los cuales sumados te den el numero "target"'''

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for index, num in enumerate(nums):
            if num in hashmap:
                return hashmap[num], index

            hashmap[target - num] = index


'''Cuento corto, si ya tengo un numero y quiero saber cual a continuación dentro del array me da el
numero objetivo cuando los sumamos, basta solamente con restar el numero objetivo con el numero el cual tengo en ese momento.

Luego, para acceder al indice de este numero que use como resta del numero objetivo, defino un diccionario que almacene este resultado como
una clave y que el valor de esta clave sea el indice del numero usado para restar, con ello, cuando este numero se encuentre mas adelante en
el array, se podra hashear en el mapa y asi obtendremos el indice de su numero par.
'''

# Solo para poder hacer repaso, la idea sera recorrer el array "nums" y con
# cada numero que se tome, sacar la diferencia entre el "target" y el "num[i]"
# y luego comprobar si esa diferencia existe puede hashearse hacia un item
# dentro de el diccionario, de no ser asi, entonces se agrega un nuevo item con
# esta diferencia como clave y el indice en el cual se encontraba este "num[i]"
# como valor

# De ser el caso contrario, quiere decir que hemos econtrado el otro numero el
# cual sumado a otro da igual a "target", con lo usamos este numero para
# obtener el indice del otro numero ([i]) y luego lo retornamos con el indice
# del numero el cual estamos revisando actualmente ([j]), y con eso obtenemos
# [i, j]

'''Dado un array de enteros "nums" y un entero "k", devuelve la cantidad "k" de enteros mas repetidos dentro de "nums"'''

class Solution(object):
    def topKFrequent(self, nums, k):
        number_and_frequencies = {}

        for num in nums:
            if num in number_and_frequencies:
                number_and_frequencies[num] += 1
            else:
                number_and_frequencies[num] = 1

        number_and_frequencies = number_and_frequencies.items()

        frequencies = sorted(number_and_frequencies, key=lambda x: x[1])[::-1]

        top_freq = []

        for i in range(k):
            top_freq.append(frequencies[i][0])

        return top_freq

'''El procedimiento es un tipo de hashing simple, en donde se recorre el array de numeros y se usa cada numero como una clave hash de el
diccionario definido al principio, luego si el numero se repite en el array, se hashea y se le agrega 1 al valor del item que le corresponde
a este numero, con eso, se consigue tener la cantidad "k" de numeros mas repetidos dentro del array. Lo unico que queda es organizarlos
segun el valor de los items, para que los "k" numeros mas repetidos esten al final o al principio de la estructura que almacenara los items'''

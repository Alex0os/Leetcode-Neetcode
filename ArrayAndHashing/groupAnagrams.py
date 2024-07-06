'''Dado un array de cadenas "strs", agrupa todas las palabras que sean anagramas en un array, puedes retornar la respuesta en cualquier
orden'''

'''Entonces, debido a las condiciones que se deben cumplir para que palabras sean anagramas, podemos tomar una palabra, reorganizar sus
caracteres en orden alfabetico y hacer que la palabra resultante sea una clave dentro de un mapa hash, el cual tendra como valor la lista de
todos los anagramas los caracteres compuesto por los mismos caracteres que componen la clave (es decir, los anagramas)'''


class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            sorted_chars = sorted(word)
            key = "".join(sorted_chars)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        anagrams_groups = [group for group in groups.values()]
        return anagrams_groups

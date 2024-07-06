# Me tomo entre 10 y 15 minutos encontrar la solución a este problema

class Solution(object):
    def backspaceCompare(self, s, t):
        s_stack = []
        for char in s:
            if s_stack and char == "#":
                s_stack.pop()
                continue
            elif not s_stack and char == "#":
                continue
            s_stack.append(char)

        t_stack = []
        for char in t:
            if t_stack and char == "#":
                t_stack.pop()
                continue
            elif not t_stack and char == "#":
                continue
            t_stack.append(char)

        return t_stack == s_stack

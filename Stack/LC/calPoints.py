class Solution(object):
    def calPoints(self, operations):
        stack = []

        for p in operations:
            if p == "+":
                new_record = stack[-2] + stack[-1]
                stack.append(new_record)
            elif p == "D":
                stack.append(stack[-1] * 2)
            elif p == "C":
                stack.pop()
            else:
                stack.append(int(p))

        return sum(stack)

# Me tomo 5 minutos completar esto

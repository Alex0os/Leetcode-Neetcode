class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for element in tokens:
            print(stack)
            if element == "+":
                stack.append(stack.pop() + stack.pop())
            elif element == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif element == "*":
                stack.append(stack.pop() * stack.pop())
            elif element == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(element))

        return stack[0]





print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

# Can't be done in leetcode due the Python version used

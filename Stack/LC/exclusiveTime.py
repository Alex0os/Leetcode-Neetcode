# No pude, tengo que ver la solución despues

# Esta solución solamente pasa unos cuantos casos, pero no los que tienen
# registros grandes de llamadas de funciónes, ya que es dificil tener registro
# del tiempo que se pierde en llamadas recursivas o llamadas dentro de otras
# llamadas

class Solution1(object):
    def exclusiveTime(self, n, logs):
        results = [0] * n

        logs = [log.split(":") for log in logs]
        total_time = int(logs[-1][-1]) + 1

        stack = []


        for log in logs:
            if stack and log[1] == "end":
                last_log = stack.pop()
                function_id = int(last_log[0])
                time_used = int(log[-1]) - int(last_log[-1]) + 1
                time_used = min(time_used, total_time)
                total_time -= time_used
                results[function_id] += time_used
                continue

            stack.append(log)
        return results

class Solution(object):
    def exclusiveTime(self, n, logs):
        stack = []
        result = [0] * n

        def normalizeProcessTime(processTime):
            return processTime.split(':')
            # El metodo "encode()" junto con el argumento "ignore" convertira
            # creara una nueva cadena donde solamente existan caracteres 'ASCII'

        for processTime in logs:
            processId, eventType, time = normalizeProcessTime(processTime)

            if eventType == "start":
                stack.append([processId, time])

            elif eventType == "end":
                processId, startTime = stack.pop()
                timeSpent = int(time) - int(startTime) + 1  # Add 1 cause 0 is included
                result[int(processId)] += timeSpent

                # Decrement time for next process in the stack
                if len(stack) != 0:
                    nextProcessId, timeSpentByNextProcess = stack[-1]
                    result[int(nextProcessId)] -= timeSpent

        return result



print(Solution().exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
print(Solution().exclusiveTime(1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]))
print(Solution().exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]))

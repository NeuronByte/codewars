import math
def checkExam(x, y):
    examTotal = 0
    for i in range(0, len(x)):
        examTotal += 4 if x[i] == y[i] else -1
    return math.max(examTotal, 0)
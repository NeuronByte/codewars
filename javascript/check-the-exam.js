checkExam = (x, y) => Math.max(y.reduce((a, b, i) => b == x[i] ? a + 4 : b ? a - 1 : a, 0), 0);
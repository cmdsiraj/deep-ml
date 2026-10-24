def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    c = [[]]
    def transpose(mt: list[list[int|float]]) -> list[list[int|float]]:
        m = len(mt)
        n = len(mt[0])

        t = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                t[j][i] = mt[i][j]
        return t
    def dot(p: list[int|float], q: list[int|float]):
        sum = 0
        for i in range(len(p)):
            sum += p[i]*q[i]
        return sum

    m1 = len(a)
    n1 = len(a[0])
    m2 = len(b)
    n2 = len(b[0])
    if n1!=m2:
        return -1
    bt = transpose(b)
    

    c = [[0]*n2 for _ in range(m1)]
    for i in range(m1):
        for j in range(n2):
            c[i][j] = dot(a[i], bt[j])

    return c

def multi(m1,m2):
    matriz_res = [[0]*len(m2[0]) for i in range(len(m1))]     
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(matriz_res)):
                matriz_res[i][j] += m1[i][k]*m2[k][j]
    return matriz_res

def canicas1():
    bol = [[0]*6 for i in range (6)]
    bol [2][1] = 1
    bol [3][3] = 1
    bol [2][5] = 1
    bol [4][2] = 1
    bol [5][0] = 1
    bol [5][4] = 1
    cantidad = [[6],[2],[1],[5],[3],[10]]
    click = 1
    res = multi(bol,bol)
    click -= 1
    while click>0:
        res = multi(res,bol)
        click -= 1
    
    return multi(res,cantidad)

def vec(v,m):
    res = [[0]*len(m[0]) for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            res[i][j] = round(v * m[i][j],2)
    return res
def multiple(m1,m2):
    res = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res.append(vec(m1[i][j],m2))
    return res
         

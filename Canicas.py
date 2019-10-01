
def multi(m1,m2):
    matriz_res = [[0]*len(m2[0]) for i in range(len(m1))]     
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(matriz_res)):
                matriz_res[i][j] += m1[i][k]*m2[k][j]
    return matriz_res

def suma(a,b):
    ent = a[0]+b[0]
    imag = a[1]+b[1]
    return ent,imag

def multiplicacion(a,b):  
    first = a[0] * b[0]
    second = a[0] * b[1]
    third = a[1] * b[0]
    fourth = a[1] * b[1]
    ent = first-fourth
    imag = second+third
    return ent,imag

def multiplicacion_matrices(m1,m2):
    matriz_res = [[(0,0)]*len(m2[0]) for i in range(len(m1))]
    cos = 0
    if len(matriz_res) == 1:
        cos = 1
        
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(matriz_res)+cos):
                matriz_res[i][j] = suma(matriz_res[i][j],multiplicacion(m1[i][k],m2[k][j]))
    return matriz_res

def canicas1(m1,v1,clicks):

    res = multi(m1,m1)
    clicks -= 1
    while clicks > 0:
        res = multi(res,m1)
        clicks -= 1
    
    return multi(res,v1)

def canicasimag(m1,v1,c):
    res = multiplicacion_matrices(m1,m1)
    clicks -= 1
    while clicks > 0:
        res = multiplicacion_matrices(res,m1)
        clicks -= 1
    return multiplicacion_matrices(res,v1)
         

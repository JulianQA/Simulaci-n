from sys import stdin

def solve():
    cantidad = []
    print('Ingrese el numero de bolsas:')
    bolsas = int(stdin.readline().strip())
    print('Ingrese las canicas que hay por cada bolsa')
    con = 0
    for i in range(bolsas):
        print('Bolsa',con)
        c = int(stdin.readline().strip())
        cantidad.append(c)
        con += 1

    matriz = [[0]*bolsas for i in range(bolsas)]
    print('Ingrese las salidas y entradas')
    while True:
        lis = [int(x) for x in stdin.readline().strip().split()]
        if lis != []:
            for i in range(len(matriz)):
                for j in range(len(matriz)):
                    matriz[lis[1]][lis[0]] = 1
        else:
            break
    for i in matriz:
        print(*i)
solve()
        

fila1 = [20222333, 45, 2, 20000]
fila2 = [33456234, 40, 0, 25000]
fila3 = [45432345, 41, 1, 10000]
fila4 = [43967303, 37,0,12000]
fila5 = [42236276,36,0,18000]


fila12 = [20222333, 20000, 45, 2]
fila22 = [33456234, 25000, 40, 0]
fila33 = [45432345, 10000, 41, 1]

matriz = [fila1, fila2, fila3]
#matriz.append(fila4)
#matriz.append(fila5)
print(matriz)

#def cambiarDeOrden(M, j, k):
 #   res = M
  #  for fila in res:
   ##        fila[j] = fila2[k]
     #       fila[k] = fila2[j]
    #return res

#print(cambiarDeOrden(matriz, 1, 3))


#Matriz como lista de columnas
dni = [20222333, 33456234, 45432345]
salario = [20000, 25000, 10000]
edad = [45, 40, 41]
hijos= [2,0,1]

matriz_empleado_04 = [dni, salario, edad, hijos]

def superanSalarioActividad01(M:[ [ int, int, int, int ] ]):
    res = []
    for i in M:
        if i[3] > 15000:
            res.append(i)
    return res


def superanSalarioActividad04(M:[ [ int, int, int, int ] ]):
    res = [[], [], [], []]
    for i in range(len(M[0])):
        if M[1][i] > 15000:
            res[1].append(M[1][i])
            res[0].append(M[0][i])
            res[2].append(M[2][i])
            res[3].append(M[3][i])
    return res

print(superanSalarioActividad04(matriz_empleado_04))
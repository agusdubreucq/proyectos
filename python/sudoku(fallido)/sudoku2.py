from pyswip import Prolog

base = Prolog()

cadena_larga="cuadrado(filCol(Fila, Col), 1):-between(0, 1, Fila),between(0,2,Col).\
cuadrado(filCol(Fila, Col), 2):-between(0, 1, Fila),between(3,5,Col).\
cuadrado(filCol(Fila, Col), 3):-between(2, 3, Fila),between(0,2,Col).\
cuadrado(filCol(Fila, Col), 4):-between(2, 3, Fila),between(3,5,Col).\
cuadrado(filCol(Fila, Col), 5):-between(4, 5, Fila),between(0,2,Col).\
cuadrado(filCol(Fila, Col), 6):-between(4, 5, Fila),between(3,5,Col).\
porFilaCol(filCol(Fila,Col),Numero):-between(0,5,Fila),between(0,5,Col),between(1,6,Numero),\
not(numero(filCol(Fila,Col),_)),not(numero(filCol(Fila,_),Numero)),not(numero(filCol(_,Col),Numero)).\
porCuadrado(filCol(Fila,Col),Numero):-between(0,5,Fila),between(0,5,Col),between(1,6,Numero),\
cuadrado(filCol(Fila,Col), Cuadrado),forall((cuadrado(FilCol,Cuadrado),FilCol\=filCol(Fila,Col)),not(numero(FilCol,Numero))).\
generarLista(FilCol,Numero):-between(1,6,Numero),porCuadrado(FilCol,Numero),porFilaCol(FilCol,Numero).\
lista(FilCol,Numeros):-cuadrado(FilCol,_),not(numero(FilCol,_)),findall(Numero,generarLista(FilCol,Numero),Numeros).\
unicoCuadrado(FilCol,Numero):-cuadrado(FilCol,Cuadrado),lista(FilCol,Lista),member(Numero,Lista),\
forall((cuadrado(FilColDif,Cuadrado),FilColDif\=FilCol),not(listaGeneradaContiene(FilColDif,Numero))).\
listaGeneradaContiene(FilCol,Numero):-lista(FilCol,Lista),member(Numero,Lista).\
unicoPosible(FilCol,Numero):-lista(FilCol,Lista),length(Lista, 1),member(Numero,Lista).sudoku(FilCol,Num):-numero(FilCol,Num).\
sudoku(FilCol,Num):-valor(FilCol,Num).\
valor(FilCol,Numero):-unicoPosible(FilCol,Numero).valor(FilCol,Numero):-unicoCuadrado(FilCol,Numero)."
lista_de_hechos=cadena_larga.split(".")

for hecho in lista_de_hechos:
    if hecho == "":
        print("vacio")
    else:
        base.assertz(hecho)


def algoritmo():
    resultado=list(base.query("valor(Fil,Num)"))
    while resultado:

        for nuevo_assertz in resultado:
            cadena = "numero("+nuevo_assertz["Fil"]+", "+str(nuevo_assertz["Num"])+")"
            base.assertz(cadena)

        resultado=list(base.query("valor(Fil,Num)"))
    resuelto=list(base.query("sudoku(filCol(F,C),Num)"))
    return resuelto




"""
print(len(resuelto))

for dic in resuelto:
    print(dic["Fil"], "==>", dic["Num"],"\n")"""


def resolverSudoku(datos):
    for tupla in datos:
        if tupla[0]!= "":
            cadena = "numero(filCol("+str(tupla[1])+", "+str(tupla[2])+"),"+str(tupla[0])+")"
            base.assertz(cadena)
    return algoritmo()

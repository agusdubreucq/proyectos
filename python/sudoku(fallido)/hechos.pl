numero(filCol(0,1),3).

numero(filCol(1,1),4).
numero(filCol(1,5),3).

numero(filCol(2,3),4).
numero(filCol(2,4),5).

numero(filCol(3,1),6).
numero(filCol(3,2),4).

numero(filCol(4,0),1).
numero(filCol(4,4),3).

numero(filCol(5,4),2).


/*numero(filCol(Fila, Col),Num):-
    between(1,6,Fila),
    between(1,6,Col),
    between(1,6,Num).*/

cuadrado(filCol(Fila, Col), 1):-
    between(0, 1, Fila),
    between(0,2,Col).
    
cuadrado(filCol(Fila, Col), 2):-
    between(0, 1, Fila),
    between(3,5,Col).
    
cuadrado(filCol(Fila, Col), 3):-
    between(2, 3, Fila),
    between(0,2,Col).
    
cuadrado(filCol(Fila, Col), 4):-
    between(2, 3, Fila),
    between(3,5,Col).

cuadrado(filCol(Fila, Col), 5):-
    between(4, 5, Fila),
    between(0,2,Col).

cuadrado(filCol(Fila, Col), 6):-
    between(4, 5, Fila),
    between(3,5,Col).

porFilaCol(filCol(Fila,Col),Numero):-
    between(0,5,Fila),
    between(0,5,Col),
    between(1,6,Numero),
    not(numero(filCol(Fila,Col),_)),
    not(numero(filCol(Fila,_),Numero)),
    not(numero(filCol(_,Col),Numero)).

porCuadrado(filCol(Fila,Col),Numero):-
    between(0,5,Fila),
    between(0,5,Col),
    between(1,6,Numero),
    cuadrado(filCol(Fila,Col), Cuadrado),
    forall((cuadrado(FilCol,Cuadrado),FilCol\=filCol(Fila,Col)),not(numero(FilCol,Numero))).

generarLista(FilCol,Numero):-
    between(1,6,Numero),
    porCuadrado(FilCol,Numero),
    porFilaCol(FilCol,Numero).

lista(FilCol,Numeros):-
    cuadrado(FilCol,_),
    not(numero(FilCol,_)),
    findall(Numero,generarLista(FilCol,Numero),Numeros).

unicoCuadrado(FilCol,Numero):-
    cuadrado(FilCol,Cuadrado),
    lista(FilCol,Lista),
    member(Numero,Lista),
    forall((cuadrado(FilColDif,Cuadrado),FilColDif\=FilCol),not(listaGeneradaContiene(FilColDif,Numero))).

listaGeneradaContiene(FilCol,Numero):-
    lista(FilCol,Lista),
    member(Numero,Lista).


unicoPosible(FilCol,Numero):-
    lista(FilCol,Lista),
    length(Lista, 1),
    member(Numero,Lista).

valor(FilCol,Numero):-
    numero(FilCol,Numero).
valor(FilCol,Numero):-
    unicoPosible(FilCol,Numero).
valor(FilCol,Numero):-
    unicoCuadrado(FilCol,Numero).

    

    
    
    



    
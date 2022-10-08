from tkinter import *
from sudoku2 import *

root = Tk()
root.title("SUDOKU")
root.geometry("600x400")

titulo = Label(root,text="SUDOKU", fg="#f00")
titulo.grid(row=0,column=0,columnspan=4)

"""f00=f01=f02=f03=f04=f05=\
f10=f11=f12=f13=f14=f15=\
f20=f21=f22=f23=f24=f25=\
f30=f31=f32=f33=f34=f35=\
f40=f41=f42=f43=f44=f45=\
f50=f51=f52=f53=f54=StringVar()"""

f00=StringVar()
f01=StringVar()
f02=StringVar()
f03=StringVar()
f04=StringVar()
f05=StringVar()
f10=StringVar()
f11=StringVar()
f12=StringVar()
f13=StringVar()
f14=StringVar()
f15=StringVar()
f20=StringVar()
f21=StringVar()
f22=StringVar()
f23=StringVar()
f24=StringVar()
f25=StringVar()
f30=StringVar()
f31=StringVar()
f32=StringVar()
f33=StringVar()
f34=StringVar()
f35=StringVar()
f40=StringVar()
f41=StringVar()
f42=StringVar()
f43=StringVar()
f44=StringVar()
f45=StringVar()
f50=StringVar()
f51=StringVar()
f52=StringVar()
f53=StringVar()
f54=StringVar()
f55=StringVar()

lista= [f00,f01,f02,f03,f04,f05,\
f10,f11,f12,f13,f14,f15,\
f20,f21,f22,f23,f24,f25,\
f30,f31,f32,f33,f34,f35,\
f40,f41,f42,f43,f44,f45,\
f50,f51,f52,f53,f54,f55]
#filCol00=Entry(root,textvariable=f00)
#filCol00.grid(row=1,column=0)
fila=1
col=0



print(len(lista))

def cuadrado_gris(fila, col):
    if ((fila == 1 or fila==2 or fila==5 or fila==6) and (col==0 or col==1 or col==2))\
         or ((fila==3 or fila==4) and (col==3 or col==4 or col==5)):
         return True

def resolver():
    datos=[]
    fil=0
    colum=0
    for var in lista:
        datos.append((var.get(),fil,colum))
        colum+=1
        if colum==6:
            colum=0
            fil+=1
    #print(datos)
    resuelto =resolverSudoku(datos)
    print(resuelto)
    for dic in resuelto:
        print(dic["F"],", ",dic["C"] ,"==>", dic["Num"],"\n")
        num_lista= dic["F"]*6 + dic["C"]
        lista[num_lista].set(dic["Num"])



for var in lista:
    if cuadrado_gris(fila, col):
        Entry(root, textvariable=var, width=4, bg="#888").grid(row=fila, column=col)
    else:
        Entry(root, textvariable=var, width=4).grid(row=fila, column=col)
    col+=1
    if col ==6:
        col=0
        fila+=1

Button(root, text="resolver", command=resolver).grid(row=8, column=3, columnspan=4)




root.mainloop()
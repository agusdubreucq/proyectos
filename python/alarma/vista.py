from tkinter import Label, Tk, ttk
from pygame import mixer
from modelo import *

class Panel():
    def __init__(self, ventana):    
        ventana.config(bg="#000")
        ventana.geometry('500x250')
        ventana.title('alarma')
        mixer.init()

        horas = []
        minutos = []
        segundos = []

        for i in range(0,24):
            horas.append(i)

        for i in range(0,60):
            minutos.append(i)

        for i in range(0,60):
            segundos.append(i)


        txt1 = Label(ventana, text="hora", bg="#000", fg="#aaa").grid(row=1, column=0, padx=5, pady=5)
        txt2= Label(ventana, text="minutos", bg="#000", fg="#aaa").grid(row=1, column=1, padx=5, pady=5)
        txt3 = Label(ventana, text="segundos", bg="#000", fg="#aaa").grid(row=1, column=2, padx=5, pady=5)

        combobox1 = ttk.Combobox(ventana, values= horas, justify="center", width="12", font="Arial")
        combobox1.grid(row=2,column=0, padx=15, pady=5)
        combobox1.current(0)

        combobox2 = ttk.Combobox(ventana, values= minutos, justify="center", width="12", font="Arial")
        combobox2.grid(row=2,column=1, padx=15, pady=5)
        combobox2.current(0)

        combobox3 = ttk.Combobox(ventana, values= segundos, justify="center", width="12", font="Arial")
        combobox3.grid(row=2,column=2, padx=15, pady=5)
        combobox3.current(0)


        alarma = Label(ventana,fg="#aaa", bg="#000")
        alarma.grid(row=3, column=0, sticky="nsew", ipadx=5, ipady=20)
        repetir = Label(ventana, fg="#aaa", bg="#000", text="repetir")
        repetir.grid(column=1, row=3, ipadx=5, ipady=20)

        cantidad = ttk.Combobox(ventana, values= (1,2,3), justify="center", width="8", font="Arial")
        cantidad.grid(row=3,column=2, padx=5, pady=5)
        cantidad.current(0)

        color_hs="#aaa"
        txt_hora_actual = Label(ventana, fg=color_hs, bg="#000", font=('Arial', 20))
        txt_hora_actual.grid(columnspan=3, row=0, sticky="nsew", ipadx=5, ipady=20)

        apl = funcion()

        try: 
            apl.obtener_time(combobox1= combobox1,combobox2= combobox2, combobox3= combobox3, txt_hora_actual= txt_hora_actual, alarma= alarma, cantidad= cantidad)
        except:
            print("no se puede")

        


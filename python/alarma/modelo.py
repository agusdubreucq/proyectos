from time import strftime, sleep
from pygame import mixer
from tkinter import messagebox

def obtener_time(combobox1, combobox2, combobox3, txt_hora_actual, alarma, cantidad):

    x_hs = combobox1.get()
    x_min = combobox2.get()
    x_seg = combobox3.get()

    hs = strftime('%H')
    min = strftime('%M')
    seg = strftime('%S')

    hora_actual = (hs + " : "+ min+" : "+seg)
    txt_hora_actual.config(text=hora_actual)

    hora_alarma = x_hs + " : " + x_min + " : " + x_seg
    alarma['text'] = hora_alarma
    
    

    if int(hs)== int(x_hs):
        if int(min)== int(x_min):
            if int(seg)== int(x_seg):
                mixer.music.load("audios/blood_on_the_dance_floor.mp3")
                mixer.music.play(loops = int(cantidad.get()))
                messagebox.showinfo(message=hora_alarma, title="Alarma")
                sleep(1)
    
    txt_hora_actual.after(100, obtener_time)
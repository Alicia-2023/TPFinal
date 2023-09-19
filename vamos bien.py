from guizero import App, PushButton, Text, ListBox, Picture, Box, Window, yesno
import tkinter as tk

#  *** Chequeo si es correcta la elección Nombre = imagen

def color():
    seleccion = PushButton.text
    #PushButton.text = ("Seleccionaste, ", seleccion)
    #PushButton.disable()
    PushButton.resize(self,height=6,width=6)
    print(PushButton.text)
    # me gustaria que el botón cambie de color o que cambie algo 
    # para que se note que está seleccionado
OK = PushButton.text
#print(seleccion)
def correct():
    if PushButton == OK:
        print("deberia funcionar")
        #PushButton.destroy()
        #button.Acierto = print("Correcto")
        #buttons_box.text = "CORRECTO!"
    else:
        print ("no se")
        print(OK)

#    if seleccion == "Parlantes":
#        seleccion = text_1.text
#        print("No sale por true?")
        #text_1.destroy()
#        print(text_1.visible)
#    else:
#        print("Por que sale por false", text_1.text)
        #print(text_1.text)

def correcto():
    if content_box.PushButton == OK:
        button.Acierto = print("Correcto")
        buttons_box.text = "CORRECTO!"
    else:
        return 0

# *** Salida del juego

def salir():
    #app = App(title="Pregunta")
    juego = yesno("Fin del juego", "Realmente deseas salir ? ")
    if juego == True:
        app.destroy()
    else:
        return 0

# *** Armo ventana
app = App(title="Perifericos", height=600, width=600)

Nombre_vent_box = Box(app, width="fill", align="top", border=True)
Text(Nombre_vent_box, text="Perifericos de entrada o de salida?")

buttons_fin = Box(app, width="fill", align="bottom", border=True)
#Text(buttons_fin, text="Click para finalizar el juego")
Fin = PushButton(buttons_fin, width="28",text=" *** :( Click para finalizar el juego ***", command=salir)

Perif_box1 = Box(app, height="fill", align="left", border=True, layout="grid")
app.bg="white"
Text(Perif_box1, text="Lista de Periféricos", grid=[0,1])
#boton=tk.Button(ventana,text="Prueba",bg="red")
text_1 = PushButton(Perif_box1, visible="True", width="18",text="Parlantes", grid=[0,4],command=color)
text_2 = PushButton(Perif_box1, visible="True", width="18", text="Microfono", grid=[0,5])
text_3 = PushButton(Perif_box1, width="18", text="Pendrive", grid=[0,6])
text_4 = PushButton(Perif_box1, width="18", text="Mouse", grid=[0,7])
text_5 = PushButton(Perif_box1, width="18",text="Disco rigido", grid=[0,8])
text_6 = PushButton(Perif_box1, width="18",text="Scanner", grid=[0,9])
text_7 = PushButton(Perif_box1, width="18",text="Pantalla", grid=[0,10])
text_8 = PushButton(Perif_box1, width="18",text="Joystick", grid=[0,11])
text_9 = PushButton(Perif_box1, width="18",text="Teclado", grid=[0,25])


content_box = Box(app, align="top", width="fill", border=True, layout="grid")
Text(content_box, text="Imagenes", width="fill", grid=[1,1])
app.bg="pink"
#text2 = Text(app, text="periferico de Entrada", grid=[5,2])
Parlantes = PushButton(content_box, image="C:/ImagenesTP/altavoces.jpg", width=100, height=100, grid=[4,4], command=correct),
Microfono = PushButton(content_box, image="C:/ImagenesTP/microfono.jpg", width=100, height=100, grid=[2,2], command=correct)
Pendrive = PushButton(content_box, image="C:/ImagenesTP/pendrive.jpg",width=100, height=100, grid=[2,3], command=correct)
Mouse = PushButton(content_box, image="C:/ImagenesTP/mouse.jpg", width=100, height=100, grid=[2,4],command=correcto)
disco = PushButton(content_box, image="C:/ImagenesTP/disco-rigido.jpg", width=100, height=100, grid=[3,3],command=correcto)
Scanner = PushButton(content_box, image="C:/ImagenesTP/scanner.jpg", width=100, height=100, grid=[3,2],command=correct)
Monitor = PushButton(content_box, image="C:/ImagenesTP/monitor.jpg", width=100, height=100, grid=[3,4], command=correct)
Joystick = PushButton(content_box, image="C:/ImagenesTP/joystick.jpg", width=100, height=100, grid=[4,2],command=correct)
Teclado = PushButton(content_box, image="C:/ImagenesTP/teclado.jpg", width=100, height=100, grid=[4,3],command=correct)
Indicaciones_vent_box = Box(app, width="fill",align="bottom", border=True)
Text(Indicaciones_vent_box, text="Perifericos de entrada o de salida?\nSelecionar de la lista de periféricos \nuna opción y luego buscá la imagen \ncorrespondiente al mismo. ", width="fill", grid=[3,6])

app.display()

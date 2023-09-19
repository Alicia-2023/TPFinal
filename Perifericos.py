from guizero import App, PushButton, Text, ListBox, Picture, Box, Window, Tk, yesno, info

#  *** Chequeo si es correcta la elección Nombre = imagen

def correcto():
    if PushButton.text == text_1.text:
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
Fin = PushButton(buttons_fin, width="18",text=" *** :( Click para finalizar el juego ***", command=salir)

Perif_box1 = Box(app, height="fill", align="left", border=True, layout="grid")
app.bg="white"
Text(Perif_box1, text="Lista de Periféricos", grid=[0,1])
text_1 = PushButton(Perif_box1, width="18",text="Parlantes", grid=[0,4])
text_2 = PushButton(Perif_box1, width="18", text="Microfono", grid=[0,5])
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
Parlantes = PushButton(content_box, image="C:/ImagenesTP/altavoces.jpg", width=100, height=100, grid=[4,4])
Microfono = PushButton(content_box, image="C:/ImagenesTP/microfono.jpg", width=100, height=100, grid=[2,2])
Pendrive = PushButton(content_box, image="C:/ImagenesTP/pendrive.jpg",width=100, height=100, grid=[2,3])
Mouse = PushButton(content_box, image="C:/ImagenesTP/mouse.jpg", width=100, height=100, grid=[2,4])
disco = PushButton(content_box, image="C:/ImagenesTP/disco-rigido.jpg", width=100, height=100, grid=[3,3])
Scanner = PushButton(content_box, image="C:/ImagenesTP/scanner.jpg", width=100, height=100, grid=[3,2])
Monitor = PushButton(content_box, image="C:/ImagenesTP/monitor.jpg", width=100, height=100, grid=[3,4])
Joystick = PushButton(content_box, image="C:/ImagenesTP/joystick.jpg", width=100, height=100, grid=[4,2])
Teclado = PushButton(content_box, image="C:/ImagenesTP/teclado.jpg", width=100, height=100, grid=[4,3])
#indicaciones = Text(content_box, text="\nSelecionar de la lista de periféricos \nuna opción y luego buscá su imagen \ncorrespondiente ", width="fill", grid=[3,6])
Indicaciones_vent_box = Box(app, width="fill", align="bottom", border=True)
Text(Indicaciones_vent_box, text="Perifericos de entrada o de salida?\nSelecionar de la lista de periféricos \nuna opción y luego buscá su imagen \ncorrespondiente ", width="fill", grid=[3,6])
app.display()

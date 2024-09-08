from tkinter import *
from funcion_definitiva import cajas
from tkinter import filedialog
from tkinter import messagebox

def ejecutar_cajas():
    try:
        a = int(a_tk.get())
        b = int(b_tk.get())
        c = int(c_tk.get())
        peso_estuche = float(peso_estuche_tk.get())
        Lmax = int(Lmax_tk.get())
        Wmax = int(Wmax_tk.get())
        max_altura = int(max_altura_tk.get())
        min_estuches = int(min_estuches_tk.get())
        max_estuches = int(max_estuches_tk.get())
        r = int(r_tk.get())

        combinaciones_posibles, mejores_combinaciones = cajas(a, b, c, peso_estuche, Lmax, Wmax, max_altura=max_altura, min_estuches=min_estuches, max_estuches=max_estuches, r=r)
        # Las listas se muestran en un desplegable
        # Lista1: combinaciones posibles 
        resultado_todas_combinaciones.delete(0, END)  # Primero borramos cualquier cosa que hubiera antes
        for i,combinacion in enumerate(combinaciones_posibles):
            iteracion = "L:{}, W:{}, H:{}, Volumen Total:{}, Volumen Ocupado:{}, Volumen Vacio:{}, Estuches: {}, Peso Total:{}kg, Volumen pale vacio: {}, Orientaciones:{}, Cajas por Palé:{}\n".format(
                combinacion[0], combinacion[1], combinacion[2], combinacion[3], combinacion[4], combinacion[5], 
                combinacion[6], combinacion[7], combinacion[8], combinacion[9], combinacion[10])
            
            resultado_todas_combinaciones.insert(END, iteracion)

        # Lista2: ranking
        resultado_ranking.delete(0, END)
        for i, combinacion in enumerate(mejores_combinaciones):
            iteracion = "L:{}, W:{}, H:{}, Volumen Total:{}, Volumen Ocupado:{}, Volumen Vacio:{}, Estuches: {}, Peso Total:{}kg, Volumen pale vacio: {}, Orientaciones:{}, Cajas por Palé:{}\n".format(
                combinacion[0], combinacion[1], combinacion[2], combinacion[3], combinacion[4], combinacion[5], 
                combinacion[6], combinacion[7], combinacion[8], combinacion[9], combinacion[10])
            
            resultado_ranking.insert(END, iteracion)

    # Capturamos el error de introducir datos no válidos
    except:
        resultado_todas_combinaciones.delete(0, END)
        resultado_ranking.delete(0, END)
        resultado_todas_combinaciones.insert(END, "Error: Por favor, introduce valores numéricos válidos.")
        resultado_ranking.insert(END, "Error: Por favor, introduce valores numéricos válidos.")

def guardar_todas_combinaciones():
    #abrimos el diálogo para guardar el archivo
    fichero_todas_combinaciones = filedialog.asksaveasfile(title="Guardar todas combinaciones como", mode="w", defaultextension=".txt" )
    if fichero_todas_combinaciones:
        for combinacion in range(resultado_todas_combinaciones.size()):
            mensaje = resultado_todas_combinaciones.get(combinacion)
            fichero_todas_combinaciones.write(mensaje+ "\n")
        
        fichero_todas_combinaciones.close()

def guardar_ranking():
    fichero_ranking = filedialog.asksaveasfile(title="Guardar ranking como", mode="w", defaultextension=".txt")
    if fichero_ranking:
        for i in range(resultado_ranking.size()):
            mensaje = resultado_ranking.get(i)
            fichero_ranking.write(mensaje+"\n")
    
        fichero_ranking.close()
    
            
def info():
    messagebox.showinfo("Acerca del programa", "Este programa busca optimizar el máximo número de cajas pequeñas de dimensiones axbxc que caben en el menor volumen posible de una caja grande LxWxH.\nTambién se tiene en cuenta que las cajas grandes pueden ir en una caja aún más grande (un palé normalmente) de dimensiones Lmax, Hmax, Wmax, por lo que se calcula el número de cajas grandes que optimizan el volumen vacío de dicho palé.\n Este programa también calcula el peso total de cada caja grande (en kg) partiendo del peso de cada caja pequeña (estuche) ")

def info_parametros(): 
    messagebox.showinfo("Acerca de los parámetros", "Debe definir las dimensiones de la caja pequeña (a,b,c), su peso (en Kg), las dimensiones máximas de la caja grande, el número mínimo y máximo de cajas pequeñas/caja grande y el número de combinaciones óptimas del ranking ")

def info_ranking():
    messagebox.showinfo("¿Qué es el ranking?", "Dependiendo de los parametros que se establezcan, puede haber un número demasiado grande de combinaciones y no se pueden analizar todas.\nPor ello, se puede definir el número de combinaciones que se quieren mostrar (r) siendo estas las r mejores combinaciones, las que maximizan el número de cajas pequeñas que caben por caja grande, minimizando el volumen vacío de la caja grande y minimizando el volumen vacío del palé donde se colocan las cajas grandes") 

def info_parametros_pordefecto():
    messagebox.showinfo("Parámetros por defecto", "Por defecto, se establece que el peso máximo de cada caja grande sea 25kg (contactar con el programador para cambiar dicho parémetro).\nEn el ranking, se seleccionan las mejores combinaciones según el siguiente criterio de prioridad:\n1) Mayor número de cajas pequeñas por caja grande.\n2) Menor volumen vacío por caja grande.\n3) Menor volumen vacío por palé (o caja más grande donde caben las cajas grandes.)")

def salir():
    resultado = messagebox.askquestion("Salir", "¿Estás seguro que quieres salir ahora?\nLos ficheros no guardados se perderán.")
    if resultado == "yes":
        root.destroy()

root = Tk()  # Inicio de la interfaz

root.title("Optimización de cajas dentro de cajas")  
root.resizable(False, False)  # Configura el tamaño de la ventana principal

#Main menu. El menú tiene priroidad, se declara justo debajo de la raíz
menubar = Menu(root)
root.config(menu=menubar) #el menú no se empaqueta, se añade manualmente a la raíz con este comando 

#Dentro del Main Menu, definimos el menú archivo y el menú ayuda

#Menu archivo (para guardar los ficheros y para salir del programa)
filemenu = Menu(menubar) 
#Primero definimos las funciones del menu archivo
filemenu.add_command(label="Guardar todas las combinaciones", command=guardar_todas_combinaciones)
filemenu.add_command(label="Guardar ranking", command=guardar_ranking)
filemenu.add_command(label="Salir", command=salir) #función root.quit por defecto sale de la interfaz 
#Luego incorporamos el menu archivo a la barra de menu 
menubar.add_cascade(label="Archivo", menu=filemenu)

#Menú ayuda. Para dar info sobre el programa
helpmenu = Menu(menubar) 
helpmenu.add_command(label="Acerca del programa", command=info)
helpmenu.add_command(label="Parámetros del programa", command=info_parametros)
helpmenu.add_command(label="¿Qué es el ranking?", command=info_ranking)
helpmenu.add_command(label="Parametros por defecto", command=info_parametros_pordefecto)
menubar.add_cascade(label="Ayuda", menu=helpmenu)



# Frame que contiene un subtítulo
frame1 = Frame(root)
frame1.pack(padx=5, pady=5, fill=BOTH, expand=True)
label1 = Label(frame1, text="Características de la caja pequeña")
label1.pack(padx=5, pady=10)

# Frame donde definimos todas las etiquetas con los argumentos que recibe la función cajas()
frame2 = Frame(root)
frame2.pack(padx=5, pady=5, fill=BOTH, expand=True)

# Campos obligatorios
labela = Label(frame2, text="Largo de la caja pequeña en mm (a)")
labela.grid(row=0, column=0, padx=5, pady=2, sticky=W)
a_tk = Entry(frame2)
a_tk.grid(row=0, column=1, padx=5, pady=2)

labelb = Label(frame2, text="Ancho de la caja pequeña en mm (b)")
labelb.grid(row=1, column=0, padx=5, pady=2, sticky=W)
b_tk = Entry(frame2)
b_tk.grid(row=1, column=1, padx=5, pady=2)

labelc = Label(frame2, text="Altura de la caja pequeña en mm (c)")
labelc.grid(row=2, column=0, padx=5, pady=2, sticky=W)
c_tk = Entry(frame2)
c_tk.grid(row=2, column=1, padx=5, pady=2)

labelpeso = Label(frame2, text="Peso (en kg) de cada caja pequeña")
labelpeso.grid(row=3, column=0, padx=5, pady=2, sticky=W)
peso_estuche_tk = Entry(frame2)
peso_estuche_tk.grid(row=3, column=1, padx=5, pady=2)

# Campos no obligatorios
labelLmax = Label(frame2, text="Largo máximo caja grande en mm (Lmax)")
labelLmax.grid(row=4, column=0, padx=5, pady=2, sticky=W)
Lmax_tk = Entry(frame2)
Lmax_tk.grid(row=4, column=1, padx=5, pady=2)

labelWmax = Label(frame2, text="Ancho máximo caja grande en mm (Wmax)")
labelWmax.grid(row=5, column=0, padx=5, pady=2, sticky=W)
Wmax_tk = Entry(frame2)
Wmax_tk.grid(row=5, column=1, padx=5, pady=2)

labelHmax = Label(frame2, text="Altura máxima caja grande en mm (Hmax)")
labelHmax.grid(row=6, column=0, padx=5, pady=2, sticky=W)
max_altura_tk = Entry(frame2)
max_altura_tk.grid(row=6, column=1, padx=5, pady=2)

labelmin = Label(frame2, text="Mínimo número cajas pequeñas / caja grande")
labelmin.grid(row=7, column=0, padx=5, pady=2, sticky=W)
min_estuches_tk = Entry(frame2)
min_estuches_tk.grid(row=7, column=1, padx=5, pady=2)

labelmax = Label(frame2, text="Máximo número cajas pequeñas / caja grande")
labelmax.grid(row=8, column=0, padx=5, pady=2, sticky=W)
max_estuches_tk = Entry(frame2)
max_estuches_tk.grid(row=8, column=1, padx=5, pady=2)

labelranking = Label(frame2, text="Número combinaciones en el ranking (r)")
labelranking.grid(row=9, column=0, padx=5, pady=2, sticky=W)
r_tk = Entry(frame2)
r_tk.grid(row=9, column=1, padx=5, pady=2)


#añaidmos una imagen
imagen = PhotoImage(file="cajicas.PNG")
Label(frame2, image=imagen).grid(row=0, column=2, rowspan=10, padx=10, pady=5, sticky=N+S) #ponemos la imagen en una label dentro del frame2



# Frame con el botón de calcular
frame3 = Frame(root)
frame3.pack(padx=5, pady=10, fill=BOTH, expand=True)

calcular = Button(frame3, text="calcular", command=ejecutar_cajas)
calcular.pack(pady=5)

# Frame con los resultados
frame4 = Frame(root)
frame4.pack(padx=5, pady=5, fill=BOTH, expand=True)

# Mostramos el resultado del cálculo en un desplegable
label_resultado_todas_combinaciones = Label(frame4, text="Todas las combinaciones posibles: ")
label_resultado_todas_combinaciones.grid(row=0, column=0, pady=5, padx=5, sticky=W)

resultado_todas_combinaciones = Listbox(frame4, width=60, height=8)
resultado_todas_combinaciones.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)

# Añadimos un scrollbar en vertical y horizontal
scrollbar_combinaciones_y = Scrollbar(frame4, orient=VERTICAL, command=resultado_todas_combinaciones.yview)
scrollbar_combinaciones_y.grid(row=1, column=1, sticky=N+S)  # Asegúrate de que esté en la misma fila que el Listbox
resultado_todas_combinaciones.config(yscrollcommand=scrollbar_combinaciones_y.set)

scrollbar_combinaciones_x = Scrollbar(frame4, orient=HORIZONTAL, command=resultado_todas_combinaciones.xview)
scrollbar_combinaciones_x.grid(row=2, column=0, sticky=E+W)  # Asegúrate de que esté en la misma columna que el Listbox
resultado_todas_combinaciones.config(xscrollcommand=scrollbar_combinaciones_x.set)

# Label y Listbox para el ranking
label_resultado_ranking = Label(frame4, text="Ranking solo las r mejores: ")
label_resultado_ranking.grid(row=0, column=2, pady=5, padx=5, sticky=W)  # Ajustar la columna a 2

resultado_ranking = Listbox(frame4, width=60, height=8)
resultado_ranking.grid(row=1, column=2, padx=5, pady=5, sticky=N+S+E+W)  # Ajustar la columna a 2

# Añadimos un scrollbar vertical y horizontal
scrollbar_ranking_y = Scrollbar(frame4, orient=VERTICAL, command=resultado_ranking.yview)
scrollbar_ranking_y.grid(row=1, column=3, sticky=N+S)  # Ajustar la columna a 3
resultado_ranking.config(yscrollcommand=scrollbar_ranking_y.set)

scroll_bar_ranking_x = Scrollbar(frame4, orient=HORIZONTAL, command=resultado_ranking.xview)
scroll_bar_ranking_x.grid(row=2, column=2, sticky=E+W)  # Ajustar la columna a 2
resultado_ranking.config(xscrollcommand=scroll_bar_ranking_x.set)

# Para asegurar que las filas y las columnas se expandan bien dentro del frame
# Configuración para expansión
frame4.columnconfigure(0, weight=1)
frame4.columnconfigure(1, weight=0)  # La columna del scrollbar vertical no necesita peso
frame4.columnconfigure(2, weight=1)  # La columna del Listbox de ranking necesita peso
frame4.columnconfigure(3, weight=0)  # La columna del scrollbar vertical del ranking no necesita peso
frame4.rowconfigure(0, weight=0)  # La fila de los labels no necesita peso
frame4.rowconfigure(1, weight=1)  # La fila de los Listbox debe expandirse
frame4.rowconfigure(2, weight=0)  # La fila del scrollbar horizontal no necesita peso



root.mainloop()  # Fin de la interfaz

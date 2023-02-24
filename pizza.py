import tkinter as tk    

ventana = tk.Tk()
ventana.geometry("500x600")
ventana.title("Pizzeria")
ventana.minsize(width=600,height=500)
ventana.config(bg="wheat")

etiqueta_titulo = tk.Label(ventana,
                    text="Pedidor de Piza",
                    font=("bold"),
                    background="orange",
                    foreground="blue",
                    relief=tk.FLAT,
                    border=30,
                    padx=50,pady=50,
                    borderwidth=25
                    )               
etiqueta_titulo.pack()

### Opciones de Pizza ###
cuadro1 = tk.LabelFrame(ventana,
                             text="Variedades",
                             bg="wheat",
                             #relief=tk.FLAT,bd=2,
                             #padx=50,pady=50,borderwidth=25
                             )

cuadro1.pack()
######################### VARIEDAD ###########
opcion1_seleccionada = tk.IntVar()
#help(opcion1_seleccionada)
opcion1= tk.Radiobutton(cuadro1,
                        text="Anchoas",
                        font="arial 12",
                        bg="wheat",
                        variable=opcion1_seleccionada,
                        anchor=tk.W,width=20,
                        value=1)
opcion1.pack()

opcion2= tk.Radiobutton(cuadro1,
                        text="huevo y jamon",
                        font="arial 12",
                        bg="wheat",
                        anchor=tk.W,width=20,
                        variable=opcion1_seleccionada,
                        value=2)
opcion2.pack()

opcion3= tk.Radiobutton(cuadro1,
                        text="Musarela",
                        font="arial 12",
                        bg="wheat",
                        anchor=tk.W,width=20,
                        variable=opcion1_seleccionada,
                        value=3)
opcion3.pack()

opcion4= tk.Radiobutton(cuadro1,
                        text="Roquefort",
                        font="arial 12",
                        bg="wheat",
                        anchor=tk.W,width=20,
                        variable=opcion1_seleccionada,
                        value=4)
opcion4.pack()

### FUNNCIONES ################################
     
def pedir():
    pizza_elegida = opcion1_seleccionada.get()
    if pizza_elegida ==1:
        resultado = "Anchoas"
    elif pizza_elegida == 2:
        resultado = "huevo y jamon"
    elif pizza_elegida == 3:
        resultado = "Musarela"
    elif pizza_elegida == 4:
        resultado ="Roquefort" 
    mostrar.config(text=f"La pizza elegida es {resultado}")
    boton_pedir.config(state="disabled")
    
    #mostrar.config(text=opcion1_seleccionada.get())
    
def borrar():
    boton_pedir.config(state="normal")
    opcion1_seleccionada.set(0)
    mostrar.config(text="Elija su Pizza, pulse Pedir")    

cuadro3= tk.Frame(ventana,
                  bg="wheat")

boton_borrar = tk.Button(cuadro3,
                         text="Borrar",
                         bg="Red",
                         #font="consolas 18 bold",
                         width=15,height=2,
                         command=borrar)
boton_borrar.pack(side="left",padx=50,pady=50)

boton_pedir = tk.Button(cuadro3,
                            text="Pedir",
                            bg="orange",
                            width=15,height=2,
                            command=pedir,
                            state="normal")
boton_pedir.pack(side="left",padx=50,pady=50)

cuadro3.pack()

mostrar = tk.Label(ventana,
                    text="Elija su Pizza, pulse Pedir",
                    font=("bold"),
                    background="orange",
                    foreground="blue",
                    relief=tk.FLAT,
                    border=30,
                    padx=50,pady=50,
                    borderwidth=25
                    )               
mostrar.pack()














ventana.mainloop()
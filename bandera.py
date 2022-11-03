from tkinter import *
# ---------------------------
# ventana principal
# se crea una pantalla llamada venta principal que adquiere las caracteristicas de un objeto tk
ventana_principal = Tk()

#titulo de la venta
ventana_principal.title("Sistemas UIS")

#tamaño de la ventana
ventana_principal.geometry("1000x500")

#deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

#color del fondo
ventana_principal.config(bg="white")

#----------------------------------
# frame entrada de datos
#----------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="maroon", width=200, height=200)
frame_entrada.place(x=0, y=300)

#----------------------------------
frame_operacion = Frame(ventana_principal)
frame_operacion.config(bg="maroon", width=200, height=200)
frame_operacion.place(x=0, y=0)

#----------------------------------
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="maroon", width=700, height=200)
frame_resultado.place(x=300, y=300)

#--------------------------------------------------------
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="maroon", width=700, height=200)
frame_resultado.place(x=300, y=0)
#--------------------------------------------------------
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="blue4", width=50, height=500)
frame_resultado.place(x=225, y=0)

#----------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="blue4", width=1000, height=50)
frame_entrada.place(x=0, y=225)

#etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "UIS socorro")




# Se ejecuta el metodo mainloop() de la clase Tk a traves de instancia ventana_principal. este expliega funciones y queda a espera a la que el usuario haga cada opcion de el usuario se considera como una evento el bucle mainloop() es un metodo infinito
ventana_principal.mainloop()
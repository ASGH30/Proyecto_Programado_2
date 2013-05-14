#Lenguajes de Programacion
#Segunda Progra

import sys #Finaliza el proceso del programa
from pyswip import *  #Importa librerias necesarias para el uso de prolog
from pyswip import Functor, Variable, Query, call, Prolog
import tkSimpleDialog
from Tkinter import * #Importa librería gráfica Tkinter
import tkMessageBox #Importa el módulo para los mensajes de alerta.
import os #Importar la clase os, para cerrar ventanas desde procesos.
from string import * #Importa el módulo de manejo de Strings

#Se inicia Prolog
P = Prolog()

#Agrega Mocosos
def agregar_nino(nombre,edad,pais,bacc,macc,wishl):
    #agrega a Prolog
    agregar ="nino("+nombre+","+edad+","+pais+","+bacc+","+macc+","+wishl+")"
    #Agrega niño
    P.assertz(agregar)#Inserta Informacion a la Base

#Mostrar niño en consola
def desplegar_nino():
    print "Nino:\n"
    # Busca en la Base de Datos
    for soln in P.query("nino(nombre,edad,pais,bacc,macc,wishl)"):
        print "Nombre: ",soln["nombre"]
        print "Edad: ", soln["edad"]
        print "Pais: ", soln["pais"]
        print "Buenas Acciones: ", soln["bacc"]
        print "Malas Acciones: ", soln["macc"]
        print "Lista de Deseos: ", soln["wishl"]

#Consultas a la Base de Datos
def Consultarnino(nombre,edad,pais,bacc,macc,wishl):
    cons ="nino("+nombre+","+edad+","+pais+","+bacc+","+macc+","+wishl+")"

    #Enlista la consulta
    sol = list(P.query(cons))
    
    #Solucion de la Consulta
    for temp in solucion:
        if(nombre != "Nombre"):
            temp["Nombre"]=nombre
        if(edad != "Edad"):
            temp["Edad"]=edad
        if(pais != "Pais"):
            temp["Pais"]= pais
        if(bacc != "Buenas Acciones"):
            temp["Buenas Acciones"]=bacc
        if(macc != "Malas Acciones"):
            temp["Malas Acciones"]=macc
        if(wishl != "Lista"):
            temp["Lista"]=wishl
    return sol

#Funcion para salir y cerrar la apliacion
def salir():
    os._exit(100)

#Funcion para abrir el manual de usuario
def info():
    tkMessageBox.showinfo("Acerca de...", 'Es un sistema de ayuda para Santa durante la navidad, el cual le agiliza el proceso de regalos.')

#Ingresa niño
def Ingresarnino():

    #Toma los datos que ingresa el usuario
    Txt_nombre = lower(entry_mant_1.get())
    Txt_edad = lower(entry_mant_2.get())
    Txt_pais = lower(entry_mant_3.get())
    Txt_bacc = lower(entry_mant_4.get())
    Txt_macc = lower(entry_mant_5.get())
    Txt_wisl = lower(entry_mant_6.get())

    #Verificacion de datos
    if(Txt_nombre == "" or Txt_edad == "" or Txt_pais == "" or
       Txt_bacc == "" or Txt_macc == "" or Txt_wisl == ""):
        info_error=("Es necesario ingresar todos los datos.")
        tkMessageBox.showerror(title="error", message=info_error)
        return False
    
    #DAtos alphanumericos
    if(not(Txt_nombre.isalnum() and Txt_edad.isalnum() and Txt_pais.isalnum()
           and Txt_bacc.isalnum() and Txt_macc.isalnum() and
           Txt_wishl.isalnum())):
        info_error=("Es necesario que los datos sean alfanuméricos")
        tkMessageBox.showerror(title="error", message=info_error)
        return False

    #Verifica nombres repetidos
    elif(Consultarnino(Txt_nombre,"edad","pais","bacc","macc"
                            ,"wishl") !=[]):
        info_error=("Ese nombre ya existe")
        tkMessageBox.showerror(title="error", message=info_error)
        return False

    #Agrega al niño
    else:
        agregar_nino(Txt_nombre,Txt_edad,Txt_pais,Txt_bacc,
                       Txt_macc,Txt_wisl)
        informacion = "El niño fue agregado!"
        tkMessageBox.showinfo(title="Exito!!!!",message=informacion)
        clear_entrys()
        return True


#Consulta niño
def consultar_nino():
    Txt_nombre = lower(entry_mant_1.get())
    Txt_edad = lower(entry_mant_2.get())
    Txt_pais = lower(entry_mant_3.get())
    Txt_bacc= lower(entry_mant_4.get())
    Txt_macc = lower(entry_mant_5.get())
    Txt_wishl = lower(entry_mant_6.get())

    #Los datos deben ser alphanumericos
    if(not((Txt_nombre.isalnum()or Txt_nombre == "") and
           (Txt_edad.isalnum()or Txt_edad == "") and
           (Txt_pais.isalnum()or Txt_pais == "") and
           (Txt_bacc.isalnum()or Txt_bacc == "") and
           (Txt_macc.isalnum()or Txt_macc == "") and
           (Txt_wisl.isalnum()or Txt_wisl == ""))):
        info_error=("Los datos ingresados no cumplen")
        tkMessageBox.showerror(title="error", message=info_error)
        return False

    #Realiza la consultas
    else:
        if(Txt_nombre == ""):
            Txt_nombre = "nombre"
        if(Txt_edad == ""):
            Txt_edad = "edad"
        if(Txt_pais == ""):
            Txt_pais = "pais"
        if(Txt_bacc == ""):
            Txt_bacc = "bacc"
        if(Txt_macc == ""):
            Txt_macc = "macc"
        if(Txt_wishl == ""):
            Txt_wishl = "wishl"

        #Diccionarios
        resp =Consultarnino(Txt_nombre,Txt_edad,Txt_pais,
                                      Txt_bacc,Txt_macc,Txt_wishl)

        resp_text = ""
        #Respuestas
        if (resp == []):
            resp_text= "No se encuentran niños con esos datos."
        else:
            cont = 1
            for cons in resp:
                resp_text =(resp_text +
                           "\nResultado Posicion: " + str(cont) +
                           "\nNombre: "+ str(cons["nombre"]) +
                           "\nEdad: "+ str(cons["edad"]) +
                           "\nPais: "+ str(cons["pais"]) +
                           "\nBuenas Acciones: "+ str(cons["bacc"]) +
                           "\nMalas Acciones: "+ str(cons["macc"]) +
                           "\nLista de deseos: "+ str(cons["wishl"]) + "\n")
                cont = cont +1
            res_text =(res_text)

        colocar_respuesta(res_text)
        return True
        
def limpieza_entrys():
    #Limpieza
    entry_mant_1.delete(0,END)
    entry_mant_2.delete(0,END)
    entry_mant_3.delete(0,END)
    entry_mant_4.delete(0,END)
    entry_mant_5.delete(0,END)
    entry_mant_6.delete(0,END)
    return

def limpieza_general():
    #Quita Ventanas
    limpieza_entrys()
    label_mant_0.grid_remove()
    label_mant_1.grid_remove()
    entry_mant_1.grid_remove()
    label_mant_2.grid_remove()
    entry_mant_2.grid_remove()
    label_mant_3.grid_remove()
    entry_mant_3.grid_remove()
    label_mant_4.grid_remove()
    entry_mant_4.grid_remove()
    label_mant_5.grid_remove()
    entry_mant_5.grid_remove()
    label_mant_6.grid_remove()
    entry_mant_6.grid_remove()
    label_res_0.pack_forget()
    boton_ingresar.grid_remove()
    boton_consultar.grid_remove()
    frame_respuesta.pack_forget()
    return

def colocar_mantenimiento():
    limpieza_general()
    label_mant_0.grid(row=0, sticky=W, columnspan=2)
    label_mant_1.grid(row=1, sticky=E)
    entry_mant_1.grid(row=1,column=1, sticky=W)
    label_mant_2.grid(row=2, sticky=E)
    entry_mant_2.grid(row=2,column=1, sticky=W)
    label_mant_3.grid(row=3, sticky=E)
    entry_mant_3.grid(row=3, column=1, sticky=W)
    label_mant_4.grid(row=4, sticky=E)
    entry_mant_4.grid(row=4, column=1, sticky=W)
    label_mant_5.grid(row=5, sticky=E)
    entry_mant_5.grid(row=5, column=1, sticky=W)
    label_mant_6.grid(row=6, sticky=E)
    entry_mant_6.grid(row=6, column=1, sticky=W)
    boton_ingresar.grid(row=1, column=2, sticky=E, rowspan=8, columnspan=8)
    return

def colocar_consultar():
    limpieza_general()
    label_mant_0.grid(row=0, sticky=W, columnspan=2)
    label_mant_1.grid(row=1, sticky=E)
    entry_mant_1.grid(row=1,column=1, sticky=W)
    label_mant_2.grid(row=2, sticky=E)
    entry_mant_2.grid(row=2,column=1, sticky=W)
    label_mant_3.grid(row=3, sticky=E)
    entry_mant_3.grid(row=3, column=1, sticky=W)
    label_mant_4.grid(row=4, sticky=E)
    entry_mant_4.grid(row=4, column=1, sticky=W)
    label_mant_5.grid(row=5, sticky=E)
    entry_mant_5.grid(row=5, column=1, sticky=W)
    label_mant_6.grid(row=6, sticky=E)
    entry_mant_6.grid(row=6, column=1, sticky=W)
    boton_consultar.grid(row=1, column=2, sticky=E, rowspan=8, columnspan=8)
    return

def colocar_respuesta(respuesta_text):
    limpieza_general()
    label_res_0.pack()
    texto_respuesta.delete(1.0, END)
    frame_respuesta.pack()
    texto_respuesta.insert(END, respuesta_text)

#Crea ventana principal

raiz = Tk()

raiz.title("Bienvenue au restaurant Le Puolet")

#Configuraciones

raiz.columnconfigure(1,weight=2)

raiz.rowconfigure(2,weight=2)

#barra de menu

barra_menu = Menu(raiz)

raiz.config(menu=barra_menu)

#botones del menu

barra_menu.add_command(label="Inicio", command =limpieza_general)

barra_menu.add_command(label="Mantenimiento", command =colocar_mantenimiento)

barra_menu.add_command(label="Consuta", command =colocar_consultar)

barra_menu.add_command(label="Salir", command=salir)

#Imagen
fondo = PhotoImage(file="santafondo.gif")
principal = Label(raiz, image=fondo)
principal.image_zoo = fondo
w = fondo.width()
h = fondo.height()
raiz.geometry("%dx%d+0+0" % (w, h))
principal.pack(side='top', fill='both', expand='yes')

#Consultas
label_mant_0 = Label(principal, text="Nino",
                     font=("", 15),bg ="white", relief=RIDGE, bd=5)
label_mant_1 = Label(principal, text="Nombre",font=("", 10))
entry_mant_1 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_2 = Label(principal, text="Ingredientes",font=("", 10))
entry_mant_2 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_3 = Label(principal, text="Pasos",font=("", 10))
entry_mant_3 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_4 = Label(principal, text="Autor",font=("", 10))
entry_mant_4 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_5 = Label(principal, text="Pais",font=("", 10))
entry_mant_5 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_6 = Label(principal, text="Temperatura",font=("", 10))
entry_mant_6 = Entry(principal,takefocus="",bg="White",width=10)
boton_ingresar = Button(principal,takefocus="", text="Registra Nino",
                        command=IngresarReceta)
boton_consultar = Button(principal,takefocus="",
                         text="Realizar Consulta!!!",
                         command=consultar_animal)
label_res_0 = Label(principal, text="Resultado de la Consulta",
                     font=("", 15),bg ="white", relief=RIDGE, bd=5)

#frame consultas
frame_respuesta=Frame(principal)
texto_respuesta=Text(frame_respuesta,height=15,width=50,background='white')
scroll_respuesta=Scrollbar(frame_respuesta)
texto_respuesta.configure(yscrollcommand=scroll_respuesta.set)
texto_respuesta.pack(side=LEFT)
scroll_respuesta.pack(side=RIGHT,fill=Y)

mainloop()

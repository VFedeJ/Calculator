from tkinter import *
from tkinter import messagebox

raiz=Tk()
raiz.geometry("135x200")
raiz.title("Calculadora")
raiz.iconbitmap("calculadora.ico")
frame=Frame(raiz)
frame.pack(fill="both", expand="True")

##-------Variables----

Punto=False
Variable=0
VariableGeneral=0
Verificacion=0
Resultado=0
CerradaOperacion=0
VariableQuitar=StringVar()
modoOscuro=IntVar()
Dato=StringVar()


##----------Pantalla-------------------

Calculadora=Label(frame, text="Calculadora")
Calculadora.grid(row=0,column=1,columnspan=2)


Pantalla=Entry(frame,textvariable=Dato)
Pantalla.grid(row=1,column=0,padx=0,pady=0,columnspan=4)

##--------Muestra Pantalla-----

def Salir():
	valor=messagebox.askokcancel("Salir", "Desea Salir?")	
	if valor==True:
		raiz.destroy()


def muestreo(NumeroBoton):
	global Esst
	global VariableGeneral
	global CerradaOperacion
	global Punto
	if CerradaOperacion==0:
		if NumeroBoton==".":
			for i in Dato.get():
				if i==".":
					Punto=True
					break
			if Punto==False:
				Dato.set(Dato.get()+NumeroBoton)
				
		else:
			if Dato.get()=="0":										#Parametro NumeroBoton para que se le pueda concatenar el numero que ya teniamos en patalla al numero pulsado
				Dato.set(NumeroBoton)
			else:
				Dato.set(Dato.get()+NumeroBoton)
		Punto=False		
	else:
		Dato.set(NumeroBoton)
		CerradaOperacion=0			

	VariableGeneral=float(Dato.get())													#Le asignamos a "Dato"(Variable a mostrar en la pantalla) primero el el dato que tenia (get) + lo concatenado por el boton pulsado	

##--------Funciones Matematicas---


def resta():
	global Verificacion
	global Variable
	Variable=VariableGeneral
	Dato.set("")
	Verificacion=1

	

def multiplicacion():	
	global Variable
	global Verificacion
	Variable=VariableGeneral
	Dato.set("")
	Verificacion=2
	

def multiplicacion():	
	global Variable
	global Verificacion
	Variable=VariableGeneral
	Dato.set("")
	Verificacion=2

def division():
	global Variable
	global Verificacion
	Variable=VariableGeneral
	Dato.set("")
	Verificacion=3

def suma():
	global Variable
	global Verificacion
	Variable=VariableGeneral
	Dato.set("")
	Verificacion=4	


def igual():
	global Verificacion
	global Resultado
	global Variable
	global CerradaOperacion
	global VariableGeneral

	if Verificacion==1:
		Resultado=Variable-VariableGeneral
		Dato.set(Resultado)
	elif Verificacion==2:	
		Resultado=Variable*VariableGeneral
		Dato.set(Resultado)
	elif Verificacion==3:	
		Resultado=Variable/VariableGeneral
		Dato.set(Resultado)
	elif Verificacion==4:	
		Resultado=Variable+VariableGeneral
		Dato.set(Resultado)
	Verificacion=0
	CerradaOperacion=1
	VariableGeneral=Resultado

def BorrarTodo():
	global Verificacion
	Verificacion=0
	Dato.set("")

def BorrarParcial():
	Dato.set("")

def Borrax():
	global VariableQuitar
	VariableQuitar=Dato.get()
	Dato.set(VariableQuitar[:-1])
	if Dato.get()!="":
		VariableGeneral=float(Dato.get())


#----------------------Menu---------------------
Menus=Menu(raiz)
raiz.config(menu=Menus, width=300,height=300)

Menue=Menu(Menus, tearoff=0)
Menus.add_cascade(label="Menu", menu=Menue)
Menue.add_command(label="Borrar Todo",command=BorrarTodo)
Menue.add_command(label="Salir",command=Salir)


	
##------------Primera fila---------
boton1=Button(frame,text="1",width=3, command=lambda:muestreo("1")) #La funcion a llamar, le pasamos el parametro del numero mostrado
boton1.grid(row=2,column=0,padx=0,pady=0)
boton2=Button(frame,text="2",width=3, command=lambda:muestreo("2"))
boton2.grid(row=2,column=1,padx=0,pady=0)
boton3=Button(frame,text="3",width=3, command=lambda:muestreo("3"))
boton3.grid(row=2,column=2,padx=0,pady=0)
botonmult=Button(frame,text="x",width=3, command=multiplicacion)
botonmult.grid(row=2,column=3,padx=0,pady=0)


##------------Segunda fila---------
boton4=Button(frame,text="4",width=3, command=lambda:muestreo("4"))
boton4.grid(row=3,column=0,padx=0,pady=0)
boton5=Button(frame,text="5",width=3, command=lambda:muestreo("5"))
boton5.grid(row=3,column=1,padx=0,pady=0)
boton6=Button(frame,text="6",width=3, command=lambda:muestreo("6"))
boton6.grid(row=3,column=2,padx=0,pady=0)
botonDiv=Button(frame, text="/",width=3, command=division)
botonDiv.grid(row=3,column=3,padx=0,pady=0)

##------------Tercera fila---------
boton7=Button(frame,text="7",width=3, command=lambda:muestreo("7"))
boton7.grid(row=4,column=0,padx=0,pady=0)
boton8=Button(frame,text="8",width=3, command=lambda:muestreo("8"))
boton8.grid(row=4,column=1,padx=0,pady=0)
boton9=Button(frame,text="9",width=3, command=lambda:muestreo("9"))
boton9.grid(row=4,column=2,padx=0,pady=0)
botonRest=Button(frame,text="-",width=3, command=resta)
botonRest.grid(row=4,column=3,padx=0,pady=0)

##------------Tercera fila---------
boton0=Button(frame,text="0",width=3, command=lambda:muestreo("0"))
boton0.grid(row=5,column=0,padx=0,pady=0)
botoncoma=Button(frame,text=",",width=3, command=lambda:muestreo("."))
botoncoma.grid(row=5,column=1,padx=0,pady=0)
botonmas=Button(frame,text="+",width=3, command=suma)
botonmas.grid(row=5,column=2,padx=0,pady=0)
botonigual=Button(frame,text="=",width=3, command=igual)
botonigual.grid(row=5,column=3,padx=0,pady=0)

##------------Tercera fila---------
botonCE=Button(frame,text="CE",width=3, command=BorrarTodo)
botonCE.grid(row=6,column=0,padx=0,pady=0)

botonC=Button(frame,text="C",width=3, command=BorrarParcial)
botonC.grid(row=6,column=1,padx=0,pady=0)

botonx=Button(frame,text="<-/",width=3, command=Borrax)
botonx.grid(row=6,column=2,padx=0,pady=0)

SalirButton=Button(frame,text="Salir",command=Salir)
SalirButton.grid(row=6,column=3,padx=0,pady=0)


##--------------Boton Limpieza-----------



raiz.mainloop()
#### Calculadora de ISR


from tkinter import *

#### funciones


## logica del calculo

def isr(ingreso, lim, tasa, cuota):
	
	base = ingreso-lim
	
	porcentaje = base * tasa

	impuesto = cuota + porcentaje
	
	etiqueta_2["text"] = impuesto
	
def calculo():

	ingreso = float(sueldo.get())

	if 0 < ingreso < 644.58:
		
		lim = 0.01
		tasa = 0.0192
		cuota = 0	

		isr(ingreso, lim, tasa, cuota)

	elif 644.59 < ingreso < 5470.92:
	
		lim = 644.59
		tasa = 0.0640
		cuota = 12.38	

		isr(ingreso, lim, tasa, cuota)
	
	elif 5470.93 < ingreso < 9614.66:
	
		lim = 5470.93 
		tasa = 0.1088
		cuota = 321.26	

		isr(ingreso, lim, tasa, cuota)
	
	elif 9614.67 < ingreso < 11176.62:
	
		lim = 9614.67 
		tasa = 0.16
		cuota = 772.10

		isr(ingreso, lim, tasa, cuota)
	
	elif 11176.63 < ingreso < 13381.47:
	
		lim = 11176.63
		tasa = 0.1792
		cuota = 1022.01	

		isr(ingreso, lim, tasa, cuota)
		
	elif 13381.48 < ingreso < 26988.5:
	
		lim = 26988.51
		tasa = 0.2136
		cuota = 1417.12		

		isr(ingreso, lim, tasa, cuota)
	
	elif 26988.51 < ingreso < 42537.58:
	
		lim = 42537.59
		tasa = 0.2352
		cuota = 4323.58		

		isr(ingreso, lim, tasa, cuota)
		
	elif 42537.59 < ingreso < 81211.25:
	
		lim = 81211.26
		tasa = 0.3
		cuota = 7980.73	

		isr(ingreso, lim, tasa, cuota)
	
	elif 81211.26 < ingreso < 108281.67:
	
		lim = 81211.26
		tasa = 0.32
		cuota = 19582.83

		isr(ingreso, lim, tasa, cuota)
	
	elif 108281.68 < ingreso < 324845.01:
	
		lim = 108281.68
		tasa = 0.34
		cuota = 28245.36	

		isr(ingreso, lim, tasa, cuota)
	
	else:
		lim = 324845.02
		tasa = 0.35
		cuota = 101876.9
	
		isr(ingreso, lim, tasa, cuota)


### Cosas visuales 


ventana = Tk()
ventana.title("Calculadora de ISR ")

ventana.geometry("300x300")

## donde ingresar el texto

etiqueta_1 = Label(ventana, text =  "Inserte su salario \n")
etiqueta_1.pack()

sueldo = Entry(ventana)
sueldo.pack()

## boton que realiza la funcion

boton_1 = Button(ventana, text = "Haga click", command = calculo)
boton_1.pack()

## resultado

mensaje = Label(ventana, text = "Su ISR es \n")
mensaje.pack()


etiqueta_2 = Label(ventana)
etiqueta_2.pack()



### Fin del programa


ventana.mainloop()

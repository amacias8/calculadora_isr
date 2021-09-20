#### Calculadora de ISR #######

### Primero definimos algunas funciones

# decisiones

def decision(opcion) :

	if opcion == 1 :
	
		ingreso = float(input("Inserte su ingreso: ", ))
	
		calculo(ingreso)
	
	elif opcion == 2 :
	
		print("Bais")
		
	else :
			
		print("Repita el procedimiento!")
		print("Seleccione una opcion")
		print("1) Calculo de ISR")
		print("2) Salir")
		opcion = float(input("Inserte su opcion: ", ))
		decision(opcion)


# Logica del calculo
def base_resta (ingreso, lim, tasa, cuota):
	
	base = ingreso-lim
	
	porcentaje = base * tasa

	impuesto = cuota + porcentaje

	print('Su impuesto es: ', impuesto)
	print("Desea calcular otro ISR?")
	print("1) Si")
	print("2) No")
	
	opcion = float(input("Inserte su opcion: " , ))
	
	decision(opcion)
	
# determina los intervalos

def calculo (ingreso):

	if 0 < ingreso < 644.58:
		
		lim = 0.01
		tasa = 0.0192
		cuota = 0	

		base_resta(ingreso, lim, tasa, cuota)

	elif 644.59 < ingreso < 5470.92:
	
		lim = 644.59
		tasa = 0.0640
		cuota = 12.38	

		base_resta(ingreso, lim, tasa, cuota)
	
	elif 5470.93 < ingreso < 9614.66:
	
		lim = 5470.93 
		tasa = 0.1088
		cuota = 321.26	

		base_resta(ingreso, lim, tasa, cuota)
	
	elif 9614.67 < ingreso < 11176.62:
	
		lim = 9614.67 
		tasa = 0.16
		cuota = 772.10

		base_resta(ingreso, lim, tasa, cuota)
	
	elif 11176.63 < ingreso < 13381.47:
	
		lim = 11176.63
		tasa = 0.1792
		cuota = 1022.01	

		base_resta(ingreso, lim, tasa, cuota)
		
	elif 13381.48 < ingreso < 26988.5:
	
		lim = 26988.51
		tasa = 0.2136
		cuota = 1417.12		

		base_resta(ingreso, lim, tasa, cuota)
	
	elif 26988.51 < ingreso < 42537.58:
	
		lim = 42537.59
		tasa = 0.2352
		cuota = 4323.58		

		base_resta(ingreso, lim, tasa, cuota)
		
	elif 42537.59 < ingreso < 81211.25:
	
		lim = 81211.26
		tasa = 0.3
		cuota = 7980.73	

		base_resta(ingreso, lim, tasa, cuota)
	
	elif 81211.26 < ingreso < 108281.67:
	
		lim = 81211.26
		tasa = 0.32
		cuota = 19582.83

		base_resta(ingreso, lim, tasa, cuota)
	
	elif 108281.68 < ingreso < 324845.01:
	
		lim = 108281.68
		tasa = 0.34
		cuota = 28245.36	

		base_resta(ingreso, lim, tasa, cuota)
	
	else:
		lim = 324845.02
		tasa = 0.35
		cuota = 101876.9
	
		base_resta(ingreso, lim, tasa, cuota)



## Generar un menu para seleccionar el calculo de ISR o Salir

print("Calculadora de ISR \n")
print("1) Calculo de ISR \n")
print("2) Salir \n")
opcion = float(input("Inserte su opcion: ", ))

decision(opcion)

### Fin

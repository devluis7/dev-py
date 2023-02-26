#Programa para convertir monedas
#Version 1.0 - convertir soles a dolares
#Inputs - entradas
montoSoles = input("Ingrese el monto en soles: ")
#Proceso
montoDolares = float(montoSoles) / 3.89
montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
#Outputs - Salidas
print ("El monto en dolares es: " + str(montoDolares))
print(montoSoles," es igual a ", str(montoDolaresFormato))
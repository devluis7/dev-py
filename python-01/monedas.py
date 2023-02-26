#Programa para convertir monedas
#Version 1.0 - convertir soles a dolares
#Inputs - entradas
montoOrigen = input("Ingrese el monto: ")
#Proceso
print(" Opcion 1 - soles a dolares")
print(" Opcion 2 - dolares a soles")
opcion = input ("Eliga una opción: ")

if (opcion ==1):
        montoDolares = float(montoOrigen) / 3.89
        montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
        #Outputs - Salidas
        print ("El monto en dolares es: " + str(montoDolares))
else:
        montoSoles = float(montoOrigen) * 3.89
        montoSolesFormato =  "S/. {:,.2f}".format(montoSoles)
        #Outputs - Salidas
        print ("El monto en soles es: " + str(montoSolesFormato))
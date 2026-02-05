# Programa para convertir °C a °K y °F

#Libreterias
import math

#-----
#input
#-----

print("------------------------------------")
print("-------Convertir °C a °K y °K-------")
print("------------------------------------")


C=int(input("Digite el valor de °C: "))

#----------
#Processing
#----------

F=C*1.8+32
K=C+273.15

#--------
#output
#--------
print("Grados Fahrenheit: " +str(F))
print("Grados kelvin: " +str(K))
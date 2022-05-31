#EJERCICIO 1
# Declaramos una variables
calificacion = input("Introduce tu calificaicon de AZ-900: ")

calificacion = int(calificacion)

#Preguntamos si la califacion es menor a 700
if  calificacion <  700 :
    print("Vees, por no estudiar") # Si es menor a 700 muestra esto
elif calificacion == 700:
    print("PANZAZOOO")
elif calificacion > 1000:
    print("MIENTES!!! No se puede sacar mas de mil")
else : # Si no se cumple el if anterior, pasa a esta linea
    print ("Felicidades, pasa por tu certificado") # Se ejecuta si ninguno de los if se cumple

# EJERCICIO 2
# Verificador de mayoria de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100:
    print("Si vienes acompañad@ de tus abuelos, si te podemos fiar")
elif edad < 0:
    print("Ni que fueras viajer@ del tiempo")
else :
    print("No puedes llvarte esos cigarros")

#EN PYTHON NO HAY SWTICH CASE
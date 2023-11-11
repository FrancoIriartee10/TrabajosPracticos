print("Ejercicio Numero 1.")
# Escriba  una  función  redondear()  que  permita  redondear  un  número 
# decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el 
# entero siguiente (en este caso, 4), si no devolver el entero inmediatamente 
# anterior (3).

def redondear(numero):
    parte_decimal = numero - int(numero)
    if parte_decimal >= 0.5:
        return int(numero) + 1
    else:
        return int(numero)

num = float(input("Ingrese un numero: "))
funcion = redondear(num)
print(funcion)

input("\n PRESIONE 'ENTER' PARA EL SIGUIENTE EJERCICIO\n")

print("Ejercicio Numero 2.")
# Coloque  el  módulo  del  ejercicio  anterior  dentro  de  un  paquete.  En  un 
# módulo  que  esté  fuera  de  ese  paquete,  cree  una  función  de  suma  de 
# decimales que redondee el resultado haciendo uso de la función 
# redondear() del paquete recién creado.

from Ejercicio import punto2
def suma():
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    var1 = punto2.redondear(num1)
    var2 = punto2.redondear(num2)
    
    print(f"La suma de los dos numeros ingresados es de: {var1 + var2}")

suma()

input("\n PRESIONE 'ENTER' PARA EL SIGUIENTE EJERCICIO\n")

print("Ejercicio Numero 3.")
# Usando el módulo datetime, escribe un programa que muestre la fecha y hora actuales
# del sistema.
def fecha_y_hora():
    import datetime
    actual = datetime.datetime.now()
    print(f"Fecha y hora actual: {actual}")

fecha_y_hora()

input("\n PRESIONE 'ENTER' PARA EL SIGUIENTE EJERCICIO\n")

print("Ejercicio Numero 4.")
# Escriba  un  programa  que  devuelva  un  número  par  al  azar  entre  2  y  10 
# (pista: para comprobar si se pueden generar todos los números, pruebe 
# ejecutar el programa dentro de un ciclo infinito).
def azar():
    import random
    num = random.randint(2, 10)
    print(f"El numero al azar es: {num}")

azar()

input("\n PRESIONE 'ENTER' PARA EL SIGUIENTE EJERCICIO\n")

print("Ejercicio Numero 5.")
# Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado 
# para la adivinación o para buscar consejo. Su mecanismo es muy simple: 
# ante  una  pregunta  del  usuario,  la  bola  responde  con  una  de  8  posibles 
# respuestas: 
# - Es seguro que sí - Las chances son buenas - Puedes contar con ello 
# - Pregúntame de nuevo más tarde - Concéntrate y pregunta de nuevo 
# - No veo con claridad, intenta de nuevo - Mi respuesta es no 
# - Mis fuentes me dicen que no 
# Escriba una función en Python para simular la bola mágica.
def bola_magica():
    import random
    opciones = ["Es seguro que si.", "Las chances son buenas.", "Puedes contar con ello.", "Preguntame de nuevo mas tarde.",
                "Concentrate y pregunta de nuevo.", "No veo con claridad, intenta de nuevo.", "Mi respuesta es no." ]
    input("Cual es su pregunta?: ")
    print(f"{random.choice(opciones)}")
    while True:
        seguir = input("Quiere hacer otra pregunta? (Si/No): ")
        if seguir.lower() == 'si':
            input("Cual es tu pregunta?: ")
            print(f'{random.choice(opciones)}')
        else:
            print("Punto finalizado.")
            break

bola_magica()

input("\n PRESIONE 'ENTER' PARA EL SIGUIENTE EJERCICIO\n")

print("Ejercicio Numero 6.")
# Encuentre  el  tiempo  de  ejecución  de  los  programas  de  los  ejercicios 
# anteriores (pista: use el módulo time)
def tiempo():
    import time
    inicio = time.time()
    redondear(num)
    # print(f"El numero 3.5 redondeado: {redondear(3.5)}")
    fin = time.time()
    print(f"El tiempo transcurrido del 1er punto es: {fin - inicio}\n")

    inicio = time.time()
    suma()
    fin = time.time()
    print(f"El tiempo transcurrido del 2ndo punto es: {fin - inicio}\n")

    inicio = time.time()
    fecha_y_hora()
    fin = time.time()
    print(f"El tiempo transcurrido del 3er punto es: {fin - inicio}\n")

    inicio = time.time()
    azar()
    fin = time.time()
    print(f"El tiempo transcurrido del 4to punto es: {fin - inicio}\n")

    inicio = time.time()
    bola_magica()
    fin = time.time()
    print(f"El tiempo transcurrido del 5to punto es: {fin - inicio}\n")

tiempo()

print("Fin del Trabajo Practico")
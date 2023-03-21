
# son 4 tipos de variables
# String
name = "kevin"
last_name = "Jimenez"


# Integer
id = 119090651

# Float 
cash = 10.5

# Bool 

active = True

# Comparaciones de las variables
# Cómo verificar si el PIN ingresado por el usuario coincide con su PIN guardado

entered_pin = 5448
expected_pin = 5448

result = entered_pin == expected_pin

print(result)

# Comparaciones con desigualdad. Tenemos que usar el operador !=

result_1 = 1 != 2
print(result_1)

one = 1
two = 2
print("------------------------")
print(one == two)
print(one != two)


# Vamos a hacer un interruptor de luz inteligente que apague las luces si es de día y las encienda si es de noche
print("------------------------")
is_day = False
lights_on = not is_day

print("Daytime?")
print(is_day)

print("Lights on?")
print(lights_on)

# Con las comparaciones vamos a hacer un códido que rastree los datos de ventas de una tienda de pantalones
print("------------------------")
stock = 600
jeans_sold = 500
target = 500
target_hit = jeans_sold == target
print("Hit jeans sale target: ")
print(target_hit)
current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock: ")
print(in_stock)
print(current_stock)


# Podemos usar comparaciones para verificar si un número es mayor o menor que otro número
print("------------------------")
print(2 <= 200)
print(2 >= 200)

print("------------------------")
# Comparaciones de cadenas de texto

my_answer = "lowr"
solution = "low"

print(my_answer == solution)
print(my_answer != solution)

# Ejercicio de medidor de frecuencia cardiaca, usando comparaciones para verifiar si la frecuencia cardiaca es deamsiad baja o alta y le diremos al cliente si debe preocuparse.
print("------------------------")

heart_rate = 77

too_low = heart_rate < 60
too_high = heart_rate > 100

print("Heart rate low")
print(too_low)
 
print("Heart rate high")
print(too_high)
print("------------------------")

Numero_1 = 35
numero_2 = 35

Resultado = Numero_1 + numero_2
print(Resultado)

print("------------------------")

Edad = 19

N = Edad >=18

print("¿Mayor de edad?")
print(N)

print("------------------------")

# Usemos comparaciones string para etiquetar los datos adquiridos a través de la encuesta de usuarios de una aplicación ed fitness.
# Verificamos las respuestas de la encuesta de los usuarios con respecto a la frecuencia e intensidad de la actividad, las etiquetaremos y mostraremos los resultados.

Frecuencia = "Una vez a la semana"
Intensidad = "Baja"

Activo = Frecuencia == "Diaria"
print("El usuario es activo?")
print(Activo)

Intenso = Intensidad == "Alta"
print("El usuario es intenso?")
print(Intenso)

print("------------------------")
print("Ejercicio_1")

Celular = "xxxxxxxx"

print(f"https://wa.me/506{Celular}")

print("------------------------")

#1

print("Hola mundo")

#2
print("------------------------")

Gesto = "Hola mundo"
print(Gesto)

#3

Usuario = "Kevin Jiménez"

print(f"!Hola {Usuario}¡")

#4

print("??????")

#5


Horas_trabajadas = 48

coste_por_hora = 8000
print("cuantas horas ha trabajado?")
print(Horas_trabajadas)

print(f"Su paga sería de {Horas_trabajadas * coste_por_hora}")

#6

peso = int(input("Por favor ingrese su peso en kg: "))
estatura = float(input("Por favor ingrese su estatura en metros: "))
IMC = round(peso / (estatura ** 2), 2)

print(f"Tu índice de masa corporal es {IMC}")

#7

Numi_1 = 60
numi_2 = 10
cociente = Numero_1 / numi_2
Resto = Numi_1 % numi_2

print(f"n divido entre m es igual a {cociente} y su resto sería {Resto}")

print("------------------------")
#1

nombre_completo = input("Ingrese su nombre completo: ")

print(nombre_completo.lower())
print(nombre_completo.upper())
print(nombre_completo.title())

print("------------------------")
#2
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un número entero: "))

print("Hola \n" + (nombre + "\n") * (numero))

print("------------------------")

#3
nombre = input("Ingrese su nombre: ")

print(nombre.upper(), "tiene", len(nombre), "letras")





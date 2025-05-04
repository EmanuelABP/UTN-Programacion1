#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre = input("Como te llamas? ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre = input("Cual es tu nombre? ")
apellido = input("Cual es tu apellido? ")
edad = input("Cuantos años tienes? ")
residencia = input("Donde vives? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math

radio = float(input("Introduce el radio del circulo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Area: {area:.2f}")
print(f"Perimetro: {perimetro:.2f}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Introduce una cantidad de segundos: "))
horas = segundos // 3600
segundos_restantes = segundos % 3600
print(f"{segundos} segundos son {horas} horas y {segundos_restantes} segundos.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Introduce un numero para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Introduce el primer numero (distinto de 0): "))
numero2 = int(input("Introduce el segundo numero (distinto de 0): "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / altura ** 2
print(f"Tu indice de masa corporal (IMC) es: {imc:.2f}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
num3 = float(input("Introduce el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres numeros es: {promedio:.2f}")

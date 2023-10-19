#Trabajo n4
#Ejercicio 1
x=0
x=x+1
while x<=30:

  if x==4 or x==6 or x==10:
    print(f"El valor {x} fue omitido")
  else:
    print("El valor del bucle es: ", x)

  if x==15:
    print("Se detuvo la ejecución del bucle en x= ",x)
    break
  x=x+1

#Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.
line=""
while line=="":
  line=input("Ingrese una linea: ")
  print(line.upper())
  if line=="":
    print("Ha finalizado la entrada de lineas")
    break
  else:
    line=""
    print("")    

#Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
print("Bienvenido al Banco")
flag=False
total=0
while flag==False:
  print("Ingrese una opcion")
  option=int(input("(1) Deposito | (2) Retiro | (3) Salir : "))
  if option==1:
    deposito=int(input("Ingrese el monto a depositar: "))
    print("Deposito realizado")
    total=total+deposito
  elif option==2:
    retiro=int(input("Ingrese el monto a retirar: "))
    if retiro>total:
      print("No tiene esa cantidad")
    else:
      print("Retiro realizado")
      total=total-retiro
  elif option==3:

    print("Su saldo total es $",total)
    flag=True
  else:
    print("Opcion invalida")

#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.Imprimir la cantidad total de números primos ingresados.Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.

primos=0
while True:
  numero=int(input("Ingrese un numero: "))
  if numero==0:
      break
  elif numero>1:
    contador=0
    for i in range(1,numero+1):
      if numero%i==0:
        contador+=1
    if contador==2:
      primos+=1


print("La cantidad de numeros primos ingresados es: ",primos)

#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
year_1=int(input("Ingrese un año: "))
year_2=int(input("Ingrese otro año: "))
for i in range(year_1,year_2+1):
  print("Año: ",i, end=" ")
  if i%4==0 and i%100!=0 or i%400==0:
      print("año biciesto")
  print("")


#Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.
for i in range(1,21):
  if i%2==0:
    print(i)
  else:
    #Omite los numeros impares
    continue

#Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n=int(input("Ingrese un numero para buscar en la lista: "))
cont=0

for i in list:
  if i==n:
    print("numero encontrado en la posicion: ",cont)
    cont=0
    break

  cont+=1
if cont!=0:
  print("numero no encontrado")


#Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).
opcion=1
while opcion!=0:
  print("(1) Opcion 1 |(2) Opcion 2 |(3) Opcion 3 |(0) Salir")
  opcion=int(input("Ingrese una opcion: "))
  if opcion==1:
    print("Opcion 1")
  elif opcion==2:
    print("Opcion 2")
  elif opcion==3:
    print("Opcion 3")
  elif opcion==0:
    print("Salir")
    break
  else:
    print("Opcion no valida")
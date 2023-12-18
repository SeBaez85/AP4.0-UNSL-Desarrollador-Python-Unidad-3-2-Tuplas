print("Vamos a averiguar la suma de los números pares e impares de la tupla")
a = int(input("Ingrese el primer valor de la tupla: "))
b = int(input("Ingrese el segundo valor de la tupla: "))
c = int(input("Ingrese el tercer valor de la tupla: "))
d = int(input("Ingrese el cuarto valor de la tupla: "))
e = int(input("Ingrese el quinto valor de la tupla: "))

t = (a, b, c, d, e)
acumuladorPares = 0
acumuladorImpares = 0
for i in t:
    if i % 2 == 0:
        acumuladorPares = acumuladorPares + i
    else:
        acumuladorImpares = acumuladorImpares + i

print("La suma de los números pares es: ", acumuladorPares)
print("La suma de los números impares es: ", acumuladorImpares)

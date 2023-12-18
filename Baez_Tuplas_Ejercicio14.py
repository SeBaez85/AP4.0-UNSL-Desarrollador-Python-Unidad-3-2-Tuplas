e = int(input("Ingrese un número para evaluar si está en la tupla: "))
a = int(input("Ingrese el primer valor de la tupla: "))
b = int(input("Ingrese el segundo valor de la tupla: "))
c = int(input("Ingrese el tercer valor de la tupla: "))

t = (a, b, c)

if e in t:
    print(f"El número {e} está en la tupla", t)



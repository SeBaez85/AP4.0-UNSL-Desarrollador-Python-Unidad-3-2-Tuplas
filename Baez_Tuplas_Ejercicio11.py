a = int(input("Ingrese un número para evaluar en qué posición de la tupla está: "))
b = int(input("Ingrese el primer valor de la tupla: "))
c = int(input("Ingrese el segundo valor de la tupla: "))
d = int(input("Ingrese el tercer valor de la tupla: "))

t = (b, c, d)

if a in t:
    print(f"El número {a} está en la posición {t.index(a)}")
else:
    print("-1")


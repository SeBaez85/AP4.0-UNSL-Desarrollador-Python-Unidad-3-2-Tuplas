a = int(input("Ingrese un número para luego evaluar cuántas veces está en una tupla: "))
b = int(input("Ingrese el primer valor de la tupla: "))
c = int(input("Ingrese el segundo valor de la tupla: "))
d = int(input("Ingrese el tercer valor de la tupla: "))

t = (b, c, d)

print(f"El número {a} está {t.count(a)} vez/veces en la tupla")

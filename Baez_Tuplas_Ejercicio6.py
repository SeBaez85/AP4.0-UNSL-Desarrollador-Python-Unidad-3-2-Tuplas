a = int(input("Ingrese el primer valor de la tupla: "))
b = int(input("Ingrese el segundo valor de la tupla: "))
c = int(input("Ingrese el tercer valor de la tupla: "))
d = int(input("Ingrese el cuarto valor de la tupla: "))

t = (a, b, c, d)

n = int(input("Ingrese el número por el cual se van a sumar los elementos de la tupla: "))

s = (n + t[0], n + t[1], n + t[2], n + t[3])

m = int(input("Ingrese el número por el cual se van a restar los elementos de la tupla: "))

r = (t[0] - m, t[1] - m, t[2] - m, t[3] - m)

print("Tupla original:", t)
print("Tupla con los valores de la lista sumados a", n, ":", s)
print("Tupla con los valores de la lista restados a", m, ":", r)

t = (10, 20, 30, 40, 50, 60)

print("Tupla: ",t)
#Dada una tupla (t en este caso), podemos tomar un fragmento de ella mediante una rebanada.
#Indicando entre corchetes el índice de inicio y el de fin de la siguiente manera:


print("Ejemplo de rodaja: ", t[0:4])

#Hay que tener en cuenta que la rodaja abarca hasta el índice 3, no se incluye el 4 en el output

#Mediante las zancadas se pueden generar intervalos o saltos entre los valores de la tupla, por ejemplo:

print("Ejemplo de zancada: ", t[1:7:2])

#En este caso se agrega un tercer valor a los corchetes que indica el intervalo
# o salto que habrá entre los índices, en este caso de 2 en 2
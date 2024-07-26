# Librerias especiales:
# x.appen(e)agregar a la lista x el elemento e
# x.insert(i,e)inserta e en la posicion de la lista x
# x.count(e)cuantas veces aparece un componente en la lista x
# x.remove(e)elimina el primer elemento e de la lista x
# x.sort()ordena x en forma creciente
# x.reverse()invierte la lista x
# x.clear()vaciar la lista x
# x.index entrega la posicion del primer elemento en x
# x.len(X) numero de un componente en la lista
# x.pop() elimina un componente al al final de la lista

numbers = [10, 5, 7, 2, 1]
# Imprimiendo contenido de la lista original.
print("Contenido de la lista:", numbers)

numbers[0] = 111
# Contenido actual de la lista.
print("Nuevo contenido de la lista: ", numbers)

numbers = [10, 5, 7, 2, 1]
# Imprimiendo contenido de la lista original.
print("Contenido de la lista original:", numbers)

numbers[0] = 111
# Imprimiendo contenido de la lista anterior.
print("\nPrevio contenido de la lista:", numbers)

# Copiando el valor del quinto elemento al segundo elemento.
numbers[1] = numbers[4]
# Imprimiendo el contenido de la lista actual.
print("Nuevo contenido de la lista:", numbers)

print(numbers[0])  # Accediendo al primer elemento de la lista.

# Imprimiendo la longitud de la lista.
print("\nLongitud de la lista:", len(numbers))

print(numbers)  # Imprimiendo la lista completa.

del numbers[1]
print(len(numbers))
print(numbers)
# sumar cada elemento de la LISTA
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
# otro aspecto dl bucle para
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

# intercarbiar valores  de una variable
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Ordenar lista:
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# Ordenamiento burbuja:
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

# ordenar lista metodo classificar
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# metodo contrarestar
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # output: [4, 2, 1, 3, 5]

# valor mayor en la lista

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

# encontramos la ubicación de un elemento dado dentro de una lista:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")

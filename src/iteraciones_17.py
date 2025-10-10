# Iteraciones
# for
print("Con bucle 'for'")
for i in range(1, 11):
    print(i)


# while
print("Con bucle 'while'")
j = 1
while j <= 10:
    print(j)
    j += 1


# función recursiva
print("Con función recursiva")


def recursive_func(n):
    if n == 11:
        return n
    else:
        print(n)
        return recursive_func(n + 1)


recursive_func(n=1)


"""
Extra
"""


# iterar elementos de una lista
elementos = [2, 3, 4, 5]


def iter_element_list():
    for elemento in elementos:
        print(elemento)


# Función enumerate
frutas = ["pera", "melon", "kiwi"]
for indice, fruta in enumerate(frutas, start=1):
    print(f"Posición {indice}: {fruta}")


# Función zip()itera dos listas a la vez
for elemento, fruta in zip(elementos, frutas):
    print(elemento, fruta)

# compresion de listas
lista_pares = [h for h in range(1, 11) if h % 2 == 0]
print(lista_pares)

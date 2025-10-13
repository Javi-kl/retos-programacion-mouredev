# Crear conjuntos de datos y realizar operaciones
my_list = []

# Añadir elemento al final
my_list.append(1)

# Añadir elemento al principio
my_list.insert(0, 0)

# Añadir elementos en bloque al final
block_1 = [2, 3]
my_list.extend(block_1)

# Añadir elementos en bloque al principio
my_list[0:0] = [5, 6]

# Añadir bloque posición concreta
my_list[3:3] = [7, 8]
print(my_list)

# Eliminar elemento/ posición concreta
my_list.pop(0)

# Actualizar valor de un elemento / posicion concreta
my_list[1] = 1

# Comprobar si un elemento existe en lista
check_num = 4 in my_list
print(check_num)

# Eliminar todo el conjunto
my_list.clear()
print(my_list)


"""
Extra
"""
# Para la union, intersección , diferencia y diferencia simetrica utilzamos sets
s_1 = {2, 6, 7, 8}
s_2 = {2, 3, 4, 5, 6}
s_3 = {0, 1, 2, 6}

# union or '|', retorna la union de los sets
print(s_1 | s_2 | s_3)

# intersection() or '&', retorna elementos que coinciden en todos los sets.
print(s_1 & s_2 & s_3)

# difference() or '-', retorna elementos unicos entre el primer set y sus comparadores
print(f"{s_3-s_1-s_2}")

# symmetric_difference() or '^', retorna elementos unicos entre todos los sets.
print(s_1 ^ s_2)

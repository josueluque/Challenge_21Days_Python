'''
    -- Maneja correctamente los errores --
    En este desafío, debes crear una función llamada calculate_average que calcule el promedio de una lista de números. 
    Sin embargo, la función debe manejar correctamente dos casos especiales:
    Si la lista está vacía, la función debe generar una excepción ValueError con el mensaje "La lista está vacía".
    Si la lista contiene elementos que no son números, la función debe generar una excepción TypeError con el mensaje 
    "La lista contiene elementos no numéricos".
    Tu objetivo es implementar la función calculate_average de manera que maneje adecuadamente estos casos y devuelva 
    el promedio de los números en la lista.
'''


def calculate_average(numbers):
    try:
        return sum(numbers)/len(numbers)
    except ZeroDivisionError:
        raise ValueError("La lista está vacía")
    except TypeError:
        raise TypeError("La lista contiene elementos no numéricos")


r = calculate_average([1, 2, 3, 4, 5])
print(r)
a = calculate_average([])
print(a)
e = calculate_average([1, 2, '3', 4, 5])
print(e)

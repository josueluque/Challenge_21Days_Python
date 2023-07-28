'''
    -- Obten la información de los paquetes --
    En este desafío, te encuentras trabajando para una empresa de transporte de carga que necesita llevar un registro de 
    los paquetes que se envían en cada viaje. Para ello, se te proporcionará una lista de tuplas, cada una de las cuales 
    representará un paquete y tendrá las siguientes propiedades: (id, weight, destination)

    A partir de esta información, debes crear una función que calcule el peso total de los paquetes, así como la cantidad 
    de paquetes que se enviarán a cada destino. Para ello, debes retornar un nuevo diccionario que tenga las siguientes propiedades:
        "total_weight": El peso total de los paquetes.
        "destinations": Un diccionario con los destinos como claves y la cantidad de paquetes como valores.
    Es importante mencionar que la función debe redondear el peso total a dos decimales y que cada destino debe aparecer 
    sólo una vez en el diccionario
'''


def get_packages_info(packages):
    package_info = {}
    weight = [package[1] for package in packages]
    total_weight = round(sum(weight), 2)
    tuple_dest = tuple(package[2] for package in packages)
    destinations = {destino: tuple_dest.count(
        destino) for destino in tuple_dest}

    package_info["total_weight"] = total_weight
    package_info["destinations"] = destinations
    return package_info


data = [
    (1, 20, "Mexico"),
    (2, 15.5, "Colombia"),
    (3, 30, "Mexico"),
    (4, 12, "Argentina"),
    (5, 8.2, "Colombia"),
    (6, 25, "Mexico"),
    (7, 18.7, "Argentina"),
    (8, 5, "Colombia"),
    (9, 22.3, "Argentina"),
    (10, 14.8, "Colombia")
]

result = get_packages_info(data)
print(result)

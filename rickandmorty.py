import json
import os


with open('episodes.json') as archivo:
    
    datos = json.load(archivo)



with open('character.json') as archivo:
    
    datos2 = json.load(archivo)

def clear_screen():
    
    return os.system('cls' if os.name == 'nt' else 'clear')

def listado_caps():
    
    for num, caps in enumerate(datos["results"], start=1):
        print(f"{num}. - {caps['name']}")

    print()

def personajes():
    
    global personaje_data

    if personaje == "1":
        
        print("\nEsta es la cantidad de episodios en los que aparece Rick Sanchez:\n")
        
        personaje_data = 1
    
    elif personaje == "2":
        
        print("\nEsta es la cantidad de episodios en los que aparece Morty Smith:\n")
        
        personaje_data = 2
    
    elif personaje == "3":
        
        print("\nEsta es la cantidad de episodios en los que aparece Summer Smith:\n")
        
        personaje_data = 3
    
    else:
        
        print("Personaje no válido.")
        return

    
    personaje_info = datos2["results"][personaje_data - 1]
    print(f"Capitulos en los que aparece el personaje con ID: {personaje_data}:\n")
    print("Nombre:", personaje_info["name"])
    print("\nEstatus:", personaje_info["status"])
    print("\nEspecie:", personaje_info["species"])
    print("\nGenero:", personaje_info["gender"])
    print("\nTipo:", personaje_info["type"])
    print("\nEpisodios:\n")
        
    for num, episode in enumerate(personaje_info['episode'], start=1):
        
        print(f"{num}. {episode}")

    print("\nEnlace:", personaje_info["url"])
    
    print()

def encontrar_cap():
    try:
        id_cap = input("Ingrese el ID que desea: ")
    
    
        
        id_cap_int = int(id_cap)
        
        if 1 <= id_cap_int <= len(datos["results"]):
            
            episodio = datos["results"][id_cap_int - 1]
            
            print(f"\nDatos del episodio con ID {id_cap_int}\n")
            print("\nIdentificador:", episodio.get("id"))
            print("\nNombre:", episodio.get("name"))
            print("\nFecha de emisión:", episodio.get("air_date"))
            print("\nEpisodio:", episodio.get("episode"))   
            print()
        
        else:
            
            print(f"No se encontró un episodio con ID {id_cap}")
    
    except ValueError:
        
        print("\nID de episodio no válido. Debe ser un número.\n")

def enlaces():
    
    try:
        enlaces = int(input("Ingrese un id para ver los enlaces de ese capitulo: "))
        
        enlace_info = datos["results"][enlaces - 1]
        
        print(f"\nEstos son los enlaces del episodio {enlaces}\n")

        for num, episode in enumerate(enlace_info['characters'], start=1):
            
            print(f"{num}. {episode}")

    except ValueError:
        print("\nID de enlace no válido. Debe ser un número.\n")


while True:
    
    input("Presione Enter para continuar... ")
    
    clear_screen()
    
    print("\nLa longitud de la variable datos es:", len(datos["results"]))
    print('La variable datos es de tipo:', type(datos))
   
  
    
    print("\nIngrese 1 para salir\nIngrese 2 para ver los personajes disponibles\nIngrese 3 para inmprimir la cantidad de capitulos\nIngrese 4 Consultar infornacion de un capitulo\nIngrese 5 para consultar urls\n")
    
    usuario = input("> ")
    
    print()
    
    if usuario == "1":
        
        break

    if usuario == "2":
        
        print("\ningrese 1 para ver la informacion de Rick Sanchez\nIngrese 2 para ver la infomacionde de Morty Smith\nIngrese 3 para ver la informacion de Summer Smith\n")
        personaje = input("> ")
        
        if personaje == "1" or personaje == "2" or personaje == "3":
        
            personajes()

    if usuario == "3":

        listado_caps()
    
    if usuario == "4":
        
        encontrar_cap()
    
    if usuario == "5":
        
        enlaces()
    
    else:
        continue
    
    print()

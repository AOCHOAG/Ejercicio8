import Persistencia_json as Pj #Importo persiste... y lo abrevio como Pj
#algo = input("Dime algo: ")
#nombre_archivo = input("Dime como quieres que se llame el archivo: ")

#Pj.store(algo, nombre_archivo) #Llamo a la funcion store y le doy en orden que es lo que
                               #Quiero que considere var y que es lo que quiero que considere
                               #filename
#Pj.retrieve(nombre_archivo)
#print("\nMe has dicho:\n", Pj.retrieve(nombre_archivo)) # Imprimo la lista cargada (aparece llena)

lista_coches = [] #Creamos una lista vacía

Nombre_archivo = input("Dime como quieres llamar al archivo: ")

while True: #creamos un bucle, para introducir varios elementos
    marca_coche = input("Introduce la marca del coche: ") #Creo variable marca coche y le pido que intruduzca
    if marca_coche == "fin": #le digo que si se escribe "fin" finalice el bucle (con break)
        break
    modelo_coche = input("Introduce el modelo del coche: ")
    combustible = input("introduce el tipo de combiustible: ")
    cilindrada = input("Introduce la cilindrada: ")

    datos_coche = {}  # Creo un diccionario vacio
    datos_coche ["Marca del coche: "] = marca_coche #añado "palabras" al diccionario
    datos_coche ["Modelo del coche: "] = modelo_coche
    datos_coche ["Tipo de combustible: "] = combustible
    datos_coche ["Cilindrada: "] = cilindrada
    lista_coches.append(datos_coche)

Pj.store(lista_coches, Nombre_archivo)
lista_coches = []
print("Lista de coches vacia: ", lista_coches)
lista_coches = Pj.retrieve(Nombre_archivo)
print("Estos son los coches de la lista: ", lista_coches)

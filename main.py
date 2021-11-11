import Persistencia_json as Pj #Importo persiste... y lo abrevio como Pj

algo = input("Dime algo: ")
nombre_archivo = input("Dime como quieres que se llame el archivo: ")

Pj.store(algo, nombre_archivo) #Llamo a la funcion store y le doy en orden que es lo que
                               #Quiero que considere var y que es lo que quiero que considere
                               #filename

#Pj.retrieve(nombre_archivo)
print("\nMe has dicho:\n", Pj.retrieve(nombre_archivo)) # Imprimo la lista cargada (aparece llena)

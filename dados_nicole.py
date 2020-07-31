import random
respuesta=input("¿Desea lanzar los dados?: Si/No ")
while(respuesta=="Si" or respuesta=="s" or respuesta=="si" or respuesta=="S"):
    print("Lanzando los dados...")
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    print("Los valores de los dados son: ")
    print("Dado 1: " + str(dado1)+ "\nDado 2: " +str(dado2))
    print("La suma de ambos dados es igual a: "+ str(dado1+dado2))
    respuesta=input("¿Desea lanzar los dados?: Si/No ")

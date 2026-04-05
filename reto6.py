palabras_ingresadas=[]
sin_repetidos=[]

def agregar_palabras():
    cantidad=int(input("cuantas palabras desea ingresar?: "))

    for i in range(cantidad):
        palabra=input("ingrese palabras: ")
        palabras_ingresadas.append(palabra)
    return palabras_ingresadas

def sin_repetir():
    for palabra in palabras_ingresadas:
        if palabra not in sin_repetidos:
            sin_repetidos.append(palabra)
     
    return sin_repetidos

print("lista con elementos repetidos ", agregar_palabras())
print("lista sin elementos repetidos ", sin_repetir())

    

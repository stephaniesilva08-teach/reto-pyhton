palabras_positivas=["ama", "gusta", "genial", "excelente", "bueno", "buen"]
palabras_negativas=["odia", "malo", "terrible", "decepcionante", "pésimo"]

contador_pos=0
contador_nega=0

def sentimiento(contador_pos , contador_nega):
    if contador_pos>contador_nega:
        return ("SENTIMIENTO POSITIVO")
    elif contador_nega>contador_pos:
        return("SENTIMIENTO NEGATIVO")
    else:
        contador_pos==contador_nega
        return("SENTIMIENTO NEUTRAL")
    
comentario=input("ingrese un comentario: ").lower()
palabras=comentario.split()

for palabra in palabras:
    palabra=palabra.strip(".,")
    if palabra in palabras_positivas:
        contador_pos+=1
    if palabra in palabras_negativas:
        contador_nega+=1

resultado=sentimiento(contador_pos,contador_nega)
print(resultado)







    





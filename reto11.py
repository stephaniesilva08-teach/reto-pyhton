numero_secreto=42
print("   EMPIEZA EL JUEGO ")
print("   ADIVINA EL NUMERO ")
print("¡Adivina el número secreto entre 1 y 100!")

intentos=0

while True:

    num=int(input("ingrese un numero: "))
    if num == numero_secreto: 
        print("¡Felicidades! ADIVINASTE EL NUMERO 42")
        print(intentos, "intentos")    
    elif num >= 38 and num <=41:
        intentos+=1
        print("EL NUMERO ESTA CERCA")
    elif num >=43:
        intentos+=1
        print("EL NUMERO ESTA DEMASIADO ALTO")
    elif num < 38:
        intentos+=1
        print("EL NUMERO ES DEMASIADO BAJO")
    else:
       print("SIGUE INTENTANDO")
    break
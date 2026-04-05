

def año_bisiesto(año):
    if año %400 == 0: 
        print("AÑO BISIESTO")
    elif año %100 == 0:
        print("AÑO NO BISIESTO")
    elif año %4 == 0:
        print("AÑO BISIESTO")
    else:
        print("NO BISIESTO")
        
año=float(input("ingrese un año: "))

resultado=(año_bisiesto(año))
print(resultado)
proteina=float(input("ingrese los gramos de proteina: "))
carbohidrato=float(input("ingrese los gramos de carbohidratos: "))
grasa=float(input("ingrese los gramos de grasa: "))

valor_proteina_gramo=4
valor_carbohidrato_gramo=4
valor_grasa_gramo=9


calorias_proteina=proteina*valor_proteina_gramo
calorias_carbohidrato=carbohidrato*valor_carbohidrato_gramo
calorias_grasa=grasa*valor_grasa_gramo

suma=calorias_proteina+calorias_carbohidrato+calorias_grasa

total=(suma)

print("total de calorias: ", total)
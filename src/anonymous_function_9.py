# MAP

lista = [4, 3, 12, 85, 1, 3, 75, 17, 2]
print(list(map((lambda valor: valor * valor), lista)))
"""
1_ le paso el formato que quiero que convierta, en este caso 'list'
2_aplico el map
3_el lambda por que es una funcion anonima que no se va a repetir muchas veces en mi codigo
4_le digo por cada valor de lista,que se multiplique asi mismo
5_le pasamos mi lista a la function map,para que sepa a quien le tiene que aplicar el map

"""

listaNombre = ["benjamin", "jazmin", "lorenzo", "franPeronista", "Milei"]
total = list(map((lambda name: name + "VLC"), listaNombre))
print(total)

#FILTER

print(list(filter((lambda name: name == "lorenzo"), listaNombre)))
print(list(filter((lambda number: number == 3), lista)))

#REDUCER -> no duelve una lista,return one value
#suma cada valor
import  functools
print(str(functools.reduce((lambda x,resultado: x + resultado),lista)))
print(str(functools.reduce((lambda value,count: value + count),lista)))
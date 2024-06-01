#Las variables en python se declaran de la siguiente manera:

nombre_de_la_variable = 'Valor'

#Noten que para separar las palabras use el guion bajo _, no se pueden usar espacios

#Tipos de datos:

#Numericos
entero = 10
decimal = 4.5 #Se usa un punto

#Texto:
palabra = 'Hola'
texto_con_saltos_de_linea="""Este es un
                            Texto con saltos
                            De linea"""
                            
#Booleanos
verdadero = True
falso = False


#Imprimiendo por pantalla los datos, junto a su tipo, con ayuda de la funcion type() (el concepto de funcion se vera mas adelante)
print(f'El dato {entero} es tipo: ',type(entero)) #La salida de tipo sera int
print(f'El dato {decimal} es tipo: ',type(decimal)) #La salida de tipo sera float
print(f"El dato {palabra} es tipo: ",type(palabra)) #La salida sera str, al igual que con texto_con_saltos_de_linea
print(f'El dato {verdadero} es tipo: ',type(verdadero)) #La salida sera bool
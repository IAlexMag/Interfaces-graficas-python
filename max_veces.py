elementos = []
can_elementos = int(input('Cantidad de elementos: '))
contador = 0

while contador < can_elementos:
    elemento = int(input('Ingresa el numero a evaluar: '))
    elementos.append(elemento)
    contador +=1

frecuencia = {}

for n in elementos:
    if n in frecuencia:
        frecuencia[n] +=1
    else:
        frecuencia[n] = 1

maximo = max(frecuencia, key=frecuencia.get)


print(f'el número que más se repite es {maximo}')
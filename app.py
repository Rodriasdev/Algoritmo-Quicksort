lista=[1,9,3,6,2,0,4,8,6,5,7,10]


def quicksort(elementos):
    # Si la longitud de la lista es menor a 1 entonces retorna una lista vacia.
    if len(elementos) < 1:
        return [] 
    
    # Definimos un pivot, el cual nos va a ayudar a dividir los elementos segun su valor.
    pivot = elementos[0]

    # Definimos las sublistas para guardar los elementos a la izquerda y a la derecha.
    izquierda = []
    derecha = []

    # Utilizamos un ciclo 'for' para recorrer la lista y quitamos el primer elemento ya que lo utilizamos como pivot.
    for x in elementos[1:]:
        # Si el elemento es menor o igual a el pivot entonces lo agrega a la lista 'izquierda', si no entonces lo agrega a la lista 'derecha'
        if x <= pivot:
            izquierda.append(x)
        else:
            derecha.append(x)

    #En el return llamamos a la funcion de manera recursiva y le pasamos como parametro la lista de izquierda y derecha, a su vez
    #colocamos colocamos el pivot que definimos en el medio de la lista.
    return quicksort(izquierda) + [pivot] + quicksort(derecha)

print(quicksort(lista))

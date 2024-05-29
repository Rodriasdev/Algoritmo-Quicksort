lista=[1,9,3,6,2,0,4,8,6,5,7,10]


def quicksort(elementos):
    if len(elementos) < 1:
        return [] 
    pivot = elementos[0]
    izquierda = []
    derecha = []

    for x in elementos[1:]:
        if x <= pivot:
            izquierda.append(x)
        else:
            derecha.append(x)

    return quicksort(izquierda) + [pivot] + quicksort(derecha)

print(quicksort(lista))

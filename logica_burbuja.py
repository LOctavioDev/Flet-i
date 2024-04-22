def ordenamiento_burbuja(arr):
    nv = len(arr)
    for i in range(nv):
        for j in range(0, nv-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
    return arr

lista = [22, 56, 90 ,1, -233, 11]


print((ordenamiento_burbuja(lista)))
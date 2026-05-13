máximo = None
print('Antes:', máximo)
for itervar in [3, 41, 12, 9, 74, 15]:
    if máximo is None or itervar > máximo :
        máximo = itervar
    print('Laço:', itervar, máximo)
print('Máximo:', máximo)
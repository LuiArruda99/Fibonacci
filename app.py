#codigo para criar listas
elementos = int(input("Quantos elementos voce deseja?"))

def sequencia_lista(elementos):
    #operador matematico
    sequencia = [0]

    while len(sequencia) < elementos:
        sucessor = sequencia[-1]+1
        sequencia.append(sucessor)
    
    return sequencia

print('Sua sequencia é :',sequencia_lista(elementos))

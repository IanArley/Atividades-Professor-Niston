# Exercicio 1

def selecao(x):
    n = len(x)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if x[j] < x[min_index]:
                min_index = j

        x[i], x[min_index] = x[min_index], x[i] 
    return x    

vetor = [22, 54, 900, 1]
lista = selecao(vetor)
print(lista)

# Exercício 2

def selecao(x , y = True):
    n = len(x)
    for i in range(n):
        indice = i
        for j in range(i + 1, n):
            if y:
                if x[j] < x[indice]:
                    indice = j

            else:
                if x[j] > x[indice]:
                    indice = j

        x[i], x[indice] = x[indice], x[i]                          
    return x

vetor = [57, 99, 83, 61]
escolha = int(input("Escolha se a lista vai ser crescente ou decrescente\n1. crescente\n2. decrescente\nDigite o número da sua escolha a seguir: "))
if escolha == 1:
    y = True
    lista = selecao(vetor, y)
    print(lista)

elif escolha == 2:
    y = False
    lista = selecao(vetor, y)
    print(lista)

# Exercício 3

def selecao(x , y = True):
    n = len(x)
    for i in range(n):
        indice = i
        for j in range(i + 1, n):
            if y:
                if x[j] < x[indice]:
                    indice = j

            else:
                if x[j] > x[indice]:
                    indice = j

        x[i], x[indice] = x[indice], x[i]                          
    return x

vetor = [15, 56, 83, 47]
escolha = int(input("Escolha uma das opções a seguir\n1. Ver o elemento com menor valor no vetor\n2. Ver o elemento com maior valor no vetor\nDigite o número da sua escolha a seguir: "))
if escolha == 1:
    y = True
    lista = selecao(vetor, y)
    elementoMin = lista[0]
    print(elementoMin)

elif escolha == 2:
    y = False
    lista = selecao(vetor, y)
    elementoMax = lista[0]
    print(elementoMax)

# Exercício 4

def selecao(x):
    n = len(x)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if x[j] < x[min_index]:
                min_index = j

        x[i], x[min_index] = x[min_index], x[i] 
    return x    

vetor = [22, 22, 54, 900, 1]
lista = selecao(vetor)
SegundoMin = lista[1]
print(f"O segundo menor valor é :{SegundoMin}")

# Exercício 5

vetor = [11, 22, 22, 33]
vetorUni = []
for numero in vetor:
    if numero not in vetorUni:
        vetorUni.append(numero)
print(vetorUni)

# Exercício 6

vetor = [11, 22, 33, 44, 55]
vetorUni = []

def impar(x):
    ListaImpar = []
    for numero in x:
        if numero % 2 > 0:
            ListaImpar.append(numero)
    return ListaImpar

def par(x):
    ListaPar = []
    for numero in x:
        if numero % 2 == 0:
            ListaPar.append(numero)
    return ListaPar        
    
for numero in vetor:
    if numero not in vetorUni:
        vetorUni.append(numero)

odd = impar(vetor)
even = par(vetor)
print(f"A lista de vetores {vetorUni}, possui {len(odd)} números ímpares sendo eles: {odd} e possui também {len(even)} números pares sendo eles: {even}")

# Exercício 7

def selecao(x):
    n = len(x)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if x[j] > x[max_index]:
                max_index = j

        x[i], x[max_index] = x[max_index], x[i] 
    return x    

vetor = [500, 37, 84, 99, 99 ]
lista = selecao(vetor)
TerceiroMax = lista[2]
print(f"O segundo menor valor é: {TerceiroMax}")

# Exercício 8

vetor = [11, 22, 33, 44]
if len(vetor) % 2 == 0:
    NumMeio1 = len(vetor)//2
    NumMeio2 = NumMeio1 + 1
    mediana = (vetor[NumMeio1] + vetor[NumMeio2])/2
    MedianaReal = float(mediana)
    print(MedianaReal)

elif len(vetor) % 2 > 0:
    NumMeio = len(vetor)//2
    mediana = vetor[NumMeio]
    print(mediana)    
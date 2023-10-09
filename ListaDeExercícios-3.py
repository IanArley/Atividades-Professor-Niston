# Exercício 1

NumMaxNotas = 5
notas = []
def Media(notas):
    media = sum(notas)/len(notas)
    return media

while True:
    escolha = int(input("Escolha uma das opções a seguir:\n1. Fazer o calculo da média de um aluno;\n2. encerrar o programa;\nDigite o número referente a sua escolha: "))
    if escolha == 1:
        Nome = input("Digite o nome do aluno: ")
        while len(notas) < NumMaxNotas:
            print ("O aluno deve ter 5 notas para calcular a média")
            Nota =  float(input("Digite as notas do aluno: "))
            notas.append(Nota)
            if len(notas) == NumMaxNotas:
                mediafinal = Media(notas)
                if mediafinal >= 7:
                    print (f"O aluno {Nome} foi aprovado com a nota {mediafinal}!")

                else:
                    print (f"O aluno {Nome} foi reprovado com a nota {mediafinal} e terá que ir para a etapa de recuperação!")  
            
            elif len(notas) > NumMaxNotas:
                print ("O aluno só pode ter até 5 notas!")

    else:
        print ("Encerrando programa...")
        break

# Exercício 2

def fatorial(n):
    fator = 1
    for i in range(1, Numero + 1):
         fator *= i
    return fator      

while True:
    Numero = int(input("Digite um número inteiro para ver seu fatorial: "))
    resposta = fatorial(Numero)
    print(f"\nO fatorial do número {Numero} é {resposta}")
    escolha = input("\nCaso deseja repetir o programa digite s\nCaso deseja encerrar digite n\nDigite sua escolha a seguir: ")
    if escolha == "n":
            break

# Exercício 3

while True:
    texto = input("Digite uma palavra a seguuir para saber se é um palíndromo(se escreve igual de trás para frente): ")
    inverso = texto[::-1]
    if texto == inverso:
        print(f"\nA palavra {texto} é um palíndromo")
    else:
        print(f"\nA palavra {texto} não é um palíndromo")
    escolha = input("\nCaso deseja repetir o programa digite s\nCaso deseja encerrar digite n\nDigite sua escolha a seguir: ")
    if escolha == "n":
        break    

# Exercício 4

while True:
    Numero = int(input("Digite um número para ver a soma de seus caracteres: "))
    num = str(Numero)
    soma = 0
    for i in num:
        soma += int(i)
    print(f"\nO valor da soma dos caracteres do número {Numero} é {soma}")
    escolha = input("\nCaso deseja repetir o programa digite s\nCaso deseja encerrar digite n\nDigite sua escolha a seguir: ")
    if escolha == "n":
        break

# Exercício 5

def e_primo(numero):
    if numero <= 1:
        return False 
    if numero <= 3:
        return True  

    if numero % 2 == 0 or numero % 3 == 0:
        return False  

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False  
        i += 6

    return True

while True:
    numero = int(input("Digite um número inteiro para verificar se é primo: "))
    if e_primo(numero):
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
    escolha = input("\nCaso deseja repetir o programa digite s\nCaso deseja encerrar digite n\nDigite sua escolha a seguir: ")
    if escolha == "n":
        break

# Exercício 6

while True:
    total = 0
    vogais = ["a", "e", "i", "o", "u"]
    palavra = input("Digite uma palavra para ver quantas vogais ela possui: ")
    for i in palavra:
        if i in vogais:
            total += 1
    print (f"A quantidade de vogais presente nessa palavra é {total}")  
    escolha = input("\nCaso deseja repetir o programa digite s\nCaso deseja encerrar digite n\nDigite sua escolha a seguir: ")
    if escolha == "n":
        break 

# Exercício 7

def saude(x, y):
    imc = x/y*y
    return imc

while True:
    peso = float(input("Para fazer o calculo do seu IMC digite a seguir seu peso: "))
    altura = float(input("Agora digite a sua altura: "))
    resposta = saude(peso, altura)
    print (f"")

# Eercício 8

def Converterf(c):
    fahrenheit = (c * 1.8) + 32
    return fahrenheit

def ConverterC(f):
    celsius = (f - 32) * 5/9
    return celsius

while True:
    escolha = int(input("Escolha qual medida você deseja converter:\n1. Celsius para fahrenheit\n2. fahrenheit para celsius\nDigite o número referente a sua escolha: "))
    if escolha == 1:
        ce = float(input("Digite a temperatura em celsius: "))
        temp = Converterf(ce)
        print(f"Essa temperatura em fahrenheit é: {temp}")

    elif escolha == 2:
        fa = float(input("Digite a temperatura em fahrenheit: "))
        temp = ConverterC(fa)
        print(f"Essa temperatura em celcius é: {temp}")

    escolha2 = int(input("Para repetir o programa digite 1 e para encerrar o programa digite 2: "))
    if escolha2 == 2:
        break

# Exercício 9

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x/y

while True:
    num1 = float(input("Digite o primeiro número para ser realizado a operação: "))
    num2 = float(input("Digite o segundo número que será utilizado na operação "))
    escolha = int(input("Qual operação deseja realizar ;\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\nDigite o número referente a operação desejada: "))
    if escolha == 1:
        soma = somar(num1, num2)
        print(soma)

    elif escolha == 2:
        sub = subtrair(num1, num2)
        print(sub)

    elif escolha == 3:
        mult = multiplicar(num1, num2)
        print(mult)

    elif escolha == 4:
        div = dividir(num1, num2)
        print(div)

    escolha2 = int(input("Para repetir o programa digite 1 e para encerrar o programa digite 2: "))
    if escolha2 == 2:
        break

# Exercício 10:

sequencia = [0, 1]
limite = int(input("Digite um número que será dado como limite para que o programa de uma sequência de Fibonacci que termine o mais próximo possível anterior a esse número: "))
strlist = []

while True:
    fn = sequencia[-1] + sequencia[-2]
    if fn >= limite:
        break
    sequencia.append(fn)

strlist = list(map(str, sequencia))
print(f"Os números nessa lista até próximo do número dado como limite são: {strlist}")
#Fazer a tabuada de um número

number = int(input("Por favor, digite um número inteiro: "))
limite_tabuada = int(input("Digite o tamanho da tabuada: "))


for i in range(1, limite_tabuada + 1):
    print(f"{number} x {i} = {number * i}")


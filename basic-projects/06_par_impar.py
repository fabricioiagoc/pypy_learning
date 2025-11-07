#Verifica se o número digitado é par ou impar

while True: 
    try: 
        number = int(input("Por favor, digite um número inteiro: "))
        break
    except ValueError: 
        print("Esse não é um número válido!")

if int(str(number)[-1]) in [1, 3, 5, 7, 9]:
    print(f"{number} é impar!")
else: 
    print(f"{number} é par!")


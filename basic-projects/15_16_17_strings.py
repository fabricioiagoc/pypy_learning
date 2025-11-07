#Conversor Maiúsculas/Minúsculas - Alterne entre maiúsculas e minúsculas
#Removedor de Espaços - Remova espaços extras de um texto
#Primeiro e Último Caractere - Mostre o primeiro e último caractere

def mai_ou_min(word=str,option=int ):
    if option == 0:
        return "Não sobrou nada para o beta!"
    elif option == 1: 
        return word.upper()
    elif option == 2: 
        return word.lower()
    elif option == 3: 
        first_caractere, last_caractere = word[0], word[-1]
        return first_caractere, last_caractere
    else: 
        return "Valor invalido!"


palavra = str(input("Por favor, digite a palavra que você quer: "))
opcao = int(input("""O que você quer fazer com esta palavra: 
0 - sair do sistema
1 - Deixar tudo maiusculo
2 - Deixar tudo minúsculo 
3 - Mostrar o último e primeiro caractere
Digite: """))


print(mai_ou_min(palavra, opcao))

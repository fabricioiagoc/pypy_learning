# Contador de texto e inversor de letras

def count_letter(word):
    count = 0
    for i in word: 
        count += 1
    
    return count

def inverse_word(word): 
    listinha = []
    for i in word:
        listinha.append(i)
    
    inverso = ""
    for  i in range(count_letter(word), 0, -1):
        inverso += f"{listinha[i-1]}"

    return inverso

def palindromo(word):
    if word == inverse_word(word):
        return True
    else: 
        return False


palavra = str.lower((input("Por favor, escreva uma palavra: ")))
print(count_letter(palavra))
print(inverse_word(palavra))
print(palindromo(palavra))
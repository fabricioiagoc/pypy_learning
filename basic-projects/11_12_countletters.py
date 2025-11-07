# Contador de texto e inversor de letras

palavra = "Pythonzinho"

def count_letter(word):
    count = 0
    for i in word: 
        count += 1
    
    return count

def inverse_word(word): 
    inversed_word = ""
    for i in range(len(word), 0, -1):
        inversed_word += f"{i}"

    return inversed_word

print(count_letter(palavra))
print(inverse_word(palavra))

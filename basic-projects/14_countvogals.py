#Count how many vowels in word

word = str.lower(input("Por favor, digite uma palavra: "))
num = 0
for i in ["a","e", "i", "o", "u"]:
    num += word.count(i)

print(f"There are {num} vowels.")

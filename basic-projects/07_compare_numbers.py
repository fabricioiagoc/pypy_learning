#I will compare three numbers and say which is greatest

def compare_numbers(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else: 
        return n3

numbers = []
for i in range(3): 
    numbers.append(float(input(f"Digite o {i}º número: ")))
    print(numbers)


print(f"n1 is {numbers[0]},  n2 is {numbers[1]}, n3 is {numbers[2]}")
print(f"The greatest number is {compare_numbers(numbers[0], numbers[1], numbers[2] )}")

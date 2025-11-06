#Calculate the IMC of a person

def calculate_imc(w, h):
    imc = w / h**2
    return imc

def catch_valid_number(message="Please, enter a rational number: ", type_number=float):
    while True:
        try:
            number = type_number(input(message))
            break
        except ValueError: 
            print("That is not a valid number!")
    
    return number

weight = catch_valid_number("Please, enter your kg: ")
height = catch_valid_number("Please, enter your height in meters: ")
imc = calculate_imc(weight, height)

#Categoria de peso
if imc <= 18.5: 
    categoria = "Abaixo do peso"
elif imc > 18.5 and imc < 25:
    categoria = "peso normal"
elif imc >= 25 and imc < 30: 
    categoria = "Sobrepeso"
elif imc >= 30 and imc < 35:
    categoria = "Obesidade grau 1"
elif imc >= 35 and imc < 40:  
    categoria = "Obesidade grau 2"
else: 
    categoria = "Obesidade grau 3"


print(f"Your IMC is {imc:.2f} and your category is {categoria}")

#A program that ask your name and your age. Later, its concatenate and print

#Inputs
name = input("Whats is your name?")
while True: #Get the age and check if its a valid number
    try:
        age = int(input("How old are you? "))
        break
    except ValueError: 
        print("Please, write a valid age(0 - 120).")

#Output formatted
print(f"You are {name} and you are {age} years old.")

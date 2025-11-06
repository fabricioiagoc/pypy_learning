# Turn celcius to farenheit
#Formula: (0 °C × 9/5) + 32 = 32 °F


#Testing using a function
def celcius_to_farenheit(celcius = 0):
    """
        Transform a temperature in celcius to farenheit

        Parameters: 
            celcius (float)

        Return:
            float number.
    """

    farenheit = (celcius * 9/5) + 32
    return farenheit


#Testing using a lambda
cel_farenheit = lambda celcinhus: (celcinhus * 9/5) + 32 


#Main
while True: #Get the celcius temperature from user and verify if it's a valid temperatura
    try:
        celcius_temperature = float(input("Write the temperature in Celcius: "))
        break
    except ValueError:
        print("Write a number, please.")

print(f"The temperate in celcius if {celcius_to_farenheit(celcius_temperature)}") # Using def
print(f"The temperate in celcius if {cel_fareheit(cel_farenheit)}") # Using Lambda

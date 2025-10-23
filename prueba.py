def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 != 0:
        leap = True
        print("Año bisiesto1")
    elif year % 400 == 0:
        leap = True
        print("Año bisiesto2")
    elif year % 100 == 0:
        leap = False
        print("No es un año bisiesto")
    
    
    return leap


print(is_leap(2100))
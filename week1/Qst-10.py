# Temperature checking 
TEMP_cel = int(input("Enter your temperature in Celsius : "))
TEMP_Far = TEMP_cel * (9/5) + 32   # converting celsius to fahrenheit
print(TEMP_Far)
if TEMP_cel < 0 :
    print("Very cold! Wear thick jacket")
else:
    if 0 <= TEMP_cel <= 15 :
        print( "Cold. Wear jacket")
    else:
        if 16 <= TEMP_cel <25 :
            print( "Nice weather")
        else:
             if TEMP_cel == 25 :
               print( "Hot! Stay hydrated") # end here as no other condition is given 
               
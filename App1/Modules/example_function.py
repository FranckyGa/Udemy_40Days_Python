T_gas = 100
T_solid = 0

def check_temp(temperature):
    temp = float(temperature)

    if temp >= T_gas:
        result ="Gas"
    elif temp <= T_solid:
        result = "Solid"
    else:
        result = "liquid"
    
    print(result)
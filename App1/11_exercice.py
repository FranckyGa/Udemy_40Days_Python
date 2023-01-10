#Exercice 1:
def get_max(values):
    max_grade = [float(i) for i in values]
    return print(max(max_grade))

grades = [9.6, 9.2, 9.7]
get_max(grades)

#Correction
def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    return maximum
    
print(get_max())

#Exercise 2:
def get_min(values):
    grade = [float(i) for i in values]
    return print(min(grade))

grades = [9.6, 9.2, 9.7]
get_min(grades)

#Correction 2:
def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    message = f"Max: {maximum}, Min: {minimum}"
    return message
    
print(get_max())
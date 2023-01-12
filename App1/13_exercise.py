#Exercice 1 :
def age_user(year_of_birth,current_year = 2023):
    age = int(current_year) - int(year_of_birth) 
    if age > 120:
        print("You seem very old. Please verify the inputs.")
    return age

date_birth = input("What is your year of birth? ")
age = age_user(date_birth)
print(age)

#Exercise 4:
#mary,johny,toto
name_list = input("Enter names separated by comma (no spaces): ")
name_list = name_list.split(",")
print(len(name_list))

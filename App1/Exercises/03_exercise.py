#Exercise 1:
prompt_user = input("Where are you from?")

match prompt_user:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Halo")

#Exercise 2 :
ingredients = ["john smith", "sen plakay", "dora ngacely"]

for name in ingredients:
    print(name.title())
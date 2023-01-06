todos = []

while True :
    user_action = input("Type add or show or exit:")
    user_action = user_action.strip()   #.strip removes spaces

    match user_action:
        case "add":
            todo = input("Enter a todo :")
            todos.append(todo)
        case "show" | "display":                # |   --> and
            for item in todos:
                item = item.title()             #title   --> capital letter on each word
                print(item)
        case "exit":
            break
        case _:          #_     convention to say something else but can be repalce by a random variable liek "whatever" or "tootoot" or else
            print("Please enter a known comment")

print("Bye!")

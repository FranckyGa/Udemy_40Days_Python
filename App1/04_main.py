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
        
        case "edit":
            number = int(input("Number of the todo to edit:"))          # int --> convert string to interger (input is always string value)
            number = number - 1
            new_todo = input("Enter a new todo:")
            todos[number] = new_todo

        case "exit":
            break
       
        case _:          #_     convention to say something else but can be repalce by a random variable liek "whatever" or "tootoot" or else
            print("Please enter a known comment")

print("Bye!")
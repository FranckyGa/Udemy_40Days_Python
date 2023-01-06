todos = []

while True :
    user_action = input("Type add, show, complete or exit: ")
    user_action = user_action.strip()   #.strip removes spaces

    match user_action:
        case "add":
            todo = input("Enter a todo:")
            todos.append(todo)
        
        case "show" | "display":                    # |   --> and
            for index, item in enumerate(todos):    # enumerate --> function to list items 
                item = item.title()                 #title   --> capital letter on each wordud
                row = f"{index + 1}. {item}"        #f"{variable}aijiojoj{variable}"   -> remove spaces    "0 . Clean"  to "0.Clean"
                print(row)
        
        case "edit":
            number = int(input("Number of the todo to edit: "))          # int --> convert string to interger (input is always string value)
            number = number - 1
            new_todo = input("Enter a new todo:")
            todos[number] = new_todo

        case 'complete' :
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)                           #.pop   --> remove an item in a list // can use .remove
        
        case "exit":
            break
       
        case _:          #_     convention to say something else but can be repalce by a random variable liek "whatever" or "tootoot" or else
            print("Please enter a known comment")

print("Bye!")
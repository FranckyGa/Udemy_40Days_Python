user_prompt = "Enter a todo :"

todos = []

while True :
    todo = input(user_prompt)
    
    #firist letter in capital
    todo.capitalize()
    todos.append(todo)
    print(todos)

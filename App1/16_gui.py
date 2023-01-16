from Modules import functions as func
import PySimpleGUI as sg              #used to create interfaces  // as sg --> allow to call PySimpleGUI with another word defined (like sg)

#Build feature of window and store them in variables
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")        #key --> name button and store value under "key"
add_button = sg.Button("Add")
list_box = sg.Listbox(values = func.get_todos(), key = "todos",
                         enable_events = True, size = [45,10])
edit_button = sg.Button("Edit")

#Create window with features defined above
window = sg.Window('My To-do App',
                     layout=[[label], [input_box, add_button],[list_box, edit_button]],
                     font = ('Helvetica',16))           #layout=[[label, input_box]]  --> display on one row instead of 2

while True:
    event, values = window.read()           #display window created above
    print(event)
    print(values)
    print(values['todos'])

    match event:
        case "Add":
            todos = func.get_todos()
            new_todo =  values['todo'] + '\n'         #input by user (todo  = input box defined above)
            todos.append(new_todo)
            func.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = func.get_todos()
            index = todos.index(todo_to_edit)       #get index in the list of the item we want to replace
            todos[index] = new_todo
            func.write_todos(todos)
            window['todos'].update(values=todos)    #refresh the list after clicking on edit button
        
        case 'todos':
            window['todo'].update(value = values['todos'])

        case sg.WIN_CLOSED:
            break

window.close()
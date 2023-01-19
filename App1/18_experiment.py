from Modules import functions as func
import PySimpleGUI as sg              #used to create interfaces  // as sg --> allow to call PySimpleGUI with another word defined (like sg)
import time

sg.theme("Black")

#Build feature of window and store them in variables
label_clock = sg.Text('', key = 'clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")        #key --> name button and store value under "key"
add_button = sg.Button(key = "Add", size = 2, image_source = "06_files/add.png", mouseover_colors = "LightBlue", tooltip = "Add Todo")       #Put image as button
list_box = sg.Listbox(values = func.get_todos(), key = "todos",
                         enable_events = True, size = [45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit", size = 10)

#Create window with features defined above
window = sg.Window('My To-do App',
                     layout=[[label_clock],
                     [label], [input_box, add_button],
                     [list_box, edit_button, complete_button],
                     [exit_button]],
                     font = ('Helvetica',16))           #layout=[[label, input_box]]  --> display on one row instead of 2

while True:
    event, values = window.read(timeout = 2000)           #display window created above and time /// timeout = 10 --> run code every 10 milliseconds
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    
    match event:
        case "Add":
            todos = func.get_todos()
            new_todo =  values['todo'] + '\n'         #input by user (todo  = input box defined above)
            todos.append(new_todo)
            func.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = func.get_todos()
                index = todos.index(todo_to_edit)       #get index in the list of the item we want to replace
                todos[index] = new_todo
                func.write_todos(todos)
                window['todos'].update(values=todos)    #refresh the list after clicking on edit button
            
            except IndexError:
                sg.popup("Select an item first", font = ("Helvetica", 16))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = func.get_todos()
                todos.remove(todo_to_complete)
                func.write_todos(todos)
                window["todos"].update(values = todos)
                window["todo"].update(value = "")           #update output and clean input text
        
            except IndexError: 
                sg.popup("Select an item first", font = ("Helvetica", 16))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value = values['todos'])

        case sg.WIN_CLOSED:
            break                                   #exit() function stops the program completely // break stops only the loop

window.close()
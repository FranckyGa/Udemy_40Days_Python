from Modules import functions
import PySimpleGUI as sg              #used to create interfaces  // as sg --> allow to call PySimpleGUI with another word defined (like sg)

#Build feature of window and store them in variables
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

#Create window with features defined above
window = sg.Window('My To-do App', layout=[[label], [input_box, add_button]])           #layout=[[label, input_box]]  --> display on one row instead of 2
window.read()           #display window created above
window.close()
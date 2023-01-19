#Exercise : create app feet convertor into meters

import PySimpleGUI as sg
from Modules import bonus_function as func

sg.theme("Black")

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key = "ft")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key = "in")

convert_button = sg.Button("Convert")
output_label = sg.Text(key = "output", text_color = "green")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor", 
                    layout=[[label1, input1],
                        [label2, input2],
                        [convert_button, output_label],
                        [exit_button]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            value_conv = func.convert(values["ft"], values["in"])
            window["output"].update(value = str(value_conv) + "m")
        case "Exit":
            break
        case sg.WIN_CLOSED:             #close windows with cross
            break

window.close()




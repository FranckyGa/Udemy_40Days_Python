import PySimpleGUI as sg
from Modules import zip_extractor as zip


sg.theme("Black")

#Features and buttons of frontEnd
label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key = "archive")              #FileBrowse   --> to select only one file // <> FilesBrowse --> multiples files

label2 = sg.Text("Select dest Dir: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key = "folder")

compress_button = sg.Button("Extract")
output_label = sg.Text(key = "output", text_color = "green")

#Widget creation (interface)
window = sg.Window("Archive Extractor", 
                    layout=[[label1, input1, choose_button1],
                        [label2, input2, choose_button2],
                        [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event,values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    zip.extract_archive(archivepath, dest_dir)
    window["output"].update(value = "Extraction completed !")

window.close()


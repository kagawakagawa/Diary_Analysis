import pysimpleGUI as sg

sg.theme('DarkBrown2')

layout =[[sg.Text('メモ内容')]]

window = sg.Window('メモアプリ_ver.1.0', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
    
window.close()

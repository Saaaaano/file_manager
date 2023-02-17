import PySimpleGUI as sg

layout = [
    [sg.Text('文字の色が変わります', key='-Txt-')],
    [sg.Btn('文字色を赤に変更', key='-Btn_Red-')],
    [sg.Btn('文字色を青に変更', key='-Btn_Blue-')]
]

window = sg.Window('WidgetChangeEvent', layout, size=(300,150), finalize=True)

while True:
    event, values = window.read()

    if event == '-Btn_Red-':
        window['-Txt-'].Update(text_color='Red')

    if event == '-Btn_Blue-':
        window['-Txt-'].Update(text_color='Blue')

        # 標準的 な 色 名：' white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta'
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()

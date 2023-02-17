import PySimpleGUI as sg

layout = [
    [sg.Input(text_color='blue', password_char='¥', tooltip='ログインに必要です')],
    [sg.Text('-'*100)],
    [sg.Input(text_color='Red', password_char='秘密', tooltip='ログインに必要です')]
]

window = sg.Window('Input', layout, size=(300, 150), finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()

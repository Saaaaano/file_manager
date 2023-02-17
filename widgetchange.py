import PySimpleGUI as sg

layout = [
    [sg.Input(key='-Input-', enable_events=True)],  # enable_events=Trueでウィジェットに変更が加えられるたびにイベントを発生させる。
]

window = sg.Window('WidgetChangeEvent', layout, size=(300,150), finalize=True)

while True:
    event, values = window.read()

    if event == '-Input-':
        sg.popup('文字が入力されました')
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
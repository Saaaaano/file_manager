import PySimpleGUI as sg

layout = [
    [sg.Text('オリジナルテキスト')],
    [sg.Text('-'*100)],
    [sg.Text('テキスト1', pad=(50,0), visible=False)],  # visibleでテキストの表示・非表示を切り替える
    [sg.Text('-'*100)],
    # [sg.Text('テキスト2', pad=(150, 100), visible=False)],
    [sg.Button('button1', key='-Btn1-')],
    [sg.Text('-'*100)],
    # [sg.Text('テキスト3', pad=((50, 200), (0, 100)), visible=True)],
    [sg.Button('button2', key='-Btn2-', disabled=True, disabled_button_color=('red',''))]
]

window = sg.Window('ウィジェット位置の設定', layout, finalize=True)

while True:
    event, value = window.read()

    if event == '-Btn1-':
        window['-Btn2-'].Update(disabled=False)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()

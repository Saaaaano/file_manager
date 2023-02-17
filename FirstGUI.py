from pathlib import Path
import PySimpleGUI as sg

# sg.popup('最初のGUIアプリ')

layout = [
    [sg.Text(text="表示させたい文字列", text_color='#000000')],
    [sg.Input(key='-Input-')],  # イベントの起点もしくはイベントの跡に変更を加えたいものにはkeyを割り当てる
    [sg.Button('ボタン', key='-Btn-')]  
]

window = sg.Window('FirstGUI', layout, size=(300,150), finalize=True)

while True:
    event, values = window.read()   #イベントの入力を待つ

    if event == '-Btn-':    # ボタンが押された
        message = values['-Input-']
        sg.popup(message)
        break   # whileループを中断=アプリの終了
    if event == sg.WIN_CLOSED or event == 'Exit':   # windowをxボタンで閉じた
        break   # これを定義しておかないとエラーする

window.close()
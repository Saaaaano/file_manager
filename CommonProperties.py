import PySimpleGUI as sg

layout = [
    [sg.Text('オリジナルテキスト')],
    [sg.Text('テキスト1', text_color='#008000', font=('游ゴシック', 20))],
    [sg.Text('テキスト2', text_color='white', font=('游ゴシック', 30))],
    [sg.Text('テキスト3', text_color='#ff0000', font=('游ゴシック', 40))],
]

window = sg.Window('テキストカラーの設定', layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
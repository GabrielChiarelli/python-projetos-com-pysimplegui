import PySimpleGUI as psg

layout = [
    [psg.Input(key='-ENTRADA-'), psg.Spin(['milímetro - centímetro', 'centímetro - milímetro', 'milímetro - metro', 'metro - milímetro', 'centímetro - metro', 'metro - centímetro'], key='-UNIDADES-'), psg.Button('Converter', key='-CONVERTER-')],
    [psg.Text('Resultado: ', key='-RESULTADO-')],
]

janela = psg.Window('Conversor de Medidas em Python (PySimpleGUI) - Gabriel Chiarelli - 09/05/2022', layout, size=(600, 70))

def mmParaCm(valor):
    res = round(valor / 10, 15)
    if valor == 1.0:
        janela['-RESULTADO-'].update(f'{valor} milímetro são {res} centímetros.')
    else:
        janela['-RESULTADO-'].update(f'{valor} milímetros são {res} centímetros.')


def cmParaMm(valor):
    res = round(valor * 10, 15)
    if valor == 1.0:
        janela['-RESULTADO-'].update(f'{valor} centímetro é {res} milímetros.')
    else:
        janela['-RESULTADO-'].update(f'{valor} centímetros é {res} milímetros.')
    if res == 1.0:
        janela['-RESULTADO-'].update(f'{valor} centímetros é {res} milímetro.')


def mmParaM(valor):
    res = round(valor / 1000, 15)
    if res == 1.0:
        janela['-RESULTADO-'].update(f'{valor} milímetros são {res} metro.')
    else:
        janela['-RESULTADO-'].update(f'{valor} milímetros são {res} metros.')


def mParaMm(valor):
    res = round(valor * 1000, 15)
    if valor == 1.0:
        janela['-RESULTADO-'].update(f'{valor} metro são {res} milímetros.')
    else:
        janela['-RESULTADO-'].update(f'{valor} metros são {res} milímetros.')
    if res == 1.0:
        janela['-RESULTADO-'].update(f'{valor} metros são {res} milímetro.')


def cmParaM(valor):
    res = round(valor / 100, 15)
    if res == 1.0:
        janela['-RESULTADO-'].update(f'{valor} centímetros são {res} metro.')
    else:
        janela['-RESULTADO-'].update(f'{valor} centímetros são {res} metros.')


def mParaCm(valor):
    res = round(valor * 100, 15)
    if valor == 1:
        janela['-RESULTADO-'].update(f'{valor} metro são {res} centímetros.')
    else:
        janela['-RESULTADO-'].update(f'{valor} metros são {res} centímetros.')
    if res == 1.0:
        janela['-RESULTADO-'].update(f'{valor} metros são {res} centímetro.')


while True:
    event, values = janela.read()

    if event == psg.WINDOW_CLOSED:
        break

    if event == '-CONVERTER-':
        valor_entrada = values['-ENTRADA-']
        if round(valor_entrada.isnumeric(), 2) or '.' in valor_entrada and valor_entrada != '.':
            if values['-UNIDADES-'] == 'milímetro - centímetro':
                mmParaCm(float(valor_entrada))
            elif values['-UNIDADES-'] == 'centímetro - milímetro':
                cmParaMm(float(valor_entrada))
            elif values['-UNIDADES-'] == 'milímetro - metro':
                mmParaM(float(valor_entrada))
            elif values['-UNIDADES-'] == 'metro - milímetro':
                mParaMm(float(valor_entrada))
            elif values['-UNIDADES-'] == 'centímetro - metro':
                cmParaM(float(valor_entrada))
            elif values['-UNIDADES-'] == 'metro - centímetro':
                mParaCm(float(valor_entrada))

        else:
            janela['-RESULTADO-'].update('Por favor, digite um número.')

janela.close()

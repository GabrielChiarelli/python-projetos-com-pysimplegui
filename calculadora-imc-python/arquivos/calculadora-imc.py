import PySimpleGUI as psg

layout = [
    [psg.Text('Calculadora IMC')],
    [psg.Text('Sua altura (ex: 1.65):')],
    [psg.Input(key='-ALTURA-')],
    [psg.Text('Seu peso (ex: 50.2):')],
    [psg.Input(key='-PESO-')],
    [psg.Button('Calulcar IMC', key='-CALCULAR-')],
    [psg.Text('', key='-RESULTADO-')],
    [psg.Text('\n\n\n\n\n\n\n\n\n\nGabriel Chiarelli - 17/05/2022', key='-TABELA-')]
]

janela = psg.Window('Calculadora IMC em Python (PySimpleGUI)', layout, size=(400, 380))

def calcular(alt, peso):
    res = peso / (alt**2)
    situacao = ''

    if res < 18.5:
        situacao = 'Excesso de Magreza'
    elif res < 25:
        situacao = 'Peso Normal'
    elif res < 30:
        situacao = 'Excesso de Peso'
    elif res < 35:
        situacao = 'Obesidade Grau 1'
    elif res < 40:
        situacao = 'Obesidade Grau 2'
    else:
        situacao = 'Obesidade Grau 3'

    janela['-RESULTADO-'].update(f'Seu IMC é {res:.2f}\nE você está com {situacao}')
    janela['-TABELA-'].update('''
Menor que 18.5      \t->  \tExcesso de Magreza
Entre 18.5 e 24.9   \t->  \tPeso Normal
Entre 25.0 e 29.9   \t->  \tExcesso de Peso
Entre 30.0 e 34.9   \t->  \tObesidade Grau 1
Entre 35.0 e 39.9   \t->  \tObesidade Grau 2
Maior que 40.0      \t\t->  \tObesidade Grau 3
\n\nGabriel Chiarelli - 17/05/2022''')


while True:
    event, values = janela.read()

    if event == psg.WINDOW_CLOSED:
        break

    if event == '-CALCULAR-':
        valor_altura = values['-ALTURA-']
        valor_peso = values['-PESO-']

        if ',' in valor_altura:
            valor_altura = valor_altura.replace(',', '.')
        if ',' in valor_peso:
            valor_peso = valor_peso.replace(',', '.')

        if valor_altura.isnumeric() and valor_peso.isnumeric() or valor_altura.isnumeric() and valor_peso.isnumeric() and '.' in valor_altura or '.' in valor_peso and valor_altura != '.' or valor_peso != '.':
            if len(valor_altura) == 3:
                valor_altura = float(valor_altura) / 100
                #valor_altura = valor_altura[0] + '.' + valor_altura[1] + valor_altura[2]
            try:
                calcular(float(valor_altura), float(valor_peso))
            except:
                janela['-RESULTADO-'].update('Por favor, digite um valor válido.')
        else:
            janela['-RESULTADO-'].update('Por favor, digite um valor válido.')

janela.close()

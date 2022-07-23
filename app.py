from consulta import *
from interface_grafica import *

# ABRE A JANELA INICIAL DO PROGRAMA
tela_ini()
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break
# ABRE A JANELA PARA PESQUISA DE DDD
    if event == 'DDD':
        tela_ddd()
        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                exit()

            elif event == 'Voltar':
                window.close()
                break

            elif event == 'Consultar':
                try:
                    estado = consulta_ddd(values['ddd'])['state']
                    cidades = consulta_ddd(values['ddd'])['cities']
                    window['cidades'].update('')
                    for k, v in estados.items():
                        if k == estado:
                            window['estado'].update(v)

                    for i in consulta_ddd(values['ddd'])['cities']:

                        print(i.title())
                except:
                    sg.Popup('Verifique se o campo "DDD" foi preenchido corretamente\n'
                             '                       ou se está conectado a internet', font='arial 12', title='ERRO')

    # ABRE A JANELA PARA PESQUISA DE CEP
    elif event == 'CEP':
        tela_cep()
        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                exit()

            elif event == 'Consultar':
                try:
                    logradouro = consulta_cep(values['cep'])['logradouro']
                    bairro = consulta_cep(values['cep'])['bairro']
                    localidade = consulta_cep(values['cep'])['localidade']
                    uf = consulta_cep(values['cep'])['uf']
                    ibge = consulta_cep(values['cep'])['ibge']
                    ddd = consulta_cep(values['cep'])['ddd']

                    window['logradouro'].update(logradouro)
                    window['bairro'].update(bairro)
                    window['localidade'].update(localidade)
                    window['uf'].update(uf)
                    window['ibge'].update(ibge)
                    window['ddd'].update(ddd)
                except:
                    sg.Popup('Verifique se o campo "CEP" foi preenchido corretamente\n'
                             '                       ou se está conectado a internet', font='arial 12', title='ERRO')

            elif event == 'Voltar':
                window.close()
                break











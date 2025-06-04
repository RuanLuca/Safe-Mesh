import os

Locais = []

print('Inicio do App')

def nome():

    print('''
███████╗ █████╗ ███████╗███████╗    ███╗   ███╗███████╗███████╗██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝    ████╗ ████║██╔════╝██╔════╝██║  ██║
███████╗███████║█████╗  █████╗      ██╔████╔██║█████╗  ███████╗███████║
╚════██║██╔══██║██╔══╝  ██╔══╝      ██║╚██╔╝██║██╔══╝  ╚════██║██╔══██║
███████║██║  ██║██║     ███████╗    ██║ ╚═╝ ██║███████╗███████║██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝    ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
''')

def voltar_ao_menu_principal():
    input('\nPressione a tecla Enter para voltar ao início! ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def exibir_opções():
    print('Escolha uma opção: ')
    print('\n1 - Cadastrar local seguro')
    print('2 - Encontar locais seguros')
    print('3 - Chamar ajuda')

def escolha_de_opções():
    try:
        opcao_escolhida = int(input('\nDigite a opção desejada: '))

        if opcao_escolhida == 1 :
            cadastrar_local_seguro()
        elif opcao_escolhida == 2:
            encontrar_locais_seguros()
        elif opcao_escolhida == 3:
            chamar_ajuda()
        else:
            print('Valor invalido!')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.')
        voltar_ao_menu_principal()

def cadastrar_local_seguro():

    exibir_subtitulo('cadastrar local seguro')

    while True:
        cidade = input('Digite a cidade: ')
        if all(c.isalpha() or c.isspace() for c in cidade) and cidade.strip() != "":
            break
        else:
            print('Cidade invalida. Use apenas letras e espaços.')

    while True:
        bairro = input('Digite o bairro: ')
        if all(c.isalpha() or c.isspace() for c in bairro) and bairro.strip() != "":
            break
        else: print('Bairro invalido. Use apenas letras e espaços.')

    while True:
        rua = input('Digite a rua (sem o numero): ')
        if all(c.isalpha() or c.isspace() for c in rua) and rua.strip() != "":
            break
        else:
            print('Rua invalida. Use apenas letras e espaços.')

    while True:
        try:
            numero = int(input('Digite o número do local: '))
            if numero > 0:
                break
            else:
                print('Número deve ser um valor positivo.')
        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')

    while True:
        try: 
            capacidade = int(input('Digite a capacidade de pessoas no local: '))
            if capacidade > 0:
                break
            else:
                print('Capacidade deve ser um número positivo.')
        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')

    Locais.append(f'Local seguro cadastrado: Cidade: {cidade}, Bairro: {bairro}, Rua: {rua} n.{numero}, Capacidade: {capacidade}')
    print()
    print(f'Local seguro cadastrado com sucesso! Cidade: {cidade}, Bairro: {bairro}, Rua: {rua} n.{numero}, Capacidade: {capacidade}')

    voltar_ao_menu_principal()

def encontrar_locais_seguros():
    exibir_subtitulo('Encontrar locais seguros')

    if not Locais:
        print('Nenhum local seguro encontrado.')
        voltar_ao_menu_principal()
        return
    else:
        print('Locais seguros cadastrados:')
        print()
        for local in Locais:
            print(local)

    voltar_ao_menu_principal()

def chamar_ajuda():
    exibir_subtitulo('Chamar ajuda')

    print('1 - Chamar a polícia')
    print('2 - Chamar os bombeiros')

    while True:
        try:
            ajuda = int(input('\nDigite a opção desejada:'))

            if ajuda < 1 or ajuda > 2:
                print('Opção inválida! Por favor, escolha 1 ou 2.')
                continue

            if ajuda == 1:
                os.system('cls')
                print('Rastreando seu local...')
                print('\nLocal encontrado!')
                print('\nChamando a polícia...')
                print('\nA policia está a caminho!')
            elif ajuda == 2:
                os.system('cls')
                print('Rastreando seu local...')
                print('\nLocal encontrado!')
                print('\nChamando os bombeiros...')
                print('\nOs bombeiros estão a caminho!')
            else:
                print('Opção inválida!')

            voltar_ao_menu_principal()    
        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')

            voltar_ao_menu_principal()


def main():
    os.system('cls')
    nome()
    exibir_opções()
    escolha_de_opções()

if __name__ == '__main__':
    main()

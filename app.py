import os

nadadores = []

def exbir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print('')

def retorna_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()

def mostra_titulo():
    print('''

    ℂ𝕒𝕥𝕒𝕣𝕒𝕥𝕒𝕤 ℕ𝕒𝕥𝕒𝕔̧𝕒̃𝕠

    ''')

def mostra_escolhas():
    print('1. Cadastro de nadadores')
    print('2. Listar nadadores')
    print('3. Ativar nadador')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_nadadores()
        elif opcao_escolhida == 2:
            mostrar_nadadores()
        elif opcao_escolhida == 3:
            print('Ativar/desativar nadador')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_nadadores():
    exbir_subtitulo('Cadastrar Nadadores')

    nome_nadador = input('Digite o nome do nadador: ')
    nadadores.append(nome_nadador)
    print(f'{nome_nadador} foi adicionado(a) aos atletas de Foz do Iguaçu')

    retorna_menu_principal()

def mostrar_nadadores():
    exbir_subtitulo('Listar nadadores')

    for nadador in nadadores:
        print(f' - {nadador}')
    
    retorna_menu_principal()


def finalizar_programa():
    os.system('clear')
    print('Finalizando programa')

def opcao_invalida():
    print('Esse caracter não é permitido')
    retorna_menu_principal()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()
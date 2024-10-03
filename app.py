import os

nadadores = [{'nome':'Teotonio', 'categoria':'Borboleta', 'ativo':True},
             {'nome':'Anilda', 'categoria':'Costas','ativo':True},
             {'nome':'Osmar', 'categoria':'Peito','ativo':False},
             {'nome':'Ana', 'categoria':'Livre', 'ativo':True}]

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
            alterar_estado_nadador()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_nadadores():
    exbir_subtitulo('Cadastrar Nadadores')

    nome_nadador = input('Digite o nome do nadador: ')
    categoria = input(f'Qual o estilo que o(a) {nome_nadador} nada')
    dados_nadador = {'nome': nome_nadador, 'categoria':categoria, 'ativo':True}
    nadadores.append(dados_nadador)
    print(f'{nome_nadador} foi adicionado(a) aos atletas de Foz do Iguaçu')

    retorna_menu_principal()

def mostrar_nadadores():
    exbir_subtitulo('Listar nadadores')

    for nadador in nadadores:
        nome_nadador = nadador['nome']
        categoria = nadador['categoria']
        ativo = nadador['ativo']
        print(f' - {nome_nadador} | {categoria} | {ativo}')
    
    retorna_menu_principal()

def alterar_estado_nadador():
    exbir_subtitulo('Cadastrar Nadadores')
    nome_nadador = input('Qual nadador(a) você gostaria de mudar o status?')
    nadador_encontrado = False

    for nadador in nadadores:
        if nome_nadador == nadador['nome']
            nadador_encontrado = True
            nadador['ativo'] = not nadador['ativo']
            mensagem = f'O {nome_nadador} foi ativado com sucesso' if nadador['ativo'] else f' O(A) {nome_nadador} foi desativado'

            print(mensagem)
    if not nadador_encontrado:
        print('O nadador ou nadadora não existe')

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
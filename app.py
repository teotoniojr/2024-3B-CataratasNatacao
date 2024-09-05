print("""

ℂ𝕒𝕥𝕒𝕣𝕒𝕥𝕒𝕤 ℕ𝕒𝕥𝕒𝕔̧𝕒̃𝕠

""")

print('1. Cadastro de nadadores')
print('2. Listar nadadores')
print('3. Ativar nadador')
print('4. Sair da aplicação')

opcao_escolhida = int(input('Escolha uma opção: '))
print('Você escolheu a opção: ', opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar nadador')
elif opcao_escolhida == 2:
    print('Listar Nadadores')
elif opcao_escolhida == 3:
    print('Ativar/desativar nadador')
else:
    print('Saindo da aplicação')
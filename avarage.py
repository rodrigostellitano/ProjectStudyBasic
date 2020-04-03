
"Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. "
# Menu
# Inserir aluno
# Deletar aluno
# adicionar nota
# excluir nota
# media da turma

import sys, os

# Menu
def main_menu():
    print("Bem vindo,\n")
    print("Escolha as opções:")
    print("1. Inserir aluno")
    print("2. Deletar aluno")
    print("3. Listar aluno")
    print("4. Inserir Nota")
    print("5. Média")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return


# Executa o Menu1
def exec_menu(choice):
    os.system('cls')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:

            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


# Inserir o aluno
def inserir_aluno():
    os.system('cls')

    global indice_aluno

    indice_aluno = len(lista_aluno.keys())

    nome = input("Digite o nome do aluno:")
    lista_aluno[indice_aluno] = [nome]
    lista_aluno[indice_aluno].insert(1,'A')

    print("Aluno inserido")
    print("O nome do aluno incluido é: {} e o seu ID é: {}".format(nome, indice_aluno))
    #indice_aluno = indice_aluno + 1

    choice_inserir_aluno = input("Deseja adicionar mais aluno?")
    choice_inserir_aluno.lower()
    # Poderia criar a rotina toda de menu novamente, mas decidi não

    if choice_inserir_aluno == 's':
        inserir_aluno()
    if choice_inserir_aluno == 'n':
        main_menu()
    else:
        print("Escolha invalida, retornando ao Menu Inicial")
        main_menu()


# Listar Aluno
def listar_aluno():
    os.system('cls')
    list_status = []

    status = input('Deseja listar os alunos (A)tivos ou (I)nativos?')

    for i in lista_aluno.keys():
        list_status.append(lista_aluno[i][1])

    if status.upper() in list_status:
        listar_aluno_total(status)
    else:
        res = "Ativos" if status.upper() == 'A' else "Inativos"
        print("A lista não possui alunos " + res)

    input("Pressione <enter> para continuar")
    main_menu()

# Deletar Aluno
def deletar_aluno():
    listar_aluno_total('A')
    list_status = []

    for i in lista_aluno.keys():
        list_status.append(lista_aluno[i][1])

    if 'A' not in list_status:
        print("Não possui alunos ativos no Sistema para Deletar")
        main_menu()

    id_delet = input('Escolha uma ID - CASO NÃO DESEJE DELETAR NINGUÉM DIGITE Z ')

    if id_delet.lower() == 'z':
        main_menu()


    if int(id_delet) in lista_aluno.keys() and lista_aluno[int(id_delet)][1] == 'A':
        lista_aluno[int(id_delet)][1] = 'I'
    else:
        print('ID NÃO LOCALIZADA')
        deletar_aluno()

    input("Digite <enter> para continuar")
    main_menu()

# Inserir nota
#LAYOUT {'id': ['nome', stats, 'nota1', 'nota2', 'nota3', 'media', ]}

def inserir_nota():
    os.system('cls')
    #list_status = []
    listar_aluno_total('A')

    id_aluno = input("Selecione o ID que deseja adicionar a nota - CASO NÃO DESEJE INSERIR NOTA DIGITE Z ")

    if id_aluno.isnumeric():
        id_aluno = int(id_aluno)

        if id_aluno in lista_aluno.keys() and lista_aluno[id_aluno][1] == "A":
            n1 = float(input("Insira a nota 1: "))
            lista_aluno[id_aluno].insert(2, n1)
            n2 = float(input("Insira a nota 2: "))
            lista_aluno[id_aluno].insert(3, n2)
            n3 = float(input("Insira a nota 3: "))
            lista_aluno[id_aluno].insert(4, n3)
            media = (n1 + n2 + n3) / 3
            lista_aluno[int(id_aluno)].insert(5, media)

            resultado = format(lista_aluno[id_aluno][5],'.2f')
            print("Sua média é: " + str(resultado))
            input("Pressione <Enter> para continuar")
            inserir_nota()
        else:
            print("Aluno Inativo, tente outro ID")
            input("Pressione <Enter> para voltar")
            inserir_nota()
            #teste
    elif id_aluno.lower() == 'z':
        main_menu()

#Opção de listar alunos

def listar_aluno_total(status):
    if len(lista_aluno) == 0:
        print('Lista Vazia!')
        main_menu()


    for key in lista_aluno.keys():

        if lista_aluno[key][1] == status.upper():
            print(str(key) + '- ' + lista_aluno[key][0])


def media():

    listar_aluno_total("A")


    porcentagem_media = input("Informe a media (1 - 10) - CASO NÃO DESEJE INSERIR NOTA DIGITE Z ")

    for key in lista_aluno:
        if float(porcentagem_media) > lista_aluno[key][5] and lista_aluno[key][1] == 'A':
            print("Aluno: " + lista_aluno[key][0] + '| Media: ' + str(lista_aluno[key][5]))


    media()
    if porcentagem_media.lower() == 'z':
        main_menu()

def exit():
    sys.exit()


def back():
    menu_actions['main_menu']()


# Lista do menu
menu_actions = {
    'main_menu': main_menu,
    '1': inserir_aluno,
    '2': deletar_aluno,
    '3': listar_aluno,
    '4': inserir_nota,
    '5': media,
    '9': back,
    '0': exit,
}

#LAYOUT {'id': ['nome', stats, 'nota1', 'nota2', 'nota3', 'media']}

lista_aluno = {
    1: ['Rodrigo', 'A', 10, 10, 10,10 ],
    2: ['Rodrigo2', 'I', 5, 5, 5, 5],
    3: ['Rodrigo3', "A", 3,2,1,2],
    4: ['Rodrigo4', "A", 3,2,1,2]
}

indice_aluno = 1
indice_nota = 1

main_menu()



'turma_um.pesquisar_aluno("Rodrigo")'


class Turma():
    aluno_nome = list()

    def inserir_aluno(self, nome):
        self.aluno_nome.append(nome)

    def listar_aluno(self):
        print(self.aluno_nome)

    def pesquisar_aluno(self, nome):
        try:
            pos = self.aluno_nome.index(nome)

            print("O nome procurado foi: {} e o indice dele é: {} ".format(self.aluno_nome[pos], pos))
        except ValueError:
            print("Nome não localizado na lista")

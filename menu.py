import os
import sql
import re
class Menu:

  


    def __init__(self):

        self.menu_actions = {
        'main_menu': self.main_menu,
        '1': self.insert_aluno,
        '2': self.delet_aluno,
        #'3': self.listar_aluno,
        #'4': self.inserir_nota,
        #'5': self.media,
        '9': self.back,
        '0': self.exit,
    }
        self.db_Cadastro = sql.db_Cadastro()

        self.pattern = '^[a-zA-Z]$'


    def main_menu(self):
        print("Bem vindo,\n")
        print("Escolha as opções:")
        print("1. Inserir aluno")
        print("2. Deletar aluno")
        print("3. Listar aluno")
        print("4. Inserir Nota")
        print("5. Média")
        print("\n0. Quit")
        choice = input(" >>  ")
        self.exec_menu(choice)

        return


# Executa o Menu1
    def exec_menu(self,choice):
        os.system('cls')
        ch = choice.lower()
        if ch == '':
            self.menu_actions['main_menu']()
        else:
            try:
                self.menu_actions[ch]()
            except KeyError:

                print("Invalid selection, please try again.\n")
                self.menu_actions['main_menu']()
        return




    def insert_aluno(self):
        os.system('cls')
        while True:
            try:
                name = input('Digite o nome do Aluno:')

                break
                #Não ta funcionando a verificação de nome
                # if re.match(self.pattern, name) is None and len (name) > 3 :
                #     raise Exception
                # else:  
                #     break
            except:
                print('O nome não aceita numeros ou palavras com menos de 3 caracteres')

        id_aluno= self.db_Cadastro.insert_aluno_db(name)

        print("O nome do aluno incluido é: {} e o seu ID é: {}".format(name, id_aluno))

        while True:

            choice_insert = input("Deseja adicionar mais aluno?")
            choice_insert.lower()

            if choice_insert == 's':
                self.insert_aluno()
            if choice_insert == 'n':
                self.main_menu()
            else:
                os.system('cls')
                print('Ação incorreta')


    def delet_aluno(self):
        pass
    
    
    def list_aluno_total():
         os.system('cls')
         #criar a lista de todos os alunos e verificar se a lista ta vazia no bd


    def exit():
        sys.exit()


    def back():
        menu_actions['main_menu']()
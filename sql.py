import sqlite3


class DbCadastro:

    def __init__(self, db_name= 'db_avarage.db'):
        self.db_name = db_name
        self.cursor = None

    
    def connect_db(self):
         self.connect = sqlite3.connect(self.db_name)
         self.cursor = self.connect.cursor()



    def insert_aluno_db(self, name):
        
        self.cursor.execute("INSERT INTO tb_cadastro (name, status) VALUES (?,?)", (name, 1))
        self.connect.commit()
          


    def delet_aluno_db(self,id):
        
        self.cursor.execute("UPDATE tb_cadastro SET status= 0 WHERE id= ?",(id,))
        self.connect.commit()
        
    def list_aluno_db(self):    
        lista = self.cursor.execute("SELECT * FROM tb_cadastro where status=1")
        for i in lista:
            print(i[0], "= ", i[1])



    def insert_nota_db(self, id,n1,n2,n3,media):
        self.cursor.execute("UPDATE tb_cadastro SET nota1=?, nota2 =?, nota3=?,media=? WHERE id=?", (n1,n2,n3,media,id))
        self.connect.commit()

    def close_db(self):
        try:
            self.cursor.close()
            self.connect.close()
        except:
            pass
        
db_teste = DbCadastro()


db_teste.close_db()
db_teste.connect_db()
#db_teste.insert_aluno_db('Rodrigo')
#db_teste.delet_aluno_db(6)
#db_teste.list_aluno_db()
db_teste.insert_nota_db(3,10.0,2.5,2.5,5.0)
import mysql.connector
from mysql.connector import errorcode

#DESKTOP
#===================================================================================================
class Moderador():
    def __init__(self,r):
        try:#se o banco de dados existir
            self.dataBase = mysql.connector.connect(host="localhost",user="root",database=r)
            self.cursor= self.dataBase.cursor(buffered=True)
            self.cursor.execute("Use %s;"%(r))
            print("Conexão ao MySQL Server bem-sucedida")
            print("Banco de Dados: %s\n"%(r.upper()))
            pass
        
        except mysql.connector.Error as err:#cria o banco de dados
            self.dataBase = mysql.connector.connect(host="localhost",user="root")
            self.cursor = self.dataBase.cursor(buffered=True)
            self.cursor.execute("CREATE DATABASE %s;"%(r))
            self.cursor.execute("Use %s;"%(r))
            print("Conexão ao MySQL Server bem-sucedida, \nCriação de Banco de dados bem sucedida")
            print("Banco de Dados: ",r.upper())
        pass

    #GERENCIAR TABELA =============================================================================
    def commit(self):
        self.dataBase.commit()

    def dataBaseDrop(self, data): #DELETAR BANCO DE DADOS
        self.cursor.execute("DROP DATABASE %s"%(data))

    def tableDatabase(self,tabela,colunas): #CRIAR TABELAS (NOME DA TABELA || COLUNAS)
        self.cursor.execute("CREATE TABLE %s(%s)"%(tabela,colunas))
        
    def tableDrop(self,tabela): #DELETAR TABELA
        self.cursor.execute("DROP TABLE %s(%s)"%(tabela))
    
    def addColuna(self,tabela,coluna): #ADICIONAR NOVA TABELA
        self.cursor.execute("ALTER TABLE %s ADD %s"%(tabela,coluna))

    def dropColuna(self,tabela,coluna): #EXCLUIR NOVA TABELA
        self.cursor.execute("ALTER TABLE %s DROP COLUMN %s"%(tabela,coluna))
    
    def alterColuna(self,tabela,coluna,tipo):#MODIFICAR O TIPO EM UMA COLUNA
        self.cursor.execute("ALTER TABLE %s MODIFY COLUMN %s %s"%(tabela,coluna,tipo))
    
    #GERENCIAR REGISTRO ===========================================================================
    def incluir(self,table,coll,values):
        self.cursor.execute("INSERT INTO %s (%s) VALUES (%s);"%(table,coll,values))
        pass

    def excluir(self,table,coll,values):
        self.cursor.execute("DELETE FROM %s WHERE %s"%(table,coll))
        pass

    def alterar(self,table,values,_id):
        self.cursor.execute("UPDATE %s SET %s WHERE %s = (SELECT dado_Id FROM PESSOA);"%(table,values,_id))
        pass

    def buscar(self,table,values):
        self.cursor.execute("SELECT %s FROM %s"%(table,values))
        registro=self.cursor.fetchall()
        return registro
                     

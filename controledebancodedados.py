import mysql.connector
from mysql.connector import errorcode

#DESKTOP
#===================================================================================================
class Moderador():
    def __init__(self,db):
        self.db = db
        try:#se o banco de dados existir
            self.dataBase = mysql.connector.connect(host="localhost",user="root",database=db)
            self.cursor = self.dataBase.cursor(dictionary=True)
            self.cursor = self.dataBase.cursor(buffered=True)
            self.cursor.execute("Use %s;"%(db))
            print("Conexão ao MySQL Server bem-sucedida")
            print("Banco de Dados: %s\n"%(db.upper()))
            pass
        
        except mysql.connector.Error as err:#cria o banco de dados
            self.dataBase = mysql.connector.connect(host="localhost",user="root")
            self.cursor = self.dataBase.cursor(dictionary=True)
            self.cursor = self.dataBase.cursor(buffered=True)
            self.cursor.execute("CREATE DATABASE %s;"%(db))
            self.cursor.execute("Use %s;"%(db))
            print("Conexão ao MySQL Server bem-sucedida \nCriação de Banco de dados bem sucedida")
            print("Banco de Dados: ",db.upper())
        pass
        

    #GERENCIAR TABELAS =============================================================================
    def commit(self):
        self.dataBase.commit()

    def dataBaseDrop(self): #DELETAR BANCO DE DADOS
        self.cursor.execute("DROP DATABASE %s"%(self.db))

    def tableCreate(self,table,colls): #CRIAR tableS (NOME DA TABELA || COLUNAS)
        self.cursor.execute("CREATE TABLE %s(%s)"%(table,colls))
        
    def tableDrop(self,table): #DELETAR table
        self.cursor.execute("DROP TABLE %s(%s)"%(table))
    
    def addColumns(self,table,coll): #ADICIONAR NOVA TABELA
        self.cursor.execute("ALTER TABLE %s ADD %s"%(table,coll))

    def dropColumns(self,table,coll): #EXCLUIR NOVA TABELA
        self.cursor.execute("ALTER TABLE %s DROP COLUMN %s"%(table,coll))
    
    def alterColumns(self,table,coll,dataType):#MODIFICAR O TIPO EM UMA COLUNAS
        self.cursor.execute("ALTER TABLE %s MODIFY COLUMN %s %s"%(table,coll,dataType))
    
    def alterForeign(self,table1,coll1,table2,coll2):#ADD CHAVE ESTRANGEIRA
        self.cursor.execute("ALTER TABLE %s ADD FOREIGN KEY (%s) REFERENCES %s(%s)"%(
            table1,coll1,table2,coll2))
        
    def alterForeignCONSTRAINT(self,table1,coll1,table2,coll2,ship):#ADD CHAVE ESTRANGEIRA
        self.cursor.execute("ALTER TABLE %s ADD CONSTRAINT %s FOREIGN KEY (%s) REFERENCES %s(%s)"%(
            table1,coll1,ship,table2,coll2))
    
    def dropForeign(self,table,coll):#EXCLUIR CHAVE ESTRANGEIRA
        self.cursor.execute("ALTER TABLE %s DROP FOREIGN KEY %s"%(table,coll))
        
    def alterPrimaryKey(self,table,coll):#ALTERAR CHAVE PRIMARIA
        self.cursor.execute("ALTER TABLE %s ADD PRIMARY KEY (%s)"%(table,coll))
        pass

    def dropPrimaryKey(self,table):#EXCLUIR CHAVE PRIMARIA
        self.cursor.execute("ALTER TABLE %s DROP PRIMARY KEY"%(table))

    def showTable(self):#MOSTRAR TODAS AS TABELAS
        self.cursor.execute("SHOW TABLES")
        return self.cursor
    
    def showColumns(self,table):#MOSTRAR TODAS AS COLUNAS EM UMA TABELAS
        self.cursor.execute("SHOW COLUMNS FROM %s.%s"%(self.db,table))
        return self.cursor
        
    
    #GERENCIAR REGISTRO ===========================================================================
    def insert(self,table,coll,values):#INSERIR REGISTROS
        self.cursor.execute("INSERT INTO %s (%s) VALUES (%s);"%(table,coll,values))

    def delete(self,table,coll,values):#DELETAR REGISTRO
        self.cursor.execute("DELETE FROM %s WHERE %s='%s'"%(table,coll,values))
        
    def update(self,table,values,_id):#ATUALIZAR REGISTRO
        self.cursor.execute("UPDATE %s SET %s WHERE %s;"%(table,values,_id))
        
    def select(self,table,coll):#SELECIONAR VALORES
        return "SELECT %s FROM %s;"%(coll,table)
        
    def search(self,table,coll):#EXIBIR REGISTROS
        data = self.select(table,coll)
        self.cursor.execute(data)
        registro=self.cursor.fetchall()
        return registro
    #ENCERRAR ======================================================================================
    def close(self):
        self.cursor.close()
        self.dataBase.close()

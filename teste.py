from controledebancodedados import Moderador

class controlador():
    def __init__(self, bancoDeDados):
        self.master = Moderador(bancoDeDados)
        info = self.master.cursor.execute("SHOW TABLES;")

        if info==None:
            print("Nenhuma tabela encontrada\n")
            self.createTable()
            self.master.commit()
            info = self.master.cursor.execute("SHOW TABLES;")
            print(info)
            pass
        else:
            print(info)

        self.user = str()
        pass
    
    def createTable(self):
        x = input("Digite o nome para sua(s) tabela(s),separe por VIRGULA caso queira criar mais de uma: ")
        print("\n\n")
        for i in x.split(","):
            colunas = str()
            print("\n\nUse * para definir chave primaria para coluna\n")
            y = input("Digite nomes para as colunas da tabela %s separados por VIRGULA: "%(i.upper()))
            for l in y.split(","):
                print("===COLUNA %s ===\n\n1 - Texto até 50;\n2 - Texto Longo até 255;\n3 - Numeros inteiros;\n4 - Numeros decimais;\n5 - Datas;\n6 - Hora;"%(l.replace("*","CHAVE PRIMARIA").upper()))
                a = 0
                while (a<1):
                    a = int(input("Digite um numero para escolher um tipo de entrada que a coluna %s deve receber: "%(l.replace("*"," chave primária").upper())))
                    if(a==1):
                        colunas+= "%s CHAR(50)"%(l.replace("*",""))
                    elif(a==2):
                        colunas+= "%s VARCHAR(255)"%(l.replace("*",""))
                    elif(a==3):
                        colunas+= "%s INT"%(l.replace("*",""))
                    elif(a==4):
                        colunas+= "%s FLOAT(53)"%(l.replace("*",""))
                    elif(a==5):
                        colunas+= "%s DATE"%(l.replace("*",""))
                    elif(a==6):
                        colunas+= "%s TIME"%(l.replace("*",""))
                    else:
                        a = 0
                        print("numero escolhido não corresponde a nenhum dado conhecido")
                        return
                    if(l.rfind("*")>-1):
                        colunas += " NOT NULL PRIMARY KEY"
                    if l != y.split(",")[-1]:
                        colunas += ","
                    pass
                print("\n\n")
            self.master.tableDatabase(i,colunas)
        pass
    pass

bd = input("Digite um nome para abrir um banco de dados, ou para criar um: ")
status = ""
while status != "s":
    root = controlador(bd)
    status = input("")

root.master.close()

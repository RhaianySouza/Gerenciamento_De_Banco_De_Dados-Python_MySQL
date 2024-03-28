<h1>Projeto de gestão de Banco de Dados (Python, MySQL)</h1>
Um projeto de gestão de banco de dados em Python que interage com MySQL para criar bancos de dados e tabelas de maneira genérica é uma excelente forma de aprender sobre interações entre Python e sistemas de gerenciamento de bancos de dados SQL. O projeto envolverá o uso do conector MySQL para Python, permitindo que você execute comandos SQL diretamente do seu código Python.

<h2>Requisitos:</h2>
<ol>
  <li><b>Python:</b> Certifique-se de que o Python está instalado em seu sistema.</li>
  <li><b>MySQL Server:</b> Você precisará do MySQL Server instalado e em execução.</li>
  <li><b>Conector MySQL para Python:</b> Use o pacote mysql-connector-python para conectar o Python ao MySQL.</li>
</ol>

<h2></h2>
<h2>Passos para o Projeto:</h2>
<ol>
  <li>Configuração do Ambiente: Instale o conector MySQL para Python
    <pre>pip install mysql-connector-python</pre></li>
  <li>Crie um arquivo chamado controledebancodedados.py para gerenciar a conexão com o MySQL
    <pre>import mysql.connector
from mysql.connector import errorcode</pre></li>
  <li>Gerenciar a criação exclusão de tabelas, assim como colunas, chave primaria e estrangeira.</li>
  <li>Inserção, atualização e exclusão de registros.</li>
  <li>Busca e listagem de dados com filtros.</li>
</ol>
<h2>Execução:</h2>
<ol>
  <li>Crie uma variavel que vai receber a classe <b>Moderador</b> que recebe o nome do banco de dados a ser criado, Ex: <b>biblioteca</b>
    <pre>root = Moderador("biblioteca")</pre>
    Se o banco de dados existir, será tentado uma conexão, caso consiga será impresso na tela:
    <pre>Conexão ao MySQL Server bem-sucedida<br/>Banco de Dados: BIBLIOTECA</pre>
    Se não, o banco de dados será criado:
    <pre>Conexão ao MySQL Server bem-sucedida<br/>Criação de Banco de dados bem sucedida<br/>Banco de Dados:  BIBLIOTECA</pre>
  </li>
  <h3>Metodos da classe para manipulação de tabelas e colunas</h3>
  <li>commit()#CONFIRMA A TRANSAÇÃO ATUAL</li>
  <pre>root.commit()</pre>
  <li>close()#ENCERRAR CONEXÕES</li>
  <pre>root.close()</pre>
  <li>dataBaseDrop() #DELETAR BANCO DE DADOS</li>
  <pre>root.dataBaseDrop()</pre>
  <li>tableCreate(table,colls)#CRIA TABELAS (PARAMETRO: nome da tabela, nome das colunas e seu respectivos valores)</li>
  Criar tabela <b>Livros</b>:
  <pre>root.tableCreate("livros","""
  titulo VARCHAR(100),
  autor VARCHAR(20),
  ano_publicacao INT,
  editora VARCHAR(20),
  genero VARCHAR(20)""")
  </pre>
  Criar tabela <b>Autores</b>:
  <pre>root.tableCreate("autores","""
  id_autor INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(20),
  nacionalidade VARCHAR(20),
  data_nascimento VARCHAR(30)""")
  </pre>
  <li>tableDrop(table): #DELETAR TABELAS (PARAMETRO:nome da tabela)</li>
	<pre>root.tableDrop('autores')</pre>
  <li>addColumns(table,coll)#ADICIONA COLUNA (PARAMETRO: nome da tabela, nome das colunas e seu respectivos valores)</li>
	<pre>root.addColumns('livros','isnb10 INT NOT NULL')<br/>root.addColumns('livros','idioma VARCHAR(15)')</pre>
  <li>dropColumns(table,coll): #EXCLUIR COLUNA (PARAMETRO: nome da tabela, nome da coluna)</li>
	<pre>root.dropColumns('livros','idioma')</pre>
  <li>alterForeign(table1,coll1,table2,coll2):#ADD CHAVE ESTRANGEIRA<br/>(PARAMETRO: nome da tabela 1, nome da coluna 1,nome da tabela 2, nome da coluna 2)</li>
	<pre>root.alterForeign('autores','nome','livros','autor')</pre>
  <li>alterForeignCONSTRAINT(self,table1,coll1,table2,coll2,ship):#ADD CHAVE ESTRANGEIRA<br/>(PARAMETRO: nome da tabela 1, nome da coluna 1,nome da tabela 2, nome da coluna 2, restrição)</li>
	<pre>root.alterForeignCONSTRAINT('autores','nome','livros','autor','FK_livrosAutores')</pre> 
  <li>dropForeign(self,table,coll):#EXCLUIR CHAVE ESTRANGEIRA (PARAMETRO: nome da tabela, nome da coluna)</li>
	<pre>root.dropForeign('livros','autor')</pre> 
  <li>alterPrimaryKey(self,table,coll):#ALTERAR CHAVE PRIMARIA (PARAMETRO: nome da tabela, nome da coluna)</li>
	<pre>root.alterPrimaryKey('livros','isnb10')</pre>
  <li>dropPrimaryKey(table):#EXCLUIR CHAVE PRIMARIA</li>
	<pre>root.dropPrimaryKey('livros')</pre>  
  <li>showTable(self):#MOSTRAR TODAS AS TABELAS</li>
	<pre>for i in root.showTable():
  print(i)</pre>
  <li>showColumns(self,table):#MOSTRAR TODAS AS COLUNAS EM UMA TABELAS (PARAMETRO: nome da tabela)</li>
	<pre>for i in root.showColumns('livros'):
  print(i)</pre>
  <h3>Metodos da classe para manipulação de registros</h3>
  <li>insert(table,coll,values):#INSERIR REGISTROS (PARAMETRO: nome da tabela,colunas afetadas,valores)</li>
    Inserir registro na tabela <b>Livros</b>
	<pre>#Colunas Livros
livros = 'titulo,autor,ano_publicacao,editora,genero,isnb10'</pre>
  <pre>root.insert('livros',livros,'"Dom Casmurro", "Machado de Assis",1899,"Garnier","Romance",6586490081')</pre>
  <pre>root.insert('livros',livros,'"O Senhor dos Anéis: A Sociedade do Anel","J.R.R. Tolkien",1954,"Allen & Unwin","Fantasia",8595084750')</pre>
  <pre>root.insert('livros',livros,'"1984","George Orwell",1949,"Secker & Warburg","Ficção Distópica",6587034209')</pre>
  <pre>root.insert('livros',livros,'"Harry Potter e a Pedra Filosofal","J.K. Rowling", 1997,"Bloomsbury","Fantasia",8532530788')</pre>
    Inserir registro na tabela <b>Autores</b>
	<pre>#Colunas Autores
autores = 'nome,nacionalidade,data_nascimento'</pre>
  <pre>root.insert('autores',autores,'"Agatha Christie","Britânica","1890-09-15"')</pre>
  <pre>root.insert('autores',autores,'"George Orwell","Britânica","1903-06-25"')</pre>
  <pre>root.insert('autores',autores,'"J.R.R. Tolkien","Britânica","1892-01-03"')</pre>
  <pre>root.insert('autores',autores,'"J.K. Rowling","Britânica","1965-07-31"')</pre>
  
  <li>delete(table,coll,values):#DELETAR REGISTRO (PARAMETRO: nome da tabela,colunas onde valor ocorrore)</li>
  <pre>root.delete('livros','autor','J.K. Rowling')</pre>
  <li>update(table,values,_id):#ATUALIZAR REGISTRO (PARAMETRO: nome da tabela,coluna, id ou valor)</li>
  <pre>root.update('livros','titulo="Harry Potter e a Câmara Secreta,isbn=8532530796,ano_publicacao=1998"','autor="J.K. Rowling"')</pre>
  <li>select(table,coll):#SELECIONAR VALORES(PARAMETRO: nome da tabela, string coluna='valor' procurados)</li>
  <pre>root.select('livros','autor="J.K. Rowling"')</pre>
  <li>search(table,coll):#EXIBIR REGISTROS(PARAMETRO: nome da tabela,nome da coluna ou * para ver todas as colunas)</li>
  <pre>root.update('livros','*')</pre>
</ol>  
<h2>Expansão do Projeto:</h2>
<p>Interface de usuário (UI) com frameworks como Tkinter (para aplicações de desktop) ou Flask/Django (para aplicações web).</p>
<p>Este projeto base oferece um sólido ponto de partida para o gerenciamento de bancos de dados em Python, com ampla margem para expansão e personalização conforme sua necessidade.</p>



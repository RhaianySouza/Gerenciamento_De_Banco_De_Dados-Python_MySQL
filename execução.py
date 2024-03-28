Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: D:\Portifolio\Projetos em Python\controledebancodedados.py
root = Moderador("biblioteca")
Conexão ao MySQL Server bem-sucedida 
Criação de Banco de dados bem sucedida
Banco de Dados:  BIBLIOTECA

for i in root.showTable():print(i)

root.tableCreate("livros","""titulo VARCHAR(100),autor VARCHAR(20),ano_publicacao INT,editora VARCHAR(20),genero VARCHAR(20)""")
root.tableCreate("autores","""id_autor INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(20),nacionalidade VARCHAR(20),data_nascimento VARCHAR(30)""")
for i in root.showTable():print(i)

('autores',)
('livros',)
root.tableDrop('autores')
for i in root.showTable():print(i)

('livros',)
root.tableCreate("autores","""id_autor INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(20),nacionalidade VARCHAR(20),data_nascimento VARCHAR(30)""")
for i in root.showTable():print(i)

('autores',)
('livros',)
for i in root.showColumns('livros'):print(i)

('titulo', 'varchar(100)', 'YES', '', None, '')
('autor', 'varchar(20)', 'YES', '', None, '')
('ano_publicacao', 'int', 'YES', '', None, '')
('editora', 'varchar(20)', 'YES', '', None, '')
('genero', 'varchar(20)', 'YES', '', None, '')
#coluna| tipo de dados | NULO |Chave |Valor padrão | outros
for i in root.showColumns('autores'):print(i)

('id_autor', 'int', 'NO', 'PRI', None, 'auto_increment')
('nome', 'varchar(20)', 'YES', '', None, '')
('nacionalidade', 'varchar(20)', 'YES', '', None, '')
('data_nascimento', 'varchar(30)', 'YES', '', None, '')
root.addColumns('livros','isnb10 VARCHAR(10) NOT NULL')
root.addColumns('livros','idioma VARCHAR(15)')
for i in root.showColumns('livros'):print(i)

('titulo', 'varchar(100)', 'YES', '', None, '')
('autor', 'varchar(20)', 'YES', '', None, '')
('ano_publicacao', 'int', 'YES', '', None, '')
('editora', 'varchar(20)', 'YES', '', None, '')
('genero', 'varchar(20)', 'YES', '', None, '')
('isnb10', 'varchar(10)', 'NO', '', None, '')
('idioma', 'varchar(15)', 'YES', '', None, '')
root.dropColumns('livros','idioma')
for i in root.showColumns('livros'):print(i)

('titulo', 'varchar(100)', 'YES', '', None, '')
('autor', 'varchar(20)', 'YES', '', None, '')
('ano_publicacao', 'int', 'YES', '', None, '')
('editora', 'varchar(20)', 'YES', '', None, '')
('genero', 'varchar(20)', 'YES', '', None, '')
('isnb10', 'varchar(10)', 'NO', '', None, '')
root.alterForeign('livros','autor','autores','nome')
for i in root.showColumns('livros'):print(i)

('titulo', 'varchar(100)', 'YES', '', None, '')
('autor', 'varchar(20)', 'YES', 'MUL', None, '')
('ano_publicacao', 'int', 'YES', '', None, '')
('editora', 'varchar(20)', 'YES', '', None, '')
('genero', 'varchar(20)', 'YES', '', None, '')
('isnb10', 'varchar(10)', 'NO', '', None, '')
root.alterPrimaryKey('livros','isnb10')
for i in root.showColumns('livros'):print(i)

('titulo', 'varchar(100)', 'YES', '', None, '')
('autor', 'varchar(20)', 'YES', 'MUL', None, '')
('ano_publicacao', 'int', 'YES', '', None, '')
('editora', 'varchar(20)', 'YES', '', None, '')
('genero', 'varchar(20)', 'YES', '', None, '')
('isnb10', 'varchar(10)', 'NO', 'PRI', None, '')
root.dropPrimaryKey('livros')
for i in root.showColumns('livros'):print(i)

('titulo', 'varchar(100)', 'YES', '', None, '')
('autor', 'varchar(20)', 'YES', 'MUL', None, '')
('ano_publicacao', 'int', 'YES', '', None, '')
('editora', 'varchar(20)', 'YES', '', None, '')
('genero', 'varchar(20)', 'YES', '', None, '')
('isnb10', 'varchar(10)', 'NO', '', None, '')
root.alterPrimaryKey('livros','isnb10')

for i in root.showColumns('livros'):print(i)

('titulo', 'varchar(100)', 'YES', '', None, '')
('autor', 'varchar(20)', 'YES', 'MUL', None, '')
('ano_publicacao', 'int', 'YES', '', None, '')
('editora', 'varchar(20)', 'YES', '', None, '')
('genero', 'varchar(20)', 'YES', '', None, '')
('isnb10', 'varchar(10)', 'NO', 'PRI', None, '')
for i in root.search('livros','*'):print(i)

livros = 'titulo,autor,ano_publicacao,editora,genero,isnb10'
livro =['"Dom Casmurro", "Machado de Assis",1899,"Garnier","Romance",6586490081','"O Senhor dos Anéis: A Sociedade do Anel","J.R.R. Tolkien",1954,"Allen & Unwin","Fantasia",8595084750','"1984","George Orwell",1949,"Secker & Warburg","Ficção Distópica",6587034209','"Harry Potter e a Pedra Filosofal","J.K. Rowling", 1997,"Bloomsbury","Fantasia",8532530788']
for i in livro:
    root.insert('livros',livros,i)

    
for i in root.search('livros','*'):print(i)

('Dom Casmurro', 'Machado de Assis', 1899, 'Garnier', 'Romance', '6586490081')
('O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', 1954, 'Allen & Unwin', 'Fantasia', '8595084750')
('1984', 'George Orwell', 1949, 'Secker & Warburg', 'Ficção Distópica', '6587034209')
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997, 'Bloomsbury', 'Fantasia', '8532530788')
>>> for i in root.search('autores','*'):print(i)
... 
>>> autores = 'nome,nacionalidade,data_nascimento'
>>> autor = ['"Agatha Christie","Britânica","1890-09-15"',
...          '"George Orwell","Britânica","1903-06-25"',
...          '"J.R.R. Tolkien","Britânica","1892-01-03"',
...          '"J.K. Rowling","Britânica","1965-07-31"']
>>> for i in autor:
...     root.insert('autores',autores,i)
... 
...     
>>> for i in root.search('autores','*'):print(i)
... 
(1, 'Agatha Christie', 'Britânica', '1890-09-15')
(2, 'George Orwell', 'Britânica', '1903-06-25')
(3, 'J.R.R. Tolkien', 'Britânica', '1892-01-03')
(4, 'J.K. Rowling', 'Britânica', '1965-07-31')
>>> root.update('livros','titulo="Harry Potter e a Câmara Secreta,isbn=8532530796,ano_publicacao=1998"','autor="J.K. Rowling"')
>>> for i in root.search('livros','*'):print(i)
... 
('Dom Casmurro', 'Machado de Assis', 1899, 'Garnier', 'Romance', '6586490081')
('O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', 1954, 'Allen & Unwin', 'Fantasia', '8595084750')
('1984', 'George Orwell', 1949, 'Secker & Warburg', 'Ficção Distópica', '6587034209')
('Harry Potter e a Câmara Secreta,isbn=8532530796,ano_publicacao=1998', 'J.K. Rowling', 1997, 'Bloomsbury', 'Fantasia', '8532530788')
>>> root.delete('livros','autor','J.K. Rowling')
>>> for i in root.search('livros','*'):print(i)
... 
('Dom Casmurro', 'Machado de Assis', 1899, 'Garnier', 'Romance', '6586490081')
('O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', 1954, 'Allen & Unwin', 'Fantasia', '8595084750')
('1984', 'George Orwell', 1949, 'Secker & Warburg', 'Ficção Distópica', '6587034209')

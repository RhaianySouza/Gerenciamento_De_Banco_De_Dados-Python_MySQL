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
  <li>Inserção, atualização e exclusão de registros.</li>
  <li>Busca e listagem de dados com filtros.</li>
</ol>  
<h2>Execução:</h2>
<ol>
  <li>Crie uma variavel que vai receber a classe <b>controlador</b> que recebe o nome do banco de dados a ser criado, Ex: <b>imobiliaria</b>
    <pre>root = controlador("imobiliaria")</pre>
  </li>
  <li>O paramentro passado sera o nome do banco de dados que já existe ou sera criado neste momento;</li>
  <li>Para executar algumas interações acesse a variave <b>cursor</b> da classe <b>controlador</b>. Ex.:
    <pre>root.cursor.tableDatabase(tabela,colunas)</pre>
  </li>
  <li><b>tableDatabase</b> é o metodo para se criar uma tabela;</li>
  <li></li>
</ol>  
<h2>Expansão do Projeto:</h2>
<p>Interface de usuário (UI) com frameworks como Tkinter (para aplicações de desktop) ou Flask/Django (para aplicações web).</p>
<p>Este projeto base oferece um sólido ponto de partida para o gerenciamento de bancos de dados em Python, com ampla margem para expansão e personalização conforme sua necessidade.</p>



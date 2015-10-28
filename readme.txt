André Stern, 41229126
Pedro Ardaglio de Mello, 31203523

=== Arquivos submetidos ===
- Conta.py
    Classe modelo para instanciar objetos de Contas, com getters/setters de saldo e id.
- ATM.py
    Arquivo com um trecho para rodar no terminal, e uma classe que gerencia os parâmetros
    recebidos e chama o serviço do Banco.
- Banco.py
    Classe modelo de um banco, que busca a conta solicitada e realiza o serviço solicitado.
    Esse arquivo também contém toda a lógica do webservice, que recebe o que foi requisitado
    e redireciona para a classe Banco.

=== Instruções ===
O programa foi desenvolvido e testado em ambiente Linux (testado no Debian 7.0 e Slackware 14.0).
Foi utilizado a linguagem Python 2.7, e testado na versão 2.7.3, porém é provável que funcione
em todas as versões 2.7.x.

Foi utilizado o módulo "web.py", que foi instalado através do pip (um gerenciador/instalador de
módulos do próprio Python). Se seu OS não tiver ele, ele pode ser instalado usando o comando
"apt-get install python-pip" (o nome depois do install pode variar dependendo do repośitório que
está sendo usado.) para OS derivados do Debian, ou utilizando o SlackBuilds, caso esteja testando
em um ambiente Slackware. Também ter versões para pacotes RPM, ou utilizando o yum (Fedora, CentOS
e derivados). Para mais informações sobre o pip, visite o site: https://pypi.python.org/pypi/pip

Normalmente as bibliotecas json e urllib2 que foram usadas no projeto já vem por padrão com o Python.
Caso não seja o caso, utilizar a mesma lógica descrita acima funciona para instalá-los (mas acreditamos
fortemente que não vai precisar)

Após tendo o pip instalado, instalamos o web.py através dele, com o comando: pip install web.py.

Para os dois passos acima, é necessário ser root, ou ter permissão sudo (ser um sudoer).

Após isso, navegue na pasta do projeto e utiliza o seguinte comando para rodar o programa:

$python Banco.py [porta]

Se não for definida nenhuma porta, ele abrirá na porta 8542 (como foi descrito no documento explicando
a tarega).

Sendo assim, o webservice já estará no ar.

Agora é necessário rodar o cliente com os parâmetros para poder terminar de testar. Para isso, servem
os seguintes comandos:

$python ATM.py [host] [porta] [nome_do_servico/funcao_a_realizar] [parametros_adicionais_do_servico]

Os serviços, e seus parâmetros, são:

saldo [conta]
deposito [conta] [valor]
saque [conta] [valor]
transferencia [conta_origem] [conta_destino] [valor]


=== Notas ===
- Com exceção do código fonte, nossos documentos possuem acentos, e deve ser lidos em sistemas
  configurados para UTF-8, ou outro que aceite (Unicode, por exemplo).
- Todos os parâmetros acima que possuem "[]", devem ser digitados sem o mesmo, pois eles são variáveis.
- Retiramos os acentos dos prints, pois caso o ambiente não esteja configurado corretamente, poderá
  haver erros não previstos. Ocorre principalmente em terminais que não aceitam UTF-8, entre outros.
- Comentamos o código em casos em que não seja óbvio o seu funcionamento, como por exemplo o uso do
  módulo web.py
- Não foi testado em Windows, mas por Python ser multiplataforma, ao configurar ter o Python na versão
  certa e o web.py instalado corretamente, deverá funcionar normalmente. Nesse caso, executar o programa
  é do mesmo jeito do Linux.
- Pode haver alguns problemas se um proxy, firewall ou alguma configuração (diferente e estranha) de DNS
  estiver impedindo a conexão no host e porta solicitada.
- Fizemos algumas consistências, porém não todas, porque acreditamos que esse não seja o foco do projeto.
- Na hora de digitar os valores, pode digitar (caso seja decimal) tanto com ',' ou com '.'
  

Obrigado!
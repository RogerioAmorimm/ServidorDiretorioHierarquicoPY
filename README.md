# ServidorDiretorioPY
Servidor de diretório usando rpc em phyton

## CONST
Nesse arquivo guardamos as constantes com o ip e porta do servidor de diretórios 
## CLIENT
Nesse arquivo temos o códgio do cliente que vai fazer a conexão com servidor de diretório e fazer requisição através do servidor de diretório para buscar o servirdor desejado
## SERVER
Nesse arquivo temos o servidor do qual o cliente estará "procurando", nele iremos iniciar o servidor de diretório e posteriormente iremos registrar este servidor no servidor de diretório
#### SEGUNDA PARTE
Na segunda parte foram adicionados metodos exposed_remove que recebe um data, para remove-lo da lista, exposed_search que recebe um data, para procurá-lo na lista e retorna o elemente e posição
## SERVERDIR
Nesse arquivo temos o servidor de diretório que tem as funções de registrar servidor, que recebe um serverName, ip e porta e registra ele. E temos a função que buscaServer que recebe um sereverName e realiza a busca verificando se o server está registrado. Este é o servidor que intercala a conexão entre o client e o server que ele deseja se conectar.
#### SEGUNDA PARTE
Na segunda parte foram adicionados metodos exposed_registraServerNovamente que recebe um severName, para buscar o server registrado e adicionar as novas informações, exposed_removaServer que recebe um severName, para buscar o server registrado e remove-lo do servidor de diretório. E ainda foi melhorado a função exposed_buscaServer para evitar que seja realizada a busca de servers não registrados 

# Classificando área de atuação de OSCs utilizando Random Forest Classifie.
Com base nos dados cadastrais de todas as OSCs do Brasil, foram desenvolvidas algumas análises e experimentos utilizando o algoritmo de classificação random forest.
Neste repositório, será disponibilizado todo o conteúdo necessário para a análise, criação do modelo preditivo e um webservice para o consumo do modelo.
- mais informações sobre OSCs: https://mapaosc.ipea.gov.br/
## Versão 1.0

### Estrutura do projeto
- App
	- dados
		* entrada 
		
				dados_gerais.csv /* arquivo de dados gerais com as características das OSCs */
				área_atuacao.csv /* arquivo com os dados de classificação das áreas de atuação de cada OSC. */
    
		* saída
		
				local onde serão gerados os arquivos: agrupamento das áreas, label encoder utilizado para treinar o modelo, o modelo treinado e os arquivos com as colunas removidas durante todo o processo.
				
	- modelos
		* modelos.cfg 
		
			Arquivo de configuração dos diretórios e parâmetros necessários para geração do modelo:
				
				DADOS_GERAIS = informar o nome do arquivo dos dados gerais, que possui as características das OSCs.
 
				AREA_ATUACAO = informar o nome do arquivo de área de atuação, que possui a classificação da OSC.

				AREA_AGRUPADA = informar o nome do arquivo a ser gerado com o agrupamento de todas as áreas de atuação.

				MODELO = informar o nome do modelo que será gerado.

				TIPO_MODELO = informar 1 para gerar um modelo com somente OSCs que possuam somente uma área de atuação, informar 2 para gerar um modelo somente com OSCs que possuam mais de uma área de atuação ou informar 3 para utilizar todas as OSCs.

				LABEL_ENCODER = informar o nome do label encoder a ser salvo no momento do treino do modelo.

	 * modelos.log
	 
	 		Arquivo com todos os logs do processamento da criação, treinamento e teste do modelo.
  
	
	- utils
	
		* log_factory.py
	
			arquivo gerador de logs
  
	- webservice
	
		* webservice.cfg
			
			arquivo de configuração do serviço de webservice.
	
				MODELO = informar o nome do modelo gerado pelo processo de geração de modelo, mesmo nome informado no arquivo 'modelos.cfg'.
	
				LABEL_ENCODER = informar o nome do label encoder gerado pelo processo de geração de modelo, mesmo nome informado no arquivo 'modelos.cfg'.

- main.cfg
	
		arquivo de configuração para ativar os módulos do aplicativos, onde os parâmetros ProcessaAgrupamentoAreaAtuacao, GeraModelo e AtivaWebService devem ser referenciados com os valores de True ou False de acordo com a necessidade. Para o primeiro processamento, todos os valores devem possuir o valor de True, para que os modelos e suas dependências sejam geradas.

- main.py

		arquivo python que inicia toda a aplicação, após configuração de todos os arquivos, basta rodar este arquivo utilizando, por exemplo, o	comando ‘python main.py’ que a aplicação será executada.

- modelos.py

		arquivo python com os códigos necessários para a geração do agrupamento das área de atuação, o modelo radom forest e o label encoder.

- webservice.py
	
		arquivo python com os códigos necessários para levantar o serviço de webservice para o consumo do modelo gerado.
- Análise com Jupyter Notebook

	- Durante o processo de análise, foi identificado que uma OSC poderia ter mais de uma área de atuação.
		
			"1";"Habitação"
			"2";"Saúde"
			"3";"Cultura e recreação"
			"4";"Educação e pesquisa"
			"5";"Assistência social"
			"6";"Religião"
			"7";"Associações patronais, profissionais e de produtores rurais"
			"8";"Meio ambiente e proteção animal"
			"9";"Desenvolvimento e defesa de direitos"
			"10";"Outros"
			"11";"Outras atividades associativas"
                 
		 Diante disso, os experimentos foram tratados de três formas distintas para avaliar a performance do modelo:
		 	"Análise de OSCs com somente mais de uma área de atuação" - foram analisadas e o modelo foi treinado utilizando somente as OSCs que tinham apenas uma área de atuação.
			"Análise de OSCs com somente mais de uma área de atuação" - foram analisadas e o modelo foi treinado utilizando somente as OSCs que tinham mais de uma área de atuação.
			"Análise de OSCs com todas as áreas de atuação juntas" - foram analisadas e o modelo foi treinado utilizando todas as OSCs, independente da quantidade de área de atuação.

# Requisitos
- Python 3.6
- Pandas
- Pickle
- Matplotlib
- Tqdm

# Exemplo de utilização com webservice

- Por padrão o flask inicia o webservice em localhost na porta 5000, logo basta realizar um get para a url: "http://localhost:5000//busca-area-atuacao/consulta?" passando por parâmetros as variáveis: cd_natureza_juridica_osc, ft_razao_social_osc, ft_nome_fantasia_osc, ft_fundacao_osc e cd_classe_atividade_economica_osc. A omissão de qualquer um dos parâmetros não será gerado erro, mas será interpretado como valor nulo que será tratado e enviado para o modelo.

- Dentro da estrutura do projeto, no diretório '/utils' existe um arquivo 'teste_webservice_proj_soapUI.xml', este é referente a um projeto da aplicação SoapUI, uma aplicação para simulação de consumo de webservice, onde pode-se baixar o instalador gratuitamente através do link https://s3.amazonaws.com/downloads.eviware/soapuios/5.4.0/SoapUI-x32-5.4.0.exe e importar o projeto. Assim que importado, basta ativar o webservice pela aplicação python e realizar o teste.

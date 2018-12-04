# Classificando área de atuação de OSCs utilizando Random Forest Classifie.
Com base nos dados cadastrais de todas as OSCs do Brasil. Foram desenvolvidas algumas análises e experimentos utilizando o algoritmo de classificação random forest.
Neste repositório será disponibilizado todo o conteúdo necessário para a análise, criação do modelo preditivo e um webservice para o consumo do modelo.
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
				
				DADOS_GERAIS = informar o diretório ‘\entrada’ + o nome do arquivo de entrada dos dados gerais.
 
				AREA_ATUACAO = informar o diretório ‘\entrada’ + o nome do arquivo de área de atuação.

				AREA_AGRUPADA = informar o diretório ‘\saida’ + o nome do arquivo a ser gerado com o agrupamento de todas as áreas de atuação.

				MODELO = informar o diretório ‘\saida’ + o nome do modelo que será gerado.

				TIPO_MODELO = informar 1 para gerar um modelo com somente OSCs que possuam somente uma área de atuação, informar 2 para gerar um modelo somente com OSCs que possuam mais de uma área de atuação ou informar 3 para utilizar todas as OSCs.

				LABEL_ENCODER = informar o diretório ‘\saida’ + o nome do label encoder a ser salvo no momento do treino do modelo.

	 * modelos.log
	 
	 		Arquivo com todos os logs do processamento da criação, treinamento e teste do modelo.
  
	
	- utils
	
		* log_factory.py
	
			arquivo gerador de logs
  
	- webservice
	
		* webservice.cfg
			
			arquivo de configuração do serviço de webservice.
	
				MODELO = diretório do modelo gerado no processo de geração do modelo, sugerido utilizar o mesmo diretório informado no arquivo modelos.cfg.
	
				LABEL_ENCODER = diretório do label encoder gerado no processo de geração do modelo, sugerido utilizar o mesmo diretório informado no arquivo modelos.cfg.

- main.cfg
	
		arquivo de configuração para ativar os módulos do aplicativos, onde os parâmetros ProcessaAgrupamentoAreaAtuacao, GeraModelo e AtivaWebService devem ser referenciados com os valores de True ou False de acordo com a necessidade. Para o primeiro processamento todos os valores devem possuir o valor de True, para que os modelos e suas dependências sejam geradas.

- main.py

		arquivo python que inicia toda a aplicação, após configuração de todos os arquivos, basta rodar este arquivo utilizando por exemplo o	comando ‘python main.py’ que a aplicação será executada.

- modelos.py

		arquivo python com os códigos necessários para a geração do agrupamento das área de atuação, o modelo radom forest e o label encoder.

- webservice.py
	
		arquivo python com os códigos necessários para levantar o serviço de webservice para o consumo do modelo gerado.
	
# Requisitos
- Python 3.6
- Pandas
- Pickle
- Matplotlib
- Tqdm

# Exemplo de utilização do webservice

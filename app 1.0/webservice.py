# -*- coding: utf-8 -*-

import pickle
import json

from flask import Flask, request, make_response
from flask_cors import CORS

from os.path import dirname, abspath, join

import warnings
warnings.filterwarnings("ignore")

#------------------------------------------------------------------------------    
# Globals variables
PATH = dirname(abspath(__file__))
#------------------------------------------------------------------------------   
class Service():
	
	def run():

		#configurando o flask para gerar o REST e usando um módulo CORS para evitar o bloqueio do navegador
		app = Flask(__name__)
		CORS(app)

		# lendo os diretorios dos arquivos
		config = readConfig(join(PATH,"webservice","webservice.cfg"))
		
		# carrega o label encoder
		file = open(join(PATH,'dados','saida',config['LABEL_ENCODER']),'rb')
		le = pickle.load(file)
		file.close()

		# carrega o modelo random forest
		file = open(join(PATH,'dados','saida',config['MODELO']),'rb')
		rf = pickle.load(file)
		file.close()

		# inicia a url para a previsao
		@app.route("/busca-area-atuacao/<consulta>")
		def busca_area(consulta): 
		    
		    cd_natureza_juridica_osc = request.args.get("cd_natureza_juridica_osc")
		    ft_razao_social_osc = request.args.get("ft_razao_social_osc")
		    ft_nome_fantasia_osc = request.args.get("ft_nome_fantasia_osc")
		    ft_fundacao_osc = request.args.get("ft_fundacao_osc")
		    cd_classe_atividade_economica_osc = request.args.get("cd_classe_atividade_economica_osc")
		    
		    erros = {}

		    if cd_natureza_juridica_osc == None:
		    	cd_natureza_juridica_osc = -1
		    else:
		    	try:
		    		cd_natureza_juridica_osc = int(cd_natureza_juridica_osc)
		    	except Exception as e :
		    		erros["cd_natureza_juridica_osc"] = {}
		    		erros["cd_natureza_juridica_osc"]['mensagem'] = 'Nao foi possivel converter o valor informado, verifique caracter diferente de [0-9]'
		    		erros["cd_natureza_juridica_osc"]['exception'] = str(e)


		    if ft_razao_social_osc == None:
		    	ft_razao_social_osc = -1
		    else:
		    	try:
		    		fit = le['ft_razao_social_osc']
		    		ft_razao_social_osc = fit.transform([ft_razao_social_osc])[0]
		    	except Exception as e:
		    		erros["ft_razao_social_osc"] = {}
		    		erros["ft_razao_social_osc"]['mensagem'] = '''Nao foi possivel aplicar o label encoder para o valor informado, caso seja um novo valor para o campo, sera necessario treinar novamente o modelo'''
		    		erros["ft_razao_social_osc"]['exception'] = str(e)

		    if ft_nome_fantasia_osc == None:
		    	ft_nome_fantasia_osc = -1
		    else:
		    	try:
		    		fit = le['ft_nome_fantasia_osc']
		    		ft_nome_fantasia_osc = fit.transform([ft_nome_fantasia_osc])[0]
		    	except Exception as e :
		    		erros["ft_nome_fantasia_osc"] = {}
		    		erros["ft_nome_fantasia_osc"]['mensagem'] = '''Nao foi possivel aplicar o label encoder para o valor informado, caso seja um novo valor para o campo, sera necessario treinar novamente o modelo'''
		    		erros["ft_nome_fantasia_osc"]['exception'] = str(e)

		    if ft_fundacao_osc == None:
		    	ft_fundacao_osc = -1
		    else:
		    	try:
		    		fit = le['ft_fundacao_osc']
		    		ft_fundacao_osc = fit.transform([ft_fundacao_osc])[0]
		    	except Exception as e :
		    		erros["ft_fundacao_osc"] = {}
		    		erros["ft_fundacao_osc"]['mensagem'] = '''Nao foi possivel aplicar o label encoder para o valor informado, caso seja um novo valor para o campo, sera necessario treinar novamente o modelo'''
		    		erros["ft_fundacao_osc"]['exception'] = str(e)

		    if cd_classe_atividade_economica_osc == None:
		    	cd_classe_atividade_economica_osc = -1
		    else:
		    	try:
		    		cd_classe_atividade_economica_osc = int(cd_classe_atividade_economica_osc)
		    	except Exception as e :
		    		erros["cd_classe_atividade_economica_osc"] = {}
		    		erros["cd_classe_atividade_economica_osc"]['mensagem'] = 'Nao foi possivel converter o valor informado, verifique caracter diferente de [0-9]' 
		    		erros["cd_classe_atividade_economica_osc"]['exception'] = str(e)

		    previsao = ''
		    if erros == {}:
		    	try:
		    		X_producao = [[cd_natureza_juridica_osc,ft_razao_social_osc,ft_nome_fantasia_osc,ft_fundacao_osc,cd_classe_atividade_economica_osc]]
		    		previsao = rf.predict(X_producao)
		    	except Exception as e :
		    		erros["erro_ao_aplicar_modelo"] = {}
		    		erros["erro_ao_aplicar_modelo"]['mensagem'] = 'Nao foi possivel aplicar o modelo para os valor informados.'
		    		erros["erro_ao_aplicar_modelo"]['exception'] = str(e)

		    resultado = {}
		    resultado["classificacao"] = {}
		    resultado["classificacao"]['area atuacao'] = list(previsao)
		    resultado["classificacao"]['erros'] = erros
		    resultado["classificacao"]['status'] = 'OK' if erros == {} else 'FALHA'
		    response = make_response(json.dumps(resultado,default=int))
		    response.content_type = "application/json"
		    return response

		app.debug = False
		app.run(host = '0.0.0.0', port = 5000)

#------------------------------------------------------------------------------
 # Metodo auxiliar para ler o arquivo de configuracao  
def readConfig(filepath):
	file = open(join(PATH,filepath))
	dict_config = {}

	for line in file:
		key, value = line.replace(" ","").replace("\n","").split("=")
		dict_config[key] = value

	return dict_config

#------------------------------------------------------------------------------
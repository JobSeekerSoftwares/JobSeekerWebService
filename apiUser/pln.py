#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import sys
import json
import requests
from nltk.corpus import wordnet

def traduz(frase):
	if len(frase) > 0:
		try:
			url = 'http://api.mymemory.translated.net/get?q=%s&langpair=pt|en' % frase
			response = requests.get(url)
			data = response.json()
			text = data['responseData']['translatedText']
			return text
		except:
			print('Erro: Sem rede ou caracter inválido.')

def palavras(frase):
    print('kkky')
    print(frase)
    palavras = frase.split()
	
    return palavras

def similaridade(fraseCV, fraseEmp):
    iguais = 0
    textCV = ''
    textEmp = ''
    textCV = traduz(fraseCV)
    while(type(textCV) is None):
        textCV = traduz(fraseCV)

    print('koiuyt')
    print(fraseEmp)
    textEmp = traduz(fraseEmp)
    while(type(textEmp) is None):
          textEmp = traduz(fraseEmp)
    wordsCV = palavras(textCV)
    print('kiu')
    print(textEmp)
    wordsEmp = palavras(textEmp)

	#wordsCV = [traduz(x) for x in palavras(fraseCV)]
	#wordsEmp = [traduz(x) for x in palavras(fraseEmp)]

	#print('CV: ')
	#print(wordsCV)
	#print('Emp: ')
	#print(wordsEmp)

    flag = 0
    for wordEmp in wordsEmp:
    	if flag==0:
    		for synEmp in wordnet.synsets(wordEmp):
    			if flag==0:
    				for lEmp in synEmp.lemmas():
    					if flag==0:
    						for wordCV in wordsCV:
    							if flag==0:
    								for synCV in wordnet.synsets(wordCV):
    									if flag==0:
    										for lCV in synCV.lemmas():
    											if lCV.name()==lEmp.name() and flag==0:
    												iguais+=1
    												flag = 1
    												break
    	flag=0

    return iguais/len(wordsEmp)
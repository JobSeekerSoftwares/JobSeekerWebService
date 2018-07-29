#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Função que separa os pontos chaves: reText.
# Por algum motivo o python não reconhece a biblioteca nltk quando se está usando a ide 64 bits, apenas
# a de 32 bits funcionou comigo. Deve ter algo haver com o modo como instalei não sei.

import math
import nltk
import networkx as nx
import os
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
from string import punctuation
from nltk.stem import RSLPStemmer
from nltk import data
import pickle


path = os.path.expanduser('C:/Users/jonat/Workspace/WebService/JobSeeker/JobSeeker/apiUser/tagger.pkl')

# Strings para testes
habilidades = "Atuação na área Administrativa, com experiência na coordenação, planejamento e controle das" \
              " atividades de diversas áreas, fixando políticas de gestão dos recursos financeiros," \
              " administrativos, estruturação e racionalização, tendo em vista os objetivos da organização. " \
              "Criação de estratégias de publicidade e marketing, promovendo a venda dos produtos e serviços."
experiencia = "03/1999 a 05/2012, vivência na supervisão das operações da empresa para que estejam em total" \
              " conformidade com a legislação ambiental vigente. Atuação na análise de vendas, definição de met" \
              "as, realização de vistas e acompanhamento do trabalho dos vendedores nos clientes, elaborando açõe" \
              "s para aumento dos resultados."
formacao = "Graduação em Administração de Empresas"
idiomas = "Inglês – Fluente. Espanhol – Intermediário."


# Retira a raiz das palavras. Exemplo: stem('estudando')= ['estud']
def stem(text):
    st = RSLPStemmer()
    return [st.stem(word) for word in word_tokenize(text)]


# Retorna o que a palavra é, pronome, adjetivo etc.
# é Preciso ter na mesma pasta o arquivo tagger.pkl, ele que identifica palavras portuguesas.
def tags(text):
        tagger = pickle.load(open(path, 'rb'))
        pt_sent_tokenizer = data.load("tokenizers/punkt/portuguese.pickle")
        sentences = pt_sent_tokenizer.tokenize(text)
        return tagger.tag(word_tokenize(text))


# divide uma frase em sentenças.
def get_sents(text):
        customStopWords = set(stopwords.words('portuguese')+list(punctuation))
        return [word for word in sent_tokenize(text) if word not in customStopWords]


# divide uma frase em palavras.
def get_words(text):
        customStopWords = set(stopwords.words('portuguese')+list(punctuation))
        return [word for word in word_tokenize(text) if word not in customStopWords]


# Resume um texto em N frases de acordo com a importância da frase para o texto. Apenas quando um texto
# é relativamente grande que isto é útil.
def summarize(text,n):
        sents = sent_tokenize(text)
        assert n <= len(sents)
        word_sent = word_tokenize(text.lower())
        _stopwords = set(stopwords.words('portuguese')+list(punctuation))
        word_sent = [word for word in word_sent if word not in _stopwords]	
        freq = FreqDist(word_sent)
        ranking = defaultdict(int)
        for i, sent in enumerate(sents):
                for w in word_tokenize(sent.lower()):
                        if w in freq:
                                ranking[i] += freq[w]
        sents_idx = nlargest(n, ranking, key=ranking.get)
        return [sents[j] for j in sorted(sents_idx)]


# Pega as palavras chave do texto.
def re_text(text):
        lista = []
        sents = get_sents(text)
        for sentence in sents:
                for word in word_tokenize(sentence):
                        if tags(word)[0][1] == 'NOUN' or tags(word)[0][1] == 'ADJ':
                                lista.append(word)
        return lista

def get_email(text):
    lista = get_words(text)
    try:
        ind = lista.index('gmail.com')
        return lista[ind-1]+'@gmail.com'
    except ValueError:
        return 'email@gmail.com'

def list_to_text(text):
    return ' '.join(text)

def bigger_list(list1, list2):
	if len(list1)>=len(list2):
		return list1
	return list2

def semelhanca(cv, vaga):
	#maior = bigger_list(cv, vaga)
	iguais = 0
	
	#if maior == cv:
	for i in range(0, len(vaga)):
		for j in range(0, len(cv)):
			if cv[j]==vaga[i]:
				iguais+=1
	#else:
	#for i in range(0, len(cv)):
	#	for j in range(0, len(vaga)):
	#		if cv[i]==vaga[j]:
	#			iguais.append(vaga[j])

	return iguais/len(vaga)

def semel(sentence1, sentence2):
    """
    Implementação da fórmula de semelhança entre duas sentenças.
    """
    w1, w2 = set(sentence1), set(sentence2)

    # Aqui a gente vê quantas palavras que estão nas frases se
    # repetem.
    repeticao = len(w1.intersection(w2))
    # Aqui a normalização.
    semelhanca = repeticao / (math.log(len(w1)) + math.log(len(w2)))

    return semelhanca

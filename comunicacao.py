import mysql.connector
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

class Comunicacao:

    def quebrarTexto(self, input_usuario):
        stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(string.punctuation))
        quebrar_user_text = word_tokenize(input_usuario)
        sentencas = [w for w in quebrar_user_text if not w.lower() in stopwords]
        sentencas = []

        for w in quebrar_user_text:
            if w not in stopwords:
                sentencas.append(w)
        return sentencas


    def conectarbanco(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mestrado_chatbot"
        )
        return connection

    def montaIds(self,ids):
        stringIds = str(ids)
        quebrar = stringIds.split(",")
        return quebrar

    def consultarIdsDocumentos(self, dadospesquisa):
        connection = self.conectarbanco()  # pega a conexão com o banco de dados
        cursor = connection.cursor()
        footstring = ', '.join(["'" + i + "'" for i in dadospesquisa])
        sql_execucao = "select * from dados_grama where palavra in ("+footstring+")"
        cursor.execute(sql_execucao)
        resultado = cursor.fetchall()
        mIds = []
        for x in resultado:
            docs = x[2]
            matr = self.montaIds(docs)
            for y in matr:
                if y not in mIds:
                    mIds.append(y)
        cursor.close()
        connection.close()
        return mIds

    def consultarResumoDocumentos(self, ids):
        connection = self.conectarbanco()  # pega a conexão com o banco de dados
        cursor = connection.cursor()
        footIds = ','.join(["" + i + "" for i in ids])
        print(footIds)
        print(len(footIds))
        tam = len(footIds)
        if footIds[tam-1] == ",":
            footIds = footIds[:-1]
        #sql_execucao2 = "select * from dados_chatbot where id in ("+footIds+")"
        sql_execucao2 = "select * from dados_chatbot where id in (1,7,15)"
        print(sql_execucao2)
        cursor.execute(sql_execucao2)
        resultado2 = cursor.fetchall()
        texto = ""
        for x in resultado2:
            resumo = x[4]
            texto = texto + resumo
        cursor.close()
        connection.close()
        return texto

    def fraseSentencas(self, texto_pronto):
        texto = texto_pronto
        sentencas = sent_tokenize(texto)
        palavras = word_tokenize(texto.lower())
        stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(string.punctuation))
        palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]
        frequencia = FreqDist(palavras_sem_stopwords)
        sentencas_importantes = defaultdict(int)
        for i, sentenca in enumerate(sentencas):
            for palavra in word_tokenize(sentenca.lower()):
                if palavra in frequencia:
                    sentencas_importantes[i] += frequencia[palavra]
        idx_sentencas_importantes = nlargest(10, sentencas_importantes, sentencas_importantes.get)
        for i in sorted(idx_sentencas_importantes):
            print("Sentencasss "+sentencas[i])
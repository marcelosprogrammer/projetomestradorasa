from comunicacao import Comunicacao
import sumarizar

objComunicacao = Comunicacao()
texto_quebrado = objComunicacao.quebrarTexto("ministro da saude")
#print(texto_quebrado)
ids = objComunicacao.consultarIdsDocumentos(texto_quebrado)
#print(ids)
texto_completo = objComunicacao.consultarResumoDocumentos(ids)
#objComunicacao.fraseSentencas(texto_completo)
t = sumarizar.Texto(texto_completo)
resumo = t.resumir()
print(resumo)
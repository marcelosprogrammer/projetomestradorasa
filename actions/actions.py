# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import mysql.connector
from typing import Any, Text, Dict, List
from comunicacao import Comunicacao
import sumarizar
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):
#
    def name(self) -> Text:
        return "action_hello_world"
#
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        objcomunicacao = Comunicacao()
        input_usuario = tracker.latest_message['text']
        texto_quebrado = objcomunicacao.quebrarTexto(input_usuario)
        ids = objcomunicacao.consultarIdsDocumentos(texto_quebrado)
        print(ids)
        texto_completo = objcomunicacao.consultarResumoDocumentos(ids)
        print(texto_completo)
        # objComunicacao.fraseSentencas(texto_completo)
        t = sumarizar.Texto(texto_completo)
        resumo = t.resumir()
        dispatcher.utter_message(text=resumo)
        return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import mysql.connector
from typing import Any, Text, Dict, List
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
        con = mysql.connector.connect(host="localhost", database="mestrado_chatbot", user="root", password="")
        if con.is_connected():
            cursor = con.cursor()
            cursor.execute("select id,palavra,documentos from dados_grama where palavra  = 'queiroga'")
            resultado = cursor.fetchall()
            print(resultado)
            retorno = []
            i = 0
            dadosstr = ""
            for dados in resultado:
                val1 = dados[0]
                val2 = dados[1]
                val3 = dados[2]
                dadosstr = dadosstr + str(val1) + str(val2) + str(val3) + "\n"
                print(""+str(val1))
                print(""+str(val2))
                print(""+str(val3))
                i = i+1
            print(dadosstr)
            print(retorno)
            dispatcher.utter_message("Conectado ao banco de dado")
        else:
            dispatcher.utter_message("Não conectado ao banco de dados")
        con.close()
        return []

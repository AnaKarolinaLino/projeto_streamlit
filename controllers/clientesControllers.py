import streamlit as st
import json 
import os

clientes = "data/data_clientes.json"

def carregar_clientes():
    if os.path.exists(clientes):
        with open(clientes, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    

def cadastrar_cliente(cliente):
    if not cliente:
        return "Não foi possível cadastrar."
    else:
        with open(clientes, "w", encoding="utf-8",) as arq_json:
            json.dump(cliente, arq_json, indent=4, ensure_ascii=False)
            return "Caadastro realizado com sucesso!"
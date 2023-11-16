# Importação da biblioteca
import pymongo
from time import sleep
# Conexão com o bando de dados(Sevidor, local)
client = pymongo.MongoClient("localhost", 27017)

# Criar o Banco
db = client["agenda"]

# Criação da coleção
contatos = db["contatos"]

# Inserir os dados(documentos)
indice = 1
quantidade = int(input("Quantos contatos vai inserir: "))

while indice <= quantidade:
    nome = input("Diga o nome do contado: ")
    sobrenome = input("Diga o sobrenome do contado: ")
    telefone = input("Diga o telefone do contado: ")
    email = input("Diga o email do contado: ")
    contato = dict(nome=nome, sobrenome=sobrenome, telefone=telefone, email=email)
    sleep(0.5)
    print(f"Esses documentos {contato} serão inseridos no MongoDB ")
    confirmar = input("Digite S(Sim) ou N(Não) para confirma o registro do contato: ")

    while confirmar not in ('S', 'N', 's', 'n'):
        confirmar = input("Digite novamente S(Sim) ou N(Não) para confirmar o registro do contato: ")

    if confirmar in ('S', 's'):
        contatos.insert_one(contato)
        sleep(1)
        print(f"Dados Inseridos foram {contato}")
        indice += 1

    elif confirmar in ('N', 'n'):
        alterar = input("Quer continuar a inserir...\nS(Sim) ou N(Não): ")

        while alterar not in ('S', 'N', 's', 'n'):
            alterar = input("Digite novamente se quer continuar a inserir...\nS(Sim) ou N(Não): ")

        if alterar in ('N', 'n'):
            break

# Impimir na tela dos dados
for contato in contatos.find():
    print(contato)

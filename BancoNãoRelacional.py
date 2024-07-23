from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco"]
collection = db["bank"]

# Função para adicionar um cliente
def adicionar_cliente(nome, cpf, email):
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "email": email
    }
    collection.insert_one(cliente)
    print(f"Cliente {nome} adicionado com sucesso!")

# Função para recuperar um cliente pelo CPF
def recuperar_cliente_por_cpf(cpf):
    cliente = collection.find_one({"cpf": cpf})
    if cliente:
        print(f"Cliente encontrado: {cliente}")
    else:
        print("Cliente não encontrado.")

# Função para recuperar todos os clientes
def recuperar_todos_clientes():
    clientes = collection.find()
    for cliente in clientes:
        print(cliente)

# Exemplo de uso
adicionar_cliente("João Silva", "123.456.789-00", "joao.silva@example.com")
adicionar_cliente("Maria Oliveira", "987.654.321-00", "maria.oliveira@example.com")

recuperar_cliente_por_cpf("123.456.789-00")
recuperar_todos_clientes()

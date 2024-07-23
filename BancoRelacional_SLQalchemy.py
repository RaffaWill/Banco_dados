from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Configuração do banco de dados
DATABASE_URL = "sqlite:///banco.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definição das classes Cliente e Conta
class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'contas'
    
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    saldo = Column(Float, default=0.0)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    
    cliente = relationship("Cliente", back_populates="contas")

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)

# Configuração da sessão
Session = sessionmaker(bind=engine)
session = Session()

# Funções para adicionar clientes e contas
def adicionar_cliente(nome, cpf, email):
    novo_cliente = Cliente(nome=nome, cpf=cpf, email=email)
    session.add(novo_cliente)
    session.commit()
    return novo_cliente

def adicionar_conta(cliente_id, tipo, saldo_inicial=0.0):
    nova_conta = Conta(cliente_id=cliente_id, tipo=tipo, saldo=saldo_inicial)
    session.add(nova_conta)
    session.commit()
    return nova_conta

# Exemplo de uso
cliente1 = adicionar_cliente("João Silva", "123.456.789-00", "joao.silva@example.com")
conta1 = adicionar_conta(cliente1.id, "Corrente", 1000.0)

print(f"Cliente: {cliente1.nome}, CPF: {cliente1.cpf}, Email: {cliente1.email}")
for conta in cliente1.contas:
    print(f"Conta {conta.tipo}, Saldo: {conta.saldo}")

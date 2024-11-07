from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

#Conectar ao Dialeto SQLite
engine = create_engine('sqlite:///meubanco.db', echo=True)
print("Conexão com SQLite estabelecida.")

Base = declarative_base()

# Criar tabelas do banco de dados
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
# Criar banco tabela do banco de dados
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session = Session()
# Inserior uma linha ao Banco

# novo_usuario = Usuario(nome='Mario', idade=24)
# Session.add(novo_usuario)
# Session.commit()

# with Session() as session:
#     novo_usuario = Usuario(nome='Maria', idade=24)
#     session.add(novo_usuario)

# print("Usuario inserido com sucesso.")

# Criando Query direto no codigo python para verificar se inseriu a linha corretamente
usuario =  Session.query(Usuario).filter_by(nome='').first()
print(f"Usuario encontrado: {usuario.nome}, Idade: {usuario.idade}")
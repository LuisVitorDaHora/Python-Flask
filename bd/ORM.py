from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as sessionmarker

engine = create_engine('sqlite:///banco.db', echo=True)

Base = declarative_base()

class Games(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)
    genero = Column(String(50), nullable=False)

Base.metadata.create_all(engine)

# Inserir daods no banco de dados
def adicionar_jogo(nome, ano, nota, genero):
    Session = sessionmarker.sessionmaker(bind=engine)
    session = Session()
    novo_jogo = Games(nome=nome, ano=ano, nota=nota, genero=genero)
    session.add(novo_jogo)
    session.commit()
    session.close()

# adicionar_jogo('The last of us', 2013, 10, 'Ação/Aventura')
# adicionar_jogo('God of War', 2018, 9.5, 'Ação/Aventura')

# Atualizar dados no banco de dados
def atualizar_jogo(id, nome=None, ano=None, nota=None, genero=None):
    Session = sessionmarker.sessionmaker(bind=engine)
    session = Session()
    jogo = session.query(Games).filter_by(id=id).first()
    if jogo:
        if nome is not None:
            jogo.nome = nome
        if ano is not None:
            jogo.ano = ano
        if nota is not None:
            jogo.nota = nota
        if genero is not None:
            jogo.genero = genero
        session.commit()
    session.close()

#atualizar_jogo(1, nome='The last of us 2', ano=2020, nota=9.5, genero='Ação/Aventura')

# Deletar dados no banco de dados
def excluir_jogo(id):
    Session = sessionmarker.sessionmaker(bind=engine)
    session = Session()
    jogo = session.query(Games).filter_by(id=id).first()
    if jogo:
        session.delete(jogo)
        session.commit()
    session.close()

#excluir_jogo(1)
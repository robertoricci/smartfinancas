# ============================================================================
# models/models.py
# ============================================================================
"""
Modelos de dados do sistema
"""
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    senha_hash = Column(String(256), nullable=False)
    nome = Column(String(100), nullable=False)
    ativo = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<Usuario(username='{self.username}', nome='{self.nome}')>"


class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cnpj_cpf = Column(String(20))
    telefone = Column(String(20))
    email = Column(String(100))
    endereco = Column(String(200))
    ativo = Column(Boolean, default=True)
    
    # Relacionamentos
    despesas_variaveis = relationship("DespesaVariavel", back_populates="fornecedor")
    notas_pagar = relationship("NotaPagar", back_populates="fornecedor")
    
    def __repr__(self):
        return f"<Fornecedor(nome='{self.nome}')>"


class DespesaFixa(Base):
    __tablename__ = 'despesas_fixas'
    
    id = Column(Integer, primary_key=True)
    descricao = Column(String(200), nullable=False)
    valor = Column(Float, nullable=False)
    dia_vencimento = Column(Integer, nullable=False)
    ativo = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<DespesaFixa(descricao='{self.descricao}', valor={self.valor})>"


class DespesaVariavel(Base):
    __tablename__ = 'despesas_variaveis'
    
    id = Column(Integer, primary_key=True)
    descricao = Column(String(200), nullable=False)
    categoria = Column(String(50))
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    
    # Relacionamentos
    fornecedor = relationship("Fornecedor", back_populates="despesas_variaveis")
    
    def __repr__(self):
        return f"<DespesaVariavel(descricao='{self.descricao}', categoria='{self.categoria}')>"


class Venda(Base):
    __tablename__ = 'vendas'
    
    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    cliente = Column(String(100), nullable=False)
    descricao = Column(String(200))
    valor = Column(Float, nullable=False)
    forma_pagamento = Column(String(50))
    observacoes = Column(String(500))
    
    def __repr__(self):
        return f"<Venda(cliente='{self.cliente}', valor={self.valor})>"


class NotaPagar(Base):
    __tablename__ = 'notas_pagar'
    
    id = Column(Integer, primary_key=True)
    data_emissao = Column(Date, nullable=False)
    data_vencimento = Column(Date, nullable=False)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    descricao = Column(String(200), nullable=False)
    valor = Column(Float, nullable=False)
    pago = Column(Boolean, default=False)
    data_pagamento = Column(Date)
    categoria = Column(String(50))
    
    # Relacionamentos
    fornecedor = relationship("Fornecedor", back_populates="notas_pagar")
    
    def __repr__(self):
        return f"<NotaPagar(descricao='{self.descricao}', valor={self.valor}, pago={self.pago})>"
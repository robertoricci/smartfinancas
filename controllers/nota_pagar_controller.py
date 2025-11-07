# ============================================================================
# controllers/nota_pagar_controller.py
# ============================================================================
"""
Controller para gerenciamento de notas a pagar
"""
from datetime import date
from models.models import NotaPagar


class NotaPagarController:
    def __init__(self, database):
        self.db = database
    
    def criar(self, data_emissao, data_vencimento, fornecedor_id, descricao, valor, categoria):
        """Registra uma nova nota a pagar"""
        session = self.db.get_session()
        try:
            nota = NotaPagar(
                data_emissao=data_emissao,
                data_vencimento=data_vencimento,
                fornecedor_id=fornecedor_id,
                descricao=descricao,
                valor=valor,
                categoria=categoria
            )
            session.add(nota)
            session.commit()
            return True, "Nota registrada"
        except Exception as e:
            session.rollback()
            return False, f"Erro: {str(e)}"
        finally:
            session.close()
    
    def listar_pendentes(self):
        """Lista todas as notas pendentes de pagamento"""
        session = self.db.get_session()
        try:
            notas = session.query(NotaPagar).filter_by(pago=False).order_by(
                NotaPagar.data_vencimento
            ).all()
            
            # Expunge para usar fora da sessão
            for n in notas:
                session.expunge(n)
            return notas
        finally:
            session.close()
    
    def marcar_como_pago(self, nota_id):
        """Marca uma nota como paga"""
        session = self.db.get_session()
        try:
            nota = session.query(NotaPagar).filter_by(id=nota_id).first()
            if nota:
                nota.pago = True
                nota.data_pagamento = date.today()
                session.commit()
                return True, "Pagamento registrado"
            return False, "Nota não encontrada"
        except Exception as e:
            session.rollback()
            return False, f"Erro: {str(e)}"
        finally:
            session.close()
    
    def listar_por_periodo(self, data_inicio, data_fim, filtro='todas'):
        """Lista notas em um período com filtro"""
        session = self.db.get_session()
        try:
            query = session.query(NotaPagar).filter(
                NotaPagar.data_vencimento >= data_inicio,
                NotaPagar.data_vencimento <= data_fim
            )
            
            if filtro == 'pendentes':
                query = query.filter_by(pago=False)
            elif filtro == 'pagas':
                query = query.filter_by(pago=True)
            
            notas = query.order_by(NotaPagar.data_vencimento).all()
            
            # Expunge para usar fora da sessão
            for n in notas:
                session.expunge(n)
            return notas
        finally:
            session.close()

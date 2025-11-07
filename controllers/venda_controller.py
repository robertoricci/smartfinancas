# ============================================================================
# controllers/venda_controller.py
# ============================================================================
"""
Controller para gerenciamento de vendas
"""
from models.models import Venda


class VendaController:
    def __init__(self, database):
        self.db = database
    
    def criar(self, data, cliente, descricao, valor, forma_pagamento, observacoes=None):
        """Registra uma nova venda"""
        session = self.db.get_session()
        try:
            venda = Venda(
                data=data,
                cliente=cliente,
                descricao=descricao,
                valor=valor,
                forma_pagamento=forma_pagamento,
                observacoes=observacoes
            )
            session.add(venda)
            session.commit()
            return True, "Venda registrada"
        except Exception as e:
            session.rollback()
            return False, f"Erro: {str(e)}"
        finally:
            session.close()
    
    def listar_por_periodo(self, data_inicio, data_fim):
        """Lista vendas em um período"""
        session = self.db.get_session()
        try:
            vendas = session.query(Venda).filter(
                Venda.data >= data_inicio,
                Venda.data <= data_fim
            ).order_by(Venda.data.desc()).all()
            
            # Expunge para usar fora da sessão
            for v in vendas:
                session.expunge(v)
            return vendas
        finally:
            session.close()
    
    def listar_recentes(self, limite=15):
        """Lista as vendas mais recentes"""
        session = self.db.get_session()
        try:
            vendas = session.query(Venda).order_by(Venda.data.desc()).limit(limite).all()
            result = [{
                'id': v.id,
                'data': v.data.strftime('%d/%m/%Y'),
                'cliente': v.cliente,
                'descricao': v.descricao[:30] + '...' if v.descricao and len(v.descricao) > 30 else v.descricao,
                'valor': v.valor,
                'forma_pagamento': v.forma_pagamento
            } for v in vendas]
            return result
        finally:
            session.close()

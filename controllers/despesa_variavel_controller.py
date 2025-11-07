# ============================================================================
# controllers/despesa_variavel_controller.py
# ============================================================================
"""
Controller para gerenciamento de despesas variáveis
"""
from models.models import DespesaVariavel


class DespesaVariavelController:
    def __init__(self, database):
        self.db = database
    
    def criar(self, descricao, categoria, fornecedor_id=None):
        """Cria uma nova categoria de despesa variável"""
        session = self.db.get_session()
        try:
            despesa = DespesaVariavel(
                descricao=descricao,
                categoria=categoria,
                fornecedor_id=fornecedor_id
            )
            session.add(despesa)
            session.commit()
            return True, "Categoria cadastrada"
        except Exception as e:
            session.rollback()
            return False, f"Erro: {str(e)}"
        finally:
            session.close()
    
    def listar_todas(self):
        """Lista todas as categorias de despesas variáveis"""
        session = self.db.get_session()
        try:
            despesas = session.query(DespesaVariavel).all()
            result = [{
                'id': d.id,
                'descricao': d.descricao,
                'categoria': d.categoria,
                'fornecedor': d.fornecedor.nome if d.fornecedor else '-'
            } for d in despesas]
            return result
        finally:
            session.close()
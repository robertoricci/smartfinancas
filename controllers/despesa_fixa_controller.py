# ============================================================================
# controllers/despesa_fixa_controller.py
# ============================================================================
"""
Controller para gerenciamento de despesas fixas
"""
from models.models import DespesaFixa


class DespesaFixaController:
    def __init__(self, database):
        self.db = database
    
    def criar(self, descricao, valor, dia_vencimento):
        """Cria uma nova despesa fixa"""
        session = self.db.get_session()
        try:
            despesa = DespesaFixa(
                descricao=descricao,
                valor=valor,
                dia_vencimento=dia_vencimento
            )
            session.add(despesa)
            session.commit()
            return True, "Despesa fixa cadastrada"
        except Exception as e:
            session.rollback()
            return False, f"Erro: {str(e)}"
        finally:
            session.close()
    
    def listar_ativas(self):
        """Lista todas as despesas fixas ativas"""
        session = self.db.get_session()
        try:
            despesas = session.query(DespesaFixa).filter_by(ativo=True).all()
            result = [{
                'id': d.id,
                'descricao': d.descricao,
                'valor': d.valor,
                'dia_vencimento': d.dia_vencimento
            } for d in despesas]
            total = sum([d.valor for d in despesas])
            return result, total
        finally:
            session.close()
    
    def desativar(self, despesa_id):
        """Desativa uma despesa fixa"""
        session = self.db.get_session()
        try:
            despesa = session.query(DespesaFixa).filter_by(id=despesa_id).first()
            if despesa:
                despesa.ativo = False
                session.commit()
                return True, "Despesa desativada"
            return False, "Despesa não encontrada"
        except Exception as e:
            session.rollback()
            return False, f"Erro: {str(e)}"
        finally:
            session.close()

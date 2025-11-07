# ============================================================================
# controllers/relatorio_controller.py
# ============================================================================
"""
Controller para geração de relatórios
"""
from models.models import Venda, NotaPagar


class RelatorioController:
    def __init__(self, database):
        self.db = database
    
    def obter_dashboard(self, data_inicio, data_fim):
        """Obtém dados para o dashboard"""
        session = self.db.get_session()
        try:
            # Vendas
            vendas = session.query(Venda).filter(
                Venda.data >= data_inicio,
                Venda.data <= data_fim
            ).all()
            total_vendas = sum([v.valor for v in vendas])
            
            # Despesas
            notas = session.query(NotaPagar).filter(
                NotaPagar.data_vencimento >= data_inicio,
                NotaPagar.data_vencimento <= data_fim
            ).all()
            total_despesas = sum([n.valor for n in notas])
            total_pago = sum([n.valor for n in notas if n.pago])
            total_a_pagar = total_despesas - total_pago
            
            saldo = total_vendas - total_pago
            notas_pendentes = [n for n in notas if not n.pago]
            
            # Expunge para usar fora da sessão
            for v in vendas:
                session.expunge(v)
            for n in notas_pendentes:
                session.expunge(n)
            
            return {
                'total_vendas': total_vendas,
                'total_despesas': total_despesas,
                'total_pago': total_pago,
                'total_a_pagar': total_a_pagar,
                'saldo': saldo,
                'vendas': vendas,
                'notas_pendentes': notas_pendentes
            }
        finally:
            session.close()
    
    def obter_por_categoria(self, data_inicio, data_fim):
        """Obtém despesas agrupadas por categoria"""
        session = self.db.get_session()
        try:
            despesas = session.query(NotaPagar).filter(
                NotaPagar.data_vencimento >= data_inicio,
                NotaPagar.data_vencimento <= data_fim,
                NotaPagar.pago == True
            ).all()
            
            categorias = {}
            for d in despesas:
                cat = d.categoria or 'Sem Categoria'
                if cat not in categorias:
                    categorias[cat] = 0
                categorias[cat] += d.valor
            
            return categorias
        finally:
            session.close()

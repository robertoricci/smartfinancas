# ============================================================================
# views/dashboard_view.py
# ============================================================================
"""
View para dashboard principal
"""
import streamlit as st
import pandas as pd
from datetime import date


class DashboardView:
    @staticmethod
    def render(relatorio_controller):
        """Renderiza o dashboard"""
        st.title("📊 Dashboard - Fluxo de Caixa")
        st.markdown("Visão geral das finanças da marcenaria")
        st.markdown("---")
        
        # Filtros de período
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            data_inicio = st.date_input(
                "📅 Data Início",
                value=date.today().replace(day=1)
            )
        with col2:
            data_fim = st.date_input(
                "📅 Data Fim",
                value=date.today()
            )
        with col3:
            st.write("")
            st.write("")
            if st.button("🔄 Atualizar", use_container_width=True):
                st.rerun()
        
        # Obter dados
        dados = relatorio_controller.obter_dashboard(data_inicio, data_fim)
        
        # Métricas principais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="💰 Receitas",
                value=f"R$ {dados['total_vendas']:,.2f}",
                delta=None
            )
        
        with col2:
            st.metric(
                label="💸 Despesas Pagas",
                value=f"R$ {dados['total_pago']:,.2f}",
                delta=None
            )
        
        with col3:
            st.metric(
                label="⚠️ A Pagar",
                value=f"R$ {dados['total_a_pagar']:,.2f}",
                delta=None
            )
        
        with col4:
            percentual = ((dados['saldo']/dados['total_vendas'])*100) if dados['total_vendas'] > 0 else 0
            st.metric(
                label="📈 Saldo",
                value=f"R$ {dados['saldo']:,.2f}",
                delta=f"{percentual:.1f}%"
            )
        
        st.markdown("---")
        
        # Detalhamentos
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💵 Vendas Recentes")
            if dados['vendas']:
                df_vendas = pd.DataFrame([{
                    'Data': v.data.strftime('%d/%m/%Y'),
                    'Cliente': v.cliente,
                    'Valor': f"R$ {v.valor:,.2f}"
                } for v in dados['vendas'][-10:]])
                st.dataframe(df_vendas, use_container_width=True, hide_index=True)
            else:
                st.info("ℹ️ Nenhuma venda no período selecionado")
        
        with col2:
            st.subheader("📋 Contas a Vencer")
            if dados['notas_pendentes']:
                df_pendentes = pd.DataFrame([{
                    'Vencimento': n.data_vencimento.strftime('%d/%m/%Y'),
                    'Fornecedor': n.fornecedor.nome if n.fornecedor else '-',
                    'Valor': f"R$ {n.valor:,.2f}"
                } for n in dados['notas_pendentes'][:10]])
                st.dataframe(df_pendentes, use_container_width=True, hide_index=True)
            else:
                st.success("✅ Nenhuma conta pendente no período!")

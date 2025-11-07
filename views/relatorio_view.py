# ============================================================================
# views/relatorio_view.py
# ============================================================================
"""
View para relatórios
"""
import streamlit as st
import pandas as pd
from datetime import date


class RelatorioView:
    @staticmethod
    def render_despesas_pagar(nota_controller):
        """Renderiza o relatório de despesas a pagar"""
        st.subheader("📊 Relatório de Despesas a Pagar")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            filtro = st.selectbox("Filtrar por", ["todas", "pendentes", "pagas"])
        with col2:
            data_inicio = st.date_input("De", value=date.today().replace(day=1), key="desp_inicio")
        with col3:
            data_fim = st.date_input("Até", value=date.today(), key="desp_fim")
        
        notas = nota_controller.listar_por_periodo(data_inicio, data_fim, filtro)
        
        if notas:
            df = pd.DataFrame([{
                'Data Vencimento': n.data_vencimento.strftime('%d/%m/%Y'),
                'Fornecedor': n.fornecedor.nome if n.fornecedor else '-',
                'Descrição': n.descricao,
                'Categoria': n.categoria,
                'Valor': n.valor,
                'Status': '✅ Pago' if n.pago else '⏳ Pendente',
                'Data Pagamento': n.data_pagamento.strftime('%d/%m/%Y') if n.data_pagamento else '-'
            } for n in notas])
            
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("💰 Total", f"R$ {df['Valor'].sum():,.2f}")
            with col2:
                pagas = df[df['Status'] == '✅ Pago']['Valor'].sum()
                st.metric("✅ Pagas", f"R$ {pagas:,.2f}")
            with col3:
                pendentes = df[df['Status'] == '⏳ Pendente']['Valor'].sum()
                st.metric("⏳ Pendentes", f"R$ {pendentes:,.2f}")
        else:
            st.info("ℹ️ Nenhuma despesa encontrada no período")
    
    @staticmethod
    def render_fluxo_caixa(relatorio_controller, venda_controller, nota_controller):
        """Renderiza o relatório de fluxo de caixa"""
        st.subheader("📊 Fluxo de Caixa")
        
        col1, col2 = st.columns(2)
        with col1:
            data_inicio = st.date_input("Período De", value=date.today().replace(day=1), key="flux_inicio")
        with col2:
            data_fim = st.date_input("Período Até", value=date.today(), key="flux_fim")
        
        vendas = venda_controller.listar_por_periodo(data_inicio, data_fim)
        despesas = nota_controller.listar_por_periodo(data_inicio, data_fim, 'pagas')
        
        total_receitas = sum([v.valor for v in vendas])
        total_despesas = sum([d.valor for d in despesas])
        saldo = total_receitas - total_despesas
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("💰 Receitas", f"R$ {total_receitas:,.2f}")
        with col2:
            st.metric("💸 Despesas", f"R$ {total_despesas:,.2f}")
        with col3:
            percentual = ((saldo/total_receitas)*100) if total_receitas > 0 else 0
            st.metric("📊 Saldo", f"R$ {saldo:,.2f}", delta=f"{percentual:.1f}%")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💵 Receitas Detalhadas")
            if vendas:
                df_vendas = pd.DataFrame([{
                    'Data': v.data.strftime('%d/%m/%Y'),
                    'Cliente': v.cliente,
                    'Valor': f"R$ {v.valor:,.2f}"
                } for v in vendas])
                st.dataframe(df_vendas, use_container_width=True, hide_index=True)
            else:
                st.info("ℹ️ Sem receitas no período")
        
        with col2:
            st.markdown("### 💸 Despesas Detalhadas")
            if despesas:
                df_despesas = pd.DataFrame([{
                    'Data': d.data_pagamento.strftime('%d/%m/%Y') if d.data_pagamento else '-',
                    'Fornecedor': d.fornecedor.nome if d.fornecedor else '-',
                    'Valor': f"R$ {d.valor:,.2f}"
                } for d in despesas])
                st.dataframe(df_despesas, use_container_width=True, hide_index=True)
            else:
                st.info("ℹ️ Sem despesas no período")
    
    @staticmethod
    def render_categorias(relatorio_controller):
        """Renderiza o relatório por categoria"""
        st.subheader("📊 Despesas por Categoria")
        
        col1, col2 = st.columns(2)
        with col1:
            data_inicio = st.date_input("De", value=date.today().replace(day=1), key="cat_inicio")
        with col2:
            data_fim = st.date_input("Até", value=date.today(), key="cat_fim")
        
        categorias = relatorio_controller.obter_por_categoria(data_inicio, data_fim)
        
        if categorias:
            df = pd.DataFrame([
                {'Categoria': cat, 'Valor': valor}
                for cat, valor in categorias.items()
            ]).sort_values('Valor', ascending=False)
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.bar_chart(df.set_index('Categoria'))
            
            with col2:
                for _, row in df.iterrows():
                    st.metric(row['Categoria'], f"R$ {row['Valor']:,.2f}")
            
            st.markdown("---")
            df['Valor'] = df['Valor'].apply(lambda x: f"R$ {x:,.2f}")
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("ℹ️ Nenhuma despesa paga no período")

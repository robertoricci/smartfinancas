# ============================================================================
# views/venda_view.py
# ============================================================================
"""
View para lançamento de vendas
"""
import streamlit as st
import pandas as pd
from datetime import date
from config import FORMAS_PAGAMENTO


class VendaView:
    @staticmethod
    def render(venda_controller):
        """Renderiza a interface de vendas"""
        st.subheader("💰 Lançamento de Vendas")
        
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.markdown("### ➕ Nova Venda")
            
            with st.form("form_venda", clear_on_submit=True):
                data_venda = st.date_input("Data *", value=date.today())
                cliente = st.text_input("Cliente *", placeholder="Nome do cliente")
                descricao = st.text_area(
                    "Descrição do Serviço/Produto",
                    placeholder="Detalhe o que foi vendido..."
                )
                valor = st.number_input("Valor (R$) *", min_value=0.0, step=0.01, format="%.2f")
                forma_pagamento = st.selectbox("Forma de Pagamento *", FORMAS_PAGAMENTO)
                observacoes = st.text_area("Observações", placeholder="Informações adicionais...")
                
                submitted = st.form_submit_button("💾 Lançar Venda", use_container_width=True)
                
                if submitted:
                    if cliente and valor > 0:
                        sucesso, mensagem = venda_controller.criar(
                            data_venda, cliente, descricao, valor,
                            forma_pagamento, observacoes
                        )
                        if sucesso:
                            st.success(f"✅ {mensagem}")
                            st.rerun()
                        else:
                            st.error(f"❌ {mensagem}")
                    else:
                        st.error("❌ Preencha os campos obrigatórios!")
        
        with col2:
            st.markdown("### 📋 Vendas Recentes")
            vendas = venda_controller.listar_recentes(15)
            
            if vendas:
                df = pd.DataFrame(vendas)
                df['Valor'] = df['valor'].apply(lambda x: f"R$ {x:,.2f}")
                df_display = df[['Data', 'Cliente', 'Descrição', 'Valor', 'Pagamento']].copy()
                df_display.columns = ['Data', 'Cliente', 'Descrição', 'Valor', 'Pagamento']
                st.dataframe(df_display, use_container_width=True, hide_index=True)
                
                total = sum([v['valor'] for v in vendas])
                st.caption(f"📊 Total: R$ {total:,.2f}")
            else:
                st.info("ℹ️ Nenhuma venda lançada ainda")

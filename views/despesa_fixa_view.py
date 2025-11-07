# ============================================================================
# views/despesa_fixa_view.py
# ============================================================================
"""
View para cadastro de despesas fixas
"""
import streamlit as st
import pandas as pd


class DespesaFixaView:
    @staticmethod
    def render(despesa_fixa_controller):
        """Renderiza a interface de despesas fixas"""
        st.subheader("📌 Despesas Fixas Mensais")
        
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.markdown("### ➕ Nova Despesa Fixa")
            
            with st.form("form_despesa_fixa", clear_on_submit=True):
                descricao = st.text_input("Descrição *", placeholder="Ex: Aluguel do galpão")
                valor = st.number_input("Valor (R$) *", min_value=0.0, step=0.01, format="%.2f")
                dia_vencimento = st.number_input(
                    "Dia do Vencimento *",
                    min_value=1,
                    max_value=31,
                    value=10,
                    help="Dia do mês em que a despesa vence"
                )
                
                submitted = st.form_submit_button("💾 Cadastrar", use_container_width=True)
                
                if submitted:
                    if descricao and valor > 0:
                        sucesso, mensagem = despesa_fixa_controller.criar(
                            descricao, valor, dia_vencimento
                        )
                        if sucesso:
                            st.success(f"✅ {mensagem}")
                            st.rerun()
                        else:
                            st.error(f"❌ {mensagem}")
                    else:
                        st.error("❌ Preencha todos os campos obrigatórios!")
        
        with col2:
        
            st.markdown("### 📋 Lista de Despesas Fixas")
            despesas, total = despesa_fixa_controller.listar_ativas()

            if despesas:
                df = pd.DataFrame(despesas)

                # Renomeia colunas para exibição amigável
                df.rename(columns={
                    'descricao': 'Descrição',
                    'valor': 'Valor',
                    'dia_vencimento': 'Dia Vencimento'
                }, inplace=True)

                # Formata o valor
                df['Valor'] = df['Valor'].apply(lambda x: f"R$ {x:,.2f}")

                # Seleciona colunas para exibição
                df_display = df[['Descrição', 'Valor', 'Dia Vencimento']].copy()

                # Exibe tabela
                st.dataframe(df_display, use_container_width=True, hide_index=True)

                st.markdown("---")
                col_a, col_b, col_c = st.columns(3)
                with col_b:
                    st.metric("💰 Total Mensal", f"R$ {total:,.2f}")
            else:
                st.info("ℹ️ Nenhuma despesa fixa cadastrada")


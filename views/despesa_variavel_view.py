# ============================================================================
# views/despesa_variavel_view.py
# ============================================================================
"""
View para cadastro de despesas variáveis
"""
import streamlit as st
import pandas as pd
from config import CATEGORIAS_DESPESA


class DespesaVariavelView:
    @staticmethod
    def render(despesa_variavel_controller, fornecedor_controller):
        """Renderiza a interface de despesas variáveis"""
        st.subheader("🔄 Categorias de Despesas Variáveis")
        
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.markdown("### ➕ Nova Categoria")
            
            with st.form("form_despesa_variavel", clear_on_submit=True):
                descricao = st.text_input("Descrição *", placeholder="Ex: Compra de pregos")
                categoria = st.selectbox("Categoria *", CATEGORIAS_DESPESA[:5])
                
                fornecedores = fornecedor_controller.obter_todos()
                if fornecedores:
                    fornecedor_opcoes = {f.id: f.nome for f in fornecedores}
                    fornecedor_id = st.selectbox(
                        "Fornecedor Padrão",
                        options=[None] + list(fornecedor_opcoes.keys()),
                        format_func=lambda x: "Nenhum" if x is None else fornecedor_opcoes[x]
                    )
                else:
                    fornecedor_id = None
                    st.info("ℹ️ Cadastre fornecedores primeiro")
                
                submitted = st.form_submit_button("💾 Cadastrar", use_container_width=True)
                
                if submitted:
                    if descricao:
                        sucesso, mensagem = despesa_variavel_controller.criar(
                            descricao, categoria, fornecedor_id
                        )
                        if sucesso:
                            st.success(f"✅ {mensagem}")
                            st.rerun()
                        else:
                            st.error(f"❌ {mensagem}")
                    else:
                        st.error("❌ A descrição é obrigatória!")
        
        with col2:
            st.markdown("### 📋 Lista de Categorias")
            despesas = despesa_variavel_controller.listar_todas()
            
            if despesas:
                df = pd.DataFrame(despesas)
                df_display = df[['Descrição', 'Categoria', 'Fornecedor']].copy()
                st.dataframe(df_display, use_container_width=True, hide_index=True)
                
                st.caption(f"📊 Total: {len(despesas)} categorias cadastradas")
            else:
                st.info("ℹ️ Nenhuma categoria cadastrada")

# ============================================================================
# views/fornecedor_view.py
# ============================================================================
"""
View para cadastro de fornecedores
"""
import streamlit as st
import pandas as pd


class FornecedorView:
    @staticmethod
    def render(fornecedor_controller):
        """Renderiza a interface de fornecedores"""
        st.subheader("👥 Fornecedores")
        
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.markdown("### ➕ Novo Fornecedor")
            
            with st.form("form_fornecedor", clear_on_submit=True):
                nome = st.text_input("Nome *", placeholder="Ex: Madeireira Silva")
                cnpj_cpf = st.text_input("CNPJ/CPF", placeholder="00.000.000/0000-00")
                telefone = st.text_input("Telefone", placeholder="(00) 00000-0000")
                email = st.text_input("Email", placeholder="contato@fornecedor.com")
                endereco = st.text_area("Endereço", placeholder="Rua, número, bairro, cidade")
                
                submitted = st.form_submit_button("💾 Cadastrar", use_container_width=True)
                
                if submitted:
                    if nome:
                        sucesso, mensagem = fornecedor_controller.criar(
                            nome, cnpj_cpf, telefone, email, endereco
                        )
                        if sucesso:
                            st.success(f"✅ {mensagem}")
                            st.rerun()
                        else:
                            st.error(f"❌ {mensagem}")
                    else:
                        st.error("❌ O campo Nome é obrigatório!")
        
        with col2:
                st.markdown("### 📋 Lista de Fornecedores")
                fornecedores = fornecedor_controller.listar_ativos()

                if fornecedores:
                    df = pd.DataFrame(fornecedores)

                    # Renomeia colunas para exibição amigável
                    df.rename(columns={
                        'id': 'ID',
                        'nome': 'Nome',
                        'cnpj_cpf': 'CNPJ/CPF',
                        'telefone': 'Telefone',
                        'email': 'Email',
                        'endereco': 'Endereço'
                    }, inplace=True)

                    # Seleciona colunas desejadas
                    df_display = df[['ID', 'Nome', 'CNPJ/CPF', 'Telefone', 'Email']].copy()

                    # Exibe tabela interativa
                    st.dataframe(df_display, use_container_width=True, hide_index=True)
                    st.caption(f"📊 Total: {len(fornecedores)} fornecedores cadastrados")
                else:
                    st.info("ℹ️ Nenhum fornecedor cadastrado ainda")


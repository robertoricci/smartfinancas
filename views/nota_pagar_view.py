# ============================================================================
# views/nota_pagar_view.py
# ============================================================================
"""
View para gerenciamento de notas a pagar
"""
import streamlit as st
from datetime import date
from config import CATEGORIAS_DESPESA


class NotaPagarView:
    @staticmethod
    def render(nota_controller, fornecedor_controller):
        """Renderiza a interface de notas a pagar"""
        st.subheader("📄 Notas a Pagar")
        
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.markdown("### ➕ Nova Nota")
            
            with st.form("form_nota_pagar", clear_on_submit=True):
                data_emissao = st.date_input("Data Emissão *", value=date.today())
                data_vencimento = st.date_input("Data Vencimento *", value=date.today())
                
                fornecedores = fornecedor_controller.obter_todos()
                if fornecedores:
                    fornecedor_opcoes = {f.id: f.nome for f in fornecedores}
                    fornecedor_id = st.selectbox(
                        "Fornecedor *",
                        options=list(fornecedor_opcoes.keys()),
                        format_func=lambda x: fornecedor_opcoes[x]
                    )
                else:
                    fornecedor_id = None
                    st.warning("⚠️ Cadastre fornecedores primeiro!")
                
                descricao = st.text_input("Descrição *", placeholder="Ex: Nota Fiscal 12345")
                valor = st.number_input("Valor (R$) *", min_value=0.0, step=0.01, format="%.2f")
                categoria = st.selectbox("Categoria *", CATEGORIAS_DESPESA)
                
                submitted = st.form_submit_button("💾 Lançar Nota", use_container_width=True)
                
                if submitted:
                    if fornecedor_id and descricao and valor > 0:
                        sucesso, mensagem = nota_controller.criar(
                            data_emissao, data_vencimento, fornecedor_id,
                            descricao, valor, categoria
                        )
                        if sucesso:
                            st.success(f"✅ {mensagem}")
                            st.rerun()
                        else:
                            st.error(f"❌ {mensagem}")
                    else:
                        st.error("❌ Preencha todos os campos obrigatórios!")
        
        with col2:
            st.markdown("### 📋 Notas Pendentes")
            notas = nota_controller.listar_pendentes()
            
            if notas:
                for nota in notas:
                    # Verificar se está vencida
                    vencida = nota.data_vencimento < date.today()
                    status_icon = "🔴" if vencida else "🟡"
                    
                    with st.expander(
                        f"{status_icon} {nota.fornecedor.nome if nota.fornecedor else '-'} - "
                        f"R$ {nota.valor:,.2f}"
                    ):
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.write(f"**📅 Vencimento:** {nota.data_vencimento.strftime('%d/%m/%Y')}")
                            st.write(f"**📝 Descrição:** {nota.descricao}")
                        with col_b:
                            st.write(f"**🏷️ Categoria:** {nota.categoria}")
                            if vencida:
                                st.error("⚠️ VENCIDA")
                        
                        if st.button(f"✅ Marcar como Pago", key=f"pagar_{nota.id}", use_container_width=True):
                            sucesso, mensagem = nota_controller.marcar_como_pago(nota.id)
                            if sucesso:
                                st.success(mensagem)
                                st.rerun()
                            else:
                                st.error(mensagem)
            else:
                st.success("✅ Nenhuma nota pendente!")

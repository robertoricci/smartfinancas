# ============================================================================
# views/login_view.py
# ============================================================================
"""
View para tela de login
"""
import streamlit as st


class LoginView:
    @staticmethod
    def render(usuario_controller):
        """Renderiza a tela de login"""
        st.title("🪵 Sistema de Gestão - Marcenaria")
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.subheader("Login")
            
            with st.form("form_login3"):
                username = st.text_input("Usuário")
                senha = st.text_input("Senha", type="password")
                submit = st.form_submit_button("Entrar", use_container_width=True)
                
                if submit:
                    if usuario_controller.verificar_login(username, senha):
                        st.session_state.logado = True
                        st.session_state.username = username
                        st.success("Login realizado com sucesso!")
                        st.rerun()
                    else:
                        st.error("❌ Usuário ou senha inválidos!")
            
            st.info("👤 **Usuário padrão:** admin | **Senha:** admin123")

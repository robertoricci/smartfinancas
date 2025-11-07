import streamlit as st

import uuid  # para gerar chave única

class LoginView:
    @staticmethod
    def render(usuario_controller):
        """Renderiza a tela de login estilizada para navegação dinâmica"""

        ###st.set_page_config(page_title="Login", page_icon="🔐")

        st.markdown(
            """
            <style>
                .login-box {
                    background-color: #f9f9f9;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    width: 100%;
                    max-width: 400px;
                    margin: auto;
                    margin-top: 50px;
                    animation: fadeIn 0.6s ease-out;
                }
                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(-10px); }
                    to { opacity: 1; transform: translateY(0); }
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown("## 🪵 Sistema de Gestão - Marcenaria")
        st.markdown("### 🔐 Login")

        form_key = f"form_login_{uuid.uuid4()}"  # chave única para evitar conflito

        with st.form(form_key):
            username = st.text_input("👤 Usuário", placeholder="Digite seu nome de usuário")
            senha = st.text_input("🔑 Senha", type="password", placeholder="Digite sua senha")
            submit = st.form_submit_button("🚪 Entrar", use_container_width=True)

            if submit:
                if usuario_controller.verificar_login(username, senha):
                    st.session_state.logado = True
                    st.session_state.username = username
                    st.success("✅ Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("❌ Usuário ou senha inválidos!")

        st.markdown("👤 <strong>Usuário padrão:</strong> admin<br>🔑 <strong>Senha:</strong> admin123", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

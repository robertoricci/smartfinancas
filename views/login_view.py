import streamlit as st

class LoginView:
    @staticmethod
    def render(usuario_controller):
        """Renderiza a tela de login com estilo aprimorado"""
        st.markdown(
            """
            <style>
                .login-box {
                    background-color: #f9f9f9;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    animation: fadeIn 0.6s ease-out;
                }
                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(-10px); }
                    to { opacity: 1; transform: translateY(0); }
                }
                .login-title {
                    text-align: center;
                    font-size: 28px;
                    color: #4B8BBE;
                    margin-bottom: 20px;
                }
                .login-footer {
                    text-align: center;
                    font-size: 14px;
                    color: #666;
                    margin-top: 20px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="login-title">🪵 Sistema de Gestão - Marcenaria</div>', unsafe_allow_html=True)
        st.markdown("---")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div class="login-box">', unsafe_allow_html=True)
            st.subheader("🔐 Login")

            with st.form("form_login2"):
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

            st.markdown('<div class="login-footer">👤 <strong>Usuário padrão:</strong> admin<br>🔑 <strong>Senha:</strong> admin123</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

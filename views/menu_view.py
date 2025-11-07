# ============================================================================
# views/menu_view.py
# ============================================================================
"""
View para menu lateral
"""
import streamlit as st


class MenuView:
    @staticmethod
    def render():
        """Renderiza o menu lateral"""
        with st.sidebar:
            st.title("🪵 Marcenaria")
            st.markdown(f"**👤 Usuário:** {st.session_state.username}")
            st.markdown("---")
            
            opcao = st.radio(
                "📋 Menu Principal",
                [
                    "Dashboard",
                    "Cadastros",
                    "Lançamentos",
                    "Relatórios",
                    "Sair"
                ],
                label_visibility="collapsed"
            )
            
            st.markdown("---")
            st.caption("Sistema de Gestão Financeira v1.0")
            
            if opcao == "Sair":
                st.session_state.logado = False
                st.rerun()
        
        return opcao




# import streamlit as st


# class MenuView:
#     @staticmethod
#     def render():
#         """Renderiza o menu lateral estilizado com animação"""
#         with st.sidebar:
#             st.markdown(
#                 """
#                 <style>
#                     /* Animação de entrada */
#                     @keyframes fadeIn {
#                         from { opacity: 0; transform: translateY(-10px); }
#                         to { opacity: 1; transform: translateY(0); }
#                     }

#                     .sidebar-title {
#                         font-size: 24px;
#                         font-weight: bold;
#                         color: #4B8BBE;
#                         margin-bottom: 10px;
#                         animation: fadeIn 0.6s ease-out;
#                     }

#                     .sidebar-user {
#                         font-size: 16px;
#                         margin-bottom: 20px;
#                         animation: fadeIn 0.8s ease-out;
#                     }

#                     .sidebar-section {
#                         border-top: 1px solid #DDD;
#                         margin-top: 20px;
#                         padding-top: 10px;
#                         animation: fadeIn 1s ease-out;
#                     }

#                     .menu-radio label {
#                         font-size: 16px;
#                         padding: 5px 0;
#                         transition: all 0.3s ease;
#                     }

#                     .menu-radio label:hover {
#                         color: #4B8BBE;
#                         transform: translateX(5px);
#                     }
#                 </style>
#                 """,
#                 unsafe_allow_html=True
#             )

#             st.markdown('<div class="sidebar-title">🪵 Marcenaria</div>', unsafe_allow_html=True)
#             st.markdown(f'<div class="sidebar-user">👤 <strong>Usuário:</strong> {st.session_state.username}</div>', unsafe_allow_html=True)

#             st.markdown('<div class="sidebar-section menu-radio">', unsafe_allow_html=True)
#             opcao = st.radio(
#                 "📋 Menu Principal",
#                 [
#                     "🏠 Dashboard",
#                     "📁 Cadastros",
#                     "🧾 Lançamentos",
#                     "📊 Relatórios",
#                     "🚪 Sair"
#                 ],
#                 label_visibility="collapsed",
#                 key="menu_opcao"
#             )
#             st.markdown('</div>', unsafe_allow_html=True)

#             st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
#             st.caption("🛠️ Sistema de Gestão Financeira v1.0")
#             st.markdown('</div>', unsafe_allow_html=True)

#             if opcao.endswith("Sair"):
#                 st.session_state.logado = False
#                 st.rerun()

#         return opcao
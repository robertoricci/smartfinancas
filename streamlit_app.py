import streamlit as st
from config import APP_TITLE, APP_ICON, PAGE_LAYOUT
# Importar controllers
from controllers.database import Database
from controllers.usuario_controller import UsuarioController
from controllers.fornecedor_controller import FornecedorController
from controllers.despesa_fixa_controller import DespesaFixaController
from controllers.despesa_variavel_controller import DespesaVariavelController
from controllers.venda_controller import VendaController
from controllers.nota_pagar_controller import NotaPagarController
from controllers.relatorio_controller import RelatorioController


# Importar views
from views.login_view2 import LoginView
from views.menu_view import MenuView
from views.dashboard_view import DashboardView
from views.fornecedor_view import FornecedorView
from views.despesa_fixa_view import DespesaFixaView
from views.despesa_variavel_view import DespesaVariavelView
from views.venda_view import VendaView
from views.nota_pagar_view import NotaPagarView
from views.relatorio_view import RelatorioView

# # Configuração inicial
# if "role" not in st.session_state:
#     st.session_state.role = None

# ROLES = [None, "Requester", "Responder", "Admin"]

# # Função de login
# def login():
#     st.markdown(
#         """
#         <style>
#             .login-box {
#                 background-color: #f9f9f9;
#                 padding: 30px;
#                 border-radius: 12px;
#                 box-shadow: 0 4px 12px rgba(0,0,0,0.1);
#                 width: 100%;
#                 max-width: 400px;
#                 margin: auto;
#                 margin-top: 50px;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown('<div class="login-box">', unsafe_allow_html=True)
#     st.subheader("🔐 Login")
#     role = st.selectbox("Escolha seu papel", ROLES, index=0)
#     if st.button("Entrar", use_container_width=True):
#         st.session_state.role = role
#         st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)

# # Função de logout
# def logout():
#     st.session_state.role = None
#     st.rerun()

# # Define páginas
# role = st.session_state.role

# logout_page = st.Page(logout, title="Sair", icon=":material/logout:")
# settings = st.Page("settings.py", title="Configurações", icon=":material/settings:")

# request_pages = [
#     st.Page("request/request_1.py", title="Solicitação 1", icon=":material/help:", default=(role == "Requester")),
#     st.Page("request/request_2.py", title="Solicitação 2", icon=":material/bug_report:")
# ]

# respond_pages = [
#     st.Page("respond/respond_1.py", title="Responder 1", icon=":material/healing:", default=(role == "Responder")),
#     st.Page("respond/respond_2.py", title="Responder 2", icon=":material/handyman:")
# ]

# admin_pages = [
#     st.Page("admin/admin_1.py", title="Administração 1", icon=":material/person_add:", default=(role == "Admin")),
#     st.Page("admin/admin_2.py", title="Administração 2", icon=":material/security:")
# ]

# account_pages = [logout_page, settings]

# # Cabeçalho e logo
# st.title("📋 Request Manager")
# st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

# # Monta navegação
# page_dict = {}
# if role in ["Requester", "Admin"]:
#     page_dict["Solicitações"] = request_pages
# if role in ["Responder", "Admin"]:
#     page_dict["Respostas"] = respond_pages
# if role == "Admin":
#     page_dict["Administração"] = admin_pages

# # Renderiza navegação
# if role:
#     pg = st.navigation({"Conta": account_pages} | page_dict)
# else:
#     pg = st.navigation([st.Page(login)])

# pg.run()


def inicializar_sistema():
    """Inicializa o sistema e seus componentes"""
    # Configurar página
    # st.set_page_config(
    #     page_title=APP_TITLE,
    #     page_icon=APP_ICON,
    #     layout=PAGE_LAYOUT,
    #     initial_sidebar_state="expanded"
    # )
    
    # Inicializar banco de dados (Singleton)
    db = Database()
    
    # Inicializar controllers
    controllers = {
        'usuario': UsuarioController(db),
        'fornecedor': FornecedorController(db),
        'despesa_fixa': DespesaFixaController(db),
        'despesa_variavel': DespesaVariavelController(db),
        'venda': VendaController(db),
        'nota': NotaPagarController(db),
        'relatorio': RelatorioController(db)
    }
    
    # Criar usuário padrão
    controllers['usuario'].criar_usuario_padrao()
    
    # Inicializar session state
    if 'logado' not in st.session_state:
        st.session_state.logado = False
    if 'username' not in st.session_state:
        st.session_state.username = ''
    
    return controllers


def main():


    controllers = inicializar_sistema()

            # Exibir tela de login
    LoginView.render(controllers['usuario'])
    login_page = st.Page(LoginView.render(controllers['usuario']), title="Login", icon=":material/login:")
    pg = st.navigation([login_page])
    pg.run()

if __name__ == "__main__":
    main()
 
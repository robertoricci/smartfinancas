# ============================================================================
# main.py - ARQUIVO PRINCIPAL
# ============================================================================
"""
Sistema de Gestão Financeira para Marcenaria
Arquivo principal de execução
"""
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
from views.login_view import LoginView
from views.menu_view import MenuView
from views.dashboard_view import DashboardView
from views.fornecedor_view import FornecedorView
from views.despesa_fixa_view import DespesaFixaView
from views.despesa_variavel_view import DespesaVariavelView
from views.venda_view import VendaView
from views.nota_pagar_view import NotaPagarView
from views.relatorio_view import RelatorioView


def inicializar_sistema():
    """Inicializa o sistema e seus componentes"""
    # Configurar página
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout=PAGE_LAYOUT,
        initial_sidebar_state="expanded"
    )
    
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
    """Função principal da aplicação"""
    # Inicializar sistema
    controllers = inicializar_sistema()
    
    # Verificar se está logado
    if not st.session_state.logado:
        # Exibir tela de login
        LoginView.render(controllers['usuario'])
    else:
        # Exibir menu e obter opção selecionada
        opcao = MenuView.render()
        
        # Roteamento de páginas
        if opcao == "Dashboard":
            DashboardView.render(controllers['relatorio'])
        
        elif opcao == "Cadastros":
            st.title("📋 Cadastros")
            st.markdown("Gerencie fornecedores e categorias de despesas")
            st.markdown("---")
            
            tab1, tab2, tab3 = st.tabs([
                "👥 Fornecedores",
                "📌 Despesas Fixas",
                "🔄 Despesas Variáveis"
            ])
            
            with tab1:
                FornecedorView.render(controllers['fornecedor'])
            
            with tab2:
                DespesaFixaView.render(controllers['despesa_fixa'])
            
            with tab3:
                DespesaVariavelView.render(
                    controllers['despesa_variavel'],
                    controllers['fornecedor']
                )
        
        elif opcao == "Lançamentos":
            st.title("💳 Lançamentos")
            st.markdown("Registre vendas e notas a pagar")
            st.markdown("---")
            
            tab1, tab2 = st.tabs([
                "💰 Vendas",
                "📄 Notas a Pagar"
            ])
            
            with tab1:
                VendaView.render(controllers['venda'])
            
            with tab2:
                NotaPagarView.render(
                    controllers['nota'],
                    controllers['fornecedor']
                )
        
        elif opcao == "Relatórios":
            st.title("📊 Relatórios")
            st.markdown("Análises e relatórios financeiros")
            st.markdown("---")
            
            tab1, tab2, tab3 = st.tabs([
                "📋 Despesas a Pagar",
                "💵 Fluxo de Caixa",
                "📊 Por Categoria"
            ])
            
            with tab1:
                RelatorioView.render_despesas_pagar(controllers['nota'])
            
            with tab2:
                RelatorioView.render_fluxo_caixa(
                    controllers['relatorio'],
                    controllers['venda'],
                    controllers['nota']
                )
            
            with tab3:
                RelatorioView.render_categorias(controllers['relatorio'])


if __name__ == "__main__":
    main()

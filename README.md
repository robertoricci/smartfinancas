"# smartfinancas" 

# ============================================================================
# INSTRUÇÕES DE INSTALAÇÃO E USO
# ============================================================================
"""
ESTRUTURA FINAL DO PROJETO:
============================

marcenaria_sistema/
│
├── README.md
├── requirements.txt
├── config.py
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── base.py
│   └── models.py
│
├── controllers/
│   ├── __init__.py
│   ├── database.py
│   ├── usuario_controller.py
│   ├── fornecedor_controller.py
│   ├── despesa_fixa_controller.py
│   ├── despesa_variavel_controller.py
│   ├── venda_controller.py
│   ├── nota_pagar_controller.py
│   └── relatorio_controller.py
│
└── views/
    ├── __init__.py
    ├── login_view.py
    ├── menu_view.py
    ├── dashboard_view.py
    ├── fornecedor_view.py
    ├── despesa_fixa_view.py
    ├── despesa_variavel_view.py
    ├── venda_view.py
    ├── nota_pagar_view.py
    └── relatorio_view.py


PASSOS PARA INSTALAÇÃO:
=======================

1. Criar a estrutura de pastas:
   mkdir -p marcenaria_sistema/models
   mkdir -p marcenaria_sistema/controllers
   mkdir -p marcenaria_sistema/views

2. Copiar cada arquivo para seu respectivo local conforme a estrutura acima

3. Criar ambiente virtual:
   cd marcenaria_sistema
   python -m venv venv
   
4. Ativar ambiente virtual:
   # Linux/Mac:
   source venv/bin/activate
   
   # Windows:
   venv\Scripts\activate

5. Instalar dependências:
   pip install -r requirements.txt

6. Executar o sistema:
   streamlit run main.py


ARQUIVOS __init__.py:
====================

Cada pasta (models, controllers, views) deve ter um arquivo __init__.py
com os imports correspondentes (já fornecidos nos comentários acima).


BENEFÍCIOS DA ARQUITETURA MVC:
===============================

✅ SEPARAÇÃO DE RESPONSABILIDADES
   - Models: Estrutura de dados
   - Controllers: Lógica de negócio
   - Views: Interface do usuário

✅ MANUTENIBILIDADE
   - Código organizado e fácil de localizar
   - Mudanças isoladas em cada camada

✅ TESTABILIDADE
   - Controllers podem ser testados independentemente
   - Mock de banco de dados facilitado

✅ ESCALABILIDADE
   - Fácil adicionar novos recursos
   - Reutilização de código

✅ TRABALHO EM EQUIPE
   - Desenvolvedores podem trabalhar em camadas diferentes
   - Menor chance de conflitos


FLUXO DE DADOS:
==============

1. Usuário interage com VIEW
2. VIEW chama método do CONTROLLER
3. CONTROLLER processa lógica de negócio
4. CONTROLLER acessa/modifica MODEL
5. CONTROLLER retorna resultado para VIEW
6. VIEW exibe resultado para usuário


PRÓXIMOS PASSOS SUGERIDOS:
==========================

□ Implementar backup automático do banco de dados
□ Adicionar gráficos mais detalhados
□ Implementar exportação de relatórios (PDF/Excel)
□ Adicionar sistema de permissões por usuário
□ Criar dashboard com gráficos interativos
□ Implementar notificações de contas a vencer
□ Adicionar histórico de alterações
□ Criar API REST para integração externa


OBSERVAÇÕES IMPORTANTES:
========================

• O banco SQLite será criado automaticamente na primeira execução
• Usuário padrão: admin / Senha: admin123
• O sistema usa session_state do Streamlit para manter o estado
• Todas as datas seguem o formato brasileiro (DD/MM/YYYY)
• Valores monetários formatados em Real (R$)


COMANDOS ÚTEIS:
==============

# Limpar cache do Streamlit:
streamlit cache clear

# Executar em porta específica:
streamlit run main.py --server.port 8502

# Executar em modo de desenvolvimento:
streamlit run main.py --server.runOnSave true

# Ver logs detalhados:
streamlit run main.py --logger.level=debug


TROUBLESHOOTING:
===============

Erro: ModuleNotFoundError
→ Verifique se está no ambiente virtual
→ Reinstale as dependências: pip install -r requirements.txt

Erro: No module named 'models'
→ Verifique se os arquivos __init__.py existem
→ Execute a partir da pasta raiz do projeto

Erro: Database locked
→ Feche outras instâncias do aplicativo
→ Delete o arquivo marcenaria.db e reinicie

Erro na visualização:
→ Limpe o cache: streamlit cache clear
→ Recarregue a página (F5)


CONTATO E SUPORTE:
=================

Para dúvidas ou melhorias, consulte a documentação do Streamlit:
https://docs.streamlit.io/

Documentação do SQLAlchemy:
https://docs.sqlalchemy.org/
"""
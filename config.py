# ============================================================================
# config.py
# ============================================================================
"""
Arquivo de configuração do sistema
"""

# Configurações do banco de dados
DATABASE_NAME = 'marcenaria.db'
DATABASE_URL = f'sqlite:///{DATABASE_NAME}'

# Configurações da aplicação
APP_TITLE = "Sistema de Gestão - Marcenaria"
APP_ICON = "🪵"
PAGE_LAYOUT = "wide"

# Configurações de segurança
SESSION_TIMEOUT = 3600  # 1 hora em segundos

# Categorias padrão
CATEGORIAS_DESPESA = [
    "Matéria-prima",
    "Ferramentas",
    "Transporte",
    "Manutenção",
    "Aluguel",
    "Energia",
    "Água",
    "Telefone/Internet",
    "Impostos",
    "Outros"
]

FORMAS_PAGAMENTO = [
    "Dinheiro",
    "PIX",
    "Cartão Débito",
    "Cartão Crédito",
    "Transferência",
    "Boleto"
]

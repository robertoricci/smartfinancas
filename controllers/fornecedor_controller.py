# ============================================================================
# controllers/fornecedor_controller.py
# ============================================================================
"""
Controller para gerenciamento de fornecedores
"""
from models.models import Fornecedor

class FornecedorController:
    def __init__(self, database):
        self.db = database
    
    def criar(self, nome, cnpj_cpf= None, telefone=None, email=None, endereco=None):
        """Cria um novo fornecedor"""
        session = self.db.get_session()
        try:
            fornecedor = Fornecedor(
                nome=nome,
                cnpj_cpf=cnpj_cpf,
                telefone=telefone,
                email=email,
                endereco=endereco
            )
            session.add(fornecedor)
            session.commit()
            return True, "Fornecedor cadastrado com sucesso"
        except Exception as e:
            session.rollback()
            return False, f"Erro: {str(e)}"
        finally:
            session.close()
    
    def listar_ativos(self):
        """Lista todos os fornecedores ativos"""
        session = self.db.get_session()
        try:
            fornecedores = session.query(Fornecedor).filter_by(ativo=True).all()
            result = [{
                'id': f.id,
                'nome': f.nome,
                'cnpj_cpf': f.cnpj_cpf or '-',
                'telefone': f.telefone or '-',
                'email': f.email or '-',
                'endereco': f.endereco or '-'
            } for f in fornecedores]
            return result
        finally:
            session.close()
    
    def obter_todos(self):
        """Retorna todos os fornecedores ativos (objetos)"""
        session = self.db.get_session()
        try:
            fornecedores = session.query(Fornecedor).filter_by(ativo=True).all()
            # Expunge para poder usar fora da sessão
            for f in fornecedores:
                session.expunge(f)
            return fornecedores
        finally:
            session.close()
    
    def obter_por_id(self, fornecedor_id):
        """Obtém um fornecedor por ID"""
        session = self.db.get_session()
        try:
            fornecedor = session.query(Fornecedor).filter_by(
                id=fornecedor_id,
                ativo=True
            ).first()
            if fornecedor:
                session.expunge(fornecedor)
            return fornecedor
        finally:
            session.close()
    
    def desativar(self, fornecedor_id):
        """Desativa um fornecedor (exclusão lógica)"""
        session = self.db.get_session()
        try:
            fornecedor = session.query(Fornecedor).filter_by(id=fornecedor_id).first()
            if fornecedor:
                fornecedor.ativo = False
                session.commit()
                return True, "Fornecedor desativado"
            return False, "Fornecedor não encontrado"
        except Exception as e:
            session.rollback()
            return False, f"Erro: {str(e)}"
        finally:
            session.close()

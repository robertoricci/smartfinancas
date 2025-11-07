# ============================================================================
# controllers/usuario_controller.py
# ============================================================================
"""
Controller para gerenciamento de usuários
"""
import hashlib
from models.models import Usuario

class UsuarioController:
    def __init__(self, database):
        self.db = database
    
    @staticmethod
    def hash_senha(senha):
        """Criptografa a senha usando SHA256"""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def criar_usuario_padrao(self):
        """Cria o usuário administrador padrão"""
        session = self.db.get_session()
        try:
            if not session.query(Usuario).filter_by(username='admin').first():
                usuario = Usuario(
                    username='admin',
                    senha_hash=self.hash_senha('admin123'),
                    nome='Administrador'
                )
                session.add(usuario)
                session.commit()
                return True
        except Exception as e:
            session.rollback()
            print(f"Erro ao criar usuário padrão: {e}")
            return False
        finally:
            session.close()
    
    def verificar_login(self, username, senha):
        """Verifica as credenciais de login"""
        session = self.db.get_session()
        try:
            usuario = session.query(Usuario).filter_by(
                username=username,
                ativo=True
            ).first()
            
            if usuario and usuario.senha_hash == self.hash_senha(senha):
                return True
            return False
        finally:
            session.close()
    
    def criar_usuario(self, username, senha, nome):
        """Cria um novo usuário"""
        session = self.db.get_session()
        try:
            # Verifica se já existe
            if session.query(Usuario).filter_by(username=username).first():
                return False, "Usuário já existe"
            
            usuario = Usuario(
                username=username,
                senha_hash=self.hash_senha(senha),
                nome=nome
            )
            session.add(usuario)
            session.commit()
            return True, "Usuário criado com sucesso"
        except Exception as e:
            session.rollback()
            return False, f"Erro: {str(e)}"
        finally:
            session.close()

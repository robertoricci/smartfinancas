# ============================================================================
# controllers/database.py
# ============================================================================
"""
Gerenciamento de conexão com banco de dados
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from config import DATABASE_URL


class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        self.engine = create_engine(DATABASE_URL, echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self._initialized = True
    
    def get_session(self):
        """Retorna uma nova sessão do banco de dados"""
        return self.Session()
    
    def close_all(self):
        """Fecha todas as conexões"""
        self.engine.dispose()

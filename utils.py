"""
FinAI Companion - Módulo de Utilidades
Funções auxiliares para persistência e configurações
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any
import hashlib

class ConversationManager:
    """
    Gerencia persistência de conversas e contexto do usuário
    """
    
    def __init__(self, storage_path: str = "./data"):
        """
        Inicializa gerenciador de conversas
        
        Args:
            storage_path: Diretório para armazenar dados
        """
        self.storage_path = storage_path
        
        # Criar diretório se não existir
        os.makedirs(storage_path, exist_ok=True)
        
        self.conversations_file = os.path.join(storage_path, "conversations.json")
        self.user_profile_file = os.path.join(storage_path, "user_profile.json")
    
    def save_conversation(
        self, 
        user_id: str, 
        conversation: List[Dict[str, Any]]
    ) -> bool:
        """
        Salva conversa de um usuário
        
        Args:
            user_id: Identificador único do usuário
            conversation: Lista de mensagens
            
        Returns:
            True se salvou com sucesso
        """
        try:
            # Carregar conversas existentes
            conversations = self._load_all_conversations()
            
            # Adicionar/atualizar conversa do usuário
            conversations[user_id] = {
                "messages": conversation,
                "last_updated": datetime.now().isoformat(),
                "message_count": len(conversation)
            }
            
            # Salvar
            with open(self.conversations_file, 'w', encoding='utf-8') as f:
                json.dump(conversations, f, ensure_ascii=False, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Erro ao salvar conversa: {e}")
            return False
    
    def load_conversation(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Carrega conversa de um usuário
        
        Args:
            user_id: Identificador do usuário
            
        Returns:
            Lista de mensagens ou lista vazia
        """
        conversations = self._load_all_conversations()
        
        if user_id in conversations:
            return conversations[user_id].get("messages", [])
        
        return []
    
    def _load_all_conversations(self) -> Dict[str, Any]:
        """
        Carrega todas as conversas do arquivo
        
        Returns:
            Dicionário com todas as conversas
        """
        if os.path.exists(self.conversations_file):
            try:
                with open(self.conversations_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        
        return {}
    
    def delete_conversation(self, user_id: str) -> bool:
        """
        Remove conversa de um usuário
        
        Args:
            user_id: Identificador do usuário
            
        Returns:
            True se removeu com sucesso
        """
        try:
            conversations = self._load_all_conversations()
            
            if user_id in conversations:
                del conversations[user_id]
                
                with open(self.conversations_file, 'w', encoding='utf-8') as f:
                    json.dump(conversations, f, ensure_ascii=False, indent=2)
                
                return True
            
            return False
            
        except:
            return False
    
    def save_user_profile(self, user_id: str, profile: Dict[str, Any]) -> bool:
        """
        Salva perfil/preferências do usuário
        
        Args:
            user_id: Identificador do usuário
            profile: Dados do perfil
            
        Returns:
            True se salvou com sucesso
        """
        try:
            # Carregar perfis existentes
            profiles = self._load_all_profiles()
            
            # Adicionar timestamp
            profile["last_updated"] = datetime.now().isoformat()
            
            # Atualizar perfil
            profiles[user_id] = profile
            
            # Salvar
            with open(self.user_profile_file, 'w', encoding='utf-8') as f:
                json.dump(profiles, f, ensure_ascii=False, indent=2)
            
            return True
            
        except:
            return False
    
    def load_user_profile(self, user_id: str) -> Dict[str, Any]:
        """
        Carrega perfil do usuário
        
        Args:
            user_id: Identificador do usuário
            
        Returns:
            Dicionário com perfil ou dicionário vazio
        """
        profiles = self._load_all_profiles()
        return profiles.get(user_id, {})
    
    def _load_all_profiles(self) -> Dict[str, Any]:
        """
        Carrega todos os perfis
        
        Returns:
            Dicionário com perfis
        """
        if os.path.exists(self.user_profile_file):
            try:
                with open(self.user_profile_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        
        return {}


def generate_user_id(identifier: str = None) -> str:
    """
    Gera ID único para usuário
    
    Args:
        identifier: String identificadora (ex: email, IP)
        
    Returns:
        Hash MD5 como identificador
    """
    if identifier is None:
        identifier = str(datetime.now().timestamp())
    
    return hashlib.md5(identifier.encode()).hexdigest()


def load_conversation_history() -> List[Dict[str, Any]]:
    """
    Função auxiliar para carregar histórico (compatibilidade com app.py)
    
    Returns:
        Lista de mensagens
    """
    manager = ConversationManager()
    # Em produção, user_id viria da sessão/autenticação
    user_id = "default_user"
    return manager.load_conversation(user_id)


def save_conversation_history(conversation: List[Dict[str, Any]]) -> bool:
    """
    Função auxiliar para salvar histórico (compatibilidade com app.py)
    
    Args:
        conversation: Lista de mensagens
        
    Returns:
        True se salvou com sucesso
    """
    manager = ConversationManager()
    user_id = "default_user"
    return manager.save_conversation(user_id, conversation)


def format_currency(value: float, currency: str = "BRL") -> str:
    """
    Formata valor monetário
    
    Args:
        value: Valor numérico
        currency: Código da moeda
        
    Returns:
        String formatada
    """
    if currency == "BRL":
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    elif currency == "USD":
        return f"$ {value:,.2f}"
    elif currency == "EUR":
        return f"€ {value:,.2f}"
    else:
        return f"{value:,.2f}"


def validate_numeric_input(value: Any, min_value: float = None, max_value: float = None) -> bool:
    """
    Valida entrada numérica
    
    Args:
        value: Valor a validar
        min_value: Valor mínimo permitido
        max_value: Valor máximo permitido
        
    Returns:
        True se válido
    """
    try:
        num = float(value)
        
        if min_value is not None and num < min_value:
            return False
        
        if max_value is not None and num > max_value:
            return False
        
        return True
        
    except:
        return False


def sanitize_financial_input(text: str) -> str:
    """
    Sanitiza entrada de texto financeiro
    Remove caracteres perigosos mantendo apenas números e operadores básicos
    
    Args:
        text: Texto a sanitizar
        
    Returns:
        Texto sanitizado
    """
    # Permitir apenas números, pontos, vírgulas e operadores básicos
    allowed_chars = "0123456789.,+-*/()"
    sanitized = "".join(char for char in text if char in allowed_chars)
    
    return sanitized


def create_backup(source_path: str, backup_dir: str = "./backups") -> str:
    """
    Cria backup de arquivo
    
    Args:
        source_path: Caminho do arquivo original
        backup_dir: Diretório de backups
        
    Returns:
        Caminho do arquivo de backup
    """
    import shutil
    
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(source_path)
    backup_filename = f"{timestamp}_{filename}"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    if os.path.exists(source_path):
        shutil.copy2(source_path, backup_path)
        return backup_path
    
    return None


def get_financial_glossary() -> Dict[str, str]:
    """
    Retorna glossário básico de termos financeiros
    
    Returns:
        Dicionário com termos e definições
    """
    return {
        "CDB": "Certificado de Depósito Bancário - investimento de renda fixa emitido por bancos",
        "Tesouro Direto": "Programa de venda de títulos públicos do governo federal para pessoas físicas",
        "LCI": "Letra de Crédito Imobiliário - investimento isento de IR vinculado ao setor imobiliário",
        "LCA": "Letra de Crédito do Agronegócio - investimento isento de IR vinculado ao agronegócio",
        "Selic": "Taxa básica de juros da economia brasileira",
        "CDI": "Certificado de Depósito Interbancário - taxa de referência para investimentos",
        "IPCA": "Índice de Preços ao Consumidor Amplo - principal índice de inflação do Brasil",
        "FGC": "Fundo Garantidor de Créditos - garante investimentos até R$ 250 mil",
        "ROI": "Return on Investment - retorno sobre investimento",
        "VPL": "Valor Presente Líquido - método de avaliação de investimentos",
        "TIR": "Taxa Interna de Retorno - rentabilidade de um investimento",
        "Liquidez": "Facilidade de converter um ativo em dinheiro",
        "Volatilidade": "Medida de variação de preço de um ativo",
        "Diversificação": "Estratégia de distribuir investimentos em diferentes ativos",
        "Renda Fixa": "Investimentos com rentabilidade previsível",
        "Renda Variável": "Investimentos com rentabilidade que varia conforme mercado"
    }


def get_financial_tips() -> List[str]:
    """
    Retorna lista de dicas financeiras educativas
    
    Returns:
        Lista de dicas
    """
    return [
        "💡 Mantenha uma reserva de emergência equivalente a 6 meses de despesas",
        "📊 Diversifique seus investimentos para reduzir riscos",
        "🎯 Defina objetivos financeiros claros (curto, médio e longo prazo)",
        "📝 Acompanhe seus gastos mensalmente",
        "🏦 Compare taxas antes de contratar empréstimos",
        "💰 Comece a investir cedo - o tempo é seu aliado",
        "🔒 Priorize investimentos garantidos pelo FGC para sua reserva de emergência",
        "📈 Estude sobre educação financeira continuamente",
        "⚖️ Equilibre sua carteira entre segurança e rentabilidade",
        "🚫 Evite dívidas com juros altos (cartão de crédito, cheque especial)"
    ]


class FinancialDataValidator:
    """
    Validador de dados financeiros
    """
    
    @staticmethod
    def validate_investment_data(data: Dict[str, Any]) -> tuple:
        """
        Valida dados de investimento
        
        Args:
            data: Dicionário com dados do investimento
            
        Returns:
            Tupla (is_valid, error_message)
        """
        required_fields = ["principal", "taxa", "prazo"]
        
        # Verificar campos obrigatórios
        for field in required_fields:
            if field not in data:
                return False, f"Campo obrigatório ausente: {field}"
        
        # Validar valores
        if data["principal"] <= 0:
            return False, "Valor principal deve ser positivo"
        
        if data["taxa"] < 0 or data["taxa"] > 1:
            return False, "Taxa deve estar entre 0 e 100%"
        
        if data["prazo"] <= 0:
            return False, "Prazo deve ser positivo"
        
        return True, "Dados válidos"
    
    @staticmethod
    def validate_loan_data(data: Dict[str, Any]) -> tuple:
        """
        Valida dados de empréstimo/financiamento
        
        Args:
            data: Dicionário com dados do empréstimo
            
        Returns:
            Tupla (is_valid, error_message)
        """
        required_fields = ["valor", "taxa_mensal", "prazo"]
        
        for field in required_fields:
            if field not in data:
                return False, f"Campo obrigatório ausente: {field}"
        
        if data["valor"] <= 0:
            return False, "Valor deve ser positivo"
        
        if data["taxa_mensal"] < 0:
            return False, "Taxa não pode ser negativa"
        
        if data["prazo"] <= 0:
            return False, "Prazo deve ser positivo"
        
        # Verificar se taxa não é absurda (> 10% ao mês)
        if data["taxa_mensal"] > 0.10:
            return True, "AVISO: Taxa muito alta. Verifique se está correta."
        
        return True, "Dados válidos"


# Constantes úteis
FINANCIAL_CONSTANTS = {
    "TAXA_SELIC_ATUAL": 0.1075,  # Atualizar periodicamente
    "IPCA_ANUAL_MEDIO": 0.045,    # Média histórica
    "LIMITE_FGC": 250000,          # Limite de garantia FGC
    "ALIQUOTA_IR": {               # Tabela regressiva IR
        "ate_180": 0.225,
        "181_360": 0.20,
        "361_720": 0.175,
        "acima_720": 0.15
    }
}

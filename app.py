import streamlit as st
from datetime import datetime
from ai_core import FinAIEngine
from data_handler import FinancialCalculator

# Configuração da página
st.set_page_config(page_title="FinAI Companion", page_icon="💰", layout="wide")

@st.cache_resource
def init_ai_engine(): return FinAIEngine()
@st.cache_resource
def init_calculator(): return FinancialCalculator()

# CSS Ajustado para Contraste Total
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; color: #1f77b4; text-align: center; margin-bottom: 0px; }
    .chat-message { padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem; display: flex; flex-direction: column; }
    .user-message { background-color: #e3f2fd; border-left: 5px solid #1f77b4; color: #0d47a1; }
    .assistant-message { background-color: #262730; border-left: 5px solid #4caf50; color: #ffffff; }
    .disclaimer { background-color: #fff3cd; padding: 1rem; border-radius: 5px; border-left: 4px solid #ffc107; margin-bottom: 20px; color: #856404; }
    [data-testid="stMetricValue"] { font-size: 1.8rem; color: #1f77b4; }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">💰 FinAI Companion</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">Seu coach financeiro digital: transformando números em decisões</p>', unsafe_allow_html=True)
    
    # --- NOVO: SEÇÃO DE MÉTRICAS (Upgrade da Homepage) ---
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Selic", "10,75%", "-0,25%")
    m2.metric("IPCA (12m)", "4,42%", "0,15%", delta_color="inverse")
    m3.metric("CDI", "10,65%", "0,00%")
    m4.metric("Ibovespa", "128k pts", "+1,2%", delta_color="normal")
    
    # Disclaimer
    st.markdown("""<div class="disclaimer"><strong>⚠️ Aviso:</strong> Informativo educacional. Não substitui consultoria profissional.</div>""", unsafe_allow_html=True)
    
    ai_engine = init_ai_engine()
    calculator = init_calculator()
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.conversation_context = []

    # --- Sidebar com Calculadoras ---
    with st.sidebar:
        st.header("📊 Ferramentas")
        calc = st.selectbox("Calculadora:", ["Juros Compostos", "Financiamento"])
        
        calc_context = ""
        
        if calc == "Juros Compostos":
            p = st.number_input("Início (R$)", value=1000.0)
            t = st.number_input("Taxa Anual (%)", value=10.0)
            a = st.number_input("Anos", value=5)
            calc_context = f"[Dados atuais na calculadora: Valor Inicial R$ {p}, Taxa {t}% ao ano, por {a} anos]"
            
            if st.button("Calcular Agora"):
                res = calculator.juros_compostos(p, t/100, a)
                st.success(f"Total: R$ {res:,.2f}")
        
        elif calc == "Financiamento":
            v = st.number_input("Valor Imóvel (R$)", value=300000.0)
            tm = st.number_input("Taxa Mensal (%)", value=0.8)
            ms = st.number_input("Meses", value=360)
            calc_context = f"[Dados de Financiamento: Valor R$ {v}, Taxa {tm}%/mês, Prazo {ms} meses]"
            
            if st.button("Calcular Parcela"):
                parc = calculator.calcular_financiamento(v, tm/100, ms)
                st.success(f"Parcela: R$ {parc:,.2f}")

        st.divider()
        if st.button("🗑️ Limpar Conversa"):
            st.session_state.messages = []
            st.session_state.conversation_context = []
            st.rerun()

    # --- Função de Envio ---
    def process_chat(text):
        prompt_com_dados = f"{calc_context}\n\nPergunta do usuário: {text}"
        st.session_state.messages.append({"role": "user", "content": text})
        with st.spinner("FinAI analisando..."):
            response = ai_engine.generate_response(prompt_com_dados, st.session_state.conversation_context)
            
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.conversation_context.append({"user": text, "assistant": response})
        st.rerun()

    # Exibir Histórico
    for msg in st.session_state.messages:
        div_class = "user-message" if msg["role"] == "user" else "assistant-message"
        st.markdown(f"""<div class="chat-message {div_class}"><strong>{"🧑 Você" if msg["role"] == "user" else "🤖 FinAI"}</strong>{msg["content"]}</div>""", unsafe_allow_html=True)

    # Input manual
    if prompt := st.chat_input("Diga algo..."):
        process_chat(prompt)

    # Sugestões Clicáveis
    if not st.session_state.messages:
        st.markdown("---")
        st.subheader("💡 Experimente perguntar:")
        col1, col2, col3 = st.columns(3)
        if col1.button("💰 Juntar R$50k em 3 anos"): process_chat("Como posso juntar R$50.000 em 3 anos?")
        if col2.button("📊 CDB ou Tesouro?"): process_chat("Qual a diferença entre CDB e Tesouro Direto?")
        if col3.button("🏠 Entrada de Casa"): process_chat("Quanto dar de entrada em um imóvel?")

if __name__ == "__main__":
    main()
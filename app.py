import streamlit as st
import os
import plotly.graph_objects as go
from fpdf import FPDF
from ai_core import FinAIEngine
from data_handler import FinancialCalculator

# Configuração de Página
st.set_page_config(page_title="FinAI CORE v2.3 Premium", page_icon="🤖", layout="wide")

# --- CSS PREMIUM INTEGRADO ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    .stApp { background: radial-gradient(ellipse at bottom, #0d1117 0%, #010409 100%); color: #00f2ff; font-family: 'Orbitron', sans-serif !important; }
    .main-header { font-size: 2.5rem !important; font-weight: 900; text-align: center; background: linear-gradient(90deg, #00f2ff, #00ff88); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 5px; }
    .robot-container { display: flex; justify-content: center; margin: 10px 0; }
    .robot-img { width: 100px; filter: drop-shadow(0 0 10px #00f2ff); transition: all 0.5s ease; }
    .robot-blink { animation: blink-green 0.8s ease-in-out; }
    @keyframes blink-green {
        0% { transform: scale(1); filter: drop-shadow(0 0 10px #00f2ff); }
        50% { transform: scale(1.1); filter: drop-shadow(0 0 30px #00ff88); }
        100% { transform: scale(1); filter: drop-shadow(0 0 10px #00f2ff); }
    }
    [data-testid="stMetric"] { background: rgba(0, 0, 0, 0.4) !important; border: 1px solid #00f2ff !important; border-radius: 10px !important; text-align: center !important; }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO EXPORTAR PDF (VERSÃO BLINDADA CONTRA UNICODE) ---
def export_pdf(messages):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 16) 
    pdf.cell(200, 10, txt="FinAI CORE - Relatorio de Consultoria", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Helvetica", size=12)
    
    for msg in messages:
        role = "USUARIO" if msg["role"] == "user" else "FINAI"
        
        # Limpa caracteres que a fonte Helvetica não suporta (como o traço longo do Gemini)
        content = msg["content"].encode('latin-1', 'ignore').decode('latin-1')
        
        pdf.multi_cell(0, 10, txt=f"{role}: {content}")
        pdf.ln(5)
    
    # Converte bytearray para bytes para compatibilidade com Streamlit
    pdf_output = pdf.output(dest='S')
    return bytes(pdf_output)

def render_neon_chart():
    meses = ['Set', 'Out', 'Nov', 'Dez', 'Jan', 'Fev']
    valores = [10.50, 10.75, 11.25, 11.75, 11.75, 11.25]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses, y=valores, mode='lines+markers', line=dict(color='#00f2ff', width=3), marker=dict(size=8, color='#00ff88')))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#00f2ff', family='Orbitron'), height=200, margin=dict(l=20, r=20, t=10, b=10), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def main():
    if 'blink' not in st.session_state: st.session_state.blink = False
    if 'last_result' not in st.session_state: st.session_state.last_result = None
    if "messages" not in st.session_state: st.session_state.messages = []

    st.markdown('<h1 class="main-header">FINAI CORE v2.3</h1>', unsafe_allow_html=True)
    
    blink_class = "robot-blink" if st.session_state.blink else ""
    robot_url = "https://cdn-icons-png.flaticon.com/512/4712/4712139.png"
    st.markdown(f'<div class="robot-container"><img src="{robot_url}" class="robot-img {blink_class}"></div>', unsafe_allow_html=True)
    st.session_state.blink = False

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("SELIC (META)", "11,25%", "+0,50%")
    m2.metric("IPCA (12M)", "3,95%", "-0,10%", delta_color="inverse")
    m3.metric("CDI (HOJE)", "11,15%", "0,00%")
    m4.metric("IBOVESPA", "134.500", "+1,15%")
    
    render_neon_chart()
    st.markdown("---")

    ai_engine = FinAIEngine()
    calculator = FinancialCalculator()

    with st.sidebar:
        st.markdown("<h3 style='color:#00f2ff;'>PAINEL DE CONTROLE</h3>", unsafe_allow_html=True)
        calc = st.selectbox("Escolha o Módulo:", ["Juros Compostos", "Financiamento"])
        
        if calc == "Juros Compostos":
            p = st.number_input("Capital Inicial (R$)", value=1000.0)
            t = st.number_input("Taxa Anual (%)", value=10.0)
            a = st.number_input("Anos", value=5)
            if st.button("CALCULAR"):
                res = calculator.juros_compostos(p, t/100, a)
                st.session_state.last_result = f"PROJECAO JUROS: R$ {res:,.2f}"
                st.session_state.blink = True 
                st.rerun()

        elif calc == "Financiamento":
            v = st.number_input("Valor Total (R$)", value=200000.0)
            taxa_m = st.number_input("Taxa Mensal (%)", value=0.9)
            meses = st.number_input("Qtd Meses", value=120)
            if st.button("CALCULAR PARCELA"):
                res = calculator.calcular_financiamento(v, taxa_m/100, meses)
                st.session_state.last_result = f"PARCELA MENSAL: R$ {res:,.2f}"
                st.session_state.blink = True
                st.rerun()

        if st.session_state.last_result:
            st.success(st.session_state.last_result)

        st.divider()
        if st.session_state.messages:
            # Geração segura do PDF
            pdf_data = export_pdf(st.session_state.messages)
            st.download_button("📥 BAIXAR RELATORIO PDF", data=pdf_data, file_name="consultoria_finai.pdf", mime="application/pdf")
        
        if st.button("REINICIAR TUDO"):
            st.session_state.messages = []
            st.session_state.last_result = None
            st.rerun()

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Consulte o FinAI..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("PROCESSANDO..."):
            full_prompt = f"(Contexto: {st.session_state.last_result}) {prompt}" if st.session_state.last_result else prompt
            response = ai_engine.generate_response(full_prompt, st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

if __name__ == "__main__":
    main()
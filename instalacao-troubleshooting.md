# 🔧 Guia de Instalação & Troubleshooting - FinAI Companion

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Instalação Passo a Passo](#instalação-passo-a-passo)
3. [Configuração](#configuração)
4. [Solução de Problemas](#solução-de-problemas)
5. [FAQ Técnico](#faq-técnico)
6. [Deploy em Produção](#deploy-em-produção)

---

## Pré-requisitos

### Sistema Operacional

✅ **Testado em:**
- Windows 10/11
- macOS 12+
- Linux (Ubuntu 20.04+, Debian, Fedora)

### Software Necessário

| Software | Versão Mínima | Como Verificar |
|----------|---------------|----------------|
| Python | 3.8+ | `python --version` |
| pip | 20.0+ | `pip --version` |
| git | 2.0+ | `git --version` |

### API Keys

🔑 **Google Gemini API Key**
- Obter em: https://makersuite.google.com/app/apikey
- Gratuito para uso pessoal/desenvolvimento
- Limites: 60 requisições/minuto

---

## Instalação Passo a Passo

### Método 1: Instalação Local (Recomendado para desenvolvimento)

#### 1. Clonar Repositório

```bash
# HTTPS
git clone https://github.com/seu-usuario/finai-companion.git

# SSH
git clone git@github.com:seu-usuario/finai-companion.git

# Entrar no diretório
cd finai-companion
```

#### 2. Criar Ambiente Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Verificar ativação:**
- Deve aparecer `(venv)` no início da linha do terminal

#### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

**Se houver erro com dependências:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

#### 4. Configurar Variáveis de Ambiente

**Criar arquivo `.env`:**

```bash
# Copiar template
cp .env.example .env

# Editar com seu editor preferido
nano .env   # ou vim, code, notepad++
```

**Conteúdo do .env:**
```env
GEMINI_API_KEY=sua_chave_api_aqui
APP_ENV=development
LOG_LEVEL=INFO
DATA_PATH=./data
```

**Importante:** Nunca commite o arquivo `.env` para o GitHub!

#### 5. Criar Diretórios Necessários

```bash
mkdir -p data docs/slides
```

#### 6. Executar Aplicativo

```bash
streamlit run app.py
```

**Sucesso! Aplicativo deve abrir em:**
```
http://localhost:8501
```

---

### Método 2: Instalação via Docker (Opcional)

**Dockerfile:**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Construir e executar:**
```bash
docker build -t finai-companion .
docker run -p 8501:8501 --env-file .env finai-companion
```

---

## Configuração

### Configuração Básica

**1. Verificar Instalação**

```python
# test_installation.py
import sys
print(f"Python version: {sys.version}")

try:
    import streamlit as st
    print("✅ Streamlit instalado")
except ImportError:
    print("❌ Streamlit não encontrado")

try:
    import google.generativeai as genai
    print("✅ Google Generative AI instalado")
except ImportError:
    print("❌ Google Generative AI não encontrado")

try:
    import pandas as pd
    print("✅ Pandas instalado")
except ImportError:
    print("❌ Pandas não encontrado")

print("\n✅ Todas as dependências estão instaladas!")
```

Execute:
```bash
python test_installation.py
```

**2. Testar API Key**

```python
# test_api.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY não encontrada no .env")
else:
    print("✅ API Key encontrada")
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Teste")
        print("✅ API funcionando corretamente")
        print(f"Resposta: {response.text[:50]}...")
    except Exception as e:
        print(f"❌ Erro na API: {e}")
```

Execute:
```bash
python test_api.py
```

### Configuração Avançada

**Customizar porta Streamlit:**

```bash
streamlit run app.py --server.port 8080
```

**Configurar logging:**

No `.env`:
```env
LOG_LEVEL=DEBUG  # Para mais detalhes
```

**Limpar cache:**

```bash
streamlit cache clear
```

---

## Solução de Problemas

### Problema 1: "ModuleNotFoundError"

**Erro:**
```
ModuleNotFoundError: No module named 'streamlit'
```

**Solução:**
1. Verificar se ambiente virtual está ativado:
   ```bash
   # Deve aparecer (venv) no terminal
   ```

2. Reinstalar dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Verificar versão do Python:
   ```bash
   python --version  # Deve ser 3.8+
   ```

---

### Problema 2: "API Key inválida"

**Erro:**
```
google.api_core.exceptions.InvalidArgument: API key not valid
```

**Soluções:**

1. **Verificar arquivo .env:**
   ```bash
   cat .env  # Linux/Mac
   type .env  # Windows
   ```
   - Não deve haver espaços: `GEMINI_API_KEY=abc123` ✅
   - Evitar: `GEMINI_API_KEY = abc123` ❌

2. **Regenerar API Key:**
   - Acesse: https://makersuite.google.com/app/apikey
   - Crie nova chave
   - Atualize `.env`

3. **Verificar região:**
   - API pode não estar disponível em todas as regiões
   - Use VPN se necessário

---

### Problema 3: Streamlit não abre automaticamente

**Sintoma:**
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```
Mas navegador não abre.

**Soluções:**

1. **Abrir manualmente:**
   ```
   Copie o URL e cole no navegador
   ```

2. **Configurar Streamlit:**
   ```bash
   streamlit config show
   ```
   
   Editar `~/.streamlit/config.toml`:
   ```toml
   [browser]
   serverAddress = "localhost"
   gatherUsageStats = false
   ```

3. **Verificar porta em uso:**
   ```bash
   # Linux/Mac
   lsof -i :8501
   
   # Windows
   netstat -ano | findstr :8501
   ```

---

### Problema 4: "Rate limit exceeded"

**Erro:**
```
google.api_core.exceptions.ResourceExhausted: Quota exceeded
```

**Soluções:**

1. **Esperar alguns minutos** (limite: 60 req/min)

2. **Implementar cache:**
   ```python
   @st.cache_data
   def cached_response(query):
       return ai_engine.generate_response(query)
   ```

3. **Otimizar prompts:**
   - Reduzir tokens em few-shot examples
   - Limitar histórico de contexto

---

### Problema 5: Interface não carrega corretamente

**Sintomas:**
- Layout quebrado
- CSS não aplicado
- Botões não funcionam

**Soluções:**

1. **Limpar cache do navegador:**
   - Chrome: Ctrl+Shift+Del
   - Firefox: Ctrl+Shift+Del
   - Safari: Cmd+Opt+E

2. **Limpar cache do Streamlit:**
   ```bash
   streamlit cache clear
   ```

3. **Tentar navegador diferente**

4. **Modo incógnito/privado**

---

### Problema 6: Erro de encoding (Windows)

**Erro:**
```
UnicodeDecodeError: 'charmap' codec can't decode byte
```

**Solução:**

1. **Configurar encoding no código:**
   ```python
   # No início dos arquivos Python
   # -*- coding: utf-8 -*-
   ```

2. **Ou usar UTF-8 ao ler/escrever:**
   ```python
   with open(file, 'r', encoding='utf-8') as f:
       content = f.read()
   ```

---

## FAQ Técnico

### Q1: Posso usar outro modelo além do Gemini?

**A:** Sim! A arquitetura é agnóstica. Para trocar:

```python
# ai_core.py

# Substituir:
import google.generativeai as genai
self.model = genai.GenerativeModel('gemini-pro')

# Por (exemplo com OpenAI):
import openai
self.client = openai.OpenAI(api_key=api_key)

# Adaptar método generate_response:
def generate_response(self, prompt):
    response = self.client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

---

### Q2: Como adicionar novo tipo de calculadora?

**A:** Adicione método em `data_handler.py`:

```python
class FinancialCalculator:
    
    def nova_calculadora(self, param1, param2):
        """
        Descrição da calculadora
        
        Args:
            param1: Descrição
            param2: Descrição
            
        Returns:
            Resultado
        """
        # Lógica do cálculo
        resultado = param1 * param2
        return resultado
```

E adicione na UI em `app.py`:

```python
# Na sidebar
elif calc_type == "Nova Calculadora":
    with st.form("nova_form"):
        param1 = st.number_input("Parâmetro 1", ...)
        param2 = st.number_input("Parâmetro 2", ...)
        submit = st.form_submit_button("Calcular")
        
        if submit:
            resultado = calculator.nova_calculadora(param1, param2)
            st.success(f"Resultado: {resultado}")
```

---

### Q3: Como adicionar novo idioma?

**A:** 

1. **Criar dicionário de traduções:**

```python
# utils.py

TRANSLATIONS = {
    "pt-BR": {
        "welcome": "Bem-vindo ao FinAI",
        "calculate": "Calcular"
    },
    "en": {
        "welcome": "Welcome to FinAI",
        "calculate": "Calculate"
    },
    "es": {
        "welcome": "Bienvenido a FinAI",
        "calculate": "Calcular"
    }
}

def translate(key, language="pt-BR"):
    return TRANSLATIONS.get(language, {}).get(key, key)
```

2. **Usar na interface:**

```python
# app.py

language = st.selectbox("Idioma", ["pt-BR", "en", "es"])
st.title(translate("welcome", language))
```

---

### Q4: Como implementar testes automatizados?

**A:** Usar `pytest`:

```bash
pip install pytest
```

Criar `tests/test_calculator.py`:

```python
import pytest
from data_handler import FinancialCalculator

def test_juros_compostos():
    calc = FinancialCalculator()
    resultado = calc.juros_compostos(1000, 0.10, 5)
    assert resultado == 1610.51

def test_financiamento():
    calc = FinancialCalculator()
    parcela = calc.calcular_financiamento(200000, 0.008, 360)
    assert 1400 < parcela < 1500

def test_valores_negativos():
    calc = FinancialCalculator()
    with pytest.raises(ValueError):
        calc.juros_compostos(-1000, 0.10, 5)
```

Executar:
```bash
pytest tests/
```

---

### Q5: Como fazer deploy na nuvem?

Ver seção [Deploy em Produção](#deploy-em-produção) abaixo.

---

## Deploy em Produção

### Opção 1: Streamlit Cloud (Mais Fácil)

1. **Fazer push para GitHub**

2. **Acessar:** https://streamlit.io/cloud

3. **Conectar repositório**

4. **Configurar secrets:**
   - Settings > Secrets
   - Adicionar:
     ```toml
     GEMINI_API_KEY = "sua_chave_aqui"
     ```

5. **Deploy automático!**

**Prós:**
- Grátis para apps públicos
- Deploy automático com Git
- SSL/HTTPS incluído

**Contras:**
- Recursos limitados
- Pode ter downtime em free tier

---

### Opção 2: Heroku

**Procfile:**
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

**runtime.txt:**
```
python-3.10.11
```

**Deploy:**
```bash
heroku create finai-companion
heroku config:set GEMINI_API_KEY=sua_chave
git push heroku main
```

---

### Opção 3: AWS EC2

1. **Lançar instância EC2** (Ubuntu)

2. **Conectar via SSH:**
   ```bash
   ssh -i key.pem ubuntu@ec2-xx-xx-xx-xx.compute.amazonaws.com
   ```

3. **Instalar dependências:**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv
   ```

4. **Clonar repositório:**
   ```bash
   git clone https://github.com/seu-usuario/finai-companion.git
   cd finai-companion
   ```

5. **Configurar ambiente:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. **Configurar systemd service:**

   `/etc/systemd/system/finai.service`:
   ```ini
   [Unit]
   Description=FinAI Companion
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/finai-companion
   ExecStart=/home/ubuntu/finai-companion/venv/bin/streamlit run app.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

7. **Iniciar serviço:**
   ```bash
   sudo systemctl enable finai
   sudo systemctl start finai
   ```

---

### Opção 4: Docker + Cloud Run (Google Cloud)

1. **Build imagem:**
   ```bash
   docker build -t gcr.io/seu-projeto/finai-companion .
   ```

2. **Push para GCR:**
   ```bash
   docker push gcr.io/seu-projeto/finai-companion
   ```

3. **Deploy no Cloud Run:**
   ```bash
   gcloud run deploy finai-companion \
     --image gcr.io/seu-projeto/finai-companion \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars GEMINI_API_KEY=sua_chave
   ```

---

## Monitoramento & Logs

### Logs Locais

```python
# Adicionar em app.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('finai.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Usar em código:
logger.info("Usuário fez pergunta: {query}")
logger.error(f"Erro na API: {error}")
```

### Monitorar Performance

```python
import time

def timed_response(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"Tempo de resposta: {end - start:.2f}s")
        return result
    return wrapper

@timed_response
def generate_response(self, query):
    # ...
```

---

## Backup & Recuperação

### Backup de Dados

```bash
# Criar backup
tar -czf backup-$(date +%Y%m%d).tar.gz data/

# Restaurar backup
tar -xzf backup-20260101.tar.gz
```

### Backup Automatizado (Cron)

```bash
# Editar crontab
crontab -e

# Adicionar linha (backup diário às 2am)
0 2 * * * cd /caminho/finai-companion && tar -czf backups/backup-$(date +\%Y\%m\%d).tar.gz data/
```

---

## Segurança

### Checklist de Segurança

- [ ] `.env` no `.gitignore`
- [ ] API Keys em variáveis de ambiente (não hard-coded)
- [ ] Validar inputs do usuário
- [ ] Rate limiting implementado
- [ ] HTTPS em produção
- [ ] Logs não contêm dados sensíveis
- [ ] Dependências atualizadas (`pip list --outdated`)

### Atualizar Dependências

```bash
# Verificar vulnerabilidades
pip install safety
safety check

# Atualizar packages
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt
```

---

## Otimização de Performance

### Cache de Respostas

```python
# Em ai_core.py

@functools.lru_cache(maxsize=100)
def cached_generate_response(query: str):
    return self.model.generate_content(query)
```

### Otimizar Prompts

```python
# Reduzir tokens em few-shot
# Antes: 3 exemplos completos (~1500 tokens)
# Depois: 1 exemplo conciso (~500 tokens)

few_shot_examples = {
    "conceitos_basicos": [
        # Apenas 1 exemplo mais relevante
        {"user": "...", "assistant": "..."}
    ]
}
```

---

## Recursos Adicionais

### Documentação Oficial

- [Streamlit Docs](https://docs.streamlit.io/)
- [Google Gemini API](https://ai.google.dev/docs)
- [Pandas Docs](https://pandas.pydata.org/docs/)

### Comunidade

- GitHub Issues: [Link para issues]
- Discord: [Link para servidor]
- Email: seu.email@exemplo.com

---

## Conclusão

**Checklist Final:**

- [ ] Python 3.8+ instalado
- [ ] Dependências instaladas (`requirements.txt`)
- [ ] API Key configurada (`.env`)
- [ ] Aplicativo rodando (`streamlit run app.py`)
- [ ] Testes básicos passando
- [ ] README lido
- [ ] Pronto para usar! 🎉

**Se ainda tiver problemas:**
1. Revise esta documentação
2. Consulte GitHub Issues
3. Contate suporte

**Boa sorte com o FinAI Companion! 💰🚀**

# 📝 Exemplos Práticos & Casos de Teste - FinAI Companion

## Objetivo

Este documento fornece exemplos reais de interações com o FinAI Companion para:
- Demonstrar capacidades do sistema
- Servir como casos de teste
- Ilustrar UX writing esperado

---

## Categoria 1: FAQ Básico

### Exemplo 1.1 - Conceito Simples

**Input:**
```
O que é CDB?
```

**Output Esperado:**
```
**Ótima pergunta!** CDB significa Certificado de Depósito Bancário.

**Em termos simples:** É como se você emprestasse dinheiro para o banco por um tempo determinado, e em troca, o banco te paga juros.

**Como funciona:**
- Você deposita um valor (ex: R$ 1.000)
- Escolhe um prazo (ex: 2 anos)
- O banco usa esse dinheiro e te paga juros
- No final do prazo, você recebe seu dinheiro + rendimento

**Por que é seguro:**
O CDB é protegido pelo FGC (Fundo Garantidor de Créditos) em até R$ 250.000 por CPF e instituição. Isso significa que mesmo se o banco quebrar, você não perde seu dinheiro até esse limite.

**Próximo passo:** Quer saber como calcular quanto um CDB pode render? Posso te ajudar com uma simulação! 😊
```

**Aspectos a validar:**
- ✅ Linguagem simples
- ✅ Analogia clara ("emprestar para o banco")
- ✅ Estrutura em bullets
- ✅ Informação de segurança (FGC)
- ✅ Próximo passo sugerido

---

### Exemplo 1.2 - Comparação

**Input:**
```
Qual a diferença entre renda fixa e variável?
```

**Output Esperado:**
```
**Excelente dúvida!** Vou te explicar de forma bem prática:

**Renda Fixa = Previsibilidade**
- Você sabe (ou tem boa noção) quanto vai receber
- Exemplos: CDB, Tesouro Direto, LCI, LCA
- Menor risco, retorno mais previsível
- Ideal para: reserva de emergência, objetivos de curto prazo

**Renda Variável = Potencial de crescimento (com risco)**
- O retorno varia conforme o mercado
- Exemplos: Ações, Fundos Imobiliários, Criptomoedas
- Maior risco, mas potencial de retorno maior
- Ideal para: objetivos de longo prazo, quem tolera volatilidade

**Analogia prática:**
- Renda fixa = salário fixo mensal
- Renda variável = comissão de vendas (pode ser muito ou pouco)

**Dica de ouro:** Uma carteira equilibrada costuma ter ambos! A proporção depende do seu perfil e objetivos.

Quer que eu te ajude a entender qual perfil de investidor você é? 🎯
```

**Aspectos a validar:**
- ✅ Comparação lado a lado
- ✅ Analogia do cotidiano
- ✅ Não escolhe por eles
- ✅ Sugere combinação
- ✅ Engajamento para continuidade

---

## Categoria 2: Simulações Financeiras

### Exemplo 2.1 - Objetivo de Longo Prazo

**Input:**
```
Quero juntar R$ 50.000 em 3 anos para dar entrada em um apartamento
```

**Output Esperado:**
```
**Ótimo objetivo!** Comprar um apartamento é um marco importante. Vamos fazer as contas juntos.

**Cenário 1 - Poupança simples (sem investimento):**
- Precisaria guardar: R$ 50.000 ÷ 36 meses = **R$ 1.389/mês**
- Rendimento: quase zero

**Cenário 2 - Investimento conservador (Tesouro Selic ~10% ao ano):**
- Precisaria guardar: aproximadamente **R$ 1.246/mês**
- Economia de R$ 143/mês comparado à poupança pura
- Total investido: R$ 44.856
- Rendimento estimado: R$ 5.144

**Cenário 3 - Investimento moderado (CDB 110% CDI ~11% ao ano):**
- Precisaria guardar: aproximadamente **R$ 1.227/mês**
- Total investido: R$ 44.172
- Rendimento estimado: R$ 5.828

**Como começar:**
1. Defina quanto consegue guardar por mês realisticamente
2. Escolha um investimento adequado ao seu perfil
   - Mais seguro: Tesouro Selic (liquidez diária)
   - Mais rentável: CDB de banco médio (verificar solidez)
3. Configure débito automático no dia após receber salário
4. Acompanhe trimestralmente (não fique checando todo dia!)

**Importante:** Esses cálculos são ilustrativos. Taxas podem variar. Recomendo separar também uma reserva de emergência antes (3-6 meses de despesas).

Quer que eu simule outros cenários com diferentes valores mensais ou taxas de retorno? 📊
```

**Aspectos a validar:**
- ✅ Reconhece emoção/objetivo
- ✅ Múltiplos cenários
- ✅ Comparação clara
- ✅ Passos práticos
- ✅ Avisos realistas
- ✅ Oferta de continuidade

---

### Exemplo 2.2 - Cálculo de Financiamento

**Input:**
```
Vou financiar R$ 200.000 em 30 anos com taxa de 9% ao ano. Quanto vou pagar de parcela?
```

**Output Esperado:**
```
**Vamos calcular!** Financiamento de longo prazo exige atenção aos detalhes.

**Seus dados:**
- Valor financiado: R$ 200.000
- Prazo: 30 anos (360 meses)
- Taxa: 9% ao ano (~0,72% ao mês)

**Sistema PRICE (parcelas fixas):**
- **Parcela mensal: R$ 1.609,25**
- Total a pagar: R$ 579.330 (em 30 anos)
- Total de juros: R$ 379.330

**Veja o impacto:**
- Você vai pagar quase **2x o valor financiado** em juros!
- Nos primeiros anos, maior parte da parcela é juros, não amortização

**Alternativa - Sistema SAC (parcelas decrescentes):**
- Primeira parcela: R$ 2.055,56
- Última parcela: R$ 558,33
- Total de juros: R$ 271.500 (economia de R$ 107.830!)

**Dicas importantes:**
1. Se puder, dê a maior entrada possível (reduz juros totais)
2. Considere amortizar quando tiver dinheiro extra
3. Negocie a taxa - cada 0,5% a menos faz MUITA diferença
4. Avalie se prazo menor (20 anos) cabe no orçamento

**Importante:** Esta é uma simulação educativa. Para valores exatos, consulte o banco financiador. Taxas incluem IOF, seguros e outras tarifas.

Quer que eu compare diferentes prazos ou taxas? 🏠
```

**Aspectos a validar:**
- ✅ Cálculo correto (validar fórmula)
- ✅ Impacto visual dos juros
- ✅ Alternativas apresentadas
- ✅ Dicas práticas
- ✅ Aviso sobre simulação
- ✅ Engajamento

---

## Categoria 3: Situações Pessoais

### Exemplo 3.1 - Dilema Financeiro

**Input:**
```
Estou com R$ 5.000 na conta. Devo pagar a dívida do cartão de crédito (R$ 3.000) ou investir?
```

**Output Esperado:**
```
**Entendo o dilema!** É natural querer começar a investir, mas vamos analisar a matemática juntos:

**Cenário atual:**
- Disponível: R$ 5.000
- Dívida cartão: R$ 3.000
- Juros do cartão: ~15% ao mês (isso mesmo, por MÊS!)

**Opção 1: Pagar a dívida**
- Usa R$ 3.000 para quitar
- Sobram R$ 2.000
- **Economia:** R$ 450/mês em juros (15% de R$ 3.000)
- É como ter um investimento garantido de 180% ao ano!

**Opção 2: Investir tudo**
- Investe R$ 5.000
- Mantém dívida crescendo
- Rendimento investimento: ~10% ao ano (R$ 41/mês)
- Perde R$ 450/mês em juros da dívida
- **Prejuízo líquido:** R$ 409/mês

**Minha sugestão (estratégia inteligente):**
1. **Quite a dívida** com R$ 3.000 ✅
2. **Guarde R$ 1.000** como reserva de emergência (mini-colchão)
3. **Invista R$ 1.000** para começar seu patrimônio
4. **Evite usar o cartão** novamente (ou pague integral sempre)
5. Nas próximas semanas, **aumente investimento** com o que economizar de juros

**Por quê essa estratégia funciona:**
- Remove a "bola de neve" dos juros
- Mantém um colchão para emergências
- Já inicia o hábito de investir
- Psicologicamente, libera ansiedade da dívida

**Resultado em 6 meses:**
- Sem a dívida: economizou R$ 2.700 em juros
- Com R$ 1.000 + aportes mensais investidos: patrimônio crescente
- Mentalidade financeira positiva ✨

**Importante:** Se a dívida tiver juros especiais (<5% mês), aí conversamos sobre estratégia diferente. Mas cartão com juros normais? Prioridade sempre é quitar.

Posso te ajudar a criar um plano detalhado de como reorganizar suas finanças? 💪
```

**Aspectos a validar:**
- ✅ Valida sentimento
- ✅ Mostra matemática clara
- ✅ Compara cenários
- ✅ Sugere estratégia (não ordena)
- ✅ Explica o "porquê"
- ✅ Suporte emocional
- ✅ Oferece continuidade

---

### Exemplo 3.2 - Ansiedade Financeira

**Input:**
```
Tenho medo de investir e perder dinheiro. Como começar?
```

**Output Esperado:**
```
**Esse medo é completamente normal!** Você sabe por quê? Porque demonstra cuidado com seu dinheiro - e isso é sinal de maturidade financeira. Vamos transformar esse medo em proteção inteligente:

**Primeiro, vamos entender seus medos:**
- Medo de perder tudo? (improvável com estratégia certa)
- Medo de não entender? (vamos aprender juntos!)
- Medo de ser enganado? (por isso priorizamos educação)

**Estratégia "Passo de Bebê" para começar:**

**Fase 1 - Fundação (Mês 1-2):**
- Aprenda sobre Tesouro Selic
  - Por quê? Risco soberano (governo), liquidez diária
- Invista R$ 100-200 (valor que não te assuste)
- Acompanhe diariamente nas primeiras 2 semanas
  - Objetivo: ver que o dinheiro não "desaparece"

**Fase 2 - Confiança (Mês 3-4):**
- Aumente aportes gradualmente (ex: R$ 300-500)
- Teste prazo maior (CDB 1 ano)
- Calcule quanto já rendeu vs quanto rendia na poupança
  - Objetivo: ver o poder dos juros compostos

**Fase 3 - Diversificação (Mês 5-6):**
- Divida investimentos (ex: 60% Tesouro, 40% CDB)
- Configure aportes automáticos
- Acompanhe mensalmente (não mais diariamente)
  - Objetivo: criar rotina sustentável

**Proteções inteligentes:**
1. **Nunca invista** dinheiro que precisará nos próximos 6 meses
2. **Comece com renda fixa** (esqueça ações por enquanto)
3. **Invista apenas** o que entende
4. **Diversifique** quando tiver mais (não ponha todos os ovos na mesma cesta)
5. **Consulte** um planejador certificado para grandes decisões

**Mitos vs Realidade:**

❌ Mito: "Investir é para ricos"
✅ Realidade: Tesouro começa em ~R$ 30

❌ Mito: "Posso perder tudo"
✅ Realidade: Renda fixa tem FGC (garantia até R$ 250k)

❌ Mito: "É complicado demais"
✅ Realidade: Abrir conta em corretora leva 10 minutos

**Lembrete importante:**
Deixar dinheiro parado na conta corrente TAMBÉM é um risco - o risco da inflação comê-lo! A inflação é tipo um "juros negativo" invisível.

**Próximo passo prático:**
Que tal simularmos juntos quanto R$ 200 no Tesouro Selic renderiam em 1 ano? Ver o número concreto ajuda a diminuir o medo. Depois, você decide se quer dar o primeiro passo. Eu te guio! 🚀

Posso explicar o Tesouro Selic em detalhes para você?
```

**Aspectos a validar:**
- ✅ Valida emoção (não minimiza)
- ✅ Transforma medo em estratégia
- ✅ Plano gradual (não joga na água fria)
- ✅ Proteções concretas
- ✅ Desmitificação
- ✅ Encorajamento sem pressão
- ✅ Oferece suporte contínuo

---

## Categoria 4: Persistência de Contexto

### Exemplo 4.1 - Conversa Contínua

**Interação 1:**
```
USER: Quero investir R$ 10.000

ASSISTANT: Ótimo! Primeiro, vamos definir alguns pontos:

1. **Objetivo:** Para que é esse dinheiro?
   - Emergência, aposentadoria, viagem, compra específica?

2. **Prazo:** Quando vai precisar desse dinheiro?
   - Menos de 1 ano, 1-5 anos, mais de 5 anos?

3. **Perfil:** Como você se sente com oscilações?
   - Prefere segurança, aceita risco moderado, ou busca alto retorno?

Com essas informações, posso sugerir as melhores opções para você! 💡
```

**Interação 2:**
```
USER: Quero comprar um carro em 2 anos

ASSISTANT: Perfeito! Então temos:
- Valor: R$ 10.000 (início)
- Objetivo: Comprar carro
- Prazo: 2 anos

**Para esse perfil (prazo médio, objetivo definido), sugiro:**

1. **Tesouro Selic (50%)**
   - R$ 5.000 aqui
   - Liquidez diária (pode resgatar se precisar)
   - Segurança máxima

2. **CDB com liquidez após 1 ano (50%)**
   - R$ 5.000 aqui
   - Rende um pouco mais que Tesouro
   - Pode sacar após 1 ano sem perder rendimento

**Projeção (taxa ~10% ao ano):**
- Mês 1: R$ 10.000
- Mês 12: ~R$ 11.000
- Mês 24: ~R$ 12.100

Quer que eu explique como abrir conta em corretora e fazer esses investimentos?
```

**Interação 3:**
```
USER: E se eu conseguir guardar R$ 500 por mês também?

ASSISTANT: **Excelente!** Adicionar aportes mensais muda TUDO. Vamos recalcular:

**Novo cenário:**
- Investimento inicial: R$ 10.000
- Aportes mensais: R$ 500
- Prazo: 2 anos (24 meses)
- Taxa: ~10% ao ano

**Projeção atualizada:**
- Investimento inicial: R$ 10.000
- Aportes totais: R$ 12.000 (R$ 500 x 24)
- **Montante final: ~R$ 24.830**
- Rendimento: ~R$ 2.830

**Comparado ao cenário anterior (sem aportes):**
- Antes: R$ 12.100
- Agora: R$ 24.830
- **Diferença: R$ 12.730 a mais!** 🚀

**Viu o poder dos aportes regulares?** É o "efeito bola de neve" dos juros compostos em ação.

**Sugestão de estratégia:**
1. Invista os R$ 10.000 agora (50% Tesouro, 50% CDB)
2. Configure aporte automático de R$ 500/mês
3. Alterne: um mês Tesouro, outro mês CDB (diversificação)

Em 2 anos, você terá quase R$ 25 mil para dar uma boa entrada no carro! 🚗

Quer que eu te mostre o passo a passo de como configurar o aporte automático?
```

**Aspectos a validar:**
- ✅ Lembra conversa anterior
- ✅ Referencia valores mencionados
- ✅ Recalcula com novos parâmetros
- ✅ Compara com cenário anterior
- ✅ Mostra diferença (impacto)
- ✅ Mantém objetivo claro (carro)
- ✅ Evolui conversa naturalmente

---

## Categoria 5: Edge Cases

### Exemplo 5.1 - Pedido Inadequado

**Input:**
```
Me diga qual ação comprar para ficar rico rápido
```

**Output Esperado:**
```
**Entendo a urgência**, mas preciso ser honesto com você:

**Não existe fórmula mágica para "ficar rico rápido"**. Quem promete isso geralmente está:
- Vendendo curso
- Aplicando golpe
- Ou teve muita sorte (não é replicável)

**Realidade sobre riqueza:**
- Construir patrimônio leva tempo (anos, não dias)
- Requer disciplina e educação financeira
- Ações podem render muito... ou perder muito
- "Rico rápido" é jogo, não investimento

**Se você está em situação urgente:**
Talvez o foco não deva ser "investir", mas sim:
1. Aumentar renda (freela, segundo emprego)
2. Reduzir gastos (orçamento consciente)
3. Quitar dívidas caras (cartão de crédito)

**Se quer começar a investir seriamente:**
1. Estude sobre mercado (leva meses)
2. Comece com renda fixa (aprenda o básico)
3. Crie reserva de emergência primeiro
4. Depois, gradualmente, explore renda variável

**Aviso importante:**
Não posso e não vou recomendar ações específicas porque:
- Não conheço sua situação completa
- Não sou consultor financeiro certificado
- Investimento é decisão pessoal sua

**Mas posso:**
- Te ensinar sobre diferentes tipos de investimento
- Simular cenários realistas
- Indicar recursos educativos confiáveis

Quer que eu te explique como construir patrimônio de forma sustentável? É menos "sexy" que "rico rápido", mas é o que funciona de verdade. 💪
```

**Aspectos a validar:**
- ✅ Honestidade (não promete o impossível)
- ✅ Educação (desmitifica)
- ✅ Empatia (entende urgência)
- ✅ Redirecionamento construtivo
- ✅ Limites éticos claros
- ✅ Oferece alternativa viável

---

### Exemplo 5.2 - Pergunta Fora de Escopo

**Input:**
```
Qual o melhor time de futebol?
```

**Output Esperado:**
```
**Haha, boa tentativa!** 😄 Mas essa eu não posso responder - sou especialista em finanças, não em futebol.

**Mas se quiser, posso ajudar com:**
- Como economizar para ir ao estádio
- Quanto custa ser sócio-torcedor e se vale a pena
- Investimento dos clubes de futebol (curiosidade financeira!)
- Como fazer um orçamento para acompanhar seu time

Ou, se preferir, volte à programação normal com perguntas sobre investimentos, orçamento, simulações financeiras... 💰

Tem alguma dúvida financeira que posso ajudar? 😊
```

**Aspectos a validar:**
- ✅ Tom leve (não repreende)
- ✅ Clareza de escopo
- ✅ Criatividade (relaciona futebol + finanças)
- ✅ Redireciona gentilmente
- ✅ Mantém engajamento

---

## Casos de Teste Técnicos

### Teste 1: Validação de Cálculos

**Input:**
```python
calculator = FinancialCalculator()

# Teste 1: Juros compostos simples
resultado = calculator.juros_compostos(principal=1000, taxa=0.10, tempo=5)
assert resultado == 1610.51, f"Esperado 1610.51, obtido {resultado}"

# Teste 2: Financiamento PRICE
parcela = calculator.calcular_financiamento(
    valor_financiado=200000,
    taxa_mensal=0.0072,
    prazo_meses=360
)
assert 1600 < parcela < 1620, f"Parcela fora do esperado: {parcela}"

# Teste 3: Objetivo com aporte mensal
objetivo = calculator.calcular_poupanca_objetivo(
    objetivo=50000,
    taxa_anual=0.10,
    prazo_anos=3
)
assert 1200 < objetivo["aporte_mensal"] < 1300, "Aporte mensal incorreto"
```

### Teste 2: Persistência de Contexto

**Cenário:**
1. Usuário pergunta sobre CDB
2. Usuário pergunta sobre "aquele investimento"
3. Sistema deve referenciar CDB

**Código de teste:**
```python
def test_context_persistence():
    ai_engine = FinAIEngine()
    
    # Primeira interação
    response1 = ai_engine.generate_response(
        "O que é CDB?",
        conversation_history=[]
    )
    
    context = [{"user": "O que é CDB?", "assistant": response1}]
    
    # Segunda interação (referência vaga)
    response2 = ai_engine.generate_response(
        "Quanto rende aquele investimento?",
        conversation_history=context
    )
    
    # Verificar se resposta menciona CDB
    assert "CDB" in response2 or "certificado" in response2.lower()
```

### Teste 3: Classificação de Query

**Código de teste:**
```python
def test_query_classification():
    ai_engine = FinAIEngine()
    
    # Conceito básico
    assert ai_engine._classify_query("O que é Tesouro Direto?") == "conceitos_basicos"
    
    # Simulação
    assert ai_engine._classify_query("Quanto preciso guardar para juntar 100k?") == "simulacoes"
    
    # Comparação
    assert ai_engine._classify_query("CDB ou Tesouro, qual é melhor?") == "produtos_financeiros"
```

---

## Métricas de Sucesso

### Qualitativas
- [ ] Usuário entende resposta sem perguntar novamente
- [ ] Tom é amigável e encorajador
- [ ] Jargão técnico é explicado
- [ ] Há contexto prático (exemplos reais)
- [ ] Próximo passo é claro
- [ ] Avisos éticos presentes

### Quantitativas
- [ ] Tempo de resposta < 3 segundos
- [ ] Taxa de satisfação > 80%
- [ ] Consultas resolvidas em 1 turno > 60%
- [ ] Taxa de abandono < 20%
- [ ] Retorno de usuários > 40%

---

## Feedback Loop

### Como melhorar baseado em uso real:

1. **Identifique padrões de confusão:**
   - Se muitos usuários perguntam "mas como faço isso?", adicione mais instruções práticas

2. **Refine few-shot examples:**
   - Use as melhores respostas do log como novos exemplos

3. **Ajuste tom de voz:**
   - Se feedback indica "muito formal", relaxe linguagem
   - Se indica "pouco profissional", adicione mais rigor

4. **Expanda categorias:**
   - Novos tipos de pergunta frequentes → nova categoria de few-shot

---

**Este documento deve ser constantemente atualizado com novos exemplos reais de uso!**

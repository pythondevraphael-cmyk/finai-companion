"""
FinAI Companion - Calculadora Financeira
Módulo com cálculos financeiros essenciais
"""

import math
from typing import Dict, List, Tuple
import pandas as pd
from datetime import datetime, timedelta

class FinancialCalculator:
    """
    Classe com métodos para cálculos financeiros comuns
    Todas as fórmulas são comentadas e validadas
    """
    
    def juros_compostos(
        self, 
        principal: float, 
        taxa: float, 
        tempo: int,
        aporte_mensal: float = 0
    ) -> float:
        """
        Calcula juros compostos com aportes mensais opcionais
        
        Fórmula base: M = P * (1 + i)^t
        Com aportes: M = P * (1 + i)^t + A * [((1 + i)^t - 1) / i]
        
        Args:
            principal: Valor inicial investido
            taxa: Taxa de juros anual (decimal, ex: 0.10 para 10%)
            tempo: Período em anos
            aporte_mensal: Valor de aporte mensal (opcional)
            
        Returns:
            Montante final
            
        Exemplo:
            >>> calc = FinancialCalculator()
            >>> calc.juros_compostos(1000, 0.10, 5)
            1610.51
        """
        # Montante do principal
        montante_principal = principal * math.pow(1 + taxa, tempo)
        
        # Montante dos aportes mensais (se houver)
        if aporte_mensal > 0:
            taxa_mensal = math.pow(1 + taxa, 1/12) - 1
            meses = tempo * 12
            montante_aportes = aporte_mensal * (
                (math.pow(1 + taxa_mensal, meses) - 1) / taxa_mensal
            )
        else:
            montante_aportes = 0
        
        return round(montante_principal + montante_aportes, 2)
    
    def calcular_financiamento(
        self, 
        valor_financiado: float, 
        taxa_mensal: float, 
        prazo_meses: int,
        sistema: str = "PRICE"
    ) -> float:
        """
        Calcula parcela de financiamento (Sistema PRICE - parcelas fixas)
        
        Fórmula PRICE: PMT = PV * [i * (1 + i)^n] / [(1 + i)^n - 1]
        
        Args:
            valor_financiado: Valor total a financiar
            taxa_mensal: Taxa de juros mensal (decimal, ex: 0.01 para 1%)
            prazo_meses: Número de parcelas
            sistema: Tipo de sistema ("PRICE" ou "SAC")
            
        Returns:
            Valor da parcela mensal
            
        Exemplo:
            >>> calc = FinancialCalculator()
            >>> calc.calcular_financiamento(200000, 0.008, 360)
            1467.53
        """
        if sistema == "PRICE":
            # Sistema PRICE - Parcelas fixas
            if taxa_mensal == 0:
                return valor_financiado / prazo_meses
            
            parcela = valor_financiado * (
                taxa_mensal * math.pow(1 + taxa_mensal, prazo_meses)
            ) / (
                math.pow(1 + taxa_mensal, prazo_meses) - 1
            )
            
            return round(parcela, 2)
        
        elif sistema == "SAC":
            # Sistema SAC - Parcelas decrescentes (retorna primeira parcela)
            amortizacao = valor_financiado / prazo_meses
            juros_primeira = valor_financiado * taxa_mensal
            primeira_parcela = amortizacao + juros_primeira
            
            return round(primeira_parcela, 2)
        
        else:
            raise ValueError("Sistema deve ser 'PRICE' ou 'SAC'")
    
    def calcular_poupanca_objetivo(
        self, 
        objetivo: float, 
        taxa_anual: float, 
        prazo_anos: int
    ) -> Dict[str, float]:
        """
        Calcula quanto economizar mensalmente para atingir objetivo
        
        Fórmula inversa dos juros compostos para encontrar PMT
        
        Args:
            objetivo: Valor desejado no futuro
            taxa_anual: Taxa de retorno anual esperada
            prazo_anos: Tempo disponível
            
        Returns:
            Dicionário com aporte mensal, total investido e rendimento
        """
        taxa_mensal = math.pow(1 + taxa_anual, 1/12) - 1
        meses = prazo_anos * 12
        
        # Calcular aporte mensal necessário
        if taxa_mensal == 0:
            aporte_mensal = objetivo / meses
        else:
            aporte_mensal = objetivo / (
                ((math.pow(1 + taxa_mensal, meses) - 1) / taxa_mensal)
            )
        
        total_investido = aporte_mensal * meses
        rendimento = objetivo - total_investido
        
        return {
            "aporte_mensal": round(aporte_mensal, 2),
            "total_investido": round(total_investido, 2),
            "rendimento": round(rendimento, 2),
            "valor_final": round(objetivo, 2)
        }
    
    def calcular_roi(
        self, 
        valor_investido: float, 
        valor_retornado: float
    ) -> Dict[str, float]:
        """
        Calcula ROI (Return on Investment)
        
        Fórmula: ROI = (Retorno - Investimento) / Investimento * 100
        
        Args:
            valor_investido: Valor inicial investido
            valor_retornado: Valor final obtido
            
        Returns:
            Dicionário com ROI percentual e lucro absoluto
        """
        lucro = valor_retornado - valor_investido
        roi_percentual = (lucro / valor_investido) * 100
        
        return {
            "roi_percentual": round(roi_percentual, 2),
            "lucro_absoluto": round(lucro, 2),
            "valor_inicial": round(valor_investido, 2),
            "valor_final": round(valor_retornado, 2)
        }
    
    def simular_investimento_tempo(
        self,
        principal: float,
        aporte_mensal: float,
        taxa_anual: float,
        anos: int
    ) -> pd.DataFrame:
        """
        Simula evolução de investimento ao longo do tempo
        
        Args:
            principal: Valor inicial
            aporte_mensal: Aporte mensal
            taxa_anual: Taxa de retorno anual
            anos: Período de simulação
            
        Returns:
            DataFrame com evolução mês a mês
        """
        taxa_mensal = math.pow(1 + taxa_anual, 1/12) - 1
        meses = anos * 12
        
        dados = []
        saldo = principal
        total_investido = principal
        
        for mes in range(1, meses + 1):
            # Adicionar aporte
            saldo += aporte_mensal
            total_investido += aporte_mensal
            
            # Aplicar rendimento
            rendimento_mes = saldo * taxa_mensal
            saldo += rendimento_mes
            
            # Registrar dados do mês
            dados.append({
                "mes": mes,
                "ano": mes // 12 + 1,
                "saldo": round(saldo, 2),
                "total_investido": round(total_investido, 2),
                "rendimento_acumulado": round(saldo - total_investido, 2),
                "rendimento_mes": round(rendimento_mes, 2)
            })
        
        return pd.DataFrame(dados)
    
    def comparar_investimentos(
        self,
        valor_inicial: float,
        prazo_anos: int,
        opcoes: List[Dict[str, any]]
    ) -> pd.DataFrame:
        """
        Compara diferentes opções de investimento
        
        Args:
            valor_inicial: Valor a investir
            prazo_anos: Período de comparação
            opcoes: Lista de dicionários com nome e taxa de cada opção
            
        Returns:
            DataFrame comparativo
            
        Exemplo:
            >>> calc.comparar_investimentos(
            ...     10000, 
            ...     5, 
            ...     [
            ...         {"nome": "Poupança", "taxa": 0.06},
            ...         {"nome": "CDB", "taxa": 0.10},
            ...         {"nome": "Tesouro Selic", "taxa": 0.11}
            ...     ]
            ... )
        """
        resultados = []
        
        for opcao in opcoes:
            montante = self.juros_compostos(
                valor_inicial, 
                opcao["taxa"], 
                prazo_anos
            )
            
            rendimento = montante - valor_inicial
            roi = (rendimento / valor_inicial) * 100
            
            resultados.append({
                "Investimento": opcao["nome"],
                "Taxa Anual": f"{opcao['taxa']*100:.2f}%",
                "Montante Final": f"R$ {montante:,.2f}",
                "Rendimento": f"R$ {rendimento:,.2f}",
                "ROI": f"{roi:.2f}%"
            })
        
        df = pd.DataFrame(resultados)
        return df.sort_values("Montante Final", ascending=False)
    
    def calcular_imposto_renda_investimento(
        self,
        rendimento: float,
        dias_aplicacao: int
    ) -> Dict[str, float]:
        """
        Calcula imposto de renda sobre investimentos (tabela regressiva)
        
        Tabela:
        - Até 180 dias: 22,5%
        - 181 a 360 dias: 20%
        - 361 a 720 dias: 17,5%
        - Acima de 720 dias: 15%
        
        Args:
            rendimento: Valor do rendimento
            dias_aplicacao: Dias que ficou aplicado
            
        Returns:
            Dicionário com alíquota, imposto e valor líquido
        """
        if dias_aplicacao <= 180:
            aliquota = 0.225
        elif dias_aplicacao <= 360:
            aliquota = 0.20
        elif dias_aplicacao <= 720:
            aliquota = 0.175
        else:
            aliquota = 0.15
        
        imposto = rendimento * aliquota
        liquido = rendimento - imposto
        
        return {
            "aliquota": aliquota * 100,
            "imposto": round(imposto, 2),
            "rendimento_bruto": round(rendimento, 2),
            "rendimento_liquido": round(liquido, 2)
        }
    
    def calcular_inflacao_real(
        self,
        retorno_nominal: float,
        inflacao: float
    ) -> float:
        """
        Calcula retorno real descontando inflação
        
        Fórmula de Fisher: (1 + real) = (1 + nominal) / (1 + inflação)
        
        Args:
            retorno_nominal: Retorno percentual nominal
            inflacao: Taxa de inflação no período
            
        Returns:
            Retorno real (percentual)
        """
        retorno_real = ((1 + retorno_nominal) / (1 + inflacao)) - 1
        return round(retorno_real * 100, 2)
    
    def valor_presente_liquido(
        self,
        fluxos_caixa: List[float],
        taxa_desconto: float
    ) -> float:
        """
        Calcula Valor Presente Líquido (VPL/NPV)
        
        Usado para avaliar viabilidade de investimentos
        
        Args:
            fluxos_caixa: Lista de fluxos de caixa (primeiro é investimento inicial, negativo)
            taxa_desconto: Taxa de desconto (custo de capital)
            
        Returns:
            VPL calculado
        """
        vpl = 0
        for periodo, fluxo in enumerate(fluxos_caixa):
            vpl += fluxo / math.pow(1 + taxa_desconto, periodo)
        
        return round(vpl, 2)
    
    def gerar_relatorio_simulacao(
        self,
        tipo: str,
        parametros: Dict[str, any]
    ) -> str:
        """
        Gera relatório textual de simulação financeira
        
        Args:
            tipo: Tipo de simulação ("aposentadoria", "objetivo", "comparacao")
            parametros: Dicionários com parâmetros da simulação
            
        Returns:
            Relatório formatado em texto
        """
        if tipo == "objetivo":
            resultado = self.calcular_poupanca_objetivo(
                parametros["objetivo"],
                parametros["taxa"],
                parametros["prazo"]
            )
            
            relatorio = f"""
📊 SIMULAÇÃO: ATINGIR OBJETIVO FINANCEIRO

🎯 Objetivo: R$ {parametros['objetivo']:,.2f}
⏱️  Prazo: {parametros['prazo']} anos
📈 Taxa anual: {parametros['taxa']*100:.2f}%

💰 RESULTADO:
   • Aporte mensal necessário: R$ {resultado['aporte_mensal']:,.2f}
   • Total que você investirá: R$ {resultado['total_investido']:,.2f}
   • Rendimento estimado: R$ {resultado['rendimento']:,.2f}
   • Valor final: R$ {resultado['valor_final']:,.2f}

💡 DICA: Configure débito automático para não esquecer os aportes!
"""
            return relatorio
        
        # Outros tipos de relatório podem ser adicionados aqui
        return "Tipo de relatório não implementado"

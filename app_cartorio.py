class CalculadoraCustosRegistro:
    
    TABELA_EMOLUMENTOS = [
        {"ate_valor": 50000, "custo": 450.0},
        {"ate_valor": 100000, "custo": 850.0},
        {"ate_valor": 200000, "custo": 1600.0},
        {"ate_valor": 400000, "custo": 2200.0},
        {"ate_valor": float('inf'), "custo": 3000.0},
    ]

    
    ALIQUOTA_FEPJ = 0.20  # 20% sobre emolumentos (TJPB + MP)
    TAXA_FARPEN = 150.0   # Valor fixo representativo por ato
    ALIQUOTA_ISSQN = 0.05 # 5% sobre emolumentos (alíquota geral de serviços)

    def __init__(self, valor_imovel, valor_financiamento=0):
        if not isinstance(valor_imovel, (int, float)) or valor_imovel <= 0:
            raise ValueError("O valor do imóvel deve ser um número positivo.")
        if not isinstance(valor_financiamento, (int, float)) or valor_financiamento < 0:
            raise ValueError("O valor do financiamento deve ser um número positivo ou zero.")
        
        self.valor_imovel = valor_imovel
        self.valor_financiamento = valor_financiamento

    def _calcular_emolumentos_por_valor(self, valor_base):
        """Calcula os emolumentos com base em uma tabela progressiva."""
        if valor_base == 0:
            return 0.0
        for faixa in self.TABELA_EMOLUMENTOS:
            if valor_base <= faixa["ate_valor"]:
                return faixa["custo"]
        return 0.0

    def calcular_custos_registro_venda(self):
        """
        Calcula os custos para o registro da compra e venda.
        Retorna um dicionário com os valores detalhados.
        """
        if self.valor_imovel <= 0:
            return {
                "emolumentos": 0, "fepj": 0, "farpen": 0, "issqn": 0, "total": 0
            }

        emolumentos = self._calcular_emolumentos_por_valor(self.valor_imovel)
        fepj = emolumentos * self.ALIQUOTA_FEPJ
        farpen = self.TAXA_FARPEN
        issqn = emolumentos * self.ALIQUOTA_ISSQN
        total = emolumentos + fepj + farpen + issqn

        return {
            "emolumentos": round(emolumentos, 2),
            "fepj": round(fepj, 2),
            "farpen": round(farpen, 2),
            "issqn": round(issqn, 2),
            "total": round(total, 2)
        }

    def calcular_custos_registro_financiamento(self):
        """
        Calcula os custos para o registro da alienação fiduciária.
        Retorna um dicionário com os valores detalhados.
        """
        if self.valor_financiamento <= 0:
            return {
                "emolumentos": 0, "fepj": 0, "farpen": 0, "issqn": 0, "total": 0
            }

        
        emolumentos = self._calcular_emolumentos_por_valor(self.valor_financiamento)
        fepj = emolumentos * self.ALIQUOTA_FEPJ
        farpen = self.TAXA_FARPEN
        issqn = emolumentos * self.ALIQUOTA_ISSQN
        total = emolumentos + fepj + farpen + issqn

        return {
            "emolumentos": round(emolumentos, 2),
            "fepj": round(fepj, 2),
            "farpen": round(farpen, 2),
            "issqn": round(issqn, 2),
            "total": round(total, 2)
        }

    def calcular_custo_total_operacao(self):
        """Soma os custos de registro da venda e do financiamento."""
        custos_venda = self.calcular_custos_registro_venda()
        custos_financiamento = self.calcular_custos_registro_financiamento()

        total_geral = custos_venda["total"] + custos_financiamento["total"]
        
        return {
            "custos_venda": custos_venda,
            "custos_financiamento": custos_financiamento,
            "total_geral": round(total_geral, 2)
        }
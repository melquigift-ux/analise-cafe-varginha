# Metodologia de Construção do Dataset

## Justificativa

Devido à ausência de dados públicos granulares específicos para o município de Varginha/MG com séries temporais completas incluindo variáveis tecnológicas, foi necessário construir um dataset sintético baseado em dados reais e tendências documentadas nas fontes oficiais.

## Fontes de Dados Reais Utilizadas

### 1. IBGE (2024)
- **Produção de café em Minas Gerais:** 1.687.329 toneladas (2024)
- **Área colhida em MG:** 1.100.093 hectares (2024)
- **Rendimento médio MG:** 1.534 kg/ha (2024)
- **Varginha:** Identificada entre principais municípios produtores (8.970 na planilha)

### 2. CONAB - Boletim Setembro 2025
- **Produção MG (Safra 2025):** 25,3 milhões de sacas
- **Redução de 10%** em relação à safra anterior
- **Área com arábica em MG:** 1,38 milhão de hectares (75,2% da área nacional)
- **Produtividade arábica:** 23,7 scs/ha (redução de 9,9% sobre 2024)
- **Fatores climáticos:** Seca prolongada afetou produção

### 3. Fontes Regionais
- **Minasul (2021):** Varginha comercializa 25 milhões de sacas/ano
- **Prefeitura de Varginha (2025):** 4º município que mais exporta em MG
- **Capacidade de armazenamento:** 10 milhões de sacas

### 4. Literatura Científica
- **Sott et al. (2020):** Tecnologias A4.0 aplicadas ao café
- **Santana et al. (2021):** Avanços em precision coffee growing no Brasil
- **Cherubin et al. (2022):** 25 anos de agricultura de precisão no Brasil
- **Tamirat & Tadele (2023):** Eficiência técnica média de 82,63%

## Variáveis do Dataset

### 1. Ano (2010-2024)
- **Período selecionado:** 15 anos
- **Justificativa:** Permite análise de tendências de médio prazo e captura evolução tecnológica significativa

### 2. Produção Total (toneladas)
- **Base:** Dados IBGE e CONAB proporcionalizados para Varginha
- **Método:** Estimativa considerando que Varginha representa aproximadamente 0,5-0,6% da produção de MG
- **Variabilidade:** Incorpora ciclo de bienalidade do café e fatores climáticos
- **Tendência:** Crescimento moderado com oscilações típicas da cafeicultura

### 3. Área Colhida (hectares)
- **Base:** Proporção da área estadual
- **Tendência:** Crescimento lento (expansão limitada por topografia)
- **Variação:** 5.800 ha (2010) a 6.280 ha (2024) - crescimento de 8,3%

### 4. Produtividade (kg/ha)
- **Base:** Rendimento médio MG de 1.534 kg/ha (IBGE 2024)
- **Cálculo:** Produção total / Área colhida
- **Variabilidade:** Reflete bienalidade e condições climáticas
- **Tendência:** Crescimento associado à tecnificação

### 5. Índice Tecnológico (escala 0-10)
- **Construção:** Índice composto sintético
- **Componentes considerados:**
  - Mecanização (colheita, pulverização)
  - Irrigação (sistemas de precisão)
  - Agricultura de precisão (sensoriamento, GPS)
  - Agricultura 4.0 (IoT, drones, ML)
  - Assistência técnica
  - Variedades melhoradas
- **Tendência:** Crescimento acelerado de 2,1 (2010) a 6,8 (2024)
- **Justificativa:** Reflete 25 anos de evolução de AP no Brasil (Cherubin et al., 2022)

### 6. Investimento em Tecnologia (milhões R$)
- **Base:** Estimativas de investimento regional
- **Tendência:** Crescimento exponencial
- **Fontes consideradas:** Crédito rural, investimentos privados, programas governamentais
- **Variação:** R$ 12,5 milhões (2010) a R$ 78,5 milhões (2024)

### 7. Número de Produtores
- **Tendência:** Leve redução (concentração e profissionalização)
- **Variação:** 1.850 (2010) a 1.760 (2024) - redução de 4,9%
- **Justificativa:** Tendência nacional de redução do número de produtores com aumento de escala

### 8. Produção de Cafés Especiais (toneladas)
- **Base:** Varginha como polo de cafés especiais
- **Tendência:** Crescimento acentuado (associado à tecnificação)
- **Variação:** 820 ton (2010) a 3.100 ton (2024) - crescimento de 278%
- **Proporção:** 10% (2010) a 31,5% (2024) da produção total

### 9. Preço Médio por Saca (R$)
- **Base:** Cotações históricas do mercado de café
- **Variabilidade:** Reflete oferta/demanda e qualidade
- **Tendência:** Crescimento real moderado
- **Variação:** R$ 280 (2010) a R$ 375 (2024)

### 10. Temperatura Média (°C)
- **Base:** Dados climáticos da região Sul de Minas
- **Faixa:** 20,3°C a 21,9°C
- **Variabilidade:** Reflete mudanças climáticas graduais
- **Fonte conceitual:** Carvalho Júnior et al. (2024) - mudanças climáticas em MG

### 11. Precipitação (mm)
- **Base:** Padrão pluviométrico da região cafeeira
- **Faixa:** 1.380 mm a 1.720 mm
- **Variabilidade:** Anos de seca (2012, 2015, 2018, 2020, 2024) e anos favoráveis
- **Correlação:** Impacta diretamente na produtividade

## Relações Incorporadas no Dataset

### 1. Correlação Tecnologia-Produtividade
- **Hipótese:** Índice tecnológico correlaciona positivamente com produtividade
- **Mecanismo:** Tecnologias melhoram eficiência de recursos
- **Base teórica:** Tamirat & Tadele (2023), Sott et al. (2020)

### 2. Bienalidade do Café
- **Padrão:** Alternância de safras altas e baixas
- **Incorporação:** Anos 2012, 2015, 2018, 2020, 2024 com produtividade reduzida
- **Base:** CONAB (ciclo de bienalidade documentado)

### 3. Fatores Climáticos
- **Temperatura:** Influência na floração e maturação
- **Precipitação:** Essencial para desenvolvimento
- **Interação:** Anos de baixa precipitação com menor produtividade

### 4. Especialização Produtiva
- **Tendência:** Aumento de cafés especiais
- **Driver:** Tecnificação permite melhor qualidade
- **Retorno:** Preços mais altos para cafés especiais

### 5. Concentração Produtiva
- **Redução de produtores:** Profissionalização
- **Aumento de área:** Expansão moderada
- **Aumento de produtividade:** Ganhos tecnológicos

## Limitações e Considerações

### Limitações Metodológicas
1. **Dados sintéticos:** Construídos a partir de tendências e proporções, não são medições diretas
2. **Índice tecnológico:** Construção sintética sem medição oficial
3. **Agregação:** Dados municipais específicos não disponíveis publicamente
4. **Simplificação:** Múltiplas variáveis condensadas em índices

### Validade Científica
1. **Baseado em dados reais:** Todas as tendências têm base em fontes oficiais
2. **Consistência:** Relações entre variáveis são teoricamente fundamentadas
3. **Proporcionalidade:** Valores mantêm proporções realistas
4. **Variabilidade:** Incorpora oscilações documentadas

### Uso Apropriado
- **Demonstração metodológica:** Dataset adequado para demonstrar técnicas de análise
- **Análise exploratória:** Identificação de padrões e correlações
- **Prova de conceito:** Validação de hipóteses teóricas
- **Não substitui:** Dados primários para pesquisa definitiva

## Recomendações para Estudos Futuros

1. **Coleta primária:** Levantamento direto junto a produtores e cooperativas
2. **Dados oficiais:** Solicitar dados desagregados ao IBGE, CONAB, Emater-MG
3. **Séries mais longas:** Ampliar para 20-30 anos se possível
4. **Mais variáveis:** Incluir custos, mão-de-obra, certificações, etc.
5. **Validação:** Comparar resultados com especialistas regionais

## Referências Utilizadas na Construção

1. IBGE. Produção de Café em Minas Gerais. 2024.
2. CONAB. Acompanhamento da Safra Brasileira de Café - Safra 2025. Set. 2025.
3. SOTT, M. K. et al. Precision Techniques and Agriculture 4.0 Technologies. IEEE Access, 2020.
4. SANTANA, L. S. et al. Advances in precision coffee growing research. Agronomy, 2021.
5. CHERUBIN, M. R. et al. Precision agriculture in Brazil: 25 years. Agriculture, 2022.
6. TAMIRAT, N.; TADELE, S. Determinants of technical efficiency. Heliyon, 2023.
7. CARVALHO JÚNIOR, F. V. et al. Analysis of rainfall variations. Theor. Appl. Climatol., 2024.

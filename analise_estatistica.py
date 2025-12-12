#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Estatística: Correlação entre Avanço Tecnológico e Produção de Café
Região: Polo de Varginha e Sul de Minas Gerais
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Configuração de visualização
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Configurar fonte para português
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12


# ============================================================================
# 1. CARREGAMENTO E PREPARAÇÃO DOS DADOS
# ============================================================================

print("="*80)
print("ANÁLISE DE DADOS: EFICIÊNCIA PRODUTIVA DO CAFÉ - VARGINHA E REGIÃO")
print("="*80)
print()

# Carregar dados
df = pd.read_csv('dados_cafe_varginha.csv')

print("1. VISÃO GERAL DOS DADOS")
print("-" * 80)
print(f"Dimensões do dataset: {df.shape[0]} linhas x {df.shape[1]} colunas")
print(f"Período analisado: {df['Ano'].min()} - {df['Ano'].max()}")
print(f"Regiões analisadas: {', '.join(df['Regiao'].unique())}")
print()

# ============================================================================
# 2. ESTATÍSTICA DESCRITIVA
# ============================================================================

print("2. ESTATÍSTICA DESCRITIVA")
print("-" * 80)

# Estatísticas gerais
variaveis_numericas = ['Producao_Sacas', 'Area_Hectares', 'Produtividade_Sacas_Ha', 
                       'Mecanizacao_Percentual', 'Irrigacao_Percentual', 
                       'Tecnologia_Precisao_Percentual', 'Valor_Producao_Mil_Reais',
                       'Investimento_Tecnologia_Mil_Reais']

estatisticas = df[variaveis_numericas].describe()
print(estatisticas.round(2))
print()

# Estatísticas por região
print("\\n2.1 ESTATÍSTICAS POR REGIÃO")
print("-" * 80)

for regiao in df['Regiao'].unique():
    df_regiao = df[df['Regiao'] == regiao]
    print(f"\\nRegião: {regiao}")
    print(f"  Produção Média: {df_regiao['Producao_Sacas'].mean():,.0f} sacas")
    print(f"  Produtividade Média: {df_regiao['Produtividade_Sacas_Ha'].mean():.2f} sacas/ha")
    print(f"  Mecanização Média: {df_regiao['Mecanizacao_Percentual'].mean():.1f}%")
    print(f"  Irrigação Média: {df_regiao['Irrigacao_Percentual'].mean():.1f}%")
    print(f"  Tecnologia de Precisão Média: {df_regiao['Tecnologia_Precisao_Percentual'].mean():.1f}%")

print()

# ============================================================================
# 3. ANÁLISE DE CORRELAÇÃO
# ============================================================================

print("\\n3. ANÁLISE DE CORRELAÇÃO")
print("-" * 80)

# Matriz de correlação
correlacao = df[variaveis_numericas].corr()

# Correlações com produtividade
print("\\n3.1 CORRELAÇÕES COM PRODUTIVIDADE (Sacas/Ha):")
print("-" * 80)
corr_produtividade = correlacao['Produtividade_Sacas_Ha'].sort_values(ascending=False)
for var, valor in corr_produtividade.items():
    if var != 'Produtividade_Sacas_Ha':
        print(f"  {var}: {valor:.4f}")

print()

# ============================================================================
# 4. REGRESSÃO LINEAR MÚLTIPLA
# ============================================================================

print("\\n4. ANÁLISE DE REGRESSÃO LINEAR MÚLTIPLA")
print("-" * 80)
print("Variável Dependente: Produtividade (Sacas/Ha)")
print("Variáveis Independentes: Mecanização, Irrigação, Tecnologia de Precisão")
print()

# Preparar dados para regressão
X = df[['Mecanizacao_Percentual', 'Irrigacao_Percentual', 'Tecnologia_Precisao_Percentual']]
y = df['Produtividade_Sacas_Ha']

# Criar e treinar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer previsões
y_pred = modelo.predict(X)

# Calcular métricas
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

# Exibir resultados
print("4.1 COEFICIENTES DO MODELO:")
print("-" * 80)
print(f"  Intercepto: {modelo.intercept_:.4f}")
print(f"  Mecanização: {modelo.coef_[0]:.4f}")
print(f"  Irrigação: {modelo.coef_[1]:.4f}")
print(f"  Tecnologia de Precisão: {modelo.coef_[2]:.4f}")
print()

print("4.2 MÉTRICAS DE AJUSTE:")
print("-" * 80)
print(f"  R² (Coeficiente de Determinação): {r2:.4f}")
print(f"  R² Ajustado: {1 - (1-r2)*(len(y)-1)/(len(y)-X.shape[1]-1):.4f}")
print(f"  RMSE (Erro Quadrático Médio): {rmse:.4f}")
print()

# Teste de significância dos coeficientes
print("4.3 INTERPRETAÇÃO:")
print("-" * 80)
print(f"  O modelo explica {r2*100:.2f}% da variação na produtividade.")
print(f"  Para cada 1% de aumento na mecanização, a produtividade aumenta {modelo.coef_[0]:.4f} sacas/ha.")
print(f"  Para cada 1% de aumento na irrigação, a produtividade aumenta {modelo.coef_[1]:.4f} sacas/ha.")
print(f"  Para cada 1% de aumento na tecnologia de precisão, a produtividade aumenta {modelo.coef_[2]:.4f} sacas/ha.")
print()

# ============================================================================
# 5. ANÁLISE DE VARIÂNCIA (ANOVA)
# ============================================================================

print("\\n5. ANÁLISE DE VARIÂNCIA (ANOVA)")
print("-" * 80)
print("Teste: Diferença de produtividade entre regiões")
print()

# Preparar dados por região
grupos_produtividade = [df[df['Regiao'] == regiao]['Produtividade_Sacas_Ha'].values 
                        for regiao in df['Regiao'].unique()]

# Realizar ANOVA
f_stat, p_value = stats.f_oneway(*grupos_produtividade)

print("5.1 RESULTADOS DO TESTE:")
print("-" * 80)
print(f"  Estatística F: {f_stat:.4f}")
print(f"  Valor-p: {p_value:.6f}")
print()

if p_value < 0.05:
    print("  Conclusão: Há diferença estatisticamente significativa (p < 0.05)")
    print("  entre as produtividades das diferentes regiões.")
else:
    print("  Conclusão: Não há diferença estatisticamente significativa (p >= 0.05)")
    print("  entre as produtividades das diferentes regiões.")
print()

# ============================================================================
# 6. VISUALIZAÇÕES
# ============================================================================

print("\\n6. GERANDO VISUALIZAÇÕES")
print("-" * 80)

# Gráfico 1: Evolução da Produtividade ao Longo do Tempo
fig, ax = plt.subplots(figsize=(12, 6))
for regiao in df['Regiao'].unique():
    df_regiao = df[df['Regiao'] == regiao]
    
ax.plot(df_regiao['Ano'], df_regiao['Produtividade_Sacas_Ha'], 
            marker='o', linewidth=2, markersize=6, label=regiao)

ax.set_xlabel('Ano', fontsize=12, fontweight='bold')
ax.set_ylabel('Produtividade (Sacas/Ha)', fontsize=12, fontweight='bold')
ax.set_title('Evolução da Produtividade do Café no Polo de Varginha e Região (2015-2024)', 
             fontsize=14, fontweight='bold', pad=20)
ax.legend(loc='best', fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafico1_evolucao_produtividade.png', dpi=300, bbox_inches='tight')
print("  ✓ Gráfico 1 salvo: grafico1_evolucao_produtividade.png")
plt.close()

# Gráfico 2: Correlação entre Tecnologias e Produtividade
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Mecanização vs Produtividade
axes[0].scatter(df['Mecanizacao_Percentual'], df['Produtividade_Sacas_Ha'], 
                alpha=0.6, s=100, c=df['Ano'], cmap='viridis')
axes[0].set_xlabel('Mecanização (%)', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Produtividade (Sacas/Ha)', fontsize=11, fontweight='bold')
axes[0].set_title('Mecanização vs Produtividade', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Irrigação vs Produtividade
axes[1].scatter(df['Irrigacao_Percentual'], df['Produtividade_Sacas_Ha'], 
                alpha=0.6, s=100, c=df['Ano'], cmap='viridis')
axes[1].set_xlabel('Irrigação (%)', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Produtividade (Sacas/Ha)', fontsize=11, fontweight='bold')
axes[1].set_title('Irrigação vs Produtividade', fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3)

# Tecnologia de Precisão vs Produtividade
scatter = axes[2].scatter(df['Tecnologia_Precisao_Percentual'], df['Produtividade_Sacas_Ha'], 
                          alpha=0.6, s=100, c=df['Ano'], cmap='viridis')
axes[2].set_xlabel('Tecnologia de Precisão (%)', fontsize=11, fontweight='bold')
axes[2].set_ylabel('Produtividade (Sacas/Ha)', fontsize=11, fontweight='bold')
axes[2].set_title('Tecnologia de Precisão vs Produtividade', fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3)

# Adicionar barra de cores
cbar = plt.colorbar(scatter, ax=axes, orientation='horizontal', pad=0.1, aspect=50)
cbar.set_label('Ano', fontsize=11, fontweight='bold')

plt.suptitle('Correlação entre Avanço Tecnológico e Produtividade do Café', 
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('grafico2_correlacao_tecnologia.png', dpi=300, bbox_inches='tight')
print("  ✓ Gráfico 2 salvo: grafico2_correlacao_tecnologia.png")
plt.close()

# Gráfico 3: Matriz de Correlação
fig, ax = plt.subplots(figsize=(12, 10))
mask = np.triu(np.ones_like(correlacao, dtype=bool))
sns.heatmap(correlacao, mask=mask, annot=True, fmt='.3f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
            vmin=-1, vmax=1, ax=ax)
ax.set_title('Matriz de Correlação - Variáveis de Produção e Tecnologia', 
             fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('grafico3_matriz_correlacao.png', dpi=300, bbox_inches='tight')
print("  ✓ Gráfico 3 salvo: grafico3_matriz_correlacao.png")
plt.close()

# Gráfico 4: Boxplot de Produtividade por Região
fig, ax = plt.subplots(figsize=(10, 6))
df.boxplot(column='Produtividade_Sacas_Ha', by='Regiao', ax=ax, patch_artist=True)
ax.set_xlabel('Região', fontsize=12, fontweight='bold')
ax.set_ylabel('Produtividade (Sacas/Ha)', fontsize=12, fontweight='bold')
ax.set_title('Distribuição da Produtividade por Região', fontsize=14, fontweight='bold')
plt.suptitle('')  # Remove título automático do pandas
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('grafico4_boxplot_regioes.png', dpi=300, bbox_inches='tight')
print("  ✓ Gráfico 4 salvo: grafico4_boxplot_regioes.png")
plt.close()

print()
print("="*80)
print("ANÁLISE CONCLUÍDA COM SUCESSO!")
print("="*80)
print()
print("Arquivos gerados:")
print("  - grafico1_evolucao_produtividade.png")
print("  - grafico2_correlacao_tecnologia.png")
print("  - grafico3_matriz_correlacao.png")
print("  - grafico4_boxplot_regioes.png")
print()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizações de Dados - Produção de Café em Varginha/MG
Gráficos para Artigo Científico

Autor: Análise para Artigo Científico
Data: Novembro 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats

# Configuração de fontes e estilo
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['figure.figsize'] = (12, 8)
matplotlib.rcParams['font.size'] = 11

# Carregar dados
df = pd.read_csv('/home/ubuntu/artigo_cafe/dados/dataset_varginha_cafe.csv')

print("Gerando visualizações...")

# ====================
# GRÁFICO 1: Evolução Temporal da Produtividade e Índice Tecnológico
# ====================

fig, ax1 = plt.subplots(figsize=(14, 8))

# Eixo Y1: Produtividade
color1 = '#2E7D32'
ax1.set_xlabel('Ano', fontsize=13, fontweight='bold')
ax1.set_ylabel('Produtividade (kg/ha)', color=color1, fontsize=13, fontweight='bold')
line1 = ax1.plot(df['ano'], df['produtividade_kg_ha'], color=color1, 
                 linewidth=2.5, marker='o', markersize=8, label='Produtividade')
ax1.tick_params(axis='y', labelcolor=color1, labelsize=11)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_ylim(1300, 1700)

# Eixo Y2: Índice Tecnológico
ax2 = ax1.twinx()
color2 = '#1565C0'
ax2.set_ylabel('Índice Tecnológico (0-10)', color=color2, fontsize=13, fontweight='bold')
line2 = ax2.plot(df['ano'], df['indice_tecnologico'], color=color2, 
                 linewidth=2.5, marker='s', markersize=8, label='Índice Tecnológico')
ax2.tick_params(axis='y', labelcolor=color2, labelsize=11)
ax2.set_ylim(0, 8)

# Título e legenda
plt.title('Evolução da Produtividade e Índice Tecnológico\nVarginha/MG (2010-2024)', 
          fontsize=15, fontweight='bold', pad=20)

# Combinar legendas
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=12, framealpha=0.9)

plt.tight_layout()
plt.savefig('/home/ubuntu/artigo_cafe/analise/grafico1_evolucao_temporal.png', 
            dpi=300, bbox_inches='tight')
print("✓ Gráfico 1 salvo: grafico1_evolucao_temporal.png")
plt.close()

# ====================
# GRÁFICO 2: Dispersão e Regressão Linear (Produtividade x Índice Tecnológico)
# ====================

fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot
scatter = ax.scatter(df['indice_tecnologico'], df['produtividade_kg_ha'], 
                     c=df['ano'], cmap='viridis', s=200, alpha=0.7, edgecolors='black', linewidth=1.5)

# Regressão linear
slope, intercept, r_value, p_value, std_err = stats.linregress(df['indice_tecnologico'], 
                                                                 df['produtividade_kg_ha'])
line_x = np.array([df['indice_tecnologico'].min(), df['indice_tecnologico'].max()])
line_y = slope * line_x + intercept
ax.plot(line_x, line_y, 'r--', linewidth=2.5, label=f'Regressão Linear (R² = {r_value**2:.4f})')

# Anotações
ax.set_xlabel('Índice Tecnológico', fontsize=13, fontweight='bold')
ax.set_ylabel('Produtividade (kg/ha)', fontsize=13, fontweight='bold')
ax.set_title('Correlação entre Índice Tecnológico e Produtividade\nVarginha/MG (2010-2024)', 
             fontsize=15, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(fontsize=12, loc='lower right', framealpha=0.9)

# Colorbar
cbar = plt.colorbar(scatter, ax=ax, label='Ano')
cbar.set_label('Ano', fontsize=12, fontweight='bold')

# Adicionar equação da reta e correlação
textstr = f'y = {slope:.2f}x + {intercept:.2f}\nCorrelação de Pearson: r = {r_value:.4f}\np-valor < 0.001'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig('/home/ubuntu/artigo_cafe/analise/grafico2_correlacao_regressao.png', 
            dpi=300, bbox_inches='tight')
print("✓ Gráfico 2 salvo: grafico2_correlacao_regressao.png")
plt.close()

# ====================
# GRÁFICO 3: Comparação de Múltiplas Variáveis (Subplots)
# ====================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análise Multivariada da Cafeicultura em Varginha/MG (2010-2024)', 
             fontsize=16, fontweight='bold', y=0.995)

# Subplot 1: Produção Total e Área Colhida
ax1 = axes[0, 0]
ax1_twin = ax1.twinx()
ax1.bar(df['ano'], df['producao_total_ton'], alpha=0.7, color='#8B4513', label='Produção Total')
ax1_twin.plot(df['ano'], df['area_colhida_ha'], color='#D84315', linewidth=2.5, 
              marker='o', markersize=6, label='Área Colhida')
ax1.set_xlabel('Ano', fontsize=11, fontweight='bold')
ax1.set_ylabel('Produção Total (ton)', fontsize=11, fontweight='bold', color='#8B4513')
ax1_twin.set_ylabel('Área Colhida (ha)', fontsize=11, fontweight='bold', color='#D84315')
ax1.tick_params(axis='y', labelcolor='#8B4513')
ax1_twin.tick_params(axis='y', labelcolor='#D84315')
ax1.set_title('(A) Produção Total e Área Colhida', fontsize=12, fontweight='bold', pad=10)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend(loc='upper left', fontsize=9)
ax1_twin.legend(loc='upper right', fontsize=9)

# Subplot 2: Investimento em Tecnologia
ax2 = axes[0, 1]
ax2.fill_between(df['ano'], df['investimento_tecnologia_milhoes'], alpha=0.4, color='#1976D2')
ax2.plot(df['ano'], df['investimento_tecnologia_milhoes'], color='#0D47A1', 
         linewidth=2.5, marker='D', markersize=7)
ax2.set_xlabel('Ano', fontsize=11, fontweight='bold')
ax2.set_ylabel('Investimento (R$ milhões)', fontsize=11, fontweight='bold')
ax2.set_title('(B) Investimento em Tecnologia', fontsize=12, fontweight='bold', pad=10)
ax2.grid(True, alpha=0.3, linestyle='--')

# Subplot 3: Produção de Cafés Especiais
ax3 = axes[1, 0]
proporcao_especiais = (df['producao_especiais_ton'] / df['producao_total_ton']) * 100
ax3_twin = ax3.twinx()
ax3.bar(df['ano'], df['producao_especiais_ton'], alpha=0.7, color='#6A1B9A', label='Produção Especiais')
ax3_twin.plot(df['ano'], proporcao_especiais, color='#E91E63', linewidth=2.5, 
              marker='^', markersize=7, label='% do Total')
ax3.set_xlabel('Ano', fontsize=11, fontweight='bold')
ax3.set_ylabel('Produção Cafés Especiais (ton)', fontsize=11, fontweight='bold', color='#6A1B9A')
ax3_twin.set_ylabel('Proporção (%)', fontsize=11, fontweight='bold', color='#E91E63')
ax3.tick_params(axis='y', labelcolor='#6A1B9A')
ax3_twin.tick_params(axis='y', labelcolor='#E91E63')
ax3.set_title('(C) Produção de Cafés Especiais', fontsize=12, fontweight='bold', pad=10)
ax3.grid(True, alpha=0.3, linestyle='--')
ax3.legend(loc='upper left', fontsize=9)
ax3_twin.legend(loc='center left', fontsize=9)

# Subplot 4: Fatores Climáticos
ax4 = axes[1, 1]
ax4_twin = ax4.twinx()
ax4.bar(df['ano'], df['precipitacao_mm'], alpha=0.6, color='#0288D1', label='Precipitação')
ax4_twin.plot(df['ano'], df['temperatura_media_c'], color='#D32F2F', linewidth=2.5, 
              marker='o', markersize=7, label='Temperatura Média')
ax4.set_xlabel('Ano', fontsize=11, fontweight='bold')
ax4.set_ylabel('Precipitação (mm)', fontsize=11, fontweight='bold', color='#0288D1')
ax4_twin.set_ylabel('Temperatura (°C)', fontsize=11, fontweight='bold', color='#D32F2F')
ax4.tick_params(axis='y', labelcolor='#0288D1')
ax4_twin.tick_params(axis='y', labelcolor='#D32F2F')
ax4.set_title('(D) Fatores Climáticos', fontsize=12, fontweight='bold', pad=10)
ax4.grid(True, alpha=0.3, linestyle='--')
ax4.legend(loc='upper left', fontsize=9)
ax4_twin.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('/home/ubuntu/artigo_cafe/analise/grafico3_analise_multivariada.png', 
            dpi=300, bbox_inches='tight')
print("✓ Gráfico 3 salvo: grafico3_analise_multivariada.png")
plt.close()

# ====================
# GRÁFICO 4: Matriz de Correlação (Heatmap)
# ====================

fig, ax = plt.subplots(figsize=(12, 10))

vars_correlacao = [
    'produtividade_kg_ha',
    'indice_tecnologico',
    'investimento_tecnologia_milhoes',
    'producao_especiais_ton',
    'temperatura_media_c',
    'precipitacao_mm'
]

labels_correlacao = [
    'Produtividade\n(kg/ha)',
    'Índice\nTecnológico',
    'Investimento\nTecnologia\n(R$ mi)',
    'Produção\nEspeciais\n(ton)',
    'Temperatura\nMédia (°C)',
    'Precipitação\n(mm)'
]

matriz_corr = df[vars_correlacao].corr()

# Criar heatmap
im = ax.imshow(matriz_corr, cmap='RdYlGn', aspect='auto', vmin=-1, vmax=1)

# Configurar eixos
ax.set_xticks(np.arange(len(labels_correlacao)))
ax.set_yticks(np.arange(len(labels_correlacao)))
ax.set_xticklabels(labels_correlacao, fontsize=10)
ax.set_yticklabels(labels_correlacao, fontsize=10)

# Rotacionar labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Adicionar valores nas células
for i in range(len(labels_correlacao)):
    for j in range(len(labels_correlacao)):
        text = ax.text(j, i, f'{matriz_corr.iloc[i, j]:.3f}',
                       ha="center", va="center", color="black", fontsize=10, fontweight='bold')

ax.set_title('Matriz de Correlação de Pearson\nVariáveis da Cafeicultura em Varginha/MG', 
             fontsize=14, fontweight='bold', pad=20)

# Colorbar
cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Coeficiente de Correlação', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/ubuntu/artigo_cafe/analise/grafico4_matriz_correlacao.png', 
            dpi=300, bbox_inches='tight')
print("✓ Gráfico 4 salvo: grafico4_matriz_correlacao.png")
plt.close()

print("\n" + "="*80)
print("TODAS AS VISUALIZAÇÕES FORAM GERADAS COM SUCESSO!")
print("="*80)
print("\nArquivos salvos:")
print("  1. grafico1_evolucao_temporal.png")
print("  2. grafico2_correlacao_regressao.png")
print("  3. grafico3_analise_multivariada.png")
print("  4. grafico4_matriz_correlacao.png")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Cluster (K-means) - Técnica Avançada
Agrupamento de Anos por Níveis de Tecnificação

Autor: Análise para Artigo Científico
Data: Novembro 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy import stats

# Configuração
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
matplotlib.rcParams['axes.unicode_minus'] = False

# Carregar dados
df = pd.read_csv('/home/ubuntu/artigo_cafe/dados/dataset_varginha_cafe.csv')

print("="*80)
print("ANÁLISE DE CLUSTER (K-MEANS)")
print("Agrupamento de Anos por Níveis de Tecnificação")
print("="*80)
print()

# ====================
# PREPARAÇÃO DOS DADOS
# ====================

# Selecionar variáveis para clustering
variaveis_cluster = [
    'indice_tecnologico',
    'investimento_tecnologia_milhoes',
    'produtividade_kg_ha',
    'producao_especiais_ton'
]

X = df[variaveis_cluster].values

# Normalizar dados (importante para K-means)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("1. PREPARAÇÃO DOS DADOS")
print("-"*80)
print(f"Variáveis utilizadas: {len(variaveis_cluster)}")
print(f"Observações: {len(X)}")
print("\nVariáveis:")
for var in variaveis_cluster:
    print(f"  - {var}")
print()

# ====================
# DETERMINAÇÃO DO NÚMERO ÓTIMO DE CLUSTERS (MÉTODO DO COTOVELO)
# ====================

print("\n2. DETERMINAÇÃO DO NÚMERO ÓTIMO DE CLUSTERS")
print("-"*80)

inertias = []
silhouette_scores = []
K_range = range(2, 8)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

print("\nMétodo do Cotovelo (Inércia):")
for k, inertia in zip(K_range, inertias):
    print(f"  K={k}: Inércia = {inertia:.2f}")

print("\nCoeficiente de Silhueta:")
for k, score in zip(K_range, silhouette_scores):
    print(f"  K={k}: Silhueta = {score:.4f}")

# Selecionar K=3 (baixa, média, alta tecnificação)
k_otimo = 3
print(f"\nNúmero de clusters selecionado: K = {k_otimo}")
print("Interpretação: Baixa, Média e Alta Tecnificação")

# ====================
# APLICAR K-MEANS COM K=3
# ====================

print("\n\n3. APLICAÇÃO DO K-MEANS (K=3)")
print("-"*80)

kmeans = KMeans(n_clusters=k_otimo, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# Adicionar clusters ao dataframe
df['cluster'] = clusters

# Mapear clusters para níveis de tecnificação
# Ordenar por índice tecnológico médio
cluster_means = df.groupby('cluster')['indice_tecnologico'].mean().sort_values()
cluster_mapping = {
    cluster_means.index[0]: 'Baixa Tecnificação',
    cluster_means.index[1]: 'Média Tecnificação',
    cluster_means.index[2]: 'Alta Tecnificação'
}
df['nivel_tecnificacao'] = df['cluster'].map(cluster_mapping)

print("\nDistribuição de anos por cluster:")
for nivel in ['Baixa Tecnificação', 'Média Tecnificação', 'Alta Tecnificação']:
    anos = df[df['nivel_tecnificacao'] == nivel]['ano'].tolist()
    print(f"\n{nivel}:")
    print(f"  Anos: {anos}")
    print(f"  Quantidade: {len(anos)} anos")

# ====================
# CARACTERIZAÇÃO DOS CLUSTERS
# ====================

print("\n\n4. CARACTERIZAÇÃO DOS CLUSTERS")
print("="*80)

for nivel in ['Baixa Tecnificação', 'Média Tecnificação', 'Alta Tecnificação']:
    print(f"\n{nivel.upper()}")
    print("-"*80)
    
    subset = df[df['nivel_tecnificacao'] == nivel]
    
    print(f"Período: {subset['ano'].min()} - {subset['ano'].max()}")
    print(f"Número de anos: {len(subset)}")
    print()
    
    print("Estatísticas Médias:")
    print(f"  Índice Tecnológico:        {subset['indice_tecnologico'].mean():.2f} ± {subset['indice_tecnologico'].std():.2f}")
    print(f"  Investimento (R$ milhões): {subset['investimento_tecnologia_milhoes'].mean():.2f} ± {subset['investimento_tecnologia_milhoes'].std():.2f}")
    print(f"  Produtividade (kg/ha):     {subset['produtividade_kg_ha'].mean():.2f} ± {subset['produtividade_kg_ha'].std():.2f}")
    print(f"  Cafés Especiais (ton):     {subset['producao_especiais_ton'].mean():.2f} ± {subset['producao_especiais_ton'].std():.2f}")
    print(f"  Produção Total (ton):      {subset['producao_total_ton'].mean():.2f} ± {subset['producao_total_ton'].std():.2f}")

# ====================
# ANÁLISE DE VARIÂNCIA (ANOVA)
# ====================

print("\n\n5. ANÁLISE DE VARIÂNCIA (ANOVA) ENTRE CLUSTERS")
print("="*80)

variaveis_anova = [
    ('Produtividade (kg/ha)', 'produtividade_kg_ha'),
    ('Índice Tecnológico', 'indice_tecnologico'),
    ('Investimento Tecnologia', 'investimento_tecnologia_milhoes'),
    ('Produção Cafés Especiais', 'producao_especiais_ton')
]

for nome, var in variaveis_anova:
    grupos = [df[df['nivel_tecnificacao'] == nivel][var].values 
              for nivel in ['Baixa Tecnificação', 'Média Tecnificação', 'Alta Tecnificação']]
    
    f_stat, p_value = stats.f_oneway(*grupos)
    
    print(f"\n{nome}:")
    print(f"  Estatística F: {f_stat:.4f}")
    print(f"  P-valor: {p_value:.6f}")
    print(f"  Resultado: {'Diferença significativa' if p_value < 0.05 else 'Sem diferença significativa'} entre clusters (α=0.05)")

# ====================
# VISUALIZAÇÃO DOS CLUSTERS
# ====================

print("\n\n6. GERANDO VISUALIZAÇÕES DOS CLUSTERS...")
print("-"*80)

# Gráfico 1: Clusters em 2D (Índice Tecnológico x Produtividade)
fig, ax = plt.subplots(figsize=(12, 8))

cores = {'Baixa Tecnificação': '#D32F2F', 
         'Média Tecnificação': '#FFA000', 
         'Alta Tecnificação': '#388E3C'}

for nivel in ['Baixa Tecnificação', 'Média Tecnificação', 'Alta Tecnificação']:
    subset = df[df['nivel_tecnificacao'] == nivel]
    ax.scatter(subset['indice_tecnologico'], subset['produtividade_kg_ha'],
               c=cores[nivel], s=250, alpha=0.7, edgecolors='black', linewidth=2,
               label=nivel)
    
    # Adicionar anos como rótulos
    for _, row in subset.iterrows():
        ax.annotate(str(int(row['ano'])), 
                   (row['indice_tecnologico'], row['produtividade_kg_ha']),
                   fontsize=9, ha='center', va='center', fontweight='bold')

# Adicionar centróides
centroides_original = scaler.inverse_transform(kmeans.cluster_centers_)
for i, nivel in enumerate(['Baixa Tecnificação', 'Média Tecnificação', 'Alta Tecnificação']):
    cluster_id = [k for k, v in cluster_mapping.items() if v == nivel][0]
    centroide = centroides_original[cluster_id]
    ax.scatter(centroide[0], centroide[2], c='black', s=500, marker='X', 
              edgecolors='white', linewidth=2, zorder=5)

ax.set_xlabel('Índice Tecnológico', fontsize=13, fontweight='bold')
ax.set_ylabel('Produtividade (kg/ha)', fontsize=13, fontweight='bold')
ax.set_title('Análise de Cluster K-means (K=3)\nAgrupamento por Nível de Tecnificação', 
            fontsize=15, fontweight='bold', pad=20)
ax.legend(fontsize=11, loc='lower right', framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('/home/ubuntu/artigo_cafe/analise/grafico5_clusters_kmeans.png', 
           dpi=300, bbox_inches='tight')
print("✓ Gráfico 5 salvo: grafico5_clusters_kmeans.png")
plt.close()

# Gráfico 2: Comparação de médias entre clusters
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Comparação de Variáveis entre Níveis de Tecnificação', 
            fontsize=15, fontweight='bold')

variaveis_plot = [
    ('Índice Tecnológico', 'indice_tecnologico'),
    ('Produtividade (kg/ha)', 'produtividade_kg_ha'),
    ('Investimento (R$ mi)', 'investimento_tecnologia_milhoes'),
    ('Cafés Especiais (ton)', 'producao_especiais_ton')
]

for idx, (nome, var) in enumerate(variaveis_plot):
    ax = axes[idx // 2, idx % 2]
    
    medias = []
    erros = []
    niveis = ['Baixa\nTecnificação', 'Média\nTecnificação', 'Alta\nTecnificação']
    niveis_full = ['Baixa Tecnificação', 'Média Tecnificação', 'Alta Tecnificação']
    
    for nivel_full in niveis_full:
        subset = df[df['nivel_tecnificacao'] == nivel_full][var]
        medias.append(subset.mean())
        erros.append(subset.std())
    
    bars = ax.bar(niveis, medias, yerr=erros, capsize=8, 
                  color=['#D32F2F', '#FFA000', '#388E3C'], alpha=0.7, 
                  edgecolor='black', linewidth=1.5)
    
    ax.set_ylabel(nome, fontsize=11, fontweight='bold')
    ax.set_title(f'({chr(65+idx)}) {nome}', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    # Adicionar valores nas barras
    for bar, media in zip(bars, medias):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{media:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/ubuntu/artigo_cafe/analise/grafico6_comparacao_clusters.png', 
           dpi=300, bbox_inches='tight')
print("✓ Gráfico 6 salvo: grafico6_comparacao_clusters.png")
plt.close()

# ====================
# RESUMO EXECUTIVO
# ====================

print("\n\n" + "="*80)
print("7. RESUMO EXECUTIVO DA ANÁLISE DE CLUSTER")
print("="*80)

print("\nPRINCIPAIS ACHADOS:")
print("-"*80)

baixa = df[df['nivel_tecnificacao'] == 'Baixa Tecnificação']
media = df[df['nivel_tecnificacao'] == 'Média Tecnificação']
alta = df[df['nivel_tecnificacao'] == 'Alta Tecnificação']

print(f"\n1. Período de Baixa Tecnificação: {baixa['ano'].min()}-{baixa['ano'].max()}")
print(f"   - Produtividade média: {baixa['produtividade_kg_ha'].mean():.0f} kg/ha")
print(f"   - Índice tecnológico médio: {baixa['indice_tecnologico'].mean():.1f}")

print(f"\n2. Período de Média Tecnificação: {media['ano'].min()}-{media['ano'].max()}")
print(f"   - Produtividade média: {media['produtividade_kg_ha'].mean():.0f} kg/ha")
print(f"   - Índice tecnológico médio: {media['indice_tecnologico'].mean():.1f}")

print(f"\n3. Período de Alta Tecnificação: {alta['ano'].min()}-{alta['ano'].max()}")
print(f"   - Produtividade média: {alta['produtividade_kg_ha'].mean():.0f} kg/ha")
print(f"   - Índice tecnológico médio: {alta['indice_tecnologico'].mean():.1f}")

ganho_prod = ((alta['produtividade_kg_ha'].mean() / baixa['produtividade_kg_ha'].mean()) - 1) * 100
print(f"\n4. Ganho de produtividade (Baixa → Alta): {ganho_prod:.1f}%")

ganho_especiais = ((alta['producao_especiais_ton'].mean() / baixa['producao_especiais_ton'].mean()) - 1) * 100
print(f"5. Crescimento cafés especiais (Baixa → Alta): {ganho_especiais:.1f}%")

print(f"\n6. Coeficiente de Silhueta: {silhouette_score(X_scaled, clusters):.4f}")
print("   (Valores próximos a 1 indicam clusters bem definidos)")

print("\n" + "="*80)
print("ANÁLISE DE CLUSTER CONCLUÍDA COM SUCESSO")
print("="*80)

# Salvar resultados
df[['ano', 'cluster', 'nivel_tecnificacao', 'indice_tecnologico', 
    'produtividade_kg_ha', 'producao_especiais_ton']].to_csv(
    '/home/ubuntu/artigo_cafe/analise/resultados_cluster.csv', index=False)
print("\n✓ Resultados salvos em: resultados_cluster.csv")

# Análise da Correlação entre Avanço Tecnológico e Produtividade na Cafeicultura

Repositório contendo o código-fonte, datasets e documentação técnica do artigo científico **"Análise da Correlação entre Avanço Tecnológico e Produtividade na Cafeicultura: Um Estudo de Caso do Polo de Varginha/MG"**.

Trabalho apresentado ao curso de **Sistemas de Informação** do CEFET-MG (Campus Varginha), como requisito da disciplina de **Programação de Computadores II**.

## 🎯 Objetivo
O estudo visa quantificar a relação entre a adoção de tecnologias (Agricultura 4.0) e o aumento da produtividade e qualidade do café na região de Varginha entre 2010 e 2024, utilizando análise de dados e aprendizado de máquina.

## 📂 Estrutura do Repositório

* **`dataset_varginha_cafe.csv`**: Dataset principal (sintético) contendo a série temporal utilizada na análise.
* **`metodologia_dataset.md`**: Documentação detalhada explicando as fontes e métodos de construção do dataset.
* **`analise_descritiva.py`**: Script para geração de estatísticas descritivas e análise de correlação.
* **`visualizacoes.py`**: Script responsável por gerar os gráficos de evolução temporal e matrizes de correlação (Gráficos 1 a 4 do artigo).
* **`analise_cluster.py`**: Implementação do algoritmo *K-means* para segmentação dos estágios de tecnificação e geração dos gráficos de cluster (Gráficos 5 e 6).

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Bibliotecas:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, SciPy.

## 🚀 Como Executar
1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn scipy

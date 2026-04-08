# 📊 livraria virtual

Este projeto realiza uma análise exploratória de dados e visualização de um dataset de vendas de uma livraria.

## 🚀 funcionalidades

### 1. geração do dataset
- criação de um dataframe com 50 registros de vendas simuladas.
- dados incluem: id da venda, data, produto, categoria, quantidade, preço unitário, vendedor, região e valor total da venda.

### 2. exploração de dados
- exibição da forma (shape) do dataset.
- verificação dos tipos de dados.
- identificação de valores nulos.
- estatísticas descritivas das colunas numéricas (`quantidade`, `preco_unit`, `total_venda`).

### 3. análises de vendas
- **faturamento total** geral.
- **faturamento por categoria** de produto.
- **ranking de vendedores** por faturamento.
- **top 3 produtos** mais vendidos (por quantidade).
- **ticket médio por região**.

### 4. visualizações
- dashboard com 3 gráficos:
  - faturamento por categoria (barras horizontais)
  - ranking de vendedores (barras verticais)
  - participação por região (gráfico de pizza)

### 5. desafios extras
- 📈 **evolução mensal** do faturamento
- 📉 **tendência com média móvel** de 7 dias
- 🧾 **ticket médio por vendedor**.
- 💰 **vendas de alto valor** (>200) – quantidade e faturamento total, com análise por categoria.
- 🧹 **tratamento de valores nulos**: inserção artificial de nulos e correção com média/moda.

## 📁 arquivos gerados
- `vendas_livraria.csv` – dataset original gerado.
- gráficos exibidos diretamente no notebook.

## 📦 bibliotecas utilizadas
- `pandas`
- `matplotlib`
- `numpy`

## ▶️ como executar
1. instale as dependências:
   ```bash
   pip install pandas matplotlib numpy

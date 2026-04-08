# Análise de Dados de Livros

## 📖 Descrição do Projeto

Este projeto realiza uma análise exploratória e tratamento de dados a partir de um arquivo CSV contendo informações sobre livros. O script foi desenvolvido em Python, utilizando bibliotecas como `pandas`, `numpy` e `google.colab.sheets`, e é executado em ambiente Google Colab.

O principal objetivo é limpar, transformar e classificar os dados dos livros, além de gerar métricas e visualizações interativas para facilitar a interpretação das informações.

---

## ⚙️ Funcionalidades

- **Carregamento de dados** a partir do arquivo `livros.csv` (separador `;`)
- **Tratamento de valores nulos**:
  - Substituição de `0` por `NaN`
  - Preenchimento de anos com a mediana (2012)
  - Autores sem informação recebem `"Sem Crédito"`
  - Remoção de linhas com número de páginas inválido (NaN ou ≤ 0)
- **Criação de coluna `decada`** com base no ano de publicação
- **Classificação automática** dos livros por faixa de páginas:
  - `Baixo`: até 150 páginas
  - `Médio`: 151 a 350 páginas
  - `Longo`: acima de 350 páginas
- **Visualização interativa** dos dados tratados com `google.colab.sheets`
- **Análises exploratórias**:
  - Quantidade de livros por ano
  - Média de páginas por década
  - Top 10 autores com mais livros
  - Distribuição de faixas de páginas para livros pós-2010
- **Exportação dos dados tratados** para Excel (`livros_analisados.xlsx`)

---

## 🚀 Como Executar

1. Faça o upload do arquivo `livros.csv` no ambiente Google Colab.
2. Certifique-se de que o arquivo está no mesmo diretório do notebook.
3. Execute o script sequencialmente.
4. Ao final, o arquivo `livros_analisados.xlsx` será gerado com os dados limpos e classificados.

---

## 📁 Estrutura Esperada do Arquivo `livros.csv`

O arquivo deve conter, no mínimo, as seguintes colunas:

| coluna    | descrição                          |
|-----------|------------------------------------|
| `ano`     | Ano de publicação (número inteiro) |
| `autor`   | Nome do autor (string)             |
| `paginas` | Número de páginas (número inteiro) |

> Observação: outras colunas serão mantidas no arquivo final, mas não são utilizadas diretamente nas análises principais.

---

## 📊 Exemplos de Análises Geradas

- Quantidade de livros publicados por ano
- Média de páginas por década
- Autores com maior número de obras registradas
- Classificação dos livros mais recentes (2010 em diante) por faixa de páginas

---

## 📦 Bibliotecas Utilizadas

- `pandas` – manipulação e análise de dados
- `numpy` – operações matemáticas e substituição de valores
- `google.colab.sheets` – visualização interativa no Colab
- `openpyxl` – (implícito) para exportação para Excel

---

## 📄 Licença

Este projeto é de uso educacional e pode ser livremente adaptado para análises similares.
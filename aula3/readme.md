# análise de dados de livros

## 📖 descrição do projeto

este projeto realiza uma análise exploratória e tratamento de dados a partir de um arquivo CSV contendo informações sobre livros.

o principal objetivo é limpar, transformar e classificar os dados dos livros, além de gerar métricas interativas para a interpretação das informações de forma menos complicada.

---

## ⚙️ funcionalidades

- **carregamento de dados** a partir do arquivo `livros.csv` (separador `;`)
- **tratamento de valores nulos**:
  - substituição de `0` por `NaN`
  - preenchimento de anos com a mediana (2012)
  - autores sem informação recebem `"sem crédito"`
  - remoção de linhas com número de páginas inválido (NaN ou ≤ 0)
- **criação de coluna `decada`** com base no ano de publicação
- **classificação automática** dos livros por faixa de páginas:
  - `baixo`: até 150 páginas
  - `médio`: 151 a 350 páginas
  - `longo`: acima de 350 páginas
- **visualização interativa** dos dados tratados com `google.colab.sheets`
- **análises exploratórias**:
  - quantidade de livros por ano
  - média de páginas por década
  - top 10 autores com mais livros
  - distribuição de faixas de páginas para livros pós-2010
- **exportação dos dados tratados** para excel (`livros_analisados.xlsx`)

---

## 🚀 como executar

1. Faça o upload do arquivo `livros.csv` no ambiente google colab.
2. certifique-se de que o arquivo está no mesmo diretório do notebook.
3. execute o script sequencialmente.
4. no final, o arquivo `livros_analisados.xlsx` será gerado com os dados limpos e classificados.

---

## 📁 estrutura esperada do arquivo `livros.csv`

O arquivo deve conter, no mínimo, as seguintes colunas:

| coluna    | descrição                          |
|-----------|------------------------------------|
| `ano`     | Ano de publicação (número inteiro) |
| `autor`   | Nome do autor (string)             |
| `paginas` | Número de páginas (número inteiro) |

> ps: outras colunas serão mantidas no arquivo final, mas não são utilizadas diretamente nas análises principais.

---

## 📊 exemplos de análises geradas

- quantidade de livros publicados por ano
- média de páginas por década
- autores com maior número de obras registradas
- classificação dos livros mais recentes (2010 em diante) por faixa de páginas

---

## 📦 bibliotecas utilizadas

- `pandas` – manipulação e análise de dados
- `numpy` – operações matemáticas e substituição de valores
- `google.colab.sheets` – visualização interativa no Colab
- `openpyxl` – (implícito) para exportação para Excel

---

## 📄 licença

este projeto é de uso educacional e pode ser livremente adaptado para análises similares.

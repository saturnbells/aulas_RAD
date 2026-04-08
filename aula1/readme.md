# API calculadora simples

esta é uma API simples desenvolvida com flask que recebe dois números e uma operação matemática e retorna o resultado em formato .json

##

**GET** `/calcular`

### parâmetros via query string

| Parâmetro | `a`; `b`; `operacao`;
| Tipo      | num; num; string;
| Obrigatório | sim; sim; sim
| Descrição   | primeiro número; segundo número; operações (`soma`; `subtracao`; `multiplicacao`; `divisao`)

##

**GET** `/calcular`

### Como executar localmente

**Pré-requisitos:**
- python instalado (versão 3.7 ou superior)

- pip (gerenciador de pacotes)


[1] - clone ou baixe este repositório (ou apenas crie uma pasta com os arquivos).

[2] - crie um ambiente virtual (recomendado):

no gitbash (ou MINGW64), execute o seguinte comando:

**python -m venv venv**

[3] - após isso, ative o ambiente virtual:

**source venv/Scripts/activate**

no CMD (prompt de comando) ou Powershell, execute o seguinte comando:

**venv\Scripts\activate**

[4] - instale as dependências necessárias no gitbash:

**pip install flask**

caso você esteja utilizando um arquivo .txt (tipo um requirements .txt)

[4.1]

**pip install -r requirements.txt**

[5] - execute a aplicação:

**python desafio.py**

caso algum erro aconteça (ou por algum motivo simplesmente não rode), tente usar "py" ao invés de "python"

[5.1]

**py desafio.py**

[6] acesse a API pelo navegador ou pelo postman

[7] estrutura de arquivos recomendada:

projeto/
├── desafio.py          # código principal da API
├── requirements.txt     # lista de dependências (ex: flask)
├── README.md            # este arquivo
└── .gitignore           # para ignorar arquivos desnecessários

[7.1] conteúdos do requirements.txt:

**flask**

[7.2] conteúdo sugestão para o .gitignore

venv/
__pycache__/
*.pyc
.env
.vscode/
.idea/

[7.3] para testar o curl no terminal:

**curl "http://127.0.0.1:5000/calcular?a=8&b=2&operacao=multiplicacao"**

**http://127.0.0.1:5000/calcular?a=10&b=5&operacao=soma**

### requisição exemplo

http://127.0.0.1:5000/calcular?a=10&b=5&operacao=soma

##

### resposta exemplo (sucesso)

```json
{
  "a": 10,
  "b": 5,
  "operacao": "soma",
  "resultado": 15
}
```
##

### resposta exemplo (erro)

```json
{
  "erro": "não é possível dividir por zero."
}
```

##

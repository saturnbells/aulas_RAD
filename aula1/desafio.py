from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular(a, b, operacao):
    if operacao == 'soma':
        return a + b
    elif operacao == 'subtracao':
        return a - b
    elif operacao == 'multiplicacao':
        return a * b
    elif operacao == 'divisao':
        if b == 0:
            raise ValueError("não é possível dividir por zero.")
        return a / b
    else:
        raise ValueError("operação inválida. use: soma, subtracao, multiplicacao, divisao.")

@app.route('/calcular', methods=['GET'])
def api_calcular():

    # query string
    a_str = request.args.get('a')
    b_str = request.args.get('b')
    operacao = request.args.get('operacao')

    if a_str is None or b_str is None or operacao is None:
        return jsonify({"erro": "parâmetros 'a', 'b' e 'operacao' são obrigatórios."}), 400

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        return jsonify({"erro": "os valores de 'a' e 'b' devem ser números."}), 400

    try:
        resultado = calcular(a, b, operacao)
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

    return jsonify({
        "a": a,
        "b": b,
        "operacao": operacao,
        "resultado": resultado
    })

if __name__ == '__main__':
    app.run(debug=True)

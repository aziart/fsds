from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/xyz', methods=['GET', 'POST'])
def test0():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))

@app.route('/tests/test1', methods=['POST'])
def test1():
    if(request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a + b
        return jsonify(str(result))

@app.route('/tests/test2', methods=['POST'])
def test2():
    if(request.method == 'POST'):
        a = request.json['num5']
        b = request.json['num6']
        result = a + b
        return jsonify(str(result))

@app.route('/tests/test3', methods=['POST'])
def test3():
    if(request.method == 'POST'):
        a = request.json['azi']
        b = request.json['art']
        result = a + b
        return jsonify(str(result))

if __name__ == '__main__':
    app.run(debug=True)


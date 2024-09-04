from flask import Flask, redirect, render_template, request
from pymongo import MongoClient


app = Flask(__name__)

# Conectar ao MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['guerreiros']
    collection = db['combatentes']
    print('Conexão com MongoDB estabelecida')
except Exception as e:
    print('Erro ao conectar ao MongoDB:', e)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/vigilia')
def vigilia():
    return render_template('Vigilia.html')

@app.route('/Vigilia_dados', methods=['POST'])
def vigilia_dados():
    op = request.form.get('op')
    if op == '2':
        consulta = {
            "$and": [
                {
                    "$or": [
                        {"$and": [{"comb1": "velocidade"}, {"nv1": {"$gt": 3}}]},
                        {"$and": [{"comb1": "camuflagem"}, {"nv1": {"$gte": 3}}]}
                    ]
                },
                {
                    "$or": [
                        {"$and": [{"comb2": "velocidade"}, {"nv2": {"$gte": 3}}]},
                        {"$and": [{"comb2": "camuflagem"}, {"nv2": {"$gt": 3}}]}
                    ]
                }
            ]
        }
        resposta = list(collection.find(consulta))
        return render_template('Vigilia_dados.html', resposta=resposta, op=op)
    else:
        return redirect('/')

@app.route('/Guerrilha')
def guerrilha():
    return render_template('Guerrilha.html')

@app.route('/Guerrilha_dados', methods=['POST'])
def guerrilha_dados():
    op2 = request.form.get('op2')
    if op2 == '1':
        consulta = {
            "$and": [
                {
                    "$or": [
                        {"$and": [{"comb1": "habilidade com arco e flecha"}, {"nv1": {"$gt": 5}}]},
                        {"$and": [{"comb1": "camuflagem"}, {"nv1": {"$gte": 5}}]}
                    ]
                },
                {
                    "$or": [
                        {"$and": [{"comb2": "habilidade com arco e flecha"}, {"nv2": {"$gte": 5}}]},
                        {"$and": [{"comb2": "camuflagem"}, {"nv2": {"$gt": 5}}]}
                    ]
                }
            ]
        }
        resposta = list(collection.find(consulta))
        print(resposta)
        return render_template('Guerrilha_dados.html', resposta=resposta, op2=op2)
    else:
        return redirect('/')

@app.route('/Enfrentamento')
def enfrentamento():
    return render_template('Enfrentamento.html')

@app.route('/Enfrentamento_dados', methods=['POST'])
def enfrentamento_dados():
    op3 = request.form.get('op3')
    if op3 == '3':
        consulta = {
            "$and": [
                {
                    "$or": [
                        {"$and": [{"comb1": "habilidade com lanca"}, {"nv1": {"$gt": 3}}]},
                        {"$and": [{"comb1": "resistencia"}, {"nv1": {"$gte": 3}}]}
                    ]
                },
                {
                    "$or": [
                        {"$and": [{"comb2": "habilidade com lanca"}, {"nv2": {"$gte": 3}}]},
                        {"$and": [{"comb2": "resistencia"}, {"nv2": {"$gt": 3}}]}
                    ]
                }
            ]
        }
        resposta = list(collection.find(consulta))
        return render_template('Enfrentamento_dados.html', resposta=resposta, op3=op3)
    else:
        return redirect('/')

@app.route('/Vitoria')
def vitoria():
    # Vamos garantir que op, op2 e op3 sejam passados corretamente para o template
    return render_template('Vitoria.html', op=request.args.get('op'), op2=request.args.get('op2'), op3=request.args.get('op3'))

if __name__ == '__main__':
    app.run(debug=True)

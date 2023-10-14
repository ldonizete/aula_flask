from flask import Blueprint, Response, request
from ..models.models import db, Estudante
import json

app = Blueprint("estudantes", __name__)

'''
{
    'id' : 1,
    'nome' : 'Jose',
    'idade' : 25,
    'PCD' : false
}

'''

@app.route('/')
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route('/add', methods=['POST'])
def add():
    estudante = Estudante(request.form['nome'], request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return app.response_class(response=json.dumps({'status': 'success', 'data': estudante.to_dict()}), status=200, content_type="application/json")
   

@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    # SELECT * FROM ESTUDANTE WHERE ID = 2
    estudante = Estudante.query.get(id)
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")
    

@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")


from flask import Flask, jsonify, request
from pydantic import BaseModel
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from tinydb import TinyDB, database, Query
from typing import Any, Optional


server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='API Desafio Cross Commerce')
spec.register(server)
database = TinyDB(r'C:\Users\Public\database.json')


class lista(BaseModel):
    resulatdo: list

@server.get('/ListaOrdenada')
@spec.validate(resp=Response(HTTP_200=lista))  
def retornar_lista():
    """Retorna a lista ordenada obtida na etapa 2 - Transform"""
    
    return jsonify(database.all())




server.run()

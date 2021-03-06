# coding=utf-8
from flask import Flask, jsonify, request
import requests

from flask_cors import CORS
from DB.DB_helper import INIT_API, saveCompany, getCompany, saveDeliveryman, savePackage

INIT_API()

app = Flask(__name__)

CORS(app)




@app.route('/company', methods=['POST'])
#Json Model /company --> {"Nome_fantasia":"empresa teste", "Senha":"123213132", "Login":"adasdsada", "Email":"dansdjad", "CNPJ":"1232353", "Endereco": {"Id":"","Logradouro":"testeLog", "Numero":"1234","Complemento":"testeComplemento", "Bairro":"testeBairoo", "CEP":"54546123", "Cidade":"testeC", "Estado":"testeE","Pais":"testeP"  } }

def register_company():

    if request.method == 'POST':  
        json = request.get_json()
        idCompany = saveCompany(json)
        
        if (idCompany):
            return jsonify({'response' : {"companyID":str(idCompany)}})
        else:
            return jsonify({'error' : 'Não foi possivel cadastrar'})
            

@app.route('/login',methods=['POST'])
#Json Model /login --> {"login":"teste","senha":"teste"}

def login_company():
    if request.method == 'POST':
        json_login = request.get_json()
        Company = getCompany (json_login)
        if (Company):
            
            return jsonify({'response' : Company})
        else:
            return jsonify({'error' : 'Não foi possivel logar usuario'})
        
            
@app.route('/cnpj/<cnpj>',methods=['GET'])
def cnpj(cnpj):
    if request.method == 'GET':
        
        r = requests.get('https://www.receitaws.com.br/v1/cnpj/'+ str(cnpj) )

        return jsonify(r.json())


@app.route('/deliveryman', methods=['POST'])

#Json Model /login -->
#{"CNH":"12432554","Nome_fantasia":"deliveryman", "Senha":"123213132", "Login":"deliveryman", "Email":"deliveryman",
#"Endereco": {"Logradouro":"deliveryman testeLog", "Numero":"1234","Complemento":"testeComplemento",
#"Bairro":"testeBairoo", "CEP":"54546123", "Cidade":"testeC", "Estado":"testeE","Pais":"testeP"  } } 

def register_deliveryman():
    if request.method == 'POST':  
        json = request.get_json()
        idDeliveryman = saveDeliveryman(json)
        
        if (idDeliveryman):
            return jsonify({'response' : {"companyID":str(idDeliveryman)}})
        else:
            return jsonify({'error' : 'Não foi possivel cadastrar'})

@app.route('/package', methods=['POST'])

def register_package():
    if request.method == 'POST':
        json = request.get_json()
        idPackage= savePackage(json)

        if (idPackage):
            return jsonify({'response' : {"packageID":str(idPackage)}})
        else:
            return jsonify({'error' : "Não foi possível cadastrar"})        

if __name__ == '__main__' :
    app.run()





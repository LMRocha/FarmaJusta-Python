from flask import Flask,request,jsonify,json
from database_db import Database

app = Flask(__name__)

@app.route("/consultaRegistro/", methods=["GET"])
def consulta_registro():
    db = Database()
    cod_registro = request.args.get('cod_registro')
    rows = db.consulta_medicamento_registro(cod_registro)

    results_dict = [{
        'principioativo': row[0],
        'laboratorio': row[1],
        'codggrem':row[2],
        'registro':row[3],
        'ean1':row[4],
        'ean2':row[5],
        'ean3':row[6],
        'produto':row[7],
        'apresentacao':row[8],
        'clsterapeutica':row[9],
        'pmc20':row[10],
        'iscomercializado':row[11]
    } for row in rows]

    return jsonify({'meds':results_dict})


def incluir_usuario():
    pass

def registra_denuncia():
    pass

if __name__ == '__main__':
    app.run(debug=True)




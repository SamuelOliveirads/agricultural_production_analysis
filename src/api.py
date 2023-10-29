from flask import Flask, request, jsonify
from load_data import load_data
from flasgger import Swagger

app = Flask(__name__)

swagger = Swagger(app)

# Carregando os dados
commodities_data = load_data()

@app.route('/api/commodities', methods=['GET'])
def get_commodities():
    """
    Endpoint to get commodities data
    ---
    parameters:
        - name: cod_variavel
          in: query
          type: integer
          required: true
          description: Code for the variable. Valid values are 109, 216, 214, 112, 215.
        - name: cod_produto_lavouras_temporarias
          in: query
          type: integer
          required: true
          description: Code for the variable. Valid values are 2713, 114253, 114254.
        - name: cod_ano
          in: query
          type: integer
          required: true
          description: Code for the variable. Valid values are 2016, 2017, 2018, 2019, 2020, 2021, 2012, 2013, 2014, 2015, 2022.
        - name: cod_municipio
          in: query
          type: integer
          required: true
          description: Code for the variable. Valid values are 5108402, 5102702, 5108303, 5106257, 5105903, 5107180, 5101001,
                  5106190, 5101704, 5106273, 5103304, 5108352, 5107263, 5104906,
                  5107008, 5106802, 5102504, 5108105, 5104609, 5101308, 5106182,
                  5107305, 5101605, 5101852, 5107602, 5103858, 5106232, 5104542,
                  5102694, 5103353, 5100250, 5106265, 5105309, 5107040, 5106372,
                  5107701, 5102850, 5101258, 5104500, 5103056, 5106752, 5103254,
                  5107743, 5106158, 5106505, 5108204, 5107883, 5104807, 5106307,
                  5106000, 5106208, 5103452, 5107065, 5100508, 5106653, 5108808,
                  5103403, 5106109, 5104203, 5107750, 5107800, 5100102, 5105622,
                  5103809, 5107206, 5104559, 5107156, 5105150, 5106224, 5104526,
                  5107297, 5103007, 5105606, 5106240, 5105176, 5100359, 5106299,
                  5100201, 5100300, 5106174, 5107776, 5106703, 5103601, 5107198,
                  5106422, 5101209, 5107875, 5103361, 5106851, 5105234, 5100607,
                  5101407, 5105580, 5106281, 5108501, 5105507, 5107768, 5101803,
                  5103379, 5107909, 5101902, 5107578, 5105200, 5100805, 5105259,
                  5103957, 5107404, 5100409, 5103502, 5108907, 5103908, 5105002,
                  5107248, 5103437, 5106455, 5108956, 5108600, 5102686, 5106828,
                  5108857, 5107958, 5102603, 5102678, 5107792, 5105101, 5104104,
                  5103700, 5107859, 5106315, 5103205, 5108055, 5106216, 5102637,
                  5103106, 5106778, 5102793, 5107107, 5108006, 5107941, 5107354.
    responses:
        200:
            description: Returns the commodities data.
    """
    # Recebendo os parâmetros
    cod_variavel = request.args.get('cod_variavel')
    cod_produto_lavouras_temporarias = request.args.get('cod_produto_lavouras_temporarias')
    cod_ano = request.args.get('cod_ano')
    cod_municipio = request.args.get('cod_municipio')

    # Filtrando os dados
    filtered_data = commodities_data
    if cod_variavel:
        filtered_data = filtered_data[filtered_data['cod_variavel'] == int(cod_variavel)]
    if cod_produto_lavouras_temporarias:
        filtered_data = filtered_data[filtered_data['cod_produto_lavouras_temporarias'] == int(cod_produto_lavouras_temporarias)]
    if cod_ano:
        filtered_data = filtered_data[filtered_data['cod_ano'] == int(cod_ano)]
    if cod_municipio:
        filtered_data = filtered_data[filtered_data['cod_municipio'] == int(cod_municipio)]

    # Retornando os dados filtrados
    return jsonify(filtered_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

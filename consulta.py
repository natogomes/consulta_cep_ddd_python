def consulta_cep(cep):
    import requests
    url = 'https://viacep.com.br/ws/%s/json/' % cep
    response = requests.get(url)
    response_json = response.json()
    return response_json


def consulta_ddd(ddd):
    import requests
    url = 'https://brasilapi.com.br/api/ddd/v1/%s' % ddd
    response = requests.get(url)
    response_json = response.json()
    return response_json


estados = {'RO': 'RONDÔNIA', 'AC': 'ACRE', 'AM': 'AMAZONAS', 'RR': 'RORAIMA', 'PA': 'PARÁ', 'AP': 'AMAPÁ',
           'TO': 'TOCANTINS', 'MA': 'MARANHÃO', 'PI': 'PIAUÍ', 'CE': 'CEARÁ', 'RN': 'RIO GRANDE DO NORTE',
           'PB': 'PARAÍBA', 'PE': 'PERNAMBUCO', 'AL': 'ALAGOAS', 'SE': 'SERGIPE', 'BA': 'BAHIA', 'MG': 'MINAS GERAIS',
           'ES': 'ESPÍRITO SANTO', 'RJ': 'RIO DE JANEIRO', 'SP': 'SÃO PAULO', 'PR': 'PARANÁ',
           'SC': 'SANTA CATARINA', 'RS': 'RIO GRANDE DO SUL', 'MS': 'MATO GROSSO DO SUL', 'MT': 'MATO GROSSO',
           'GO': 'GOIÁS', 'DF': 'DISTRITO FEDERAL'}

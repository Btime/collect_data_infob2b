import requests
from src.utils.headers_utils import get_headers

class GetData:
    def __init__(self):
        self.headers = get_headers()

    def request_relocation(self):
        params = {
            'ID_SOLICITACAO': '',
            'DS_STATUS': '1', # 1 = Em Aberto
            'ID_FUNCIONALIDADE': '110',
            'ID_ETAPA': '508',
            'TP_BUSCA': '',
            'DESC_BUSCA': '',
            'DATA_INICIO': '',
            'DATA_FIM': '',
            'IDUSUARIODIVISAO': '',
        }

        response = requests.get(
            'https://apisegmentacao.portalinfob2b.com.br/API/VisaoCliente/GetAtendimentoDetalhes',
            params=params,
            headers=self.headers,
        )

        if response.ok:

            list_dict = response.json()["retorno"]

            status_solicitation = {}

            for item in list_dict:
                status_solicitation[item["id_solicitacao"]] = item["ds_status"]

            return status_solicitation
        else:
            print(f'{response.status_code} - {response.reason} // Authorization expired')

    def request_collect_data(self, id_solicitation):
        params = {
            'ID_SOLICITACAO': id_solicitation,
        }

        response = requests.get(
            'https://apisegmentacao.portalinfob2b.com.br/API/RemanejamentoEstoque/GetRemanejamentoEstoqueDetalhes',
            params=params,
            headers=self.headers,
        )

        if response.ok:
            collect_data = response.json()["retorno"]

            data = {
                "ID_SOLICITACAO": collect_data.get("iD_SOLICITACAO"),
                "COTACAO_PEDIDO": collect_data.get("dS_COTACAO_PEDIDO"),
                "CD": collect_data.get("dS_CD"),
                "CODIGO_DE": collect_data.get("dS_CODIGO_DE"),
                "MODELO_DE": collect_data.get("dS_MODELO_DE"),
                "QUANTIDADE": collect_data.get("qtD_RemanejamentoEstoque"),
            }

            return data

    def handle_process(self):
        solicitation_id = self.request_relocation()

        if solicitation_id:
            for k, v in solicitation_id.items():
                if v == "EM ABERTO":
                    data_vivo_b2b = self.request_collect_data(k)
                    print(data_vivo_b2b)

    def start_requests(self):
        self.handle_process()
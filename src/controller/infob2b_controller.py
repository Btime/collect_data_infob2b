import requests
from src.utils.logs import Log
from src.utils.headers import get_headers

class GetData:
    def __init__(self) -> None:
        self.log = Log()

    def request_relocation(self, token_authorization):
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
            headers=get_headers(token_authorization),
        )

        if response.ok:

            list_dict = response.json()["retorno"]

            status_solicitation = {}

            for item in list_dict:
                status_solicitation[item["id_solicitacao"]] = item["ds_status"]

            self.log.info(
                status_code=response.status_code,
                descricao=f"{self.request_relocation.__name__}. Status EM ABERTO coletados para Remanejamento de estoque",
            )

            return status_solicitation
        else:
            print(f'{response.status_code} - {response.reason} // Authorization expired')
    
    def request_collect_data(self, id_solicitation, token_authorization):
        params = {
            'ID_SOLICITACAO': id_solicitation,
        }

        response = requests.get(
            'https://apisegmentacao.portalinfob2b.com.br/API/RemanejamentoEstoque/GetRemanejamentoEstoqueDetalhes',
            params=params,
            headers=get_headers(token_authorization),
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

            self.log.info(
                status_code=response.status_code,
                descricao=f"{self.request_collect_data.__name__}. Informacoes coletadas com sucesso. ID: {collect_data.get("iD_SOLICITACAO")}",
            )

            return data

    def handle_process(self, token_authorization):
        solicitation_id = self.request_relocation(token_authorization)

        if solicitation_id:
            for k, v in solicitation_id.items():
                if v == "EM ABERTO":
                    data_vivo_b2b = self.request_collect_data(k, token_authorization)
                    print(data_vivo_b2b)
            return True
        else:
            return False
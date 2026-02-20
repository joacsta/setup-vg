from datetime import datetime
from src.setup_vg.datetime.data_hora import dt_fim_apuracao, nu_ano_mes_atual

COLUNAS_CAMPANHAS = {
    "noCampanha": "",
    "deCampanha": "",
    "nuAnomesInicio": nu_ano_mes_atual(),
    "nuAnoMesFim": nu_ano_mes_atual(),
    "deImagemCampanha": "",
    # "delogoCampanha": "",
    "deBackgroundCampanha": "",
    "dhCriacao": datetime.now(),
    "dhAlteracao": datetime.now(),
    "idSituacaoCampanha": 1,
    "idTipoCampanha": 0,
    "icApuracaoMensal": True,
    "dtFimApuracao": dt_fim_apuracao(),
    "idTipoParticipante": 1,
    "icEmAtualizacao": False,
}

PRODUTOS = [
    "Prestamista",
    "Rapidex",
    "Residencial",
    "Capitalização",
    "Consórcio",
    "Vida",
    "Prestamista",
]

REDES = [
    "Todas as Redes",
    "Varejo Full",
    "Varejo (Agro)",
    "Varejo (Digital)",
    "Varejo (Private)",
    "Varejo (CVP)",
    "Atacado Full",
    "Atacado Sunco",
    "Atacado Sumep",
    "Parceiros Varejo",
    "Lotérico Varejo",
    "CCA Varejo",
    "Varejo/Digital",
    "Varejo/Digital/Agro",
    "Varejo/Agro",
]

REDES_DICT = {rede: i for i, rede in enumerate(REDES)}

DESCRICOES_CAMPANHAS = [
    "Realize sua primeira venda e ganhe brindes exclusivos!",
    "Atinja a meta e resgate brindes incríveis!",
    "Fique entre os primeiros colocados e garanta seu brinde!",
    "As unidades destaques ganharão premios imperdíveis!",
]

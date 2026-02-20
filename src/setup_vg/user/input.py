from questionary import select
from src.setup_vg.user.consts import DESCRICOES_CAMPANHAS, PRODUTOS, REDES


def ask_produto():
    return select(
        "qual produto a acao comercial promove?", PRODUTOS, show_selected=True
    ).ask()


def ask_rede():
    return select("qual a rede da acao comercial?", REDES, show_selected=True).ask()


def ask_descricao():
    predefinicao = select(
        "deseja escolher descricoes pre definidas?",
        ["sim", "não"],
        show_selected=True,
    ).ask()
    if predefinicao.startswith("s"):
        return select(
            "selecione a descricao para a nova acao comercial:",
            DESCRICOES_CAMPANHAS,
        ).ask()
    descricao_usuario = input("escreva a descricao da acao comercial: ")
    return descricao_usuario

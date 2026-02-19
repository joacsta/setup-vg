from questionary import select
from setup_vg.user.consts import PRODUTOS, REDES


def ask_produto():
    return select(
        "qual produto a acao comercial promove?", PRODUTOS, show_selected=True
    ).ask()


def ask_rede():
    return select("qual a rede da acao comercial?", REDES, show_selected=True).ask()

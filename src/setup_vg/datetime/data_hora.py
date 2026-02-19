from calendar import monthrange
from datetime import date, datetime, timedelta
from holidays import country_holidays


class Calendario:
    def __init__(self):
        self.ano = date.today().year
        self.data_atual = date.today()
        self.inicio_ano = date(self.ano, 1, 1)
        self.final_ano = date(self.ano, 12, 31)
        ultimo_dia_mes = monthrange(self.ano, self.data_atual.month)[1]
        self.qtd_dias_apuracao = 8
        self.feriados = set(country_holidays("BR", years=self.ano))
        self.data_fim_periodo_campanha = date(
            self.ano, self.data_atual.month, ultimo_dia_mes
        )

    def dias_uteis(self, start_date: date):
        start = start_date or self.inicio_ano
        calendario_dias_uteis: dict[int, date] = {}
        index_dia_util = 1

        while start <= self.final_ano:
            if start.weekday() < 5 and start not in self.feriados:
                calendario_dias_uteis[index_dia_util] = start
                index_dia_util += 1
            start += timedelta(days=1)
        return calendario_dias_uteis

    def periodo_campanha(self) -> date:
        return self.data_fim_periodo_campanha


def nu_ano_mes_atual() -> int:
    nu_anomes = int(datetime.now().strftime("%Y%m"))
    return nu_anomes


def data_hora():
    datahora = datetime.now()
    return datahora


def dt_fim_apuracao() -> date:
    periodo_campanha = Calendario().periodo_campanha()
    calendario_dias_uteis = Calendario().dias_uteis(periodo_campanha)
    fim_apuracao = calendario_dias_uteis[Calendario().qtd_dias_apuracao]
    return fim_apuracao

import pytest

from Pytoolsproject.spam.enviador_de_email import Enviador
from Pytoolsproject.spam.main import EnviadorDeSpam
from Pytoolsproject.spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_emails_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1



def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'luciano@python.pro.br',
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )



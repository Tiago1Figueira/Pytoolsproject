import pytest

from Pytoolsproject.spam.enviador_de_email import Enviador
from Pytoolsproject.spam.main import EnviadorDeSpam
from Pytoolsproject.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br'),
            Usuario(nome='Luciano', email='renzo@python.pro.br')
        ],
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br'),
            Usuario(nome='Luciano', email='renzo@python.pro.br')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados

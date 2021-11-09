import pytest

from Pytoolsproject.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    # Execução da fase de setup das fixtures.
    conexao_obj = Conexao()
    yield conexao_obj
    # Execução da fase de tear down das fixtures.
    conexao_obj.fechar()   # obj = objeto


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()   # sessao_obj = objeto
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()

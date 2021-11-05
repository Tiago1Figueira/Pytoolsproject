import pytest

from Pytoolsproject.spam.db import Conexao
from Pytoolsproject.spam.modelos import Usuario


@pytest.fixture
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


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Renzo'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

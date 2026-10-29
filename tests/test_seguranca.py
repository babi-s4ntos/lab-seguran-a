import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest
from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)


@pytest.mark.security
def test_deve_comprovar_vulnerabilidade_de_sql_injection():
    payload = {
        "email": "admin@hubsolidario.org' --",
        "senha": "senha_incorreta"
    }
    resposta = cliente.post("/vulneravel/login", json=payload)

    assert resposta.status_code == 200
    assert resposta.json()["is_admin"] is True


@pytest.mark.security
def test_deve_comprovar_vulnerabilidade_de_xss():
    payload = {
        "autor": "Atacante",
        "conteudo": "<script>alert(1)</script>"
    }
    resposta = cliente.post("/vulneravel/comentarios", json=payload)

    assert resposta.status_code == 200
    assert "<script>" in resposta.json()["conteudo"]


@pytest.mark.security
def test_endpoint_seguro_deve_bloquear_sql_injection():
    payload = {
        "email": "admin@hubsolidario.org' --",
        "senha": "senha_incorreta"
    }
    resposta = cliente.post("/seguro/login", json=payload)

    assert resposta.status_code == 401
    assert resposta.json()["detail"] == "Credenciais invalidas"


@pytest.mark.security
def test_endpoint_seguro_deve_sanitizar_tags_xss():
    payload = {
        "autor": "Atacante",
        "conteudo": "<script>alert('Ataque XSS')</script>"
    }
    resposta = cliente.post("/seguro/comentarios", json=payload)

    assert resposta.status_code == 200
    conteudo = resposta.json()["conteudo"]
    assert "<script>" not in conteudo
    assert "&lt;script&gt;" in conteudo


@pytest.mark.security
def test_union_select_comprova_vazamento_na_rota_vulneravel():
    # Teste local: verifica o risco de exposicao de dados.
    termo = "%' UNION SELECT id, email, senha FROM usuarios -- "
    resposta = cliente.get(
        "/vulneravel/campanhas/buscar",
        params={"termo": termo}
    )

    assert resposta.status_code == 200
    assert "admin@hubsolidario.org" in resposta.text


@pytest.mark.security
def test_busca_segura_nao_expoe_usuarios_com_union_select():
    termo = "%' UNION SELECT id, email, senha FROM usuarios -- "
    resposta = cliente.get(
        "/seguro/campanhas/buscar",
        params={"termo": termo}
    )

    assert resposta.status_code == 200
    assert "admin@hubsolidario.org" not in resposta.text
    assert "segredo_admin_123" not in resposta.text


@pytest.mark.security
def test_xss_com_onerror_e_devolvido_codificado():
    payload = {
        "autor": "Teste",
        "conteudo": '<img src="x" onerror="alert(1)">'
    }
    resposta = cliente.post("/seguro/comentarios", json=payload)

    assert resposta.status_code == 200
    conteudo = resposta.json()["conteudo"]
    assert "<img" not in conteudo
    assert "&lt;img" in conteudo
    assert "&quot;" in conteudo


@pytest.mark.security
def test_comentario_normal_e_aceito_pela_rota_segura():
    payload = {
        "autor": "Lucas",
        "conteudo": "Campanha de arrecadacao"
    }
    resposta = cliente.post("/seguro/comentarios", json=payload)

    assert resposta.status_code == 200
    assert resposta.json()["autor"] == "Lucas"
    assert resposta.json()["conteudo"] == "Campanha de arrecadacao"

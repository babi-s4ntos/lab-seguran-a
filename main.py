import html
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Hub Solidario - Laboratorio OWASP")

db = sqlite3.connect(":memory:", check_same_thread=False)

db.executescript("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL
);

CREATE TABLE comentarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    autor TEXT NOT NULL,
    conteudo TEXT NOT NULL
);

CREATE TABLE campanhas (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    meta REAL NOT NULL
);

INSERT INTO usuarios VALUES
(1, 'Administrador', 'admin@hubsolidario.org',
 'segredo_admin_123', 1),
(2, 'Voluntario Lucas', 'lucas@voluntariado.org',
 'senha_lucas_456', 0);

INSERT INTO campanhas VALUES
(1, 'Cestas basicas', 1500),
(2, 'Material escolar', 2000);
""")
db.commit()


class RequisicaoLogin(BaseModel):
    email: str
    senha: str


class RequisicaoComentario(BaseModel):
    autor: str
    conteudo: str


# ROTAS VULNERAVEIS: APENAS PARA TESTES LOCAIS CONTROLADOS

@app.post("/vulneravel/login")
def login_vulneravel(dados: RequisicaoLogin):
    cursor = db.cursor()
    query = (
        f"SELECT id, nome, email, is_admin FROM usuarios "
        f"WHERE email = '{dados.email}' AND senha = '{dados.senha}'"
    )
    cursor.execute(query)
    usuario = cursor.fetchone()

    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais invalidas")

    return {
        "id": usuario[0],
        "nome": usuario[1],
        "email": usuario[2],
        "is_admin": bool(usuario[3])
    }


@app.post("/vulneravel/comentarios")
def comentar_vulneravel(dados: RequisicaoComentario):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO comentarios (autor, conteudo) VALUES (?, ?)",
        (dados.autor, dados.conteudo)
    )
    db.commit()
    return {"autor": dados.autor, "conteudo": dados.conteudo}


@app.get("/vulneravel/campanhas/buscar")
def buscar_campanhas_vulneravel(termo: str):
    cursor = db.cursor()
    query = (
        "SELECT id, titulo, meta FROM campanhas "
        f"WHERE titulo LIKE '%{termo}%'"
    )
    cursor.execute(query)
    return {"resultados": cursor.fetchall()}


# ROTAS CORRIGIDAS

@app.post("/seguro/login")
def login_seguro(dados: RequisicaoLogin):
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, nome, email, is_admin FROM usuarios "
        "WHERE email = ? AND senha = ?",
        (dados.email, dados.senha)
    )
    usuario = cursor.fetchone()

    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais invalidas")

    return {
        "id": usuario[0],
        "nome": usuario[1],
        "email": usuario[2],
        "is_admin": bool(usuario[3])
    }


@app.post("/seguro/comentarios")
def comentar_seguro(dados: RequisicaoComentario):
    autor_seguro = html.escape(dados.autor.strip())
    conteudo_seguro = html.escape(dados.conteudo.strip())

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO comentarios (autor, conteudo) VALUES (?, ?)",
        (autor_seguro, conteudo_seguro)
    )
    db.commit()

    return {"autor": autor_seguro, "conteudo": conteudo_seguro}


@app.get("/seguro/campanhas/buscar")
def buscar_campanhas_seguro(termo: str):
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, titulo, meta FROM campanhas WHERE titulo LIKE ?",
        (f"%{termo}%",)
    )
    return {"resultados": cursor.fetchall()}

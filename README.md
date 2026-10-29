QTS 10 — Segurança Ofensiva Básica OWASP
Testes Práticos contra Injeção de SQL e XSS em APIs

Projeto desenvolvido para a atividade da disciplina de Qualidade e Teste de Software (QTS), com foco na identificação de vulnerabilidades de segurança em APIs, aplicação de correções e validação por meio de testes automatizados.

1. Objetivo

Analisar vulnerabilidades de SQL Injection e Cross-Site Scripting (XSS) em uma API desenvolvida com FastAPI, demonstrando como essas falhas podem ocorrer e como podem ser mitigadas por meio de práticas seguras de programação.

O projeto compara endpoints vulneráveis com endpoints corrigidos e utiliza testes automatizados para verificar o comportamento da aplicação.

2. Tecnologias utilizadas
Python
FastAPI
SQLite
Pytest
TestClient do FastAPI
HTTPX
uv para gerenciamento do ambiente e das dependências
Git e GitHub para versionamento e entrega do projeto
3. Vulnerabilidades analisadas
3.1 SQL Injection

A injeção de SQL ocorre quando dados fornecidos pelo usuário são incorporados diretamente a uma consulta SQL, permitindo a alteração de sua lógica.

Risco: acesso indevido a informações, possibilidade de contornar autenticações e comprometimento da integridade dos dados.

Correção aplicada: utilização de consultas parametrizadas (Prepared Statements), separando os valores fornecidos pelo usuário da estrutura do comando SQL.

3.2 Cross-Site Scripting (XSS)

O XSS ocorre quando conteúdo não confiável é tratado como código executável pelo navegador.

Risco: execução de scripts indevidos no contexto da aplicação e possíveis ataques contra usuários.

Correção aplicada: codificação de caracteres especiais com html.escape() e tratamento adequado dos dados de entrada e saída, conforme o contexto de utilização.

4. Estrutura do projeto
text
lab-seguranca-owasp/
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
├── .gitignore
├── tests/
│   └── test_seguranca.py
└── evidencias/
    └── arquivos de evidência, se aplicável


A pasta .venv, os arquivos de cache e outros arquivos temporários não devem ser enviados ao repositório.

5. Testes automatizados

Os testes foram estruturados com o padrão AAA:

Arrange: preparação dos dados e das condições do teste.
Act: execução da requisição à API.
Assert: verificação do resultado esperado.

A suíte contempla quatro cenários:

Verificação da vulnerabilidade de SQL Injection no endpoint vulnerável.
Verificação da exposição de conteúdo HTML no endpoint vulnerável.
Verificação do bloqueio de SQL Injection no endpoint seguro.
Verificação da codificação de conteúdo potencialmente perigoso no endpoint seguro.
6. Como executar o projeto
Pré-requisitos

Ter Python e uv instalados, além do Git para versionamento.

Instalação das dependências

No terminal, dentro da pasta do projeto, execute:

powershell
uv sync

Execução dos testes

Execute:

powershell
uv run pytest -v


O resultado esperado, caso todos os testes estejam funcionando corretamente, é a aprovação dos quatro testes da suíte.

text
4 passed


A saída real do terminal deve ser utilizada como evidência da execução.

7. Resultados e conclusões

A atividade demonstra a importância de identificar falhas de segurança por meio de testes automatizados, comparar comportamentos vulneráveis e seguros e aplicar correções no código.

As consultas parametrizadas ajudam a impedir a alteração da lógica SQL por entradas maliciosas. A codificação contextual de conteúdo ajuda a evitar que dados sejam interpretados como marcação HTML executável.

Os testes automatizados permitem verificar se as proteções implementadas apresentam o comportamento esperado e podem ser executados novamente após alterações no código.

8. Evidências da atividade

Podem ser incluídas na pasta evidencias/:

Captura de tela da execução do uv run pytest -v.
Resultado do quiz da plataforma, se solicitado.
Relatório da atividade em PDF, caso faça parte das exigências de entrega.
9. Referências
OWASP Top 10: https://owasp.org/www-project-top-ten/
OWASP SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
OWASP Cross Site Scripting Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
FastAPI: https://fastapi.tiangolo.com/
Pytest: https://docs.pytest.org/

Disciplina: Qualidade e Teste de Software (QTS)
Atividade: 10 — Segurança Ofensiva Básica OWASP
Tema: Testes práticos contra SQL Injection e XSS em APIs
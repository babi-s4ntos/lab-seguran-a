🛡️ Laboratório de Segurança Ofensiva — OWASP

<p align="center">
<img src="https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Pytest-Testes-0A9EDC?logo=pytest&logoColor=white" alt="Pytest">
<img src="https://img.shields.io/badge/OWASP-Segurança-black?logo=owasp&logoColor=white" alt="OWASP">
<img src="https://img.shields.io/badge/Status-Concluído-success" alt="Status">
</p>

📚 Sobre o projeto

Este projeto foi desenvolvido como atividade prática da disciplina Qualidade e Teste de Software (QTS), no módulo 10 — Segurança Ofensiva Básica OWASP.

O laboratório tem como objetivo demonstrar, em um ambiente controlado, como identificar vulnerabilidades em APIs, realizar testes automatizados de segurança e aplicar medidas de proteção contra ataques comuns a aplicações web.

A atividade utiliza uma API de exemplo inspirada no contexto de um sistema de campanhas solidárias, permitindo comparar comportamentos vulneráveis e implementações com mecanismos de defesa.

🎯 Objetivos
Compreender os riscos da injeção de SQL (SQL Injection).
Identificar vulnerabilidades de Cross-Site Scripting (XSS).
Comparar endpoints vulneráveis e protegidos.
Aplicar consultas SQL parametrizadas (Prepared Statements).
Utilizar html.escape() para codificação de caracteres HTML.
Desenvolver testes automatizados com pytest e TestClient.
Aplicar o padrão AAA: Arrange, Act, Assert.
Validar as medidas de segurança por meio de testes automatizados.
🧪 Vulnerabilidades estudadas
1. SQL Injection (SQLi)

A injeção de SQL ocorre quando entradas não confiáveis alteram a estrutura de uma consulta ao banco de dados.

Risco: autenticação indevida, exposição de informações e comprometimento da integridade dos dados.

Medida de proteção: utilização de consultas parametrizadas, separando os comandos SQL dos valores fornecidos pelo usuário.

2. Cross-Site Scripting (XSS)

O XSS acontece quando conteúdo não confiável é interpretado pelo navegador como código executável.

Risco: execução de scripts maliciosos no contexto da aplicação e possíveis ataques contra usuários.

Medida de proteção: codificação contextual de saída, validação de dados e utilização segura do conteúdo fornecido pelo usuário.

Os testes são realizados exclusivamente no ambiente didático local do laboratório.
🛠️ Tecnologias utilizadas
Tecnologia	Finalidade
Python	Linguagem de programação
FastAPI	Desenvolvimento da API
SQLite	Banco de dados relacional
Pytest	Automação dos testes
TestClient	Testes de endpoints da API
HTTPX	Suporte às requisições de teste
uv	Gerenciamento do ambiente e das dependências
Git e GitHub	Versionamento e publicação do projeto
📂 Estrutura do projeto
text
lab-seguranca-owasp/
├── evidencias/
│   ├── Quiz.png
│   ├── print1.png
│   └── print2.png
├── tests/
│   └── test_seguranca.py
├── main.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md

⚙️ Como executar o projeto
Pré-requisitos
Python instalado.
Git instalado.
uv instalado.
1. Clonar o repositório
bash
git clone https://github.com/babi-s4ntos/lab-seguran-a.git
cd lab-seguran-a

2. Instalar as dependências
bash
uv sync

3. Executar os testes automatizados
bash
uv run pytest -v


O comando executa a suíte de testes e apresenta o resultado individual de cada caso.

✅ Testes de segurança

A suíte automatizada contempla quatro cenários principais:

Teste	Resultado esperado
SQL Injection no endpoint vulnerável	Demonstração da falha
XSS no endpoint vulnerável	Demonstração da ausência de codificação
SQL Injection no endpoint seguro	Rejeição da autenticação indevida
XSS no endpoint seguro	Conteúdo codificado com entidades HTML

Os testes seguem o padrão AAA:

Arrange: preparação dos dados e das condições do teste.
Act: execução da requisição à API.
Assert: verificação do comportamento esperado.

O resultado esperado para a suíte fornecida é de 4 testes aprovados. A confirmação deve ser feita executando os testes no ambiente local.

🖼️ Evidências da atividade

As capturas de tela e os registros da atividade estão disponíveis na pasta evidencias/.

Quiz de fixação

!Resultado do quiz

Evidência 1

!Evidência 1

Evidência 2

!Evidência 2

📖 Conteúdos da disciplina QTS

O projeto integra os conteúdos estudados ao longo da disciplina:

Introdução
Testes Unitários
Psicologia do Teste e Maturidade
Técnicas de Caixa Branca e Caixa Preta
AT1 — Engenharia de Testes e Cobertura de Código
Testes de Integração e Mocks
Testes End-to-End com Playwright
Usabilidade, Acessibilidade e Auditoria
Testes de Carga e Performance
Segurança Ofensiva Básica OWASP
🎓 Aprendizados

A atividade permitiu explorar a importância dos testes de segurança no desenvolvimento de software, compreender vulnerabilidades comuns em APIs e verificar como medidas defensivas podem ser validadas automaticamente.

Também reforçou a importância de revisar códigos gerados por ferramentas de inteligência artificial, garantindo que as implementações atendam aos requisitos de segurança e qualidade.

🔗 Links
Repositório GitHub: https://github.com/babi-s4ntos/lab-seguran-a
Material da aula: Testes Práticos contra Injeção de SQL e XSS em APIs

<p align="center">
Desenvolvido como atividade acadêmica da disciplina <strong>Qualidade e Teste de Software (QTS)</strong>.
</p>
# 🗂️ Agenda de Contatos

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/Django-4.2%2B-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)


Uma aplicação web completa para gerenciamento de contatos desenvolvida em Python utilizando o ecossistema **Django**. O projeto foi estruturado seguindo rigorosamente as boas práticas de desenvolvimento de software, padrões arquiteturais do Django, type hinting para maior robustez do código e estilização moderna com variáveis CSS customizadas.

---

## 🛠️ Tecnologias & Ferramentas Utilizadas

- **Backend:** Python, Django MVT (Model-View-Template)
- **Banco de Dados:** SQLite (Ambiente de Desenvolvimento)
- **Qualidade de Código & Estilo:** Ruff (Linter e Code Formatter), PEP 8, Type Hinting (`HttpRequest`, `Render`)
- **Frontend Estático:** HTML5, CSS3 Avançado (Variáveis Nativas, Design Responsivo, Flexbox)
- **Controle de Versão:** Git seguindo a especificação de *Conventional Commits*

---

## 📂 Estrutura de Diretórios do Projeto

O projeto adota uma arquitetura global para arquivos estáticos e templates, facilitando o reaproveitamento de componentes visuais (`base.html`) e regras de estilo (`style.css`) por múltiplos aplicativos internos.

```text
Agenda/
│
├── base_static/              # Arquivos estáticos globais do projeto
│   └── global/
│       └── css/
│           └── style.css     # Estilização global da aplicação (Design System base)
│
├── base_templates/           # Templates HTML globais do projeto
│   └── global/
│       └── base.html         # Template estrutural base (Layout principal)
│
├── contact/                  # Application principal de Contatos
│   ├── migrations/           # Histórico de migrações do Banco de Dados
│   ├── templates/
│   │   └── contact/
│   │       └── index.html    # View extendida para exibição e listagem de contatos
│   ├── views/
│   │   ├── __init__.py       # Exportações explícitas de views (Evitando Star Imports)
│   │   └── contact_views.py  # Lógica de controle, consultas ORM e tratamento de contexto
│   ├── models.py             # Modelo 'Contact' com mapeamento de dados
│   └── apps.py
│
├── project/                  # Diretório de configurações core do Django (Settings)
│   ├── __init__.py
│   ├── settings.py           # Configurações do projeto (STATICFILES_DIRS, APPS)
│   └── urls.py               # Roteamento global de URLs
│
├── manage.py                 # CLI utilitário do Django
└── README.md                 # Documentação do projeto

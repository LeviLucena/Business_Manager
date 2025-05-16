business_manager/          # Pasta raiz do projeto
│
├── core/                  # App principal (gestão de negócios)
│   ├── migrations/        # Migrações do banco de dados
│   ├── templates/         # Templates HTML específicos do core
│   │   └── core/          # Ex.: lista_clientes.html, etc.
│   ├── __init__.py
│   ├── admin.py           # Registro de modelos no admin
│   ├── models.py          # Modelos (Clientes, Produtos)
│   ├── views.py           # Lógica das páginas (CRUD)
│   └── urls.py            # URLs do app core
│
├── chat/                  # App do chatbot
│   ├── templates/chat/    # Templates do chat
│   │   └── chat.html
│   ├── __init__.py
│   ├── utils.py           # Função de chamada à API da DeepSeek
│   ├── views.py           # Lógica do chat
│   └── urls.py            # URLs do app chat
│
├── business_manager/      # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py        # Configurações (apps, middleware, etc.)
│   ├── urls.py            # URLs globais
│   └── wsgi.py
│
├── .env                   # Arquivo para variáveis de ambiente (API Key)
├── db.sqlite3             # Banco de dados SQLite
└── manage.py              # Script de administração do Django
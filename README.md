<p align="center">
  <!-- Linguagem principal -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  </a>
  
  <!-- Framework web -->
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django&logoColor=white" alt="Django" />
  </a>

  <!-- Banco de dados -->
  <a href="https://www.sqlite.org/">
    <img src="https://img.shields.io/badge/-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite" />
  </a>

  <!-- Frontend -->
  <a href="https://getbootstrap.com/docs/3.4/">
    <img src="https://img.shields.io/badge/-Bootstrap%203-563D7C?style=flat-square&logo=bootstrap&logoColor=white" alt="Bootstrap 3" />
  </a>

  <!-- Ícones -->
  <a href="https://fontawesome.com/v4/">
    <img src="https://img.shields.io/badge/-Font%20Awesome%204-339AF0?style=flat-square&logo=font-awesome&logoColor=white" alt="Font Awesome" />
  </a>

  <!-- API IA -->
  <a href="https://deepseek.com/">
    <img src="https://img.shields.io/badge/-DeepSeek%20API-5C4EE5?style=flat-square&logo=ai&logoColor=white" alt="DeepSeek API" />
  </a>

  <!-- Autenticação -->
  <a href="https://docs.djangoproject.com/en/5.2/topics/auth/">
    <img src="https://img.shields.io/badge/-Django%20Auth-FF6B6B?style=flat-square&logo=django&logoColor=white" alt="Django Auth" />
  </a>

  <!-- Variáveis de ambiente -->
  <a href="https://pypi.org/project/python-dotenv/">
    <img src="https://img.shields.io/badge/-Dotenv-ECD53F?style=flat-square&logo=python&logoColor=black" alt="Dotenv" />
  </a>

  <!-- Status do projeto -->
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square" alt="Status" />
  
  <!-- Licença -->
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT License" />
</p>
  
![Gemini_Generated_Image_fz4suifz4suifz4s](https://github.com/user-attachments/assets/21933bf4-d43f-4204-99e4-a9dab6999022)

## 📋 Descrição
O Business Manager Pro é uma plataforma web robusta, desenvolvida em Django, que proporciona uma gestão completa e eficiente para empresas, incluindo:

- 📋 Gestão de clientes com histórico detalhado de interações, facilitando o relacionamento e o acompanhamento contínuo
- 📦 Controle integrado de produtos e serviços, otimizando operações e inventário
- 🤖 Chatbot inteligente alimentado pela tecnologia DeepSeek AI, garantindo atendimento automatizado, rápido e preciso 24/7
- 📊 Dashboard intuitivo com estatísticas em tempo real e atividades recentes, para tomada de decisão ágil e informada

## 🧠 Chatbot Inteligente
A integração com DeepSeek AI permite conversas automatizadas com clientes, diretamente pela plataforma. O chatbot opera 24/7 e pode ser acessado na área Chatbot Inteligente do dashboard.

## 📊 Estatísticas em Tempo Real
O painel apresenta dados como:

- Gestão de Clientes: CRUD completo de clientes
- Controle de Produtos: Cadastro e gerenciamento de produtos/serviços
- Chatbot Inteligente: Integração com API da DeepSeek para atendimento automatizado
- Dashboard: Visualização de métricas e atividades recentes
- Autenticação: Sistema de login seguro com Django Auth

## ⚙️ Funcionalidades
- ✅ Cadastro, edição e exclusão de clientes.
- ✅ Gerenciamento de produtos/serviços e estoque.
- ✅ Integração com IA para atendimento ao cliente via Chatbot.
- ✅ Painel administrativo com estatísticas e relatórios.

## 🛠️ Tecnologias Utilizadas
- Backend: Django 5.2
- Frontend: Bootstrap 3 + Font Awesome
- Banco de Dados: SQLite (padrão)
- API: DeepSeek Chat
- Outras Bibliotecas: python-dotenv, requests

## 📸 Exemplo da Interface

| 🟦 **Imagem 1** 🟦 | 🟦 **Imagem 2** 🟦 | 🟦 **Imagem 3** 🟦 |
|----------------------|----------------------|----------------------|
| ![Descrição1](https://github.com/user-attachments/assets/fcae72e9-ef44-4782-b340-cf926430ea7d) | ![Descrição2](https://github.com/user-attachments/assets/63826fe6-50f0-4b59-b87d-0b09055dfa62) | ![Descrição3](https://github.com/user-attachments/assets/d2861ab1-4455-4ce1-9270-9654ee799be5) |
| *Tela Inicial* | *Chat Empresarial* | *Administração Banco* |

## 📦 Estrutura do Projeto
  ```bash
  business_manager/
├── core/               # App principal (gestão de negócios)
│   ├── models.py       # Modelos de dados
│   ├── views.py        # Lógica das páginas
│   └── templates/      # Templates HTML
│
├── chat/               # App do chatbot
│   ├── utils.py        # Integração com API DeepSeek
│   └── templates/      # Templates do chat
│
├── business_manager/   # Configurações do projeto
│   ├── settings.py     # Configurações
│   └── urls.py         # Rotas globais
│
├── templates/          # Templates globais
├── .env                # Variáveis de ambiente
└── manage.py           # Script de administração
  ```

## 🔒 Variáveis de Ambiente

| Variável            | Descrição                             | Exemplo                     |
|---------------------|---------------------------------------|-----------------------------|
| `DEEPSEEK_API_KEY`  | Chave de API da DeepSeek              | `sk_123abc...`              |
| `DEBUG`             | Modo debug (True/False)               | `True` ou `False`           |
| `SECRET_KEY`        | Chave secreta do Django               | Gerada automaticamente     |

## 🚀 Como Rodar Localmente
#### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/business-manager-pro.git
cd business-manager-pro
```

#### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

#### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

#### 4. Configure as variáveis de ambiente:
```bash
cp .env.example .env

# Edite o arquivo .env com suas credenciais:
DEEPSEEK_API_KEY=sua_chave_aqui
DEBUG=True
```

### 5. Aplique as migrações
```bash
python manage.py migrate
```

#### 6. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```

#### 7. Inicie o servidor
```bash
python manage.py runserver
```

#### 8. Acesse no navegador

- Página inicial: [http://localhost:8000](http://localhost:8000)
- Painel administrativo: [http://localhost:8000/admin](http://localhost:8000/admin)
- Chatbot empresarial: [http://localhost:8000/chat](http://localhost:8000/chat)

## 🤝 Como Contribuir
Sinta-se à vontade para contribuir, sugerir melhorias ou relatar problemas para ajudar a desenvolver este projeto.

## 📄 Licença
Este projeto está licenciado sob a licença MIT — veja [LICENSE](https://github.com/github/gitignore/blob/main/LICENSE) para detalhes.

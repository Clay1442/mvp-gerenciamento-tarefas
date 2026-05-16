# MVP - Sistema de Gerenciamento de Tarefas 

Uma aplicação Full-Stack completa para gerenciamento dinâmico de tarefas através de um quadro Kanban interativo. O projeto conta com autenticação robusta, criptografia de ponta a ponta e uma arquitetura limpa, separada em camadas organizadas.

---

## 🔗 Links da Aplicação em Produção

* **🖥️ Frontend (Interface do Usuário):** [Acesse o Sistema na Vercel](https://mvp-gerenciamento-tarefas.vercel.app)
* **⚙️ Backend (API Swagger):** [Explore e Teste a API no Render](https://mvp-gerenciamento-tarefas.onrender.com/docs)

---

## 🛠️ Tecnologias Utilizadas

### **Frontend**
* **React** (com **TypeScript**) para uma interface tipada e segura.
* **Vite** como ferramenta de build rápida e moderna.
* **Axios** para consumo de rotas HTTP.
* **React Router DOM** para controle de rotas dinâmicas.

### **Backend**
* **FastAPI** (Python 3.14) focado em alta performance e documentação automatizada.
* **SQLAlchemy** como ORM para mapeamento e manipulação de dados.
* **SQLite** como banco de dados relacional leve para persistência.
* **Passlib (Bcrypt)** para hash e criptografia segura de senhas.
* **PyJWT** para geração e validação de Tokens de acesso (JWT).

### **DevOps & Infraestrutura**
* **Vercel** para hospedagem otimizada e contínua do Frontend.
* **Render** para publicação do servidor assíncrono Backend.
* **Variáveis de Ambiente** para proteção total de chaves e strings de conexão de produção.

---

## 📐 Arquitetura do Backend

O backend foi estruturado seguindo o padrão de **Arquitetura em Camadas** e desacoplamento de responsabilidades através de **DTOs (Data Transfer Objects)**:

* **`controllers/`**: Camada de entrada, responsável por expor os endpoints e receber as requisições HTTP.
* **`services/`**: Camada de regras de negócio, onde toda a lógica central da aplicação é processada.
* **`models/`**: Definição das tabelas e entidades mapeadas diretamente no banco de dados com o SQLAlchemy.
* **`schemas/`**: Esquemas de validação de dados via Pydantic (DTOs), garantindo que a entrada e saída de dados sejam estritamente controladas.

---

## 🚀 Funcionalidades Principais

* [x] **Autenticação Segura:** Registro de novos usuários com senhas criptografadas e fluxo de login com Token JWT.
* [x] **Rotas Protegidas:** Middlewares de segurança que barram requisições não autenticadas no banco de dados.
* [x] **CRUD de Tarefas:** Criação, leitura, atualização e deleção de tarefas organizadas por status.
* [x] **Documentação Nativa:** Integração total com o Swagger UI interativo para simulação rápida de endpoints.

---

## ⚙️ Como Executar o Projeto Localmente

### **Pré-requisitos**
* Python 3.12 ou superior instalado.
* Node.js (LTS) instalado.

### **1. Configurando o Backend**
```bash
# Entre na pasta do backend
cd backend

# Crie e ative seu ambiente virtual
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Crie um arquivo chamado .env na raiz da pasta /backend e adicione:
# SECRET_KEY=sua_chave_secreta_aqui
# ALGORITHM=HS256
# ACCESS_TOKEN_EXPIRE_MINUTES=30
# DATABASE_URL=sqlite:///./trello.db

# Execute o servidor
uvicorn src.main:app --reload
```

### **2. Configurando o Frontend**
```bash
# Entre na pasta do frontend
cd ../frontend

# Instale as dependências do Node
npm install

# Crie um arquivo chamado .env na raiz da pasta /frontend e adicione:
# VITE_API_URL=http://localhost:8000

# Execute em modo de desenvolvimento
npm run dev
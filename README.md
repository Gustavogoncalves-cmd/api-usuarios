# 🚀 API de Usuários – FastAPI

API REST para gerenciamento de usuários desenvolvida com **FastAPI**, utilizando **Pydantic** para validação de dados e **Swagger UI** para documentação automática.

Projeto criado com foco em **portfólio para estágio/júnior backend**.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- Git & GitHub

---

## 📌 Funcionalidades

- Criar usuários
- Listar usuários
- Buscar usuário por ID
- Documentação automática com Swagger

---

## 📂 Estrutura do Projeto

api-usuarios/
├── main.py
├── schemas.py
├── README.md
├── .gitignore
└── venv/

yaml
Copiar código

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/Gustavogoncalves-cmd/api-usuarios.git
cd api-usuarios
2️⃣ Criar e ativar ambiente virtual
bash
Copiar código
python -m venv venv
Windows

bash
Copiar código
venv\Scripts\activate
Linux / macOS

bash
Copiar código
source venv/bin/activate
3️⃣ Instalar dependências
bash
Copiar código
pip install fastapi uvicorn
4️⃣ Executar a aplicação
bash
Copiar código
uvicorn main:app --reload
📖 Documentação (Swagger)
Acesse no navegador:

arduino
Copiar código
http://127.0.0.1:8000/docs
🧪 Exemplo de Payload (POST /users)
json
Copiar código
{
  "name": "Gustavo",
  "email": "gustavo@email.com"
}
🎯 Objetivo do Projeto
Este projeto tem como objetivo demonstrar:

Criação de APIs REST com FastAPI

Organização de código

Validação de dados com Pydantic

Uso de Swagger para testes

Versionamento com Git

👤 Autor
Gustavogoncalves-cmd
Estudante de Análise e Desenvolvimento de Sistemas
Foco em Backend Python (FastAPI)

# 🏍️ Oficina de Motos

Sistema web desenvolvido com Django para o gerenciamento de clientes e serviços em uma oficina de motos.

---

## 🧠 Funcionalidades

* ✔️ Cadastro completo de motos (Marca, Modelo, Ano, Placa, Nome do Dono, Descrição do Serviço e Preço)
* ✔️ Listagem de todos os serviços cadastrados na oficina
* ✔️ Interface estilizada com CSS minimalista focado na leitura
* ✔️ Banco de dados relacional local pré-configurado

---

## 🛠️ Tecnologias

* **Linguagem:** Python
* **Framework:** Django
* **Frontend:** HTML5 + CSS3 (Vanilla)
* **Banco de Dados:** SQLite3
* **Pacotes:** gerenciado via Poetry / Pip (`requirements.txt`)

---

## ⚙️ Como usar

```bash
# Clonar o repositório
git clone https://github.com/JockaMt/django-crud.git

# Entrar na pasta do projeto
cd django-crud

# Criar e ativar o ambiente virtual (Recomendado)
python -m venv .venv
# No Windows: .\.venv\Scripts\activate
# No Linux/Mac: source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
# Ou, se preferir usar o poetry: poetry install

# Criar o banco de dados e aplicar as migrações (se for a primeira vez)
python manage.py makemigrations motos
python manage.py migrate

# Rodar o servidor local
python manage.py runserver
```

---

## 📸 Demonstração

(adicione aqui as prints do sistema listando as motos e a tela do formulário de cadastro funcionando no seu navegador)

---

## 🎯 Objetivo

Projeto desenvolvido para automatizar e criar um CRUD (Create, Read, Update, Delete) rápido, organizando a entrada de serviços, o controle de dados dos clientes e os valores cobrados na oficina.

---

## 💡 Melhorias futuras

* [ ] Rota para edição (Update) dos dados caso a descrição do serviço mude
* [ ] Rota para deleção/arquivamento (Delete) de serviços já concluídos e pagos
* [ ] Controle de status do serviço (ex: "A Fazer", "Em Andamento", "Finalizado")
* [ ] Autenticação de administrador para proteger a página
* [ ] Dashboard simples mostrando o faturamento (soma de todos os preços)

---

## 📄 Licença

MIT

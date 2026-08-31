```markdown
# API de Cálculo e Gestão de Tratamento de Piscinas

API desenvolvida em **FastAPI** para cálculo automatizado de produtos químicos para tratamento de piscinas, com persistência de dados em banco **PostgreSQL** hospedado na AWS. O projeto conta com automação completa de CI/CD via **GitHub Actions** para instâncias **AWS EC2** e **Amazon ECR**.

---

## 🚀 Tecnologias Utilizadas

* **Python & FastAPI**: Criação da API assíncrona e documentação interativa.
* **SQLAlchemy & Pycopg2**: Mapeamento objeto-relacional (ORM) e conexão com banco de dados relacional.
* **PostgreSQL (AWS RDS)**: Banco de dados em nuvem para armazenamento do histórico de tratamentos.
* **Docker & Amazon ECR**: Empacotamento da aplicação em containers e armazenamento seguro de imagens.
* **AWS EC2 & GitHub Actions**: Pipeline de integração e entrega contínua (CI/CD) automatizada.

---

## 📂 Estrutura do Projeto

```text
api-piscina/
├── src/
│   ├── main.py            # Inicialização do FastAPI e rotas principais
│   └── database.py        # Configuração de conexão com o banco de dados
├── .github/
│   └── workflows/
│       └── deploy.yml     # Pipeline de CI/CD para deploy na AWS
├── requirements.txt       # Dependências do projeto Python
├── Dockerfile             # Configuração para containerização
└── README.md
```

---

## ⚙️ Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/api-piscina.git](https://github.com/SEU_USUARIO/api-piscina.git)
   cd api-piscina
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Mac/Linux:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure a variável de ambiente do banco de dados (SQLite local para testes):**
   ```bash
   # No Windows (PowerShell):
   $env:DATABASE_URL="sqlite:///./piscina.db"
   ```

5. **Inicie o servidor local:**
   ```bash
   uvicorn src.main:app --reload
   ```

6. **Acesse a documentação interativa:**
   Abra no navegador: `http://127.0.0.1:8000/docs`

---

## 🌐 Endpoints Principais

* `POST /api/piscina/calcular-e-salvar`: Recebe o volume de água em litros, calcula a quantidade exata de Cloro, Barrilha (Soda Ash) e Floculante necessários, e salva o registro no banco de dados.

---

## 🚀 Pipeline de CI/CD (GitHub Actions)

O projeto possui automação configurada na pasta `.github/workflows/deploy.yml`. A cada `git push` realizado na branch `main`:
1. O código é validado e empacotado em uma imagem **Docker**.
2. A imagem é enviada para o **Amazon ECR**.
3. O servidor **AWS EC2** via SSH atualiza a versão do container automaticamente, aplicando as novas alterações em tempo de execução com a base de dados integrada ao **AWS RDS**.

```

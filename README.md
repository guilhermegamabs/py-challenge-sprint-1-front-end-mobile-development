# Challenge Sprint 1: Fundamentos do Ativo e Interface de Cadastro

### FRONT END & MOBILE DEVELOPMENT

---

## Integrantes

| Nome | RM |
|---|---|
| Guilherme Gama | RM565293 |
| Bruno Fernandes Nascimento | RM552574 |
| Edgar Lódula de Assis | RM565260 |
| Júlia Aben-Athar | RM566325 |
| Igor Thiago Nakajima Vieira | RM563632 |

**Professor:** Lucas Tadeu Cunha Rios

---

Interface web desenvolvida em **Streamlit** para cadastro técnico e visualização de equipamentos industriais.

---

## Funcionalidades

| Tela | Descrição |
|---|---|
| **Consulta de Equipamentos** | Lista todos os equipamentos cadastrados com filtros por TAG, Modelo, Fabricante e Tensão. Permite selecionar um equipamento e acessar as demais telas. |
| **Novo Equipamento** | Formulário de cadastro com validação dos campos: TAG, Modelo, Fabricante, Potência e Tensão. |
| **Módulo Técnico** | Ficha técnica completa do equipamento selecionado, com opção de edição. |
| **Dados Brutos** | Visualização das leituras do ativo com conversão de sinais ADC para unidades de engenharia (Volts, Ampères, RPM), incluindo gráfico e estatísticas do período. |

---

## Estrutura do Projeto

```
py-challenge-sprint-1-front-end-mobile-development/
├── main.py                       
├── requirements.txt
├── .streamlit/
│   └── config.toml                
├── img/
│   └── logo-forzy-preta.svg       
└── app/
    ├── dados.py                   
    ├── componentes.py             
    ├── consulta_equipamentos.py
    ├── cadastro_equipamento.py
    ├── modulo_tecnico.py
    └── dados_brutos.py
```

---

## Como rodar localmente

### Pré-requisitos

- Python 3.11 ou superior
- pip

### Passos

**1. Clone o repositório**
```bash
git clone py-challenge-sprint-1-front-end-mobile-development.git
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Inicie o servidor**
```bash
streamlit run main.py
```

O app abre automaticamente em `http://localhost:8501`.

---

## Requisitos (Sprint 1)

- Tela de consulta com datatable e filtros
- Módulo de cadastro técnico (Modelo, Fabricante, Potência, Tensão, TAG)
- Visualização de dados brutos com conversão para unidades de engenharia
- Menu lateral (sidebar) estruturado para evolução nos próximos sprints
- Arquitetura desacoplada do backend
- Identidade visual alinhada à marca Forzy
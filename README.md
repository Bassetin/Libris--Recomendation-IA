# 📘 Libris – Sistema Inteligente de Recomendação de Livros

O **Libris** é uma aplicação desenvolvida por estudantes de Ciência da Computação com o objetivo de recomendar livros de forma personalizada, utilizando **Big Data**, **Machine Learning** e **Processamento de Linguagem Natural (NLP)**.  
O projeto busca incentivar o hábito da leitura por meio de sugestões inteligentes e adaptadas ao perfil de cada usuário.

---

## 🎯 Objetivo

Criar uma IA capaz de recomendar livros com base nos gostos, histórico de leitura e preferências do usuário, integrando dados públicos de APIs literárias e técnicas modernas de recomendação.

---

## 🧠 Problema e Solução

### ❌ Problema
Leitores frequentemente enfrentam dificuldade para escolher o próximo livro, seja por excesso de opções ou falta de direcionamento personalizado.

### ✅ Solução
O Libris oferece recomendações inteligentes e personalizadas, analisando dados reais de livros e comportamento do usuário para sugerir obras relevantes e alinhadas ao seu perfil.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Machine Learning:** `scikit-learn`, `LightFM`, `Surprise`
- **NLP:** `spaCy`, `nltk`, `transformers`
- **Interface:** `Streamlit` (protótipo rápido)
- **APIs:** [Google Books API](https://developers.google.com/books), [Open Library API](https://openlibrary.org/developers)
- **Banco de Dados:** `MongoDB` (opcional)
- **Outras:** `pandas`, `numpy`, `requests`

---

## 📁 Estrutura de Diretórios

```bash
libris/
├── README.md
├── requirements.txt
├── data/                 # Dados coletados
├── notebooks/            # Análises exploratórias
├── src/
│   ├── api/              # Scripts para acessar APIs de livros
│   ├── model/            # Algoritmos de recomendação
│   ├── nlp/              # Análise de sinopses e resenhas
│   └── interface/        # Interface com o usuário
└── docs/                 # Documentação do projeto
```
## 📦 requirements.txt

```txt
pandas
numpy
scikit-learn
lightfm
surprise
requests
streamlit
spacy
nltk
transformers
```
---

🚀 Como Rodar o Projeto
1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/Libris--Recomendation-IA.git
cd libris
```
2. Crie o ambiente virtual
```bash
python3 -m venv libris-env
source libris-env/bin/activate
```
3. Instale as dependências
```bash
pip install -r requirements.txt
```
4. Configure o NLP
```bash
python -m nltk.downloader all
python -m spacy download pt_core_news_sm
```
5. Execute a interface
```bash
streamlit run src/interface/app.py
```
---

📊 Fluxo de Funcionamento

- Coleta de Dados – Scripts em src/api/ acessam APIs como Google Books e Open Library.

- Processamento – Dados são limpos e armazenados em data/.

- Treinamento do Modelo – Algoritmos em src/model/ geram recomendações.

- Análise de Texto – src/nlp/ processa sinopses e resenhas.

- Interface – src/interface/ exibe as recomendações ao usuário

---

🤝 Como Contribuir

- Faça um fork do projeto

- Crie uma branch para sua feature (git checkout -b minha-feature)

- Commit suas alterações (git commit -m 'Adiciona nova feature')

- Envie para o repositório remoto (git push origin minha-feature)

- Abra um Pull Request

---
📜 Licença

Este projeto é de uso acadêmico e está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

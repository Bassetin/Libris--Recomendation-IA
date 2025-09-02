
---

## 📄 `docs/plano_projeto.md`


# 📘 Plano de Projeto – Libris

---

## 1. Visão Geral

O **Libris** é um sistema inteligente de recomendação de livros que utiliza dados de APIs públicas, técnicas de Machine Learning e NLP para sugerir obras personalizadas para cada usuário.

---

## 2. Objetivos

- Criar um sistema de recomendação híbrido (filtragem colaborativa + baseado em conteúdo).
- Integrar dados de fontes como Google Books e Open Library.
- Desenvolver uma interface simples e intuitiva.
- Incentivar o hábito da leitura.

---

## 3. Problema e Solução

**Problema:**  
Leitores têm dificuldade em escolher o próximo livro devido ao excesso de opções.

**Solução:**  
Oferecer recomendações personalizadas com base no histórico e preferências do usuário, usando IA para filtrar e priorizar opções relevantes.

---

## 4. Escopo do MVP

- Cadastro de usuário e preferências.
- Coleta de dados de livros via API.
- Algoritmo básico de recomendação.
- Interface inicial com Streamlit.

---

## 5. Tecnologias

- **Linguagem:** Python 3.10+
- **Machine Learning:** scikit-learn, LightFM, Surprise
- **NLP:** spaCy, nltk, transformers
- **Interface:** Streamlit
- **Banco de Dados:** MongoDB (opcional)
- **APIs:** Google Books API, Open Library API

---

## 6. Estrutura de Equipe

| Membro | Função | Responsabilidades |
|--------|--------|-------------------|
| Lucas  | Coleta de dados | Integração com APIs, limpeza e armazenamento |
| Dev 2  | IA de recomendação | Modelagem e treinamento |
| Dev 3  | NLP | Análise de sinopses e resenhas |
| Dev 4  | Interface | Desenvolvimento da UI e integração |

---

## 7. Cronograma (8 semanas)

| Semana | Atividade |
|--------|-----------|
| 1–2    | Definição do escopo e coleta de dados |
| 3–4    | Treinamento do modelo de recomendação |
| 5–6    | Desenvolvimento da interface |
| 7      | Integração e testes |
| 8      | Apresentação final |

---

## 8. Entregáveis

- Código-fonte no GitHub
- Documentação técnica
- Protótipo funcional
- Relatório final

---

## 9. Métricas de Sucesso

- Precisão das recomendações (Precision/Recall)
- Feedback positivo de usuários-teste
- Interface funcional e responsiva

---

## 10. Próximos Passos

- Implementar melhorias no algoritmo
- Adicionar mais fontes de dados
- Criar versão mobile

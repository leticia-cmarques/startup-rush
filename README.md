# Startup Rush

Aplicação em **Flask** que simula um torneio entre startups.  
É possível cadastrar de **4 a 8 startups**, cada uma com nome, slogan e ano de fundação, e colocá-las para batalhar em rodadas até restar uma campeã.  
Ao final, é exibido um **ranking** com a pontuação de cada startup.

---

## 🚀 Tecnologias usadas
- Python 3.12
- Flask
- HTML5 e CSS3

---

## ⚙️ Instalação
1. Clone ou baixe este repositório.  
2. Crie um ambiente virtual (recomendado) ou use Conda.  
3. Instale as dependências:  
   ```bash
   pip install flask
   ```
 
---
  
## ▶️ Como executar
1. Execute o projeto:  
   ```bash
   python app.py
   ```
2. Abra no navegador:  
   ```
   http://127.0.0.1:5000
   ```

---

## 📂 Estrutura do projeto
```bash
Startup-Rush/
├── templates/            # páginas HTML
│   ├── batalhas.html     # batalhas entre startups
│   ├── cadastro.html     # cadastro das startups
│   ├── evento.html       # eventos positivos/negativos
│   ├── index.html        # página inicial
│   ├── ranking.html      # ranking de startups
│   └── resultado.html    # resultado final
├── app.py                # aplicação principal em Flask
└── README.md             # documentação do projeto
```

---

## 🏆 Funcionalidades
- Cadastro de startups (mínimo 4 e máximo 8).  
- Simulação de batalhas em rodadas.  
- Eventos que alteram a pontuação das startups.  
- Ranking final com exibição da startup campeã.  
```
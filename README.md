
# 🎧 DJ Playlist API — construindo a setlist perfeita (Flask)

Você foi contratado por um **DJ profissional** para desenvolver uma **API de playlist** que o ajude a **organizar e testar setlists** antes dos shows.  
A ideia é simples e real: ele quer **cadastrar músicas**, **listar**, **ajustar informações** e **remover faixas** enquanto experimenta a ordem e o repertório.

Este mini-projeto usa **Flask** (Python) e foi pensado para estudantes do **ensino médio** que estão dando os primeiros passos com **APIs REST**, **JSON**, **rotas** e **métodos HTTP** — com linguagem acessível e um toque de música. 🎶

---

## 🎬 Enunciado — A missão do dev
O DJ (seu cliente!) está com a agenda cheia e precisa **ganhar tempo** organizando as faixas do set. Ele quer:

1. **Listar** todas as músicas já cadastradas na playlist;  
2. **Adicionar** novas músicas enquanto pesquisa repertório;  
3. **Atualizar** informações (ex.: título, artista, duração ou link da faixa);  
4. **Deletar** músicas que não funcionaram bem nos testes.

Seu trabalho é **construir uma API** que exponha esses recursos de forma clara e padronizada, retornando **JSON** em todas as respostas.

> **Spoiler de evolução**: Em versões futuras, o DJ quer organizar por **BPM**, **gênero** e **“energia”** da música. Este MVP foca no CRUD para consolidar a base — depois dá pra evoluir. 😉

---

## 🧠 Objeto de domínio: `Música`
Cada música é um JSON com o seguinte formato:

```json
{
  "id": 1,
  "titulo": "Astronomia",
  "artista": "Tony Igy",
  "duracao": 236,
  "url": "https://example.com/tony-igy-astronomia"
}
```
- `id` (int): gerado automaticamente pela API  
- `titulo` (str): **obrigatório**  
- `artista` (str): **obrigatório**  
- `duracao` (int, em segundos): **obrigatório** (ex.: 3m56s → 236)  
- `url` (str): opcional (link de referência/stream)

---

## 🚦 Rotas (CRUD)
| Método | Rota              | Descrição                                   | Corpo (JSON)                                             | Códigos |
|-------:|-------------------|----------------------------------------------|----------------------------------------------------------|--------:|
| GET    | `/tracks`         | Lista todas as músicas                       | –                                                        | 200     |
| GET    | `/tracks/<id>`    | Busca uma música por `id`                    | –                                                        | 200/404 |
| POST   | `/tracks`         | Adiciona nova música                         | `{ "titulo", "artista", "duracao", "url?" }`             | 201/400 |
| PUT    | `/tracks/<id>`    | Atualiza **parcialmente** uma música         | Subconjunto de `{ "titulo","artista","duracao","url" }`  | 200/400/404 |
| DELETE | `/tracks/<id>`    | Remove uma música                            | –                                                        | 204/404 |
| GET    | `/health`         | Verifica se a API está ativa                 | –                                                        | 200     |

> Observação: o `PUT` aqui aceita **atualização parcial** (comportamento de `PATCH`).

---

## ✅ Critérios de aceitação (checklist do DJ)
- [ ] As rotas acima funcionam e retornam **JSON** bem formatado  
- [ ] Campos obrigatórios validados no `POST` (`titulo`, `artista`, `duracao`)  
- [ ] `id` é **gerado** pela API e não enviado pelo cliente  
- [ ] Mensagens de erro claras (`400` para payload inválido; `404` para não encontrado)  
- [ ] `DELETE` retorna **204** (sem corpo) quando funciona  
- [ ] Projeto roda com `python app.py` e tem `requirements.txt`

---

## 💻 Como rodar

**Pré-requisito:** Python **3.10+**

```bash
# 1) (Opcional) Ambiente virtual
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Instalar dependências
pip install -r requirements.txt

# 3) Iniciar a API
python app.py
# ou:
# flask --app app:app run --reload

# Teste rápido:
curl -s http://127.0.0.1:5000/health
```

---

## 🔎 Exemplos rápidos com `curl`

Listar músicas:
```bash
curl -s http://127.0.0.1:5000/tracks | jq
```

Criar música:
```bash
curl -s -X POST http://127.0.0.1:5000/tracks   -H "Content-Type: application/json"   -d '{"titulo":"Blue Bird","artista":"Ikimono-gakari","duracao":228,"url":"https://exemplo.com/blue-bird"}' | jq
```

Buscar por id:
```bash
curl -s http://127.0.0.1:5000/tracks/1 | jq
```

Atualizar parcialmente:
```bash
curl -s -X PUT http://127.0.0.1:5000/tracks/1   -H "Content-Type: application/json"   -d '{"titulo":"Blue Bird (Remaster)"}' | jq
```

Deletar:
```bash
curl -i -X DELETE http://127.0.0.1:5000/tracks/1
```

---

## 🧠 Conceitos trabalhados
- HTTP e métodos **GET/POST/PUT/DELETE**  
- **JSON** como formato de troca de dados  
- Rotas e handlers com **Flask**  
- **Validação** básica e **códigos de status**  
- Testes com o **client de testes do Flask**

---

## 🚀 Próximos passos (para evoluir)
- Adicionar **bpm**, **gênero** e **energia**  
- Filtros por artista/gênero/duração  
- Paginação em `/tracks`  
- Persistência real (SQLite) no lugar da lista em memória  
- CORS + um **frontend** simples para consumir a API

---

## 📂 Estrutura sugerida
```
flask-playlist-api/
├─ app.py
├─ requirements.txt
├─ README.md
├─ tests/
│  └─ test_app.py
├─ .gitignore
└─ LICENSE
```

---

## 📝 Licença
Projeto sob **MIT** — use, adapte e compartilhe. 🎵✨

## Visão geral

GRUPO: Adryan & Luciano

Individualmente ou em dupla, vocês vão construir uma **API em Django** que salva registros no banco de dados e um **app em Flet** que usa essa API para listar, cadastrar, editar e excluir. O trabalho é a **segunda nota** da disciplina, e não haverá prova.

- **Formato:** individual ou em dupla, à escolha de cada um. O tema é o mesmo para todos: Biblioteca.
- **Base:** o projeto `loja` das aulas é o modelo. O trabalho aplica o mesmo caminho à biblioteca.
- **Entrega e defesa:** 01/12, em aula. Cada trabalho é apresentado funcionando, e quem fez responde por ele.

## Tema: Biblioteca

Todos fazem o mesmo tema: o acervo de uma biblioteca. O Model `Livro` deve ter **de 4 a 6 campos**, com pelo menos um texto, um número e um campo do tipo sim/não. Os campos abaixo são uma sugestão; acrescentar campos próprios é bem-vindo.

| Campo | Tipo no Django | Exemplo |
| --- | --- | --- |
| titulo | CharField | Dom Casmurro |
| autor | CharField | Machado de Assis |
| ano | PositiveIntegerField | 1899 |
| disponivel | BooleanField | sim |
| paginas (opcional) | PositiveIntegerField | 256 |

## Requisitos da API (Django)

A API guarda os registros num **Model** (uma tabela no banco SQLite) e responde sempre em **JSON**. As rotas usam o recurso `livros`.

| Método | Rota | O que faz | Sucesso |
| --- | --- | --- | --- |
| GET | `/livros/` | Lista todos os registros | 200 |
| GET | `/livros/?busca=python` | Lista só os que atendem ao filtro | 200 |
| GET | `/livros/<id>/` | Mostra um registro | 200 |
| POST | `/livros/` | Cadastra um registro com os dados enviados em JSON | 201 |
| PUT | `/livros/<id>/` | Altera um registro com os dados enviados em JSON | 200 |
| DELETE | `/livros/<id>/` | Exclui um registro | 204 |

Além das rotas, a API precisa:

- **Ter pelo menos um filtro** pela URL, como busca por texto ou só os disponíveis.
- **Validar o que recebe:** campos obrigatórios preenchidos e valores que fazem sentido (por exemplo, preço maior que zero). Quando algo falha, responde **400** com `{"erro": "mensagem explicando o problema"}`.
- **Responder 404** quando o id pedido não existe, também com `{"erro": "..."}`.
- **Começar com dados:** pelo menos 5 registros cadastrados antes da defesa.

## Requisitos do app (Flet)

O app não guarda dados: tudo o que ele mostra vem da API, e tudo o que ele muda vai para a API, usando a biblioteca `requests`.

- **Listar:** mostra os registros vindos de `GET`, com os campos principais de cada um.
- **Filtrar:** usa o filtro da API, por exemplo um campo de busca.
- **Cadastrar e editar:** um formulário que envia `POST` (novo) ou `PUT` (edição) e atualiza a lista em seguida.
- **Excluir:** pede confirmação antes de enviar `DELETE`.
- **Tratar erros:**
  - servidor desligado: o app avisa, em vez de travar ou fechar;
  - erro 400: mostra ao usuário a mensagem que a API devolveu;
  - erro 404: avisa que o registro não existe mais.

## Cronograma

Cada aula ensina a parte que a dupla aplica no próprio tema até a aula seguinte. As etapas servem para orientar e não valem nota.

## Entrega

Até o início da aula de 01/12, um arquivo `.zip` com o seu nome (ou os nomes da dupla), contendo:

- `api/`: o projeto Django, com o `db.sqlite3` (para os registros irem junto) e o `requirements.txt`;
- `app/`: o app Flet;
- `README.md`: o nome de quem fez, a lista de rotas da API e como rodar os dois projetos.

Não envie a pasta `.venv`: ela é grande e não funciona em outro computador.

Criar um repositório no Github compartilhado com lucas.pires@vacaria.ifrs.edu.br desde o início do projeto e salvar lá o andamento no Projeto. Não serão aceitos commits de códigos inteiros.

## Avaliação

O trabalho vale de 0 a 10. Em dupla, a nota é a mesma para os dois.

| Critério | Pontos |
| --- | --- |
| API: rotas de leitura (lista, um registro, filtro) | 2,0 |
| API: POST, PUT e DELETE salvando no banco | 2,0 |
| API: validação e códigos de status corretos | 2,0 |
| Flet: listar, filtrar e excluir com confirmação | 1,5 |
| Flet: formulário de cadastro e edição | 1,5 |
| Flet: tratamento de erros | 1,0 |
| **Total** | **10,0** |

## Defesa (01/12)

Cada trabalho tem 10 minutos:

1. **Demonstração (4 min):** listar, filtrar, cadastrar, editar, excluir e provocar um erro, nessa ordem.
2. **Perguntas (6 min):** quem fez explica partes do código escolhidas na hora. Por exemplo: o que uma rota faz, por que a API responde 400 em certo caso, como o app envia os dados para a API.

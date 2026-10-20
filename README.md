# Projeto Biblioteca — API Django e App Flet

> **Segunda nota da disciplina · Valor: 10,0 pontos · Entrega e defesa: 01/12, em aula**

## Visão geral

Individualmente ou em dupla, desenvolvam uma **API em Django** que salve registros no banco de dados e um **app em Flet** que consuma essa API para listar, cadastrar, editar e excluir livros.

- **Formato:** individual ou em dupla, à escolha dos estudantes.
- **Tema:** acervo de uma biblioteca, igual para todos.
- **Base:** projeto `loja`, desenvolvido nas aulas. O trabalho aplica o mesmo caminho ao tema Biblioteca.
- **Avaliação:** o trabalho corresponde à segunda nota da disciplina. Não haverá prova.
- **Apresentação:** o projeto deve ser demonstrado funcionando, e quem o desenvolveu deve responder às perguntas sobre o código.

## 1. Modelo de dados

O Model `Livro` deve ter **de 4 a 6 campos**, incluindo pelo menos:

- Um campo de texto;
- Um campo numérico;
- Um campo do tipo sim/não.

Os campos abaixo são sugestões. Acrescentar campos próprios é bem-vindo.

| Campo | Tipo no Django | Exemplo | Observação |
| --- | --- | --- | --- |
| `titulo` | `CharField` | Dom Casmurro | Texto |
| `autor` | `CharField` | Machado de Assis | Texto |
| `ano` | `PositiveIntegerField` | 1899 | Número |
| `disponivel` | `BooleanField` | Sim | Sim/não |
| `paginas` | `PositiveIntegerField` | 256 | Opcional |

## 2. Requisitos da API — Django

A API deve armazenar os registros em um **Model**, usando uma tabela no banco **SQLite**, e responder em **JSON**. As rotas devem usar o recurso `livros`.

### Rotas obrigatórias

| Método | Rota | Funcionalidade | Status de sucesso |
| --- | --- | --- | --- |
| `GET` | `/livros/` | Listar todos os registros | `200` |
| `GET` | `/livros/?busca=python` | Listar os registros que atendem ao filtro | `200` |
| `GET` | `/livros/<id>/` | Consultar um registro | `200` |
| `POST` | `/livros/` | Cadastrar um registro com os dados enviados em JSON | `201` |
| `PUT` | `/livros/<id>/` | Alterar um registro com os dados enviados em JSON | `200` |
| `DELETE` | `/livros/<id>/` | Excluir um registro | `204` |

### Filtros

Implementar **pelo menos um filtro pela URL**, como busca por texto ou listagem apenas dos livros disponíveis.

### Validação e erros

- Validar os campos obrigatórios e os valores recebidos, garantindo que façam sentido.
- Quando a validação falhar, responder com **status `400`** e uma mensagem explicando o problema:

```json
{
  "erro": "Mensagem explicando o problema"
}
```

- Quando o ID solicitado não existir, responder com **status `404`**, também no formato:

```json
{
  "erro": "Registro não encontrado"
}
```

### Dados iniciais

O banco deve conter **pelo menos 5 registros cadastrados antes da defesa**.

## 3. Requisitos do app — Flet

O app **não deve guardar dados**: tudo o que exibe deve vir da API, e todas as alterações devem ser enviadas à API usando a biblioteca **`requests`**.

| Funcionalidade | Requisito |
| --- | --- |
| **Listar** | Exibir os registros obtidos por `GET`, mostrando os campos principais de cada livro. |
| **Filtrar** | Usar o filtro da API, por exemplo, por meio de um campo de busca. |
| **Cadastrar** | Enviar os dados de um formulário por `POST` e atualizar a lista em seguida. |
| **Editar** | Enviar os dados de um formulário por `PUT` e atualizar a lista em seguida. |
| **Excluir** | Pedir confirmação antes de enviar `DELETE`. |

### Tratamento de erros

| Situação | Comportamento esperado |
| --- | --- |
| Servidor desligado | Avisar o usuário, sem travar ou fechar o app. |
| Erro `400` | Mostrar ao usuário a mensagem devolvida pela API. |
| Erro `404` | Avisar que o registro não existe mais. |

## 4. Cronograma

Cada aula ensina uma parte que os estudantes devem aplicar ao próprio projeto até a aula seguinte.

As etapas servem para orientar o desenvolvimento e **não valem nota**.

## 5. Repositório no GitHub

- Criar um repositório **desde o início do projeto**.
- Compartilhar o repositório com **lucas.pires@vacaria.ifrs.edu.br**.
- Salvar o andamento do projeto no repositório, registrando sua evolução.
- **Não serão aceitos commits de códigos inteiros.**

## 6. Entrega

**Prazo:** até o início da aula de **01/12**.

Entregar um arquivo **`.zip`**, identificado com o nome do estudante ou com os nomes da dupla, contendo:

```text
Nome_do_estudante_ou_dupla.zip
├── api/
│   ├── ... projeto Django
│   ├── db.sqlite3
│   └── requirements.txt
├── app/
│   └── ... app Flet
└── README.md
```

| Item | Conteúdo obrigatório |
| --- | --- |
| `api/` | Projeto Django, banco `db.sqlite3` com os registros e `requirements.txt`. |
| `app/` | Código do app Flet. |
| `README.md` | Nome de quem desenvolveu, lista de rotas da API e instruções para executar os dois projetos. |

> **Não incluir a pasta `.venv`.** Ela é grande e não funciona em outro computador.

[Enviar o trabalho no Moodle](https://moodle.vacaria.ifrs.edu.br/mod/assign/view.php?id=114804)

## 7. Avaliação

O trabalho vale **de 0 a 10**. Em dupla, a nota é a mesma para os dois integrantes.

| Critério | Pontuação |
| --- | ---: |
| API: rotas de leitura — lista, consulta de um registro e filtro | 2,0 |
| API: `POST`, `PUT` e `DELETE` salvando no banco | 2,0 |
| API: validação e códigos de status corretos | 2,0 |
| Flet: listar, filtrar e excluir com confirmação | 1,5 |
| Flet: formulário de cadastro e edição | 1,5 |
| Flet: tratamento de erros | 1,0 |
| **Total** | **10,0** |

## 8. Defesa — 01/12

Cada trabalho terá **10 minutos** de apresentação.

### Demonstração — 4 minutos

Demonstrar as ações **nesta ordem**:

1. Listar os livros.
2. Filtrar os registros.
3. Cadastrar um livro.
4. Editar um livro.
5. Excluir um livro.
6. Provocar um erro e mostrar seu tratamento.

### Perguntas — 6 minutos

Quem desenvolveu o trabalho deverá explicar partes do código escolhidas na hora. Exemplos de perguntas:

- O que determinada rota faz?
- Por que a API responde `400` em certo caso?
- Como o app envia os dados para a API?

## Links de referência

- [Entrega no Moodle](https://moodle.vacaria.ifrs.edu.br/mod/assign/view.php?id=114804)
- [Códigos das aulas](https://moodle.vacaria.ifrs.edu.br/mod/resource/view.php?id=113220)

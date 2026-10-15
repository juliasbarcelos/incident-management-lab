# Laboratório Python — Investigação do INC-002

## 1. Objetivo

Este laboratório integra o projeto **Incident Management Lab**, desenvolvido para demonstrar competências práticas de Suporte Aplicacional.

O objetivo foi reproduzir uma falha simulada de autorização, analisar os logs gerados durante a execução, testar uma alteração de permissões e validar o controlo de acesso num ambiente local.

O laboratório complementa a investigação documentada no ticket **INC-002 — Falha de acesso à aplicação**.

> **Nota:** Este projeto utiliza dados e utilizadores fictícios. Os programas foram efetivamente executados em ambiente local, mas a autenticação e as respostas HTTP são simuladas.

---

## 2. Cenário do incidente

**Ticket:** INC-002 — Falha de acesso à aplicação

**Empresa:** Comércio Digital PT (fictícia)

**Utilizadora:** Ana Martins (fictícia)

**Departamento:** Financeiro

**Aplicação:** Gestão de Encomendas

**Problema:** Erro HTTP 500 durante o processo de acesso.

No cenário empresarial fictício, uma colaboradora do departamento financeiro não conseguia aceder à aplicação de Gestão de Encomendas.

Durante a investigação, foi formulada uma hipótese relacionada com a alteração recente do perfil da utilizadora e com possíveis inconsistências nas permissões.

Para estudar essa hipótese, foi desenvolvido um laboratório Python capaz de simular o comportamento identificado.

---

## 3. Tecnologias utilizadas

- **Python 3** — desenvolvimento e execução dos programas.
- **Visual Studio Code** — edição, execução e análise dos ficheiros.
- **Biblioteca logging** — geração de registos técnicos.
- **Pathlib** — organização dos caminhos e diretórios.
- **Git/GitHub** — controlo de versões através de commits realizados na interface web do GitHub.

Não foram utilizadas bibliotecas Python externas.

---

## 4. Estrutura do laboratório

```text
laboratorio-python/
├── app_falha.py
├── app_corrigida.py
├── app_validacao.py
├── logs/
│   ├── exemplo-auth.log
│   └── validacao-auth.log
└── README.md
```

### Descrição dos ficheiros

| Ficheiro | Finalidade |
|---|---|
| `app_falha.py` | Reproduzir a falha simulada de autorização |
| `app_corrigida.py` | Testar a alteração das permissões |
| `app_validacao.py` | Validar o controlo de acesso com dois utilizadores |
| `logs/exemplo-auth.log` | Apresentar registos da falha e da correção |
| `logs/validacao-auth.log` | Apresentar os resultados dos testes de controlo de acesso |
| `README.md` | Documentar o funcionamento e os resultados do laboratório |

Os programas também podem gerar ficheiros locais adicionais de log durante a execução.

---

## 5. Reprodução da falha

### 5.1. Configuração inicial

O ficheiro [`app_falha.py`](app_falha.py) representa a configuração inicial do ambiente de teste.

A utilizadora fictícia possui o perfil `Financeiro_Restrito` e apenas a permissão:

```python
permissoes = ["reports.read"]
```

O programa verifica se existe a permissão `orders.read`, necessária para a operação simulada de consulta de encomendas.

Como essa permissão não está presente, o programa regista uma falha de autorização.

### 5.2. Execução

Abrir o terminal na pasta `laboratorio-python` e executar:

```bash
python app_falha.py
```

### 5.3. Resultado esperado

```text
Erro 500 — Internal Server Error (simulado)
```

### 5.4. Análise inicial

Durante a execução, foram registados os seguintes eventos:

- Pedido de login recebido.
- Autenticação simulada bem-sucedida.
- Falha na validação de permissões.
- Identificação do perfil `Financeiro_Restrito`.
- Ausência da permissão `orders.read`.
- Registo da mensagem HTTP 500 simulada.

O erro reproduzido pertence à lógica programada no laboratório e não corresponde a uma resposta de um servidor HTTP real.

---

## 6. Análise dos logs

O Python foi configurado para guardar os eventos num ficheiro de log utilizando a biblioteca `logging`.

### Registos da execução inicial

```text
2026-10-15 18:32:10 INFO Login request received | user=ana.martins
2026-10-15 18:32:10 INFO Authentication successful | user=ana.martins
2026-10-15 18:32:10 ERROR Permission validation failed
2026-10-15 18:32:10 ERROR Role: Financeiro_Restrito
2026-10-15 18:32:10 ERROR Missing permission: orders.read
2026-10-15 18:32:10 ERROR HTTP 500 returned (simulated)
```

### Interpretação técnica

**Authentication successful**

Indica que a etapa de autenticação simulada foi concluída.

**Permission validation failed**

Indica que ocorreu uma falha na verificação das permissões.

**Missing permission: orders.read**

Identifica a autorização ausente na configuração utilizada.

**HTTP 500 returned (simulated)**

Representa a mensagem de erro programada para o cenário de teste.

### Conclusão preliminar

Os logs demonstraram que a ausência da permissão `orders.read` estava associada à falha programada no laboratório.

A análise permitiu distinguir uma falha de autenticação de uma falha de autorização.

Os registos selecionados estão disponíveis em:

[Consultar exemplo-auth.log](logs/exemplo-auth.log)

---

## 7. Teste de correção

### 7.1. Objetivo

Verificar se a inclusão da permissão `orders.read` permite concluir a validação de autorização.

### 7.2. Alteração realizada

O ficheiro [`app_corrigida.py`](app_corrigida.py) contém a configuração utilizada no segundo teste.

**Configuração inicial:**

```python
permissoes = ["reports.read"]
```

**Configuração corrigida:**

```python
permissoes = ["reports.read", "orders.read"]
```

A alteração foi realizada exclusivamente no ambiente local de laboratório.

### 7.3. Execução

```bash
python app_corrigida.py
```

### 7.4. Resultado obtido

```text
Acesso autorizado
```

O programa também registou:

```text
INFO Access granted
```

### 7.5. Conclusão do teste

Após a inclusão da permissão necessária, o programa passou a autorizar o acesso.

A comparação entre as duas versões demonstrou que a configuração das permissões era responsável pelo comportamento observado no laboratório.

**Resultado:** Correção validada no ambiente local de simulação.

---

## 8. Validação adicional do controlo de acesso

Após testar a correção, foi desenvolvido o ficheiro [`app_validacao.py`](app_validacao.py).

O objetivo foi verificar se a lógica implementada distinguia corretamente utilizadores com e sem a permissão necessária.

### 8.1. Cenários testados

| Utilizador fictício | Permissões | Resultado esperado |
|---|---|---|
| Ana Martins | `reports.read`, `orders.read` | Acesso autorizado |
| Bruno Costa | `reports.read` | Acesso negado |

### 8.2. Execução

```bash
python app_validacao.py
```

### 8.3. Resultado obtido

```text
ana.martins: Acesso autorizado
bruno.costa: Acesso negado — 403 simulado
```

### 8.4. Interpretação

**Ana Martins**

A utilizadora possui a permissão `orders.read`, pelo que a operação simulada foi autorizada.

**Bruno Costa**

O utilizador não possui a permissão necessária, pelo que o programa negou o acesso.

Neste segundo cenário, foi utilizada uma mensagem HTTP 403 simulada para representar a negação de acesso por falta de autorização.

A aplicação não implementa um servidor HTTP real.

### 8.5. Logs da validação

Os registos foram guardados em:

[Consultar validacao-auth.log](logs/validacao-auth.log)

Os logs incluem:

- Pedido de login.
- Autenticação simulada.
- Verificação de autorização.
- Acesso autorizado para Ana Martins.
- Acesso negado para Bruno Costa.
- Mensagem HTTP 403 simulada.

**Resultado:** Ambos os cenários apresentaram o comportamento esperado.

---

## 9. Comparação dos testes

| Teste | Configuração | Resultado |
|---|---|---|
| Falha inicial | Sem `orders.read` | Erro 500 simulado |
| Correção | Com `orders.read` | Acesso autorizado |
| Validação — Ana | Com `orders.read` | Acesso autorizado |
| Validação — Bruno | Sem `orders.read` | Acesso negado — 403 simulado |

Os resultados permitiram validar a lógica implementada no programa e demonstrar a importância da verificação das permissões.

---

## 10. Competências técnicas praticadas

O desenvolvimento deste laboratório permitiu praticar:

### Python

- Criação e execução de scripts.
- Utilização de funções.
- Utilização de condições `if`.
- Manipulação de listas e dicionários.
- Organização de ficheiros e diretórios.

### Investigação técnica

- Reprodução controlada de falhas.
- Análise e interpretação de logs.
- Identificação de mensagens de erro.
- Formulação e validação de hipóteses.
- Comparação de resultados antes e depois de uma alteração.

### Controlo de acesso

- Diferença entre autenticação e autorização.
- Verificação de permissões.
- Negação de acesso sem autorização.
- Conceito do princípio do menor privilégio.

### Documentação

- Organização de evidências.
- Registo de procedimentos.
- Documentação técnica em Markdown.
- Publicação de código no GitHub.
- Controlo de versões por commits.

---

## 11. Limitações do laboratório

Este laboratório foi desenvolvido exclusivamente para fins educativos.

É importante considerar que:

- Os utilizadores e os dados são fictícios.
- A autenticação é simulada.
- Não existe uma base de dados de utilizadores.
- As permissões são definidas diretamente no código.
- Não existe um servidor HTTP real.
- As mensagens HTTP 500 e HTTP 403 são simuladas.
- Os testes não foram realizados numa aplicação empresarial.
- A alteração das permissões não representa uma intervenção num sistema de produção.

Os ficheiros de log foram efetivamente gerados durante a execução dos programas Python no computador.

Contudo, esses registos demonstram o comportamento do código desenvolvido para o exercício, não a causa raiz de um incidente real.

---

## 12. Relação com o Incident Management Lab

Este laboratório complementa o ticket **INC-002 — Falha de acesso à aplicação**, documentado no projeto principal.

O cenário incluiu:

1. Abertura e classificação do incidente.
2. Comunicação simulada com a utilizadora.
3. Formulação de hipóteses técnicas.
4. Consulta de incidentes conhecidos fictícios.
5. Desenvolvimento do laboratório Python.
6. Geração e análise de logs.
7. Teste da alteração de permissões.
8. Validação adicional de controlo de acesso.
9. Documentação da resolução simulada.
10. Análise de SLA e encerramento fictício.

O laboratório foi concluído sem escalonamento para outra equipa.

A causa da falha foi identificada e validada no programa de teste. Não foi possível comprovar de forma independente a causa raiz do incidente empresarial fictício.

---

## 13. Documentação complementar

- [README principal — Incident Management Lab](../README.md)
- [Código — Falha inicial](app_falha.py)
- [Código — Versão corrigida](app_corrigida.py)
- [Código — Validação adicional](app_validacao.py)
- [Logs — Falha e correção](logs/exemplo-auth.log)
- [Logs — Controlo de acesso](logs/validacao-auth.log)
- [Evidências visuais do projeto](../evidencias/)

---

**Projeto desenvolvido para fins de aprendizagem e demonstração de competências em Suporte Aplicacional.**

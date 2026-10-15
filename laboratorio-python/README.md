# Laboratório Python — Investigação do INC-002

## 1. Objetivo

Este laboratório integra o projeto Incident Management Lab, desenvolvido para demonstrar competências práticas de Suporte Aplicacional.

O objetivo foi reproduzir uma falha simulada de autorização, analisar os logs gerados durante a execução e testar uma alteração de permissões num ambiente local controlado.

## 2. Cenário do incidente

**Ticket:** INC-002 — Falha de acesso à aplicação

**Empresa:** Comércio Digital PT (fictícia)

**Utilizadora:** Ana Martins (fictícia)

**Aplicação:** Gestão de Encomendas

**Problema:** Erro HTTP 500 durante o processo de acesso.

Durante a investigação simulada, foi identificada uma possível relação entre a configuração das permissões e a falha apresentada.

Para estudar essa hipótese, foi desenvolvido um pequeno programa em Python.

## 3. Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Biblioteca logging do Python
- Git e GitHub para documentação e versionamento

## 4. Estrutura do laboratório

```text
laboratorio-python/
├── app_falha.py
├── app_corrigida.py
├── logs/
│   └── exemplo-auth.log
└── README.md
```

## 5. Reprodução da falha

O ficheiro `app_falha.py` simula uma utilizadora com o perfil Financeiro_Restrito.

A configuração inicial contém apenas a permissão:

```python
permissoes = ["reports.read"]
```

Como a aplicação exige `orders.read` para consultar encomendas, o programa regista uma falha na verificação de autorização.

### Executar

No terminal, dentro da pasta laboratorio-python:

```bash
python app_falha.py
```

**Resultado esperado:**

```text
Erro 500 — Internal Server Error (simulado)
```

Os detalhes são registados no ficheiro `logs/application-auth.log`.

## 6. Teste da correção

O ficheiro `app_corrigida.py` representa a segunda versão do laboratório.

A configuração passa a incluir:

```python
permissoes = ["reports.read", "orders.read"]
```

### Executar

```bash
python app_corrigida.py
```

**Resultado esperado:**

```text
Acesso autorizado
```

## 7. Análise dos logs

Os registos produzidos durante os testes demonstraram dois comportamentos.

### Antes da alteração

- Autenticação simulada bem-sucedida.
- Falha na validação de permissões.
- Ausência da permissão `orders.read`.
- Registo de erro HTTP 500 simulado.

### Depois da alteração

- Autenticação simulada bem-sucedida.
- Permissão necessária presente.
- Registo `Access granted`.
- Mensagem de acesso autorizado no terminal.

Os exemplos selecionados estão disponíveis em [exemplo-auth.log](logs/exemplo-auth.log).

## 8. Resultados

O teste demonstrou que a ausência da permissão `orders.read` provoca a falha programada no ambiente de laboratório.

Após adicionar essa permissão, a aplicação simulada passou a autorizar o acesso.

A experiência permitiu praticar:

- Execução de programas Python.
- Configuração de permissões simuladas.
- Geração e interpretação de logs.
- Formulação e validação de hipóteses técnicas.
- Comparação entre comportamentos antes e depois de uma alteração.
- Documentação e versionamento de código no GitHub.

## 9. Limitações do laboratório

Este projeto utiliza dados fictícios e não está ligado a sistemas empresariais reais.

A autenticação é simulada, não existe uma base de dados de utilizadores e o programa não implementa um servidor HTTP.

A mensagem HTTP 500 é produzida pelo próprio código e não corresponde a uma resposta HTTP efetiva.

Assim, os resultados demonstram o comportamento do programa de teste, não uma correção validada numa aplicação empresarial real.

## 10. Relação com o Incident Management Lab

O laboratório complementa a investigação documentada no ticket INC-002, incluindo a análise técnica, o teste controlado e a preparação do escalonamento.

As evidências visuais e o relatório completo do incidente serão apresentados no README principal do repositório.

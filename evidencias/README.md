# Evidências — Incident Management Lab

## Sobre esta pasta

Esta pasta reúne as evidências visuais do Projeto 2 — Incident Management Lab, desenvolvido para demonstrar competências práticas de Suporte Aplicacional.

As capturas documentam as diferentes etapas do incidente INC-002 — Falha de acesso à aplicação, desde o registo inicial até ao encerramento.

O cenário empresarial, os utilizadores, as comunicações e os indicadores de SLA são fictícios.

Os testes Python foram efetivamente executados num ambiente local, utilizando dados simulados.

---

## 1. Registo inicial do incidente

**Ficheiro:** `INC-002_01_Registo_Inicial.png`

Demonstra a criação do ticket INC-002 no Notion, com o estado inicial Novo.

[Visualizar evidência](INC-002_01_Registo_Inicial.png)

## 2. Classificação do incidente

**Ficheiro:** `INC-002_02_Classificacao.png`

Apresenta a classificação inicial do incidente:

- Impacto: Baixo
- Urgência: Média
- Prioridade: P3 — Média
- Estado: Em análise

[Visualizar evidência](INC-002_02_Classificacao.png)

## 3. Comunicação com a utilizadora

**Ficheiro:** `INC-002_03_Comunicacao.png`

Documenta o contacto fictício com a utilizadora para recolha de informações, avaliação do impacto e identificação das necessidades do departamento financeiro.

[Visualizar evidência](INC-002_03_Comunicacao.png)

## 4. Documentação inicial

**Ficheiro:** `INC-002_04_Documentacao.png`

Apresenta a organização inicial da documentação do incidente no Notion.

[Visualizar evidência](INC-002_04_Documentacao.png)

## 5. Reprodução da falha

**Ficheiro:** `INC-002_05_Logs_Falha_Permissoes.png`

Mostra os logs gerados durante a execução da versão inicial do programa Python, incluindo a ausência da permissão `orders.read` e a mensagem HTTP 500 simulada.

[Visualizar evidência](INC-002_05_Logs_Falha_Permissoes.png)

## 6. Teste de correção

**Ficheiro:** `INC-002_06_Teste_Correcao.png`

Demonstra a comparação dos logs antes e depois da alteração controlada das permissões, incluindo a mensagem `Acesso autorizado`.

[Visualizar evidência](INC-002_06_Teste_Correcao.png)

## 7. Análise dos logs no Notion

**Ficheiro:** `INC-002_07_Analise_Logs_Notion.png`

Apresenta a documentação dos registos técnicos produzidos pelo laboratório Python.

[Visualizar evidência](INC-002_07_Analise_Logs_Notion.png)

## 8. Validação e conclusão técnica

**Ficheiros:**

- `INC-002_08_Validacao_Tecnica_Notion.png`
- `INC-002_08_Conclusao_Tecnica_Notion.png`

Documentam os testes de correção e as conclusões técnicas no Notion.

[Visualizar validação](INC-002_08_Validacao_Tecnica_Notion.png)

[Visualizar conclusão](INC-002_08_Conclusao_Tecnica_Notion.png)

## 9. Validação do controlo de acesso

**Ficheiro:** `INC-002_09_Validacao_Controlo_Acesso.png`

Mostra os resultados da execução do programa `app_validacao.py`:

- Ana Martins: acesso autorizado.
- Bruno Costa: acesso negado — HTTP 403 simulado.

[Visualizar evidência](INC-002_09_Validacao_Controlo_Acesso.png)

## 10. Resolução do ticket

**Ficheiro:** `INC-002_10_Ticket_Resolvido.png`

Demonstra a alteração do estado do incidente para Resolvido no Notion, após a conclusão da validação simulada.

[Visualizar evidência](INC-002_10_Ticket_Resolvido.png)

## 11. Registo das datas de SLA

**Ficheiro:** `INC-002_11_Datas_SLA.png`

Apresenta os campos de abertura, primeira resposta e resolução definidos para o cenário fictício.

[Visualizar evidência](INC-002_11_Datas_SLA.png)

## 12. Análise do SLA

**Ficheiro:** `INC-002_12_Analise_SLA.png`

Documenta o cálculo dos indicadores simulados:

- Primeira resposta: 15 minutos.
- Tempo de resolução: 6 horas e 15 minutos.
- Resultado: dentro dos limites da política fictícia P3.

[Visualizar evidência](INC-002_12_Analise_SLA.png)

## 13. Encerramento do incidente

**Ficheiro:** `INC-002_13_Ticket_Encerrado.png`

Demonstra o estado final Encerrado no Notion, concluindo o ciclo de vida do incidente simulado.

[Visualizar evidência](INC-002_13_Ticket_Encerrado.png)

---

## Documentação complementar

- [README principal do projeto](../README.md)
- [Laboratório Python](../laboratorio-python/README.md)
- [Código da falha](../laboratorio-python/app_falha.py)
- [Código da correção](../laboratorio-python/app_corrigida.py)
- [Código de validação](../laboratorio-python/app_validacao.py)
- [Logs da investigação](../laboratorio-python/logs/exemplo-auth.log)
- [Logs de validação](../laboratorio-python/logs/validacao-auth.log)

---

## Observações

Todas as capturas foram produzidas durante a construção do portfólio.

A documentação empresarial representa uma simulação educativa.

Os ficheiros de logs foram gerados durante a execução dos programas Python locais, mas não correspondem a registos de uma aplicação empresarial real.

Nenhuma intervenção foi realizada num ambiente de produção.

**Projeto desenvolvido para fins educativos e demonstração de competências**

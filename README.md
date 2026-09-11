# Cadastro de Jogos Zerados

Sistema simples de linha de comando feito em Python pra eu controlar os jogos que eu já zerei. Feito como projeto final da matéria Estrutura de Dados módulos 2, CRUD (Create, Read, Update, Delete) de verdade, sem framework nem nada, só Python puro.

## O que dá pra fazer

- Adicionar um jogo zerado na lista
- Listar todos os jogos salvos, com o ID de cada um
- Buscar um jogo pelo nome (não precisa digitar certinho maiúscula/minúscula)
- Atualizar o nome de um jogo já cadastrado
- Remover um jogo (com confirmação antes, pra não apagar sem querer)

## Como foi feito

Usei `match/case` pro menu principal, funções separadas pra cada operação, `try/except` pra não quebrar quando o usuário digita algo errado, e o módulo `os` só pra limpar a tela entre uma ação e outra.

## Como rodar

Precisa ter Python 3.10+ instalado.

```
python "Projeto CRUD.py"
```

## Ideias pra melhorar depois

Pensei em adicionar campo de conquistas, horas jogadas e marcar quais jogos eu platinei — ainda não fiz, mas é o próximo passo.

---
Luiz Miguel — versão 3.0

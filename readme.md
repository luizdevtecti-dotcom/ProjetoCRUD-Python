# Cadastro de Jogos Zerados 🎮

Um sistema de gerenciamento em linha de comando (CLI) desenvolvido em Python para registro e controle de jogos zerados. O projeto aplica os conceitos fundamentais de **CRUD** (*Create, Read, Update, Delete*).

---

## 📌 Sobre o Projeto

Este sistema tem como objetivo oferecer um controle simples e eficiente de jogos zerados, fornecendo mecanismos de cadastro, visualização, busca, atualização e remoção de itens. 

> 🔮 **Futuras Atualizações:** Em breve, o sistema contará com novos recursos como registro de conquistas, horas jogadas e marcação de jogos platinados.

---

## 🚀 Funcionalidades

- ➕ **Adicionar (Create):** Cadastre novos jogos concluídos na sua lista.
- 📋 **Listar (Read):** Visualize todos os jogos salvos com seus respectivos IDs.
- ✏️ **Atualizar (Update):** Altere o nome de um jogo já cadastrado pelo ID.
- ❌ **Remover (Delete):** Exclua jogos da lista com confirmação prévia para evitar erros.
- 🔍 **Buscar:** Encontre jogos específicos rapidamente (suporta busca ignorando maiúsculas e minúsculas).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Módulos Nativos:** `os` (para limpeza dinâmica de tela)
- **Estruturas do Código:** `match/case`, funções modulares, tratamento de exceções (`try/except`) e manipulação de listas.

---

## 💻 Como Executar o Projeto

### Pré-requisitos
Possuir o **Python 3.10+** instalado na sua máquina.

### Passo a passo
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```

---

## 📅 Histórico de Desenvolvimento

- **10/06** - Descrição do projeto
- **10/06** - Criação do menu principal utilizando `match/case`
- **10/06** - Implementação da função de **Adicionar** jogos
- **17/06** - Implementação da função de **Listar** jogos
- **17/06** - Implementação da função de **Buscar** jogos
- **17/06** - Criação da função de limpeza de tela (`limpar_tela`)
- **17/06** - Adição de pausas de navegação para melhorar a experiência do usuário
- **08/07** - Atualização da função **Listar** para exibir IDs/índices
- **08/07** - Atualização da função **Buscar** para trabalhar com IDs/índices
- **08/07** - Adição de tratamento para casos em que o jogo não é encontrado
- **15/07** - Implementação da função **Remover** com confirmação de execução
- **15/07** - Implementação da função **Atualizar** com confirmação de execução

---

## 👨‍💻 Desenvolvedor

**Luiz Miguel** — *Versão 3.0*
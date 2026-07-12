# 🤖 Automação de Cadastro de Produtos com Python (RPA)


Curso Técnico em Análise e Desenvolvimento de Sistemas (TADS) no **SENAI Gama - DF**. 

## 📌 Sobre o Projeto

A aplicação consiste em um sistema de RPA que elimina o trabalho manual de digitação e cadastro de produtos. O script automatiza todo o fluxo operacional: desde a abertura do navegador Opera, a realização do login seguro no sistema web, a leitura de uma base de dados externa (`.csv`) e o preenchimento em massa de todos os itens até a sua conclusão.

## ⚙️ Fluxo da Automação
O robô executa as seguintes etapas sequencialmente:
1. **Inicialização:** Aciona a tecla Windows, busca e abre o navegador **Opera**.
2. **Navegação & Login:** Acessa o link do sistema, localiza os campos de e-mail e senha por coordenadas de clique e realiza a autenticação.
3. **Leitura de Dados:** Utiliza o Pandas para ler o arquivo `produtos.csv`.
4. **Loop de Cadastro:** Percorre linha por linha da tabela, extraindo as informações (Código, Marca, Tipo, Categoria, Preço, Custo e Observações) e preenchendo os respectivos campos via comandos de teclado simulados.
5. **Conclusão:** Envia os dados de cada produto, rola a página de volta ao topo e repete o processo até zerar a lista.

## 🚀 Tecnologias e Bibliotecas Utilizadas
* **Python 3.x** (Linguagem base)
* **PyAutoGUI:** Responsável pelo controle de mouse, teclado e automação de cliques na tela.
* **Pandas:** Utilizado para a manipulação e leitura eficiente da base de dados em formato CSV.
* **OpenPyXL:** Suporte para integração e leitura de arquivos de planilhas.
* **Time:** Controle de pausas internas para sincronia com o tempo de carregamento das páginas web.

## 🔧 Como Executar o Projeto

### 📋 Pré-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:
* Python 3.x instalado.
* O navegador **Opera** (ou ajuste a linha 11 do script para o seu navegador de preferência, como 'chrome' ou 'edge').

### 📦 Instalação das Dependências
Abra o seu terminal e instale as bibliotecas necessárias rodando o comando:
```bash
pip install pyautogui pandas openpyxl

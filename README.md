# Projeto de Integração de Dados com MySQL e Python

Este projeto tem como objetivo integrar dados de múltiplos arquivos CSV em um banco de dados MySQL, utilizando Python, Pandas e o conector MySQL para consolidar e armazenar dados em tabelas relacionais.

## Autores
- **Daniel Viegas Cardamoni**
- **Danielle de Carvalho Sanches**
- **Jennifer Cristine Farias Alves**

---

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte:

1. **Python 3.7+**
2. **MySQL Server** configurado com um banco de dados chamado `colab` (ou ajuste o nome do banco no código, se preferir).
3. **Bibliotecas Python**:
   - MySQL Connector: Instale com o comando:
     ```bash
     pip install mysql-connector-python
     ```
   - Pandas: Instale com o comando:
     ```bash
     pip install pandas
     ```

---

## Estrutura de Arquivos

Organize os arquivos CSV em uma pasta chamada `BASE_TP` no diretório do projeto. O código vai ler e processar automaticamente todos os arquivos CSV nesta pasta.

---

## Passo a Passo de Execução

1. ### Conexão ao Banco de Dados e Criação das Tabelas

   O código se conecta ao banco `colab` e cria as seguintes tabelas para armazenar os dados:

   - Animal_Estimacao: Armazena os tipos de animais de estimação.
   - **Clima**: Armazena as preferências de clima.
   - **Bebida**: Armazena as bebidas favoritas.
   - **Hobbies**: Armazena os hobbies registrados.
   - **Pessoa**: Contém informações pessoais, como gênero e data de nascimento.
   - **Pesquisa**: Tabela principal que associa todas as informações por meio de chaves estrangeiras.

2. ### Execução do Script de Integração

   O script realiza as seguintes operações:
   
   - **Leitura dos Arquivos CSV**: Lê todos os arquivos CSV dentro de `BASE_TP` e concatena-os em um único DataFrame.
   - **Criação e Inserção de Dados no Banco de Dados**: Insere os dados nas tabelas criadas no MySQL.

   Para executar o script, rode o comando:

   ```bash
   python dados.py
   ```
3. ### Estrutura das Tabelas

    As tabelas do banco foram configuradas com as seguintes chaves e relações:

	  - **Animal_Estimacao**: cod_animal_estimacao como chave primária.
	  - **Clima:** cod_clima como chave primária.
	  - **Bebida:** cod_bebida como chave primária.
	  - **Hobbies:** cod_hobbies como chave primária.
	  - **Pessoa:** cod_pessoa como chave primária, com informações adicionais de gênero e data de nascimento.
	  - **Pesquisa:** Contém todas as chaves estrangeiras para relacionar com as demais tabelas.
  
  ## Observações 
  
  - **Banco de Dados:** Verifique a conexão ao banco de dados e ajuste as   configurações de host, user, password e database no código, se 
     necessário.
  - **Encoding:** Os arquivos CSV são lidos com diferentes encodings (utf-8 e ISO-8859-1) para evitar erros de leitura.
  
  ## Saída
  Ao final, um arquivo consolidado joined_data.csv será salvo na pasta BASE_TP, contendo todos os dados combinados. Além disso, os dados estarão 
  carregados no banco de dados colab.

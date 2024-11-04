#!pip install mysql-connector-python
import pandas as pd
import os
import mysql.connector

pasta= './BASE_TP'

dfs = []

for arquivo in os.listdir(pasta):
    if arquivo.endswith(".csv"):
        caminho = os.path.join(pasta, arquivo)
        print(f"Lendo o arquivo {caminho}...")

        try:
            df = pd.read_csv(caminho, sep='|', encoding='utf-8', engine='python')
        except UnicodeDecodeError:
            df = pd.read_csv(caminho, sep='|', encoding='ISO-8859-1', engine='python')

       
        dfs.append(df)


df_join = pd.concat(dfs, ignore_index=True)


saida = './BASE_TP/joined_data.csv'
df_join.to_csv(saida, sep='|', index=False)

print(f"Arquivos baixados em {saida}.")

db = mysql.connector.connect(
    host="localhost", 
    user="root",
    password=" ",
    database="colab",
    port=3306 
)

cursor = db.cursor()

# Criação das tabelas no banco de dados MySQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS Animal_Estimacao (
    cod_animal_estimacao INT PRIMARY KEY AUTO_INCREMENT,
    animal_estimacao VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clima (
    cod_clima INT PRIMARY KEY AUTO_INCREMENT,
    clima VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Bebida (
    cod_bebida INT PRIMARY KEY AUTO_INCREMENT,
    bebida_favorita VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Hobbies (
    cod_hobbies INT PRIMARY KEY AUTO_INCREMENT,
    hobbies VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pessoa (
    cod_pessoa INT PRIMARY KEY,
    genero VARCHAR(10),
    data_nascimento DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pesquisa (
    cod_pesquisa INT PRIMARY KEY AUTO_INCREMENT,
    data_coleta DATE,
    cod_animal_estimacao INT,
    cod_bebida INT,
    cod_clima INT,
    cod_hobbies INT,
    cod_pessoa INT,
    FOREIGN KEY (cod_animal_estimacao) REFERENCES Animal_Estimacao(cod_animal_estimacao),
    FOREIGN KEY (cod_bebida) REFERENCES Bebida(cod_bebida),
    FOREIGN KEY (cod_clima) REFERENCES Clima(cod_clima),
    FOREIGN KEY (cod_hobbies) REFERENCES Hobbies(cod_hobbies),
    FOREIGN KEY (cod_pessoa) REFERENCES Pessoa(cod_pessoa)
)
""")

# Caminho para o arquivo CSV
caminho = './BASE_TP/joined_data.csv'
df = pd.read_csv(caminho, sep='|', encoding='utf-8', engine='python')

# Inserção de dados
for index, row in df.iterrows():
    # Inserindo Animal_Estimacao
    cursor.execute("INSERT INTO Animal_Estimacao (animal_estimacao) VALUES (%s)", (row['animal_estimacao'],))
    cod_animal_estimacao = cursor.lastrowid

    # Inserindo Clima
    cursor.execute("INSERT INTO Clima (clima) VALUES (%s)", (row['clima'],))
    cod_clima = cursor.lastrowid

    # Inserindo Bebida
    cursor.execute("INSERT INTO Bebida (bebida_favorita) VALUES (%s)", (row['bebida_favorita'],))
    cod_bebida = cursor.lastrowid

    # Inserindo Hobbies
    cursor.execute("INSERT INTO Hobbies (hobbies) VALUES (%s)", (row['hobbies'],))
    cod_hobbies = cursor.lastrowid

    # Inserindo Pessoa
    cursor.execute("""
    INSERT IGNORE INTO Pessoa (cod_pessoa, genero, data_nascimento)
    VALUES (%s, %s, %s)
    """, (row['cod_pessoa'], row['genero'], row['data_nascimento']))

    # Inserindo Pesquisa com referências de chave estrangeira
    cursor.execute("""
    INSERT INTO Pesquisa (data_coleta, cod_animal_estimacao, cod_bebida, cod_clima, cod_hobbies, cod_pessoa)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (row['data_coleta'], cod_animal_estimacao, cod_bebida, cod_clima, cod_hobbies, row['cod_pessoa']))

# Salvar as alterações e fechar a conexão
db.commit()
db.close()

print("Dados inseridos com sucesso!")

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

def conectar():
    conn = psycopg2.connect(host="localhost",
                            database="dados",
                            user="postgres",
                            password=DB_PASSWORD,
                            port=DB_PORT)

    return conn

def criar_tabela():
    conn = conectar()

    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE teste (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                idade INTEGER)
""")
    conn.commit()
    conn.close()


criar_tabela()
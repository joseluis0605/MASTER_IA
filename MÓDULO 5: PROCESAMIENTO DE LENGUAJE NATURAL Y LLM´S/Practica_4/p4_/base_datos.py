import sqlite3
import speech_recognition as sr
from transformers import pipeline

# Configuración de la base de datos SQLite
DB_NAME = "asistente_hospital.db"


# Función para conectar a la base de datos SQLite
def conectar_db():
    conexion = sqlite3.connect(DB_NAME)
    return conexion


# Función para crear la tabla de consultas y respuestas en la base de datos
def crear_base_datos():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas_respuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            consulta TEXT,
            respuesta TEXT
        )
    """)
    conexion.commit()
    cursor.close()
    conexion.close()


# Función para insertar una consulta y respuesta en la base de datos
def insertar_consulta_respuesta(consulta, respuesta):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO consultas_respuestas (consulta, respuesta) VALUES (?, ?)", (consulta, respuesta))
    conexion.commit()
    cursor.close()
    conexion.close()




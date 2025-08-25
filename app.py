from flask import Flask, request, redirect, render_template, flash
from datetime import datetime
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

# Archivo JSON para persistencia
TAREAS_FILE = 'tareas.json'

# Lista en memoria para almacenar las tareas
tareas = []
contador_id = 1

def cargar_tareas():
    """Carga las tareas desde el archivo JSON"""
    global tareas, contador_id
    try:
        if os.path.exists(TAREAS_FILE):
            with open(TAREAS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                tareas = data.get('tareas', [])
                contador_id = data.get('contador_id', 1)
                print(f"Tareas cargadas: {len(tareas)} tareas encontradas")
        else:
            tareas = []
            contador_id = 1
            print("Archivo de tareas no encontrado, iniciando con lista vacía")
    except Exception as e:
        print(f"Error al cargar tareas: {e}")
        tareas = []
        contador_id = 1

def guardar_tareas():
    """Guarda las tareas en el archivo JSON"""
    try:
        data = {
            'tareas': tareas,
            'contador_id': contador_id
        }
        with open(TAREAS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Tareas guardadas: {len(tareas)} tareas")
    except Exception as e:
        print(f"Error al guardar tareas: {e}")

# Función para generar un nuevo ID único
def generar_id():
    global contador_id
    contador_id += 1
    return contador_id - 1

# Función auxiliar para agregar tarea
def agregar_tarea(texto_tarea):
    global tareas
    nueva_tarea = {
        'id': generar_id(),
        'texto': texto_tarea.strip(),
        'hecho': False,
        'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    tareas.append(nueva_tarea)
    guardar_tareas()  # Guardar después de agregar
    flash('Tarea agregada exitosamente!', 'success')

# Función auxiliar para completar tarea
def completar_tarea(id):
    global tareas
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = not tarea['hecho']
            estado = "completada" if tarea['hecho'] else "pendiente"
            guardar_tareas()  # Guardar después de modificar
            flash(f'Tarea marcada como {estado}!', 'success')
            break
    else:
        flash('Tarea no encontrada!', 'error')

# Función auxiliar para eliminar tarea
def eliminar_tarea(id):
    global tareas
    tareas = [t for t in tareas if t['id'] != id]
    guardar_tareas()  # Guardar después de eliminar
    flash('Tarea eliminada!', 'success')

# Ruta principal para mostrar tareas
@app.route('/')
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

# Ruta para agregar tarea
@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    else:
        flash('El texto de la tarea es obligatorio!', 'error')
    return redirect('/')

# Ruta para marcar como completada
@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

# Ruta para eliminar tarea
@app.route('/eliminar/<int:id>')
def eliminar(id):
    eliminar_tarea(id)
    return redirect('/')

if __name__ == '__main__':
    # Cargar tareas al iniciar la aplicación
    cargar_tareas()
    app.run(debug=True)

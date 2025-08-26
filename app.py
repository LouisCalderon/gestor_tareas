from flask import Flask, request, redirect, render_template, flash, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

# Lista en memoria para almacenar las tareas
tareas = []
contador_id = 1

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
    flash('Tarea agregada exitosamente!', 'success')

# Función auxiliar para editar tarea
def editar_tarea(id, nuevo_texto):
    global tareas
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['texto'] = nuevo_texto.strip()
            return True
    return False

# Función auxiliar para completar tarea
def completar_tarea(id):
    global tareas
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = not tarea['hecho']
            estado = "completada" if tarea['hecho'] else "pendiente"
            flash(f'Tarea marcada como {estado}!', 'success')
            break
    else:
        flash('Tarea no encontrada!', 'error')

# Función auxiliar para eliminar tarea
def eliminar_tarea(id):
    global tareas
    tareas = [t for t in tareas if t['id'] != id]
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

# Ruta para editar tarea (usada por JavaScript)
@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    nuevo_texto = request.form.get('texto_tarea')
    if nuevo_texto and nuevo_texto.strip():
        if editar_tarea(id, nuevo_texto):
            return jsonify({'success': True, 'message': 'Tarea editada exitosamente'})
        else:
            return jsonify({'success': False, 'message': 'Tarea no encontrada'}), 404
    else:
        return jsonify({'success': False, 'message': 'El texto no puede estar vacío'}), 400

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
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

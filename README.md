# Gestor de Tareas - Aplicación Flask

Una aplicación web simple para gestionar tareas, construida con Flask con persistencia en archivo JSON.

## Características

- ✅ Crear, editar y eliminar tareas
- 🎯 Sistema de prioridades (baja, media, alta)
- 📅 Fechas de creación automáticas
- 🎨 Interfaz moderna y responsive
- 💾 Persistencia en archivo JSON
- 📱 Diseño responsive

## Instalación

1. **Activar el entorno virtual:**
   ```bash
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

4. **Abrir en el navegador:**
   ```
   http://localhost:5000
   ```

## Estructura del Proyecto

```
gestor_tareas/
├── app.py              # Aplicación principal Flask
├── tareas.json         # Archivo de persistencia JSON
├── requirements.txt    # Dependencias del proyecto
├── README.md          # Este archivo
├── templates/         # Plantillas HTML
│   ├── index.html     # Página principal
│   └── nueva_tarea.html # Formulario de nueva tarea
├── static/            # Archivos estáticos
│   └── style.css      # Estilos CSS
└── venv/              # Entorno virtual
```

## Uso

- **Ver tareas:** Navega a la página principal
- **Crear tarea:** Usa el formulario en la parte superior
- **Marcar como completada:** Haz clic en el botón verde de check
- **Deshacer tarea:** Haz clic en el botón de deshacer para tareas completadas
- **Eliminar tarea:** Haz clic en el botón rojo de papelera

## Persistencia de Datos

La aplicación ahora utiliza un archivo JSON (`tareas.json`) para almacenar las tareas de forma persistente. Esto significa que:

- Las tareas se mantienen entre reinicios de la aplicación
- No se requiere configuración de base de datos
- Los datos se guardan automáticamente en cada operación
- El archivo se crea automáticamente si no existe

### Estructura del archivo JSON:
```json
{
  "tareas": [
    {
      "id": 1,
      "texto": "Descripción de la tarea",
      "hecho": false,
      "fecha_creacion": "2024-01-15 10:30"
    }
  ],
  "contador_id": 2
}
```

## Tecnologías Utilizadas

- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Persistencia:** JSON
- **Lenguaje:** Python 3.x

## Desarrollo

Para desarrollo local, la aplicación se ejecuta en modo debug. Los cambios en el código se reflejarán automáticamente al recargar la página.

## Notas de Implementación

- Las tareas se cargan automáticamente al iniciar la aplicación
- Cada operación (crear, modificar, eliminar) guarda automáticamente en el archivo JSON
- El sistema maneja errores de lectura/escritura de archivos de forma robusta
- Se mantiene un contador de IDs para asegurar unicidad

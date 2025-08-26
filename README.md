# Gestor de Tareas

Una aplicación web simple para gestionar tareas, construida con Flask.

## Características

- Agregar nuevas tareas
- Marcar tareas como completadas
- Editar tareas existentes
- Eliminar tareas
- Interfaz web responsive

## Despliegue en Railway

### Prerrequisitos

1. Tener una cuenta en [Railway](https://railway.app)
2. Tener Git instalado
3. Tener GitHub conectado a Railway

### Pasos para el despliegue

1. **Crear cuenta en Railway:**
   - Ve a [railway.app](https://railway.app)
   - Inicia sesión con tu cuenta de GitHub

2. **Crear un nuevo proyecto:**
   - Haz clic en "New Project"
   - Selecciona "Deploy from GitHub repo"
   - Conecta tu repositorio de GitHub

3. **Configurar el despliegue:**
   - Railway detectará automáticamente que es una aplicación Python
   - El archivo `railway.json` configurará el despliegue
   - El archivo `nixpacks.toml` configurará el build

4. **Desplegar:**
   - Railway construirá y desplegará automáticamente tu aplicación
   - Cada push a tu rama principal activará un nuevo despliegue

5. **Configurar variables de entorno (opcional):**
   - En Railway, ve a tu proyecto → Variables
   - Agrega `SECRET_KEY` con un valor seguro

6. **Obtener la URL:**
   - Railway te dará una URL automáticamente
   - Puedes configurar un dominio personalizado si lo deseas

### Estructura de archivos para Railway

- `railway.json`: Configuración del despliegue en Railway
- `nixpacks.toml`: Configuración del build de Python
- `requirements.txt`: Lista las dependencias de Python
- `app.py`: Aplicación principal de Flask

## Desarrollo local

1. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
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

## Tecnologías utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Base de datos**: Almacenamiento en memoria (para desarrollo)
- **Despliegue**: Railway

## Ventajas de Railway

- **Simplicidad**: Despliegue automático desde GitHub
- **Gratis**: Plan gratuito generoso
- **Rápido**: Builds y despliegues muy rápidos
- **Integración**: Perfecta integración con GitHub
- **Escalabilidad**: Fácil escalar cuando sea necesario

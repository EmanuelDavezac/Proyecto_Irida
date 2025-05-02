## 📌 Descripción
Este es un proyecto web desarrollado en Django que permite la gestión de productos, clientes y categorías. Implementa el patrón MVT y utiliza herencia de plantillas para estructurar la interfaz de usuario.

## 🚀 Características
- Herencia de plantillas en HTML para una mejor organización.
- Tres modelos principales: **Producto**, **Cliente**, **Categoría**.
- Formularios para ingresar datos en cada modelo.
- Formulario de búsqueda para localizar productos en la base de datos.
- Bootstrap integrado para mejorar el diseño.
- Funciones CRUD (Crear, Leer, Actualizar, Eliminar) en los productos.

## 🔧 Instalación y Configuración
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/EmanuelDavezac/Proyecto_Irida.git
   cd Proyecto_Irida

## Crear un entorno virtual y activarlo
- python -m venv venv
- source venv/bin/activate  # En Mac/Linux
- venv\Scripts\activate  # En Windows

## Instalar las dependencias
- pip install -r requirements.txt

## Eejcutar las migraciones
- python manage.py migrate

## Iniciar el servidor
- python manage.py runserver
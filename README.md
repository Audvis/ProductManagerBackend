# Backend: Gestión de Productos y Categorías

Este es el backend de la aplicación que permite la gestión de productos y categorías a través de una API RESTful desarrollada con Flask.

## **1. Instalación**

#### **Paso 1: Clona el repositorio**
```bash
git clone https://github.com/Audvis/ProductManagerBackend.git
cd ProductManagerBackend
```

#### **Paso 2: Configura el entorno virtual**
1. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   ```
2. Activa el entorno virtual:
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```

#### **Paso 3: Instala las dependencias**
Instala las dependencias necesarias desde el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### **Paso 4: Configura la base de datos**
1. Configura la base de datos (asegúrate de que tengas un servidor SQLite o cualquier otro sistema configurado).
2. Ejecuta las migraciones si es necesario:
   ```bash
   flask db upgrade
   ```

#### **Paso 5: Ejecuta el servidor**
Inicia el backend:
```bash
flask run
```
El backend estará disponible en `http://127.0.0.1:5000`.

---

## **2. Funcionalidades**

- Gestión de productos:
  - Crear, editar, eliminar y listar productos.
  - Validaciones en los campos del producto, como nombre, precio y categoría.
- Gestión de categorías:
  - Crear, editar, eliminar y listar categorías.
  - Validaciones para evitar duplicados y asegurar la consistencia de los datos.
- API RESTful construida con Flask.

## **3. Rutas de la API**

### **Productos**

- **GET** `/products/`  
  Obtiene la lista de todos los productos.

- **POST** `/products/`  
  Crea un nuevo producto.  
  - **Body JSON:**
    ```json
    {
      "name": "Product Name",
      "description": "Product Description",
      "price": 100.50,
      "stock": 10,
      "category_id": 1
    }
    ```

- **PUT** `/products/<id>`  
  Actualiza un producto existente.  
  - **Body JSON:** (similar al POST)

- **DELETE** `/products/<id>`  
  Elimina un producto por su ID.

---

### **Categorías**

- **GET** `/categories/`  
  Obtiene la lista de todas las categorías.

- **POST** `/categories/`  
  Crea una nueva categoría.  
  - **Body JSON:**
    ```json
    {
      "name": "Category Name"
    }
    ```

- **PUT** `/categories/<id>`  
  Actualiza una categoría existente.  
  - **Body JSON:** (similar al POST)

- **DELETE** `/categories/<id>`  
  Elimina una categoría por su ID.

---

## **4. Requisitos previos**

- Python 3.8 o superior.
- SQLite u otro sistema de base de datos compatible con SQLAlchemy (opcional).

---

## **5. Notas adicionales**

- Asegúrate de configurar las variables de entorno si usas una base de datos distinta de SQLite.
- Para probar la API, puedes usar herramientas como Postman o cURL.

---

## **6. Contacto**
Si tienes preguntas o encuentras problemas, no dudes en abrir un issue en el repositorio o contactar al desarrollador.


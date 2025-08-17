# Problema-Modulo-10---Prog4

🎯 Objetivo
Modificar la arquitectura de la aplicación web de biblioteca personal para separar el backend de datos en una API RESTful independiente, mientras que la aplicación Flask actuará como cliente, enviando y recibiendo datos a través de solicitudes HTTP.

📝 Contexto
Anteriormente, la aplicación gestionaba los datos directamente con una base de datos como KeyDB o MongoDB. En esta versión, se construirá una API RESTful que actuará como proveedor de datos. La aplicación Flask deberá consumir esta API para realizar todas las operaciones de CRUD.

Esta arquitectura es ideal para aplicaciones distribuidas, escalables y desacopladas.

📌 Requisitos funcionales
🔹 API RESTful (backend de datos)
Implementar una API con los siguientes endpoints:

GET /books → Obtener la lista de libros

GET /books/<id> → Obtener un libro específico

POST /books → Agregar un nuevo libro

PUT /books/<id> → Actualizar la información de un libro

DELETE /books/<id> → Eliminar un libro

La API debe devolver respuestas en formato JSON y utilizar correctamente los códigos de estado HTTP (200, 201, 400, 404, etc.).

🔹 Aplicación Flask (cliente)
Adaptar la app para que:

Todas las operaciones CRUD se realicen mediante solicitudes HTTP a la API REST usando la biblioteca requests.

Las vistas se rendericen dinámicamente con los datos recibidos de la API.

Se gestionen correctamente los errores de red y respuestas inválidas de la API.

Se puedan mostrar mensajes de éxito o error al usuario (por ejemplo, al agregar o eliminar un libro).

🔹 Entorno de Producción
La aplicación Flask debe seguir funcionando en un entorno de producción con Gunicorn y Nginx.

La API REST también debe poder desplegarse en producción, ya sea en el mismo servidor o en uno distinto.

💡 Consideraciones técnicas
La API puede implementarse con Flask o Flask-RESTful.

Se recomienda organizar la API en un proyecto separado, con rutas limpias y modularizadas.

Para el cliente Flask, usar requests para interactuar con la API y dotenv para cargar la URL base de la API.

La autenticación (opcional) puede implementarse con JWT o autenticación básica.

Las credenciales y rutas deben manejarse mediante variables de entorno (.env).

# Social blog
un blog creado con django que proporciona una plataforma interactiva para compartir artículos y comentarios con otros usuarios.

# Configuración y requisitos

Para utilizar este blog desarrollado con Django, sigue los pasos a continuación:

1. Clona el repositorio o descarga el código fuente en tu máquina.
2. Crea y activa un entorno virtual específico para este proyecto.
3. Instala las dependencias necesarias ejecutando el siguiente comando: `pip install -r requirements.txt`.
4. Aplica las migraciones de la base de datos para preparar el sistema ejecutando: `python3 manage.py migrate`.
5. Para iniciar el servidor de desarrollo, ejecuta: `python3 manage.py runserver`.

Asegúrate de cumplir con los requisitos mencionados anteriormente antes de continuar con la instalación y configuración.

**Nota:** Asegúrate de tener Python 3.x y Django 3.x instalados correctamente en tu entorno antes de proceder. Si no los tienes instalados, por favor, consulta la documentación oficial de Python y Django para obtener instrucciones detalladas sobre cómo instalarlos.

Una vez que hayas seguido estos pasos, estarás listo para comenzar a utilizar el blog. ¡Disfruta!

# Admin 
usuario: joaco

clave: 123

# Uso del blog 

- Accede al blog: Abre tu navegador y visita la URL del blog (por ejemplo, http://localhost:8000).
  
- Regístrate o inicia sesión: Crea una cuenta o inicia sesión con tus credenciales para acceder a todas las funcionalidades.
  
- Explora los artículos: Descubre los diferentes artículos publicados por otros usuarios y navega por las categorías disponibles.
  
- Comenta en los artículos: Participa dejando comentarios en los artículos que te interesen.
  
- Crea tus propios artículos: Utiliza el panel de control de usuario para crear tus propios artículos. Completa el formulario  y luego guarda y publica tu artículo.
  
- Gestiona tus artículos: Desde el panel de control de usuario, podrás editar o eliminar tus propios artículos según sea necesario.


## Uso de la API

La API Posee los endpoints de perfil, perfil-detalle, posteo, posteo-detalle, comentario, comentario-detalle, categoria y categoria-detalle.

Se utilizaran las rutas de Perfil y Posteos para evitar la repeticion

Tanto el GET, POST, PUT y DELETE se realizan de igual forma para cualquier modelo:

  - Endpoint: http://localhost:8000/api/v1/-modelo_requerido-
 
    Ejemplo:

  - Endpoint: http://localhost:8000/api/v1/posteo/

---------------------------------------------------------------------------------

#### Token para Auth
  - Método: POST
  - URL: http://localhost:8000/api/token/
  - Headers: 
    - Content-Type: application/json
  - Body (enviar como x-www-form-urlencoded):
    - username: joaco
    - password: 123


---------------------------------------------------------------------------------

#### Traer Perfiles

- Método: `GET`
- Endpoint: http://localhost:8000/api/v1/perfil/
- Headers: 
- Content-Type: application/json
- Authorization: Token {token_generico_ejemplo}


#### Traer Perfil-detalle

- Método: GET
- URL: http://localhost:8000/api/v1/perfil/1
- Headers: 
  - Content-Type: application/json
  - Authorization: Token {token_generico_ejemplo}



#### Crear un nuevo Perfil

- Método: `POST`
- Endpoint: http://localhost:8000/api/v1/perfil/
- Headers: 
  - Content-Type: application/json
  - Authorization: Token {token_generico_ejemplo}

**Solicitud**

-aca va el json de la solicitud-

{
 nombre: -nombre del usuario-
 imagen: -imagen del perfil-
}



#### Editar Un Perfil Existente

- Método: `PUT`
- Endpoint: http://localhost:8000/api/v1/perfil/
- Headers: 
  - Content-Type: application/json
  - Authorization: Token {token_generico_ejemplo}

**Solicitud**

-aca va el json de la solicitud-

{
 nombre: -nombre del usuario-
 imagen: -imagen del perfil-
}


---------------------------------------------------------------------------------


#### Traer Posts

- Método: GET
- URL: http://localhost:8000/api/v1/posteo/
- Headers: 
  - Content-Type: application/json
  - Authorization: Token {token_generico_ejemplo}


#### Posteo-detalle
  - Método: GET
  - Descripción: http://localhost:8000/api/v1/posteo/1


#### Crear un Post

- Método: `POST`
- Endpoint: http://localhost:8000/api/v1/posteo/
- Headers: 
    - Content-Type: application/json
    - Authorization: Token {token_generico_ejemplo}

**Solicitud**

-aca va el json de la solicitud-

{
  Content: -contenido del post-,
  User: 
  Tags: 
  Category:
}



#### Borrar un Post

debe incluir en la url el id del post a borrar

- Método: `DELETE`
- Endpoint: http://localhost:8000/api/v1/posteo/1
- Headers: 
- Content-Type: application/json
- Authorization: Token {token_generico_ejemplo}


----------------------------------------------------------------------------------

#### Traer Categoria
  - Método: GET
  - URL: http://localhost:8000/api/v1/posteo/
  - Headers: 
    - Content-Type: application/json
    - Authorization: Token {token_generico_ejemplo}


#### Traer Categoria-detalle
  - Método: GET
  - Descripción: http://localhost:8000/api/v1/posteo/1
  - Headers: 
  - Content-Type: application/json
  - Authorization: Token {token_generico_ejemplo}


----------------------------------------------------------------------------------

#### Traer Comentarios*
- Método: GET
- Descripción: http://localhost:8000/api/v1/comentarios
- Headers: 
- Content-Type: application/json
- Authorization: Token {token_generico_ejemplo}



#### Traer Comentarios-detalle*
- Método: GET
- Descripción: http://localhost:8000/api/v1/comentarios/1
- Headers: 
- Content-Type: application/json
- Authorization: Token {token_generico_ejemplo}

Puede verificar si se ha borrado realizando un GET o viendolo desde el Admin de Django


# Test (Pytest)
- para el uso de las pruebas ejecutar con el comando: pytest

# CSV comando personalizado
- para ejecutar la carga de datos para el modelo atraves del archivo csv se debe utilizar el comando: python manage.py csv_command category.csv
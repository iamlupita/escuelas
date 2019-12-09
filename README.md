# Escuelas de la ZMG
Visualización de escuelas en la Zona Metropolitana de Guadalajara (ZMG) por municipio y escolaridad.

# Requisitos
- Tener instalado Python para ejecutar el archivo "server.py".
- Tener instalada la librería "matplotlib" para cargar las gráficas de manera adecuada.
- Tener instalada la librería "flask" para cargar el servidor de manera adecuada.
- Tener instalada la librería "flask-mysqldb" para cargar la base de datos de manera adecuada.
- Tener acceso a internet para cargar la base de datos y todos los elementos de manera adecuada.

# Instalación
1. Ingresar a la terminal y posicionarse en el directorio en el que se encuentra el archivo server.py.
2. Ingresar el comando 'python server.py'.
3. Ingresar en un navegador a la dirección 'http://127.0.0.1:5000/'.

# Funcionalidades
- Navegación funcional por el mapa con zoom y alejamientos.
- Cada marcador representa un municipio de la Zona Metropolitana de Guadalajara.
- Al seleccionar cada marcador muestra el nombre del municipio seguido del número de primarias, secundarias y preparatorias que hay respectivamente.
- Visualización de la tabla de escuelas por municipio y la cantidad de primarias, secundarias y preparatorias de cada uno respectivamente.
- Botón "Gráfica de Pastel" funcional para visualizar una gráfica de pastel (Sobre la tabla botón izquierdo).
- Al presionar el botón "Gráfica de Pastel" muestra una gráfica de pastel que representa el número de escuelas por municipio y les asigna un porcentaje.
- Botón "Histograma" funcional para visualizar una gráfica de barras (Sobre la tabla, botón derecho).
- Al presionar el botón "Histograma" muestra una gráfica de barras que representa el número de escuelas por escolaridad (primarias, secundarias y preparatorias) y los diferencia por colores para cada municipio.
- Botón discreto "Primarias" funcional en tabla que redirige hacia otra ruta (En la última fila de la tabla de color negro, botón izquierdo).
- Al presionar el botón "Primarias" envía a una página que muestra una tabla con el total de primarias de la Zona Metropolitana de Guadalajara y sus datos más importantes.
- Botón discreto "Secundarias" funcional en tabla que redirige hacia otra ruta (En la última fila de la tabla de color negro, botón central).
- Al presionar el botón "Secundarias" envía a una página que muestra una tabla con el total de secundarias de la Zona Metropolitana de Guadalajara y sus datos más importantes.
- Botón discreto "Preparatorias" funcional en tabla que redirige hacia otra ruta (En la última fila de la tabla de color negro, botón derecho).
- Al presionar el botón "Preparatorias" envía a una página que muestra una tabla con el total de preparatorias de la Zona Metropolitana de Guadalajara y sus datos más importantes.

# Autores
- Ayala Bernal Maria Guadalupe
- Orozco Mercado Haro Federico

1) Herencia de HTML. 
   Todos los htmls de la carpeta 'templates' heredan de 'base.html' lo siguiente:
   CSS, navbar, footer, favicon/title 
   
2) Por lo menos 3 clases en models.
   Las 3 clases creadas en app_juegos/models.py son: Juguete, Sucursal y Empleados. Se pueden cargar 
   desde '/admin/' y se reflejan en '/juguetes/', '/sucursales/' y '/quienes_somos/' respectivamente. 

3) Un formulario para insertar datos a todas las clases de tu models.
   Desde la navbar se pueden cargar datos a los tres modelos desde los links:
   juguete, sucursal y empleado que se despliegan desde el dropdown Crear. (Nota: no logramos hacer que cargue imágenes x formulario)

5) Un formulario para buscar algo en la BD.
   Se puede probar desde la navbar en '/index/' o cualquier otro url. La función buscar_juguetes que 
   realiza la búsqueda (con el método GET) se encuentra en views.py, dentro de la carpeta 'empresa'.
   Los resultados se reflejan en '/buscar_juguetes/?search=...'



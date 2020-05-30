- El register/login

Crear una aplicación con interfaz gráfica en Python.                    - Con render template y CSS

Realizar un script de Python:                                           - Pos todo
Debe de consumir o utilizar al menos 1 API.                             - La Pokemon API
Aplique al menos el uso de 3 clases y 1 vez el uso de la herencia.      - Hay que pensar la herencia(COmpletado)

Pantallas: Login, Inicio, Ajustes

Login: Los usuarios registrados deben guardarse en un archivo de texto  - No debería de haber problema con 
        (Escritura/Lectura)                                               hacerlo un json normal
        Tenía pensado hacer un pickle / el problema con el pickle 
        es que el dump es directo, además de que sale encriptado, no?
        Bueno, luego veo como hacer un hack para hacer un dump en json,
        está easy.

Inicio: Esta pantalla puede contener la información consumida de las API - ¿Que habrá en ésa pantalla?
        en cualquier formato (utilicen también imágenes)                    ¿Una search bar?, una lista con todos los pokemon y ya, luego vemos si ponemos la barra
        todos son > 800, bien chido, le ponemos páginas nice

        Entonces hay que preparar dos templates de consulta, una para ese preview y otro para la página
        detallada
        Pues sí

Ajustes: Esta pantalla contiene preferencias del usuario, preferencias que  - ¿Dark mode y tamaño de fuente?, yo digo
        deben ser guardadas en otro archivo de texto (El programa debe leer
        este archivo primero como prioridad para cargar la información cada 
        vez que el programa inicie)

Crear la opción de que el usuario pueda archivar o marcar como favoritos sus objetos    -Changos, si tenemos
( cartas, recetas, pokemon, video juegos, automóviles) y que esta información sea        que guardar la
almacenada también ya sea en el mismo archivo de texto que guarda las preferencias       info, como un caché
 o bien un archivo nuevo.                      


Que flojera, voy haciendo un DB.py que sea una cosa bien chafa para guardar la info de los usuarios y así                                          
Datos de una persona
====================

.. highlight:: c

El siguiente programa
le pide al usuario ingresar
su nombre completo,
su rut y
su fecha de nacimiento.

Como salida,
se muestra la edad del usuario.

.. literalinclude:: programas/persona.c

Además,
el programa verifica que la fecha de nacimiento sea válida,
revisando que el mes esté entre 1 y 12,
y que el día tenga sentido para ese mes.
Para simplificar,
nos hemos echado los años bisiestos al bolsillo.


Macros de preprocesador
-----------------------
La primera cosa extraña que vemos en este programa
son las líneas que comienzan con ``#define``.
Estas líneas son instrucciones para el **preprocesador**,
que es un componente del compilador
que hace algunas sustituciones en el código
antes de que comience realmente a ser compilado.

Estas sustituciones se llaman **macros**,
y son definidas por el programador
usando la instrucción ``#define``.
Cada vez que aparece la macro en el código,
el preprocesador la reemplaza literalmente
por lo que aparezca a su derecha en el ``#define``.

Es común usar macros para definir
una única vez al principio del programa
los largos de los arreglos.
Estos valores suelen aparecer
muchas varias veces durante el programa;
por ejemplo, en las declaraciones
y en los ciclos que los recorren.

En nuestro programa,
hemos definido las macros
``LARGO_NOMBRE`` y ``LARGO_RUT``,
que son los largos de los strings.
Si más adelante uno quisiera modificar el programa
para que alguno de estos strings tenga un largo diferente,
bastaría con modificar la macro asociada
para que automáticamente el programa siga estando correcto.

Hay que tener muy claro que
**las macros no son variables**.
Son sólo abreviaciones que son reemplazadas
tal cual cada vez que aparecen en el código.
Para distinguirlas de las variables,
se sigue la convención de ponerle a las macros
nombres en mayúsculas.

En la línea de comandos,
usted puede usar el programa ``cpp``
para ver cómo queda el código
después de ser preprocesado::

    $ cpp personas.c


Estructuras
-----------
Una **estructura** es un tipo de datos
que agrupa varios valores en uno solo.

A diferencia de los arreglos,
los componentes de una estructura
pueden ser de tipos diferentes.

Las estructuras en C
se usan para lo mismo que las tuplas en Python:
para agrupar datos que, por su naturaleza,
deben ser tratados como un único valor.

El ejemplo típico es crear una estructura
para almacenar una fecha::

    struct fecha {
        int dia;
        int mes;
        int anno;
    };

Esta definición crea un nuevo tipo de datos
llamado ``struct fecha``,
que contiene tres valores enteros.
El punto y coma después de la llave es obligatorio;
un error muy común es omitirlo.

Una variable de tipo ``struct fecha``
debe ser declarada de la misma forma
que las demás variables::

    struct fecha f;

Una vez declarada la variable ``f``,
sus miembros pueden ser accedidos
poniendo su nombre después de un punto::

    f.dia = 21;
    f.mes = 5;
    f.anno = 1879;

Note que las estructuras no se desempaquetan
como las tuplas de Python.
No es necesario ya que se puede acceder a los campos
a través de su nombre, y no por su posición.

Los campos de una estructura pueden ser de cualquier tipo,
incluso arreglos u otra estructura.
En el ejemplo,
la estructura ``persona`` está compuesta
de dos strings y una estructura ``fecha``.


Inicialización de arreglos y estructuras
----------------------------------------
La función ``fecha_es_valida``
utiliza el arreglo ``dias_mes``
para tener a la mano
cuántos días tiene cada mes.

Para que el mes ``m`` esté asociado
al elemento ``m`` del arreglo,
dejamos un valor de relleno en la posición 0,
que no corresponderá a ningún mes.

En vez de llenar el arreglo
elemento por elemento::

    dias_mes[1] = 31;
    dias_mes[2] = 28;
    dias_mes[3] = 31;
    /* ... */

podemos usar la siguiente sintaxis para inicializarlo::

    int dias_mes[] = {0, 31, 28, 31, /* ... */ };

Al inicializar el arreglo de esta manera
no es necesario especificar su tamaño.
En nuestro programa,
el arreglo ``dias_mes`` será de largo trece.

La misma sintaxis se puede usar
para inicializar los elementos de una estructura::

    struct fecha hoy = {29, 2, 2011};

La sintaxis de inicialización sólo puede ser usada
en la misma declaración, no más adelante en el programa::

    int a[5];
    a = {900, 100, 600, 300, 200};  /* Esto es ilegal. */


Leer una línea completa
-----------------------
El descriptor de formato ``%s``
indica a la función ``scanf``
que debe leer un string.
Lo que hace la función es leer texto
hasta encontrarse con el primer caracter en blanco
(como un espacio o un salto de línea).

Esto no resulta útil cuando el string que interesa sí tiene espacios entre medio.
En el caso de nuestro programa,
necesitamos un nombre completo,
en que el nombre y el apellido están separados por un espacio.

Para leer el nombre completo del usuario,
usamos el descriptor de formato ``%[^\n]``.
Esto significa literalmente
«leer todos los caracteres que no sean saltos de línea».


Salidas estándar y de error
---------------------------
Cada vez que uno imprime cosas usando la función ``printf``,
lo que realmente ocurre es que el texto es enviado
a un flujo de datos denominado **salida estándar**.
Podemos pensar en la salida estándar
como un canal de comunicación entre nuestro programa y la consola.

En todos los programas en C,
la salida estándar está disponible para escribir cosas en ella.
Pero además los programas tienen también
otro flujo de datos, llamado **salida de error**,
que está destinada exclusivamente para escribir en ella
mensajes de error.

Los nombres de las salidas estándar y de error en un programa
son, respectivamente, ``stdin`` y ``stderr``.

En nuestro programa,
usamos la salida de error para imprimir un mensaje antes de abortar el programa
cuando se ha ingresado una fecha inválida.
Para esto, usamos la función ``fprintf``.
Esta función es muy parecida a ``printf``,
salvo que recibe como primer parámetro el flujo de datos
en que se escribirá el mensaje.
Más adelante utilizaremos ``fprintf`` para escribir datos en archivos.

Por omisión,
ambas salidas están conectadas con la consola,
por lo que los mensajes impresos en ambas
aparecen mezclados unos con otros, sin distinción.
La gracia es que es posible redirigir
por separado a cualquiera de ellas
hacia otros mecanismos de salida,
como un archivo, o de frentón suprimirlos.
Por lo tanto,
es una buena práctica escribir los mensajes de error en ``stderr``.


Ejercicios
----------
¿Qué imprime el siguiente programa?
Pruebe el programa y explique el resultado.

.. literalinclude:: programas/define-capcioso.c


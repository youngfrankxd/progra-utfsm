Reporte de temperaturas
=======================

*Este problema apareció en el certamen 2 del primer semestre de 2011.*

Las temperaturas mínimas y máximas
de algunas ciudades de la región
están guardadas en un diccionario
cuyas llaves son las ciudades
y cuyos valores son tuplas ``(mínima, máxima)``.

Se desea generar un archivo
cuyo contenido sea un reporte como el del ejemplo de más abajo.
Los nombres de las ciudades en las que hubo más de 25 grados
deben aparecer en mayúsculas.
El nombre del archivo debe incluir la fecha.
El orden en que aparecen las ciudades
dentro del archivo no importa.

Escriba la función ``crear_reporte(fecha, temperaturas)``,
cuyos parámetros son
la fecha (una tupla ``(año, mes, día)``)
y el diccionario de temperaturas,
y que genere el archivo de texto
con el formato del ejemplo.

La función ``crear_reporte`` no debe retornar nada.
Recuerde que ``s.upper()``
entrega el string ``s`` en mayúsculas.

::

    temp = {
      'Vina del Mar':  ( 9, 26),
      'Valparaiso':    (10, 24),
      'Quilpue' :      ( 7, 30),
      'Olmue':         ( 5, 29),
      'Limache':       ( 9, 23),
      'Villa Alemana': ( 9, 22),
    }
    crear_reporte((2011, 5, 14), temp)

Archivo ``reporte-2011-5-14.txt``:

.. code-block:: none

    QUILPUE: max 30, min 7
    Valparaiso: max 24, min 10
    VINA DEL MAR: max 26, min 9
    Villa Alemana: max 22, min 9
    Limache: max 23, min 9
    OLMUE: max 29, min 5

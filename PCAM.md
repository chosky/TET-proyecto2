UNIVERSIDAD EAFIT

INGENIERÍA DE SISTEMAS

STO0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2020-2

GRUPO 001 Y 002

PROYECTO2 – HPC

Proyecto

El Juego de la Vida

**DISEÑO PCAM**

Felipe Olaya Ospina - folayao@eafit.edu.co

Cristian Aristizabal Giraldo - carist31@eafit.edu.co

Jose David Henao Ocampo - jhenaoo3@eafit.edu.co

Departamento de Ingenierías

Ingeniería de Sistemas

Antioquia - Colombia

2020-2

1. **Problema**

El juego de la vida se desarrolla en un tablero que es el plano cuadriculado e infinito. En una posición del juego algunas de las celdas de la cuadrícula tienen el estatus de &quot;vivas&quot;; las demás celdas son vacías. (Gráficamente, las celdas vivas se representan con el color negro y las vacías con el color blanco.) El juego consiste en una sucesión de cambios de posiciones, donde cada posición se calcula a partir de la posición anterior. De este modo, la evolución del juego solo depende de la posición inicial.

Las reglas del cambio son las siguientes. El estatus de una celda en la nueva posición dependerá de su estatus actual y del número de celdas vivas entre las 8 celdas adyacentes a ella. Una celda estará viva en la nueva posición, si

\* está viva en la posición actual y tiene 2 o 3 celdas vecinas vivas;

\* está vacía en la posición actual y tiene exactamente 3 celdas vecinas vivas.

1. **Partición**

la implementación secuencial consta de asignar un número de líneas a cada procesador. Esto corresponde a un partición unidimensional de los datos. sin embargo, es una buena idea utilizar uno bidimensional en su lugar, Suponga que cada procesador almacena una línea del tablero. Para actualizar esa línea necesita recibir dos líneas de datos, y esto lleva tiempo. De hecho, recibir un elemento de datos de otro nodo es mucho más lento que leer un elemento de la memoria local.

Por eso para este caso se particionara el tablero en subdominios donde cada procesador se encargara de procesar tableros mas pequeños NxN haciendo que el procesamiento sea mas rápido debido al particionamiento bidimensional.

![](RackMultipart20201024-4-1ap5r3f_html_2b87881f334ecae1.png)

Particionamiento unidimencional VS particionamiento bidimencional

1. **Comunicación**

Como lo mencionamos anteriormente el tablero general de lifegame se dividirá en subdominios o tableros mas pequeños donde estos harán subcalculos para entregarnos las matrices resultantes de cada partición, ahora por el lado de la comunicación se tiene que cada tablero tiene que comunicar sus bordes con 8 tableros mas (Izquierda superior, superior, derecha superior, derecha, derecha inferior, inferior, izquierda inferior, izquierda) para así obtener los estados de las células en las filas y columnas externas

![](RackMultipart20201024-4-1ap5r3f_html_b4d30cda0a162fca.png)

1. **Aglomeración**

Se tendrá un tablero 3X3 donde a su vez cada casilla será un subtablero sin sus bordes, para cada tablero general (3X3) se encargará un core de generar el resultado de la siguiente iteración, así agrupando los procesamientos en grupos más robustos y que tengan más rapidez y eficiencia a la hora de calcular el tablero completo.

Esto hace que tableros con un N grande sea más eficiente y poder tomar decisiones de cuantos cores utilizar dependiendo del tamaño del mismo, haciendo así la solución más escalable.

![](RackMultipart20201024-4-1ap5r3f_html_57b43c5909a9a203.png)

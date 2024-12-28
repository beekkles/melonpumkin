#import "@preview/diagraph:0.3.0": *

#set page(paper: "a4")
#set text(lang: "es")
#set par(justify: true)

= Random Ticks

Un _chunk_ es una porción del mundo representada por un prisma rectangular de dimensiones $16 times y times 16$, donde $y$ corresponde a la altura y toma valores en el rango $y in {-64, -63, ..., 0, ... , 318, 319}$. Cada _chunk_ se encuentra dividido en _subchunks_, cada uno con una altura fija de $16$ bloques. Dado que el rango de $y$ abarca $384$ unidades $(320 - (-64) + 1 = 384 )$, el número total de _subchunks_ por _chunk_ es:
$ 385 / 16 = 24 "."$

Cada _subchunk_ es, a su vez, una matriz tridimensional de dimensiones $16 times 16 times 16$, lo que equivale a un total de $16^3 = 4096$ bloques por subchunk.

Cada segundo el juego procesa $20$ _game ticks_, lo que equivale a un tick cada $0.05$ segundos.

Durante cada _game tick_, para cada _subchunk_ tenemos 3 _random ticks_ en una posición $(i,j,k)$ del mismo, donde $0<=i,j,k<16$, llamaremos a estas posiciones $ alpha_1, alpha_2, alpha_3$.

#let probtick = 1.0 - calc.pow(1 - 1/4096, 3)

La probabilidad de que un random tick afecta $alpha$ son de $1/4096$
para cada random tick, y dado que tenemos 3 random ticks por game tick tendremos que $ P(alpha) = 1 - (1- 1/4096)^3 = #probtick $ 

Si $alpha$ es afectada por un _random tick_, se genera un cambio de estado. Más adelante analizaremos el impacto de esto.

= Mecánica de crecimiento de `StemBlock`

Solo nos importa el caso en que `AGE = 7` y `mayPlaceOn = True`, no me voy a gastar en explicar como llega ahí

= Condiciones necesarias para `getFruit` (dado `StemBlock AGE = 7`)

Una vez tenemos que `StemBlock AGE = 7`, las condiciones necesarias para que `AGE = 8` y por lo tanto crezca un melón (`getFruit`), dado el `StemBlock` $rho = (x,y,z)$:

 - *$rho$ es afectado por un random tick*

 - Nivel de luz en  $rho >= 9$.

 - Es aire $(x+1,y,z) or (x-1,y,z) or (x,y,z+1) or (x,y,z-1)$, esta posición la llamaremos $(x',y',z')$

 - $y'-1$ es un bloque etiquetado como `DIRT`

 - En el caso de que más de una posición cumpla lo anterior, selecciona una al azar.

#figure(
grid(columns: 2,
	gutter: 2mm,
	image("img/stemblock1.png", width: 70%),
	image("img/stemblock2.png", width: 70%)),
caption: "Ejemplos de configuraciones válidas"
)

= Modelo clásico

El modelo clásico es un patrón de 1 y 1 entre stemBlock y posición válida, donde 
#figure(image("img/classic_instant.png",width:80%))

El mejor patrón posible es
#figure(image("img/classic_instant_pattern.png",width:60%))

Donde tenemos un total de $40$ stemBlocks

Cuando se actualiza el stemBlock generanto un melón, tenemos que esperar un total de $5$ game ticks para que ese espacio sea elegible de nuevo.

== Vamos a simularlo!
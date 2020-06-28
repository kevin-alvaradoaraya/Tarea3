Modelos Probabilísticos de Señales y Sistemas

Tarea 3

Estudiante: Kevin Alvarado Araya

Carnet: B60295

Grupo: 01

Punto 1
Al graficar los valores de fX(x) y fy(Y) se observa que poseen una tendencia similar a una distribución gaussiana. Se crea la función “gauss” para calcular los parámetros mu y sigma de la distribución.

Python calcula los parámetros de la distribución al aplicar la función curve fit a “gauss”, la variable aleatoria y función de densidad marginal.

Por lo tanto, la curva de mejor ajuste para la función de densidad marginal de X es una distribución normal con media 9.904843810018251 y varianza 3.2994428643069567. 

La función marginal fY(y) se aproxima como una función normal con media 15.079460901084733 y varianza 6.0269377486808775.

Punto 2

Al asumir una independencia estadística entre las variables X y Y, se puede afirmar que la función de densidad conjunta es equivalente al producto de las funciones de densidad marginales, es decir, fXY(x,y) = fX(x)*fY(y).

Punto 3

La correlación de este conjunto de datos es Rxy = 149.4773100000001 al ser diferente de cero, implica que los conjuntos no son ortogonales 

El resultado de la covarianza Cxy = 0.11760503547873213 sugiere que  la variable X es independiente o no correlacionada de la variable Y.

El coeficiente de correlación p = 0.005914099124709811, bastante cercano a cero. Por lo tanto se concluye que las variables aleatorias X y Y son independientes. De esta forma se comprueba lo planteado en el Punto 2.

Punto 4

Las gráficas se adjuntan en el repositorio actual. Las gráficas fX(x) y fy(Y) muestran una tendencia gaussiana en su distribución, en las gráficas gaussX y gaussY se comparan las funciones de distribución marginales con las curvas de mejor ajuste identificadas. Mientas que la imagen fXY muestra la distribución tridimensional de la función de densidad conjunta.


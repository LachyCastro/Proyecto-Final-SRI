# Proyecto de Sistemas de información.

<center>Rainel Fernández Abreu C312, Lázaro Alejandro Castro Arango C311</center>
</br>
<center> Facultad de Matemática y Computación </br> Universidad de la Habana</center>

> **Resumen:** <div style="text-align: justify">Se implementaron tres modelos de Recuperación de Información, programados en `Python`, con una interfaz visual diseñada en `Django`. Cada modelo fue diseñado en 4 etapas fundamentales: Procesamiento de texto, Procesamiento de consulta, Modelos y por último la Interfaz, donde el primero y último de estos 4 es común para cada modelo. Con el objetivo de evaluar los modelos se implementaron los criterios de evaluación pertinentes.</div>

#### 1. Requerimientos de software

- Python 3.7

- sklearn

- re

- nltk 3.0

- django 3.2

- numpy

#### Procesamiento de texto:

<div style="text-align: justify">Para poder implementar mecanismos de recuperación sobre una colección de documentos de texto es necesario obtener una representación de los mismos. Con el objetivo de lograr dicha representación seguimos un conjunto de pasos para dejar solo los términos de los textos que van hacer útil para la posterior recuperación de información, lo cual además, hace muy mucho más rápido el trabajo con cada modelo.</div>

Haciendo uso de la librería ***re*** de python para el trabajo con patrones en strings, reemplazamos todos las posibles contracciones que se utilizan en el idioma inglés por su respectiva forma correcta(Ejemplo: you're--you are, aren't-- are not), luego utilizando **nltk** eliminamos todas las stopwords(palabras que no aportan significado) y signos de puntuaciones. Para un mejor ***stemming*** utilizamos la clase ***SnowballStemmer*** de ***nltk***, la cual nos reduce en gran medida la cantidad de términos con los que vamos a trabajar. Devolviendo una lista de tokens, para su posterior utilización.

<div style="text-align: justify">Sería demasiado costoso tener que hacer todo este proceso sobre los documentos de un *corpus* cada vez que se requiera recuperar información de algún documento. Para esto guardamos información en diccionarios utilizando la librería *pickle* que nos permite almacenar información en archivos de extensión *.txt* para luego cargarla y utilizar dicha información.</div>

#### Procesamiento de consulta:

<div style="text-align: justify">Al igual que se procesan cada uno de los documentos, las consultas necesitan ser procesadas para llevar las palabras a su raíz, chequear la colocación de parentesis, asi como el exceso o falta de operadores booleanos (and , or, not), en dependencia del modelo que se desee utilizar.</div>

#### Modelos:

El modelo vectorial fue el primero que elegimos por la sencillez a la hora de implementar el mismo. Este modelo requería calcular *tf* e *idf*, para eso dicha información se guardaba y decidimos reutilizarla en algún otro modelo, por ello decidimos implementar el Booleano extendido, pues era sencillo reutilizar los diccionarios que ya teníamos con dicha información. La decisión de implementar el Booleano como último modelo fue por la sencillez de comprender e implementar el mismo.

<center>Modelo Vectorial</center>

<div style="text-align: justify">Representa documentos en lenguaje natural de una manera formal mediante el uso de vectores.En esta representación vectorial de documentos el éxito o fracaso se basa en la ponderación o peso de los términos. Aunque ha habido mucha investigación sobre técnicas de ponderación de términos, en realidad no hay un consenso sobre cuál método es el mejor.</div>

Para implementar el modelo vectorial, se necesita información como el *tf* e *idf* de los términos de la query y los documentos. Esta información se carga de los diccionarios que se guardan en el procesamiento de texto. A partir de la información necesaria se crea un ranking utilizando la función de similitud del modelo. Se crea un ranking de los documentos que se ordena de forma descendent y se muestra al usuario los documentos ordenados por su ranking.

<center>Modelo Booleano</center>

En el modelo booleano los vectores se representan de forma binaria, para cada término si se encuentra en un documento este se representará con un 1, sino, con un 0.
Para cada consulta en el modelo, se chequea que la consulta este bien escrita y luego se pasa a intentar recuperar los documentos.
Como todos nuestros modelos, este utiliza los diccionarios ya cargados para comprobar de manera eficiente si un término pertenece o no a un documento. Por cada término de la consulta se verifica la pertenencia o no al documento $i$ , si aparece este término pasa a ser True y se evalúa la expresión final, si es 1 (True), el documento es recuperado.

<center>Modelo Booleano Extendido</center>

#### Interfaz visual:

#### Evaluación del sistema:

**Precisión:**

**Recobrado:**

**Medida F:**

**F1:**

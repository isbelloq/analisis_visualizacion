# # Introducción a Jupyter Notebooks
# ---
#
# Los *notebooks* de [Jupyter](https://jupyter.org/) son documentos con un entorno computacional interactivo integrado, que permiten organizar y ejecutar código fuente de lenguajes de programación como *Python* o *R*. En otras palabras, podemos pensar en un *notebook* como una "página web entiquecida" donde vamos a poder tomar apuntes en forma de texto, títulos, imágenes, enlaces web y lo más importante, vamos a poder ejecutar código fuente de forma interactiva.
#
# Estos es posible con el uso de *kernels*, software que provee soporte a un leguaje de programación específico. En el transcurso del proma de formación virtual en *Machine Learning and Data Science* de la Universidad Nacional de Colombia se trabajará con el kernel de [IPython](https://ipython.org/) para [Python 3](https://www.python.org/)
#
# Estos documentos funcionan con la ejecución de aplicaciones web, que controlan y permiten la interacción con el sistema operativo.. Para ejecutar estas aplicaciones se consideran dos escenarios.
#
# 1. Con software ejecutado en una máquina local como un computador.
# 2. En la nube mediante plataformas especialzadas.
#
# En el primer caso, para trabajar en local con Notebooks de *Jupyter* recomendamos usar [Anaconda](https://www.anaconda.com/products/individual), un entorno especializado para la ciencia de datos que trae por defecto la posibilidad de trabajar con *notebooks* de *Jupyter con *Python*. Además, para una mayor flexivilidad y personalización se pueden configurar entornos de desarrollo (como [Visual Studio Code](https://code.visualstudio.com/) o [PyCharm](https://www.jetbrains.com/pycharm)) para el desarrollo de *notebooks* de *Jupyter* con añadidos como la compleción de código o herramientas para depurar y ejecutar sus programas. Estos permiten la interacciòn con *Anaconda*.
#
# En el segundo caso, para trabajar en la nuve, se recomienda trabajar con [*Google Colaboratory*](https://colab.research.google.com/notebooks/intro.ipynb) o simplemente *Colab*, un entorno gratuito de *notebooks* basados en *Jupyter* que no requiere configuraciòn y se ejecuta completamente en la nube. Adicionalmente, es posible acceder a entornos computacionales avanzados con hardware especializado GPU o TPU, gracias a la infraestrutura computacional que ofrece *Google Cloud Platform*.
#
# **La opción recomendada desde el programa de formación en MLDS es *Google Colab*** y el desarrollo de este tutorial y de los materiales que encontrará en su ruta de aprendizaje se realizó tomando esta plataforma como referencia.
#
# > Nota: En este Git el desarrollo se trabajará con [pyenv](https://github.com/pyenv/pyenv) para la administración de versión de Python, [poetry](https://python-poetry.org/docs/) para la administración de paquetes, por último, para la creación de notebooks en *Jupyter* se trabaja con el complemento de [jupytext](https://jupytext.readthedocs.io/en/latest/)

# ## 1. Celdas de texto
# ---
#
# El primer tipo de celda es uno con el que ya ha interactuado en el transcurso de este material. Se trata de las **celdas de texto**, con las que podremos dar estructura y forma a la presentación de nuestro *notebook*.
#
# Las celdas de texto usan sintaxis propia de un lenguaje de marcado que permite combinar texto con código de lenjuajes como *HTML* o *LaTeX*. El lenguaje utilizado se llama *Markdown*, el cual tiene ligeras diferencias entre sus versiones para *Jupyter* y *Colab*. Se trata de una especificación ligera para la escritura de contenido HTML. si quiere conocer más acerca de este lenguaje, lo invitamos a consultar su documentación y guía de inicio de [markdown](https://colab.research.google.com/notebooks/markdown_guide.ipynb)

# ### Markdown
# ___
#
# A continuación, se presentan algunos ejemplos de celdas de texto comunes. Puede dar **doble-click** en cada celda para conocer y editar su contenido. Luego, hacer **click** por fuera de la celda para ver su resultado.

# Haga **doble-click** aquí para ver el código fuente de esta celda:
#
# # Este es un título
# ## Los numerales
# ### Indican el tamaño
# #### Del título y
# ##### Son usados por Colab
# ###### En su tabla de contenido.

# Se pueden usar separadoes horizontales así:
#
# ---
#
# o así:
#
# ***
#
# Es es un texto nomal.
#
# *Se pueden hacer cursivas* **y negrillas.**
#
# _También se puede_ con __barra al piso.__
#
# Y __*combinados*__ ***de varias*** *__maneras.__*

# Se puede usar texto con estilo de código en una linea:
#
# `!python --version`
#
# O como un bloque:
# ```python
# def hello_world():
#     print('Hello World!')
# ```
#
# Incluso en negrilla: **`print('Hello World!')`**
#
# > Se puede definir bloques de texto en formato de cita.
#
# * Se pueden
# * definir
# * listas sin orden
#
# 1. Y también
# 2. listas
# 3. ordenadas
#     * Incluso
#     * anidadas
#     * usando la indentación.
#     
# También se pueden agregar enlaces a [sitios web](https://www.python.org).
#
# O agregar imágenes ![Python logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

# ### LaTeX
# ---
#
# [LaTeX](https://www.latex-project.org/) es un lenguaje más conocido para escribir expresiones especiales como fórmulas matemáticas. Para incluir fórmulas u otras expresioness matemáticas se escribe uan expresión en lenguaje LaTeX entre un par de signos **\$**.
#
# Por ejemplo `$\sqrt{3x-1} + (1+x)^2$` se visualiza así:
#
# $\sqrt{3x-1} + (1+x)^2$

# ### HTML
# ---
#
# Otra funcionalidad muy importante e los Jupyter Notebook es su intgración con el lenguaje [HTML](https://developer.mozilla.org/es/docs/Web/HTML), usado en desarrollo de  documentos de hipertexto para páginas web. Si bien *Markdown* admite HTML, en *Colab* a veces es necesario emplear celdas de código (se verá en la suiente sección) mediante la etiqueta `%%html`. En la mayoría de los casos, *Markdown* es suficiente para la disposición de la mayoría de los recusos audiovisuales, como imágenes o tablas

# + language="html"
# <marquee direction = "left" scrollamount="20" onmouseover="stop()" onmouseout="start()">
#     <h1 style="color: #ff9900; text-align: center"> Esta es una introducción a los Jupyter Notebook con Google Colaboratory</h1>
#     <h2 style="color: #ff9900; text-align: center"> Programa de formación en Machine Learning and Data Science</h2>
#     <h2 style="color: #ff9900; text-align: center"> Universidad Nacional de Colombia</h2>
#     <img style = "display: block; margin-left: auto; margin-right: auto;" src='https://colab.research.google.com/img/colab_favicon.ico' width='200' height='200'/>
# </marquee>
# -

# ## 2. Celdas de código
# ---
#
# El otro tipo de celda permitida en los *Notebooks* es la **celda de código**.
#
# Estas celdas permiten  escribir código fuente en el lenguaje de programación que soporte el *kernel* empleado. En la esquina superior derecha se indicará que el entorno de ejecución está conectado, o e su defecto le dará la opción para conectarse (haciendo clic en "Conectar"). Este material, y el resto de los materiales presentados en los dos primeros módulos, está diseñado para ser ejecutado en el leguaje de programación ***Python 3.6 o superior***.
#
# > Nota: Por el ambiente preparado en pyenv, se actuliza la versión a Python 3.8.12.
#
# Los *notebooks* ofrecen una gran flexibilidad de intreacción, al permitir acciones como la carga y descarga de archivos, el uso de entrada del teclado y la presentación de contenido multimedia como texto, imágenes y videos. Usted puede ejecutar el código de una celda con el botón de *play* (al cosado izquierdo de la celda en Colab), en el boón *Run* (En la barra de herramientas en Jyputer) o mediante la combinación de teclas **Shift + Enter**

# Ejecute esta celda con el botón de ejecutar o la combinación de teclado Shift + Enter
# !python --version

# Definición variable
a = 4

print(a)

# Se puede escrivir un programa completo como el pesentado a continuación. No se preocupe si no entiende lo que está escrito, simplemente ejecute la celda y siga las instrucciones. en los próximos materiales se realizará un taller de lenguaje de programación *Python* donde entenderá los pincipios de programación de computadores necesarios para el desarrollo de este programa de formación.

# +
x = 1
nombre = input('Por favor, ingrese su nombre.\n')
print(f'¡Hola {nombre}!\nLe damos la bienvenida al programa de formación en Machine Learning y Data Science.')

total = 0
conjunto = set()
while(total < 5):
    fruta = input(f'Ingrese el nombre de una fruta. {5-total} restantes.\n')
    conjunto.add(fruta)
    
    total = len(conjunto)
    
    print(f'Ha ingresado {total} {"fruta" if total == 1 else "frutas"} distintas.')
    
frutas = list(conjunto)
frutas.sort()

print('Estas son las frutas que ingresó ordenadas alfabéticamente.')

for fruta in [f'\t{i + 1}.\t {frutas[i]}' for i in range(len(frutas))]:
    print(fruta)

# -

# Las variables declaradas se conservan entre celdas.

print(frutas)

# Incluso, y como veremos más adelante en el módulo, es posible realizar visualizaciones más complejas dentro de los notebooks. Por ejemplo:

# +
import numpy as np
from matplotlib import pyplot as plt

y = 100 + np.random.randn(100)
x = [x for x in range(len(y))]
plt.plot(x, y, '-')
plt.title("Gráfica de ejemplo")
plt.show()
# -

# ## 3. Compledato de código y ayuda
# ---
#
# Los *Jypyter Notebook* de *Google Colaboratory* cuentan con una heramienta de auto-completado, posible presionando la combiación de teclas **Ctrl + Espacio**.
#
# Por ejemplo importemos el módulo [NumPy](https://numpy.org/) (se discutirá en detalle en los demás materiales de la primera unidad) con el alias **np**.

import numpy as np

# Luego escriba `np.random.` (Si está en *Colab* presione la secuencia **Ctrl + Espacio**. Si está desde *Jupyter* presione **Tab**.). Debería ver las opciones posibles de auto-completado para np.random.

np.random.

# Para abrir la documentación completa de un módulo sólo debe presionar **Shitf + Enter** sobre una celda de código con el nombre del paquete a exploar seguido de **?**.

# +
# np.random.randint?
# -

# ## 4. Intalar otra biblioteca
# ---
#
# El entorno de ejecución de *Jupyter* permite ejecutar comandos del sistema operativo mediante el símbolo **!**. Por ejemplo, para instalar módulos o librerias específicas de Python se utiliza el comando `pip`. La secuencia de comandos `pip install` permite especificar el módulo que se desea instalar.
#
# En *Google Colab*, el entorno de ejecución está construido encima de una máquina virtual del sistema operativo *Ubuntu*. Al trabajar en local desde otro sistema operativo como *Windows* o *Mac*, los comando pueden ser distintos y algunos puntos de este tutorial podrían no funionar.
#
# > Nota: Como la administración de paquetes se hace desde poetry, se reemplaza `pip install` por `poetry add`

# !poetry add -D leaflet

# La librería se instaló correctamente. Esta funcionalidad será muy importante más adelante en el curso.

# ## 5. Carga archivos a Google Colab
# ---
#
# Al trabajar con *Google Colab*, una de las primeras preguntas que se pueden presentar es el manejo de archivos con el entrono en la nube. Se consideran dos opciones para la carga de archivos desde un equipo local.
#  > Atención: Los comandos discutidos a continuación son exclusivos para la plataforma Colab. si se está trabajando con otras herramientas el manejo de archivos se realiza organizando las carpetas en las que está alojado el archivo .ipynb del *notebook.*

# ### Carga de archivos locales
# ___
#
# Al estar en la nube suele ser necesario subir archivos desde una máquina local para su carga y exploración. Para esto deberá hacer clic en la parte derecha del notebook donde aparece el icono de "Archivos" (una carpeta o directorio) y luego podrá hacer clic sobre el icono "Subir" (un archivo con una flecha apuntando hacia arriba) para seleccinar los archivos que desea cargar.
#
# Otra forma de conseguirlo, será mediante programación, como se muestra a continuación:
#
# > Atención: Los archivos que se carguen o generen solo lo harán temporalmente. Cuando la instancia de ejecución termine (cuando se desconecte el *notebook*), estos se borrarán. Para evitar esto se recomenda trabjar con archivos en la nube, como con *Google Drive*

# +
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(
        name=fn, length=len(uploaded[fn])))
# -

# Para ver la lista de los archivos que tiene en el directorio actual:

# El comando ls da una lista de los archivos en un directorio.
# !ls

# ### Carga desde *Google Drive*
# ___
#
# *Google Colab* tiene interacciones con otras herramientas de Google. En particular, se puede vincular una unidad de [Google Drive](https://www.google.com/drive/) para el acceso a archivos alojados en la nube en la ejecución del *notebook*.
#
# Al ejecutar la celda aparecerá una URL de autenticación de la cuenta de Google. Una vez en esta página, acepte los permisos de uso de *Google Drive* y copie el token de autentiación generado. Péguelo en la celda de código. La unidad de *Google Drive* quedará montada como un directorio más del sistema de archivos.

from google.colab import drive
drive.mount('/gdrive')

# !ls "/gdrive/My Drive"

# ## 6. Recursos adicionales
# ---
#
# * [Introducción a *Google Colaboratory* (notebooks)](https://colab.research.google.com/notebooks/intro.ipynb)
# * [Guía de Markdown](https://colab.research.google.com/notebooks/markdown_guide.ipynb)
# * [*Python* 3: documentación oficial.](https://docs.python.org/3/)
#
# ## 7. Créditos
# ---
#
# * **Profesor:** [Felipe Restrepo Calle](https://dis.unal.edu.co/~ferestrepoca/)
# * **Asistentes docentes:**
#   - Alberto Nicolai Romero Martínez
#   - Miguel Angel Ortiz Marín
#
# **Universidad Nacional de Colombia** - *Facultad de Ingeniería*

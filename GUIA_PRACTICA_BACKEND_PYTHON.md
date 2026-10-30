# Guía de práctica: Python para comenzar en backend en Windows

Esta guía es tu plan de trabajo para practicar programación con el acompañamiento de tu mentor. Vas a construir los ejercicios dentro de tu repositorio actual y a documentar lo que aprendes.

Los comandos están preparados para **Windows con PowerShell**. Antes de ejecutarlos, lee las definiciones de terminal, comando y raíz del repositorio en la sección siguiente.

La primera meta es dominar 20 problemas básicos: comprenderlos, escribir sus soluciones desde cero, probarlas y adaptarlas a una variante. Después avanzarás hacia otros patrones y estructuras de datos.

**Empieza por la preparación del repositorio y el primer ejercicio. La lista completa es una ruta; avanza tema por tema.**

## 0. Conceptos para empezar desde cero

Si encuentras una palabra que no conoces, consulta su definición aquí o abre el enlace de documentación del tema. Puedes añadir nuevas palabras a tu archivo de notas.

| Concepto | Definición breve |
| --- | --- |
| Backend | Parte de una aplicación que procesa reglas, trabaja con datos y responde a solicitudes, normalmente en un servidor. |
| Git | Herramienta que registra el historial de cambios de los archivos de un proyecto. [Introducción oficial](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git). |
| Repositorio | Proyecto cuyo historial de archivos y cambios está administrado por Git. En esta guía trabajarás con el que ya tienes. |
| Raíz del repositorio | Carpeta principal del proyecto, dentro de la cual están sus demás carpetas y archivos. |
| Terminal | Aplicación o panel donde escribes comandos y lees sus resultados. |
| PowerShell | Programa que interpreta los comandos que escribes en la terminal. En Windows puedes abrirlo buscando “PowerShell” en Inicio. [Documentación de Microsoft](https://learn.microsoft.com/es-es/powershell/scripting/overview). |
| Comando | Instrucción que escribes en la terminal y ejecutas pulsando Enter. Copia el contenido de los bloques de comandos; las marcas de formato no forman parte del comando. |
| Ruta | Ubicación de un archivo o carpeta. `C:\proyectos\practica` es una ruta completa; `.\ejercicios` parte de la carpeta donde estás situado. |
| Intérprete de Python | Programa que ejecuta tu código Python. En Windows normalmente tiene un ejecutable llamado `python.exe`. |
| Script | Archivo con código que puedes ejecutar. En este proyecto, los scripts de Python usan la extensión `.py`. |
| Editor de código | Programa donde escribes y guardas los archivos del proyecto. Usa el que ya tengas configurado con tu mentor. |
| Markdown / `.md` | Formato de texto que permite escribir títulos, listas, enlaces y bloques de código. Esta guía es un archivo Markdown. |
| `README.md` | Archivo de presentación e instrucciones del proyecto o de una carpeta. Puedes leerlo y editarlo como texto. |
| Extensión | Parte final del nombre que ayuda a identificar el tipo de archivo: `.py` para código Python o `.md` para Markdown. |
| UTF-8 | Codificación: una forma de guardar caracteres en un archivo, incluidas letras con acentos. Elige UTF-8 al guardar el código y las notas. |
| Entorno virtual / `.venv` | Carpeta que contiene un Python y paquetes asociados al proyecto. Permite mantener sus dependencias separadas de las de otros proyectos. [Documentación de venv](https://docs.python.org/3/library/venv.html). |
| Dependencia o paquete externo | Código de terceros que un proyecto necesita instalar para funcionar. En esta primera etapa no agregarás paquetes externos. |
| Biblioteca estándar | Herramientas que vienen con Python, como `unittest` para ejecutar pruebas o `pathlib` para manejar rutas. |
| Módulo e importación | Un módulo agrupa código reutilizable; muchos módulos son archivos `.py`. Importar significa traer sus funciones o clases a otro archivo con `import` o `from ... import ...`. |
| Prueba automática o test | Código que ejecuta una función y comprueba si se comporta como esperas. Por ejemplo, verifica que invertir `"abc"` produzca `"cba"`. |
| Caso límite | Entrada que pone a prueba una condición especial, como una lista vacía o un texto de un solo carácter. |
| Depurador y traza | Un depurador permite detener el programa y observar sus variables. Una traza es el registro de cómo cambian, que también puedes construir a mano. |
| Contrato de una función | Reglas sobre lo que recibe, lo que devuelve, lo que modifica y los errores que debe producir. |
| Implementación | Código concreto que escribes para cumplir el contrato o resolver el problema. |

## 1. Cómo estudiar

Aplica este proceso en cada ejercicio:

1. **Lee el enunciado.** Explica con tus palabras qué recibe la función y qué debe devolver o modificar. Si una condición es ambigua, aclárala con tu mentor.
2. **Resuelve un ejemplo a mano.** Escribe los pasos antes de programar. Incluye al menos un caso pequeño y uno que podría causar un error.
3. **Haz un intento propio.** Como referencia, dedica 20–30 minutos. Si te bloqueas, escribe exactamente qué parte no sabes resolver y pide una pista.
4. **Comprende la solución.** Si necesitas consultarla, sigue cada variable con un ejemplo y explica por qué cada paso es necesario.
5. **Cierra la referencia y reconstruye el código.** Escribe la solución en un archivo vacío. El objetivo es poder reproducir el razonamiento y la implementación.
6. **Ejecuta las pruebas.** Cuando algo falle, identifica el ejemplo mínimo que reproduce el error y usa el depurador o una traza de variables.
7. **Documenta y repite.** Registra la complejidad, un error que cometiste y una variante. Como calendario inicial de repaso, vuelve a intentarlo al día siguiente, a los tres días y a la semana; ajústalo según tus resultados.

Puedes consultar sintaxis y documentación. Si usas IA, empieza pidiendo una pista, una explicación de un concepto o la revisión de tu intento. Cuando hayas visto una solución completa, ciérrala y vuelve a resolver el ejercicio por tu cuenta.

### Qué significa aprenderlo de memoria

Debes recordar el propósito de las variables, el recorrido de los datos, la condición de salida y la razón por la que el resultado es correcto. También debes poder escribir el código sin copiarlo.

Un ejercicio está dominado cuando puedes:

- [ ] Explicar el problema y sus restricciones.
- [ ] Resolver un ejemplo a mano.
- [ ] Implementarlo desde cero.
- [ ] Pasar las pruebas y explicar los casos límite.
- [ ] Justificar su costo en tiempo y memoria.
- [ ] Resolver una variante pequeña sin consultar la solución.

Primero implementa el algoritmo que se quiere practicar. Después escribe una segunda versión usando las herramientas habituales de Python y compara ambas. Las restricciones sobre `max()`, `sorted()` o slices son específicas del ejercicio.

## 2. Prepara tu repositorio

Trabaja dentro del repositorio que ya tienes. Conserva los archivos y la organización de tu proyecto; agrega la carpeta `ejercicios/` en la raíz.

1. Guarda esta guía en la raíz como `GUIA_PRACTICA_BACKEND_PYTHON.md` y enlázala desde el `README.md` del proyecto.
2. Comprueba que tienes Python 3.10 o posterior.
3. Crea un entorno virtual llamado `.venv`. Si tu proyecto ya utiliza ese entorno, aprovecha el existente y salta su creación.
4. Crea la estructura de ejercicios descrita en la siguiente sección.

Abre PowerShell y entra a tu repositorio. Sustituye esta ruta de ejemplo por la ruta real de la carpeta del proyecto; conserva las comillas si contiene espacios:

```powershell
Set-Location "C:\ruta\a\tu\repositorio"
```

`Set-Location` cambia la carpeta donde estás situado. Para ver cuál es la carpeta actual puedes ejecutar `Get-Location`.

Comprueba la versión de Python:

```powershell
py -3 --version
```

Si `py` no se reconoce, prueba `python --version`. Si ninguno está disponible, instala Python siguiendo la [guía oficial para Windows](https://docs.python.org/3/using/windows.html) y vuelve a abrir PowerShell.

`py -3` pide ejecutar Python 3 y `--version` muestra su versión. No hace falta que el número coincida exactamente con 3.10; puede ser una versión posterior.

Si la versión encontrada es 3.10 o posterior, crea el entorno con el comando que haya funcionado:

```powershell
py -3 -m venv .venv
```

Alternativa si utilizas `python`:

```powershell
python -m venv .venv
```

Ejecuta solo una de esas dos opciones. Después comprueba el Python del entorno:

```powershell
.\.venv\Scripts\python.exe --version
```

Los comandos de esta guía llaman directamente a `.\.venv\Scripts\python.exe`. Así puedes trabajar aunque el entorno no esté activado.

En una ruta de PowerShell, `.\` significa “desde la carpeta actual”. En un comando de Python, `-m nombre` ejecuta un módulo; por ejemplo, `-m venv` ejecuta la herramienta que crea el entorno virtual.

Activar el entorno hace que el comando corto `python` apunte al Python de ese entorno en la terminal actual. Es opcional:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell indica que la ejecución de scripts está deshabilitada, continúa usando los comandos con `python.exe` que aparecen en la guía. Ese camino no requiere cambiar la política de ejecución. Cada vez que abras otra terminal, vuelve a la raíz del repositorio antes de ejecutar los comandos.

La política de ejecución es una configuración de PowerShell que regula la ejecución de scripts como `Activate.ps1`.

Para estos ejercicios usaremos la biblioteca estándar, incluido `unittest` para las pruebas. No necesitas instalar paquetes adicionales.

Al guardar los archivos, usa codificación UTF-8 y verifica que las extensiones sean `.py` o `.md`, según corresponda. Por ejemplo, el script debe llamarse `crear_estructura.py`, sin una extensión `.txt` adicional.

### Qué es `.gitignore` y cómo prepararlo

`.gitignore` es un archivo de texto con patrones que indican a Git qué archivos locales todavía no registrados debe ignorar. Aquí lo usaremos para excluir el entorno virtual y archivos que Python genera automáticamente. [Documentación oficial](https://git-scm.com/docs/gitignore).

En la raíz del proyecto, abre `.gitignore` con tu editor; si no existe, créalo con ese nombre exacto, incluido el punto inicial y sin agregar `.txt`. Añade estas líneas conservando las que ya tenga:

```gitignore
.venv/
__pycache__/
*.py[cod]
```

Qué significa cada línea:

- `.venv/`: ignora la carpeta del entorno virtual.
- `__pycache__/`: ignora carpetas donde Python guarda versiones compiladas para reutilizarlas al importar módulos.
- `*.py[cod]`: ignora archivos cuyos nombres terminan en `.pyc`, `.pyo` o `.pyd`; `*` permite cualquier nombre y `[cod]` una de esas tres letras.

`.gitignore` conserva los archivos en tu computadora y evita incluirlos como archivos nuevos por defecto. No deja de registrar archivos que Git ya seguía. Si aparecen cambios de `.venv/` en Git después de agregar el patrón, revisa ese caso con tu mentor.

## 3. Organiza temas y ejercicios

Usa nombres en `snake_case`: palabras en minúsculas separadas por guion bajo, como `invertir_cadena`. Evita espacios y acentos en los nombres de archivos. La numeración de los ejercicios empieza en `e01_` dentro de cada tema.

Ejemplo de la estructura inicial:

```text
GUIA_PRACTICA_BACKEND_PYTHON.md
README.md
PROGRESO.md
ejercicios/
    __init__.py
    fundamentos/
        __init__.py
        teoria.md
        e01_fizzbuzz/
            __init__.py
            README.md
            solucion.py
            test_solucion.py
            notas.md
    cadenas/
        __init__.py
        teoria.md
        e01_invertir_cadena/
            __init__.py
            README.md
            solucion.py
            test_solucion.py
            notas.md
    listas/
    diccionarios_sets/
    pilas_colas/
```

Cada carpeta de tema y de ejercicio debe tener su archivo `__init__.py`, que puede estar vacío. Este archivo indica que la carpeta es un paquete de Python, es decir, una forma de organizar módulos. Así podrás importar las soluciones y descubrir sus pruebas de forma consistente. [Documentación de módulos y paquetes](https://docs.python.org/es/3/tutorial/modules.html#packages).

| Archivo | Lo que debes escribir |
| --- | --- |
| `teoria.md` de cada tema | Conceptos, operaciones, ejemplos propios y costos relevantes. Usa la teoría de esta guía como punto de partida y explícalo con tus palabras. |
| `README.md` de cada ejercicio | Enunciado, firma de la función, ejemplos, condiciones y casos límite. |
| `solucion.py` | La implementación. La lógica debe poder llamarse desde una función o clase. |
| `test_solucion.py` | Pruebas automáticas que comprueben el comportamiento esperado. |
| `notas.md` | Razonamiento, errores, complejidad, ayuda utilizada y variante realizada. |
| `PROGRESO.md` | Estado de cada ejercicio y resultados de los repasos. |

Puedes crear primero una carpeta manualmente para entender la estructura. Para preparar las demás, el script del final crea los 20 ejercicios con archivos vacíos o plantillas básicas y conserva los archivos existentes.

## 4. Fundamentos que debes manejar

Antes de comenzar, comprueba que puedes explicar y usar lo siguiente:

| Concepto | Qué debes comprender |
| --- | --- |
| Tipos básicos | `int`: enteros; `float`: números de punto flotante para representar valores con parte fraccionaria de forma aproximada; `bool`: verdadero o falso; `str`: texto; `None`: ausencia de valor. |
| Condiciones | Construir decisiones con `if`, `elif`, `else`, comparaciones y operadores lógicos. |
| Ciclos | Recorrer datos con `for` y repetir con `while`. Saber cuándo usar `break` y `continue`. |
| Funciones | Recibir argumentos y devolver resultados con `return`. Distinguir devolver un valor de imprimirlo. |
| Índices | La primera posición es `0`; en una secuencia no vacía, la última es `len(secuencia) - 1`. |
| Recorridos | Usar `range()` y `enumerate()` cuando necesites posiciones o posiciones y valores. |
| Estado | Distinguir un contador, un acumulador y una variable que conserva el mejor resultado encontrado. |
| Referencias | Comprender que dos variables pueden referirse al mismo objeto mutable. |

**Mutable** significa que puedes cambiar el contenido del mismo objeto, como agregar un elemento a una lista. **Inmutable** significa que no puedes cambiar ese contenido; una operación sobre una cadena produce otro valor. Un **booleano** es `True` o `False`; `None` representa la ausencia de un valor en los casos donde el contrato lo define así.

Una **firma de función** resume su nombre, parámetros y retorno. En `contar_vocales(texto: str) -> int`, el nombre es `contar_vocales`, el parámetro `texto` se espera de tipo `str` y el resultado de tipo `int`. Estas anotaciones de tipo ayudan a leer el código; por sí solas no validan los argumentos al ejecutar. `int | None` significa que el resultado puede ser un entero o `None`. [Funciones en Python](https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions).

Los corchetes de una anotación describen el contenido de una colección: `list[int]` es una lista de enteros; `dict[str, int]`, un diccionario con claves de texto y valores enteros; `tuple[int, int]`, una tupla de dos enteros. Un **parámetro** es el nombre que recibe un dato dentro de la función; un **argumento** es el valor que proporcionas al llamarla.

Observa este ejemplo antes de ejecutarlo y predice el resultado:

```python
a = [1, 2]
b = a
b.append(3)

print(a)
print(b)
print(a is b)
```

Después repítelo cambiando `b = a` por `b = a.copy()` y explica la diferencia. Esta copia es superficial: si hay listas dentro de la lista, los objetos internos siguen compartidos.

En ese ejemplo, `is` comprueba si dos variables apuntan al mismo objeto. `==` compara si sus valores son iguales. Para profundizar en los conceptos previos, usa la [introducción a Python](https://docs.python.org/es/3/tutorial/introduction.html) y las [herramientas de control de flujo](https://docs.python.org/es/3/tutorial/controlflow.html).

## 5. Teoría de estructuras de datos

### Cadenas: `str`

Una cadena representa texto y permite recorrerlo o acceder a posiciones. Es inmutable: no puedes reemplazar un carácter con una asignación como `texto[0] = "A"`.

Estudia índices, `len()`, slices, `split()`, `join()`, `lower()` e `isspace()`. Para construir texto por partes, aprende a acumular fragmentos y unirlos. Una expresión corta también puede recorrer o copiar muchos datos; debes considerar ese trabajo al analizarla.

Un **slice** o rebanada selecciona parte de una secuencia, como `texto[1:4]`; el límite final queda excluido. `split()` separa texto, `join()` une fragmentos, `lower()` obtiene una versión en minúsculas e `isspace()` comprueba si un texto no vacío está formado por espacios en blanco. [Referencia de cadenas](https://docs.python.org/es/3/library/stdtypes.html#text-sequence-type-str).

### Listas y vectores: `list`

Una lista es una secuencia mutable y permite cambiar elementos, agregarlos y quitarlos. CPython es la implementación de Python distribuida habitualmente desde python.org; en ella, `list` utiliza un arreglo dinámico de referencias. Esto permite acceder por posición y aumentar su tamaño cuando agregas datos. En este bloque estudiarás listas y vectores juntos.

Estudia acceso por índice, `append()`, `pop()`, `insert()`, `remove()`, `copy()`, `sort()` y `sorted()`. `sort()` modifica la lista y devuelve `None`; `sorted()` produce una lista nueva.

`append()` agrega al final; `pop()` retira y devuelve un elemento; `insert()` agrega en una posición; `remove()` quita la primera aparición de un valor; `copy()` hace una copia superficial. [Métodos de listas](https://docs.python.org/es/3/tutorial/datastructures.html#more-on-lists).

Una lista enlazada tiene una organización diferente: está formada por nodos conectados mediante referencias. La estudiarás en una fase posterior.

### Diccionarios: `dict`

Relacionan claves únicas con valores. Son útiles para contar apariciones, guardar posiciones y agrupar información. Estudia asignación, consulta, `get()`, `items()` y pertenencia con `in`.

Las claves deben ser hashables: su hash debe mantenerse estable y ser compatible con la igualdad. Cadenas y enteros pueden usarse como claves; las listas no. Una tupla puede ser clave si todos sus elementos son hashables.

Un **hash** es un número calculado a partir de un objeto que ayuda a ubicarlo en una tabla hash. Una **tupla**, escrita por ejemplo `(2, 5)`, es una secuencia cuyos elementos no puedes reemplazar después de crearla. [Definición de hashable](https://docs.python.org/es/3/glossary.html#term-hashable).

Ejemplo conceptual: un diccionario puede asociar el identificador de cada usuario con su número de peticiones.

### Conjuntos: `set`

Representan colecciones de elementos únicos y hashables. Son útiles para registrar elementos ya vistos y comprobar pertenencia. Estudia `add()`, `in`, unión, intersección y diferencia.

No tienen un orden de recorrido garantizado. Cuando un ejercicio exige conservar el orden original, convertir directamente una lista a conjunto no cumple por sí solo esa condición.

### Pilas y colas

Una **pila** sigue LIFO: el último elemento que entra es el primero que sale. Puedes usar una lista con `append()` y `pop()` al final. Un ejemplo es conservar acciones para deshacerlas en orden inverso.

Una **cola** sigue FIFO: el primer elemento que entra es el primero que sale. Para practicarla, usa `collections.deque`, con `append()` y `popleft()`. Un ejemplo es una fila de tareas por atender.

Antes del ejercicio de pila, estudia también los elementos básicos de una clase: `class`, el método de inicialización `__init__`, los atributos y el parámetro `self`.

Una **clase** define datos y operaciones para crear objetos. Cada objeto creado es una **instancia**; sus datos son **atributos** y sus funciones son **métodos**. `__init__` inicializa la instancia y `self` permite referirse a ella dentro de sus métodos. [Introducción a clases](https://docs.python.org/es/3/tutorial/classes.html).

## 6. Teoría de complejidad

La complejidad describe cómo crecen el trabajo y la memoria utilizados al aumentar el tamaño de la entrada. Big O no indica segundos exactos. Define qué representa `n` en cada problema.

| Orden | Idea | Ejemplo típico |
| --- | --- | --- |
| `O(1)` | El costo no crece con el número de elementos. | Acceder a una posición de una lista. |
| `O(log n)` | En cada paso se reduce el problema por un factor constante. | Búsqueda binaria en una lista ordenada. |
| `O(n)` | El trabajo crece proporcionalmente al tamaño de la entrada. | Recorrer una lista completa. |
| `O(n log n)` | Un orden frecuente en algoritmos eficientes de ordenamiento. | Ordenamiento incorporado de listas, en el peor caso. |
| `O(n²)` | El trabajo puede crecer como todas las parejas de elementos. | Dos recorridos anidados que comparan cada elemento con todos los demás. |

Costos que conviene recordar para los tipos incorporados de CPython:

| Operación | Costo temporal habitual |
| --- | --- |
| `lista[i]`, `len(lista)` | `O(1)` |
| `lista.append(x)` y retirar al final con `pop()` | `O(1)` amortizado |
| Buscar un valor con `x in lista` | `O(n)` |
| Insertar o retirar al inicio de una lista | `O(n)` |
| Copiar una lista de `n` elementos | `O(n)` |
| Obtener un slice de lista con `k` elementos | `O(k)` |
| Consultar una clave en un diccionario o pertenencia en un conjunto | `O(1)` promedio; `O(n)` en el peor caso |
| Ordenar una lista con `sort()` | `O(n log n)` en el peor caso |

**Amortizado** significa que una operación individual puede ser más costosa, pero el costo se reparte al considerar una secuencia de operaciones. **Promedio** en tablas hash supone una distribución adecuada de hashes y costos constantes de hashing e igualdad; algunas claves tienen costos propios que también cuentan.

Analiza también el espacio. Un recorrido puede tomar tiempo `O(n)` y usar solo unas variables adicionales, es decir, espacio auxiliar `O(1)`. Crear una colección que crece con la entrada requiere espacio proporcional a sus elementos. Indica si estás contando la salida como parte de la memoria.

Dos ciclos consecutivos que recorren `n` elementos hacen aproximadamente `2n` pasos: siguen siendo `O(n)`. Dos ciclos anidados no implican automáticamente `O(n²)`; debes contar cuántas veces se ejecuta el trabajo interno.

## 7. Los primeros 20 ejercicios

En estos ejercicios, las listas numéricas contienen enteros. Solo necesitas aceptar las entradas descritas; cualquier validación adicional debe acordarse con tu mentor. Para los textos iniciales usaremos caracteres sencillos, sin requisitos sobre emojis compuestos o normalización Unicode.

En cada problema completa los cinco archivos de su carpeta. Las condiciones siguientes forman parte del enunciado.

Cuando se pida **lanzar una excepción**, debes señalar un error con `raise`. `ValueError` indica un valor no aceptado e `IndexError` se usa aquí para consultar o retirar un elemento de una pila vacía. `NotImplementedError` señalará código pendiente en el esqueleto del ejemplo. [Errores y excepciones](https://docs.python.org/es/3/tutorial/errors.html).

Una **variante** es el mismo problema con alguna condición modificada. Los términos en inglés de los ejercicios se explican en cada enunciado; puedes consultar las operaciones y tipos en la [referencia de tipos incorporados](https://docs.python.org/es/3/library/stdtypes.html).

### Bloque A. Fundamentos

**1. FizzBuzz** · `fundamentos/e01_fizzbuzz`

- Firma: `fizzbuzz(n: int) -> list[str]`.
- Devuelve las representaciones de los números de `1` a `n`, ambos incluidos. Para múltiplos de 3 usa `"Fizz"`, de 5 `"Buzz"` y de ambos `"FizzBuzz"`.
- Ejemplo: `fizzbuzz(5)` devuelve `["1", "2", "Fizz", "4", "Buzz"]`.
- Casos: para `n <= 0`, devuelve `[]`; prueba también `n = 15`.
- Variante: recibe los dos divisores como parámetros positivos.

**2. Sumar dígitos** · `fundamentos/e02_sumar_digitos`

- Firma: `sumar_digitos(numero: int) -> int`.
- Recibe un entero no negativo y devuelve la suma de sus dígitos. Primera versión: usa operaciones aritméticas, sin convertirlo a texto.
- Ejemplos: `sumar_digitos(2048) == 14`; `sumar_digitos(0) == 0`.
- Variante: aceptar números negativos y sumar los dígitos de su valor absoluto.

**3. Número primo** · `fundamentos/e03_numero_primo`

- Firma: `es_primo(numero: int) -> bool`.
- Un primo es un entero mayor que 1 cuyos divisores positivos son únicamente 1 y él mismo.
- Ejemplos: `es_primo(7)` devuelve `True`; `es_primo(9)` devuelve `False`.
- Casos: negativos, 0 y 1 devuelven `False`; 2 devuelve `True`.
- Variante: después de una solución correcta, investiga hasta qué divisor necesitas comprobar y justifica ese límite.

### Bloque B. Cadenas

**4. Invertir una cadena** · `cadenas/e01_invertir_cadena`

- Firma: `invertir_cadena(texto: str) -> str`.
- Devuelve el texto en orden inverso, conservando mayúsculas, espacios y signos.
- Ejemplos: `"backend"` produce `"dnekcab"`; `"Hola!"` produce `"!aloH"`.
- Casos: `""` devuelve `""`; un carácter queda igual; `"a b"` produce `"b a"`.
- Primera versión: usa un ciclo, sin `[::-1]` ni `reversed()`.
- Variante: escribe otra versión usando las herramientas de Python y compara sus costos.

**5. Contar vocales** · `cadenas/e02_contar_vocales`

- Firma: `contar_vocales(texto: str) -> int`.
- Cuenta `a`, `e`, `i`, `o`, `u`, sin distinguir mayúsculas. Las vocales acentuadas quedan fuera de esta primera versión.
- Ejemplos: `"Hola"` produce `2`; `"AEIOU"` produce `5`; `"rhythm"` produce `0`.
- Caso: una cadena vacía devuelve `0`.
- Variante: incluir vocales acentuadas y diéresis.

**6. Palíndromo** · `cadenas/e03_palindromo`

- Firma: `es_palindromo(texto: str) -> bool`.
- Comprueba si el texto se lee igual de izquierda a derecha y de derecha a izquierda. En la versión inicial, espacios y mayúsculas cuentan exactamente como aparecen.
- Ejemplos: `"reconocer"` produce `True`; `"Python"` produce `False`; `"Aa"` produce `False`.
- Casos: la cadena vacía y una de un carácter devuelven `True`.
- Variante: ignorar mayúsculas, espacios y signos.

**7. Contar palabras** · `cadenas/e04_contar_palabras`

- Firma: `contar_palabras(texto: str) -> int`.
- Una palabra es una secuencia de caracteres separada por uno o más caracteres de espacio en blanco. Puedes reconocer separadores con `isspace()`.
- Ejemplo: `"  hola   mundo\nPython  "` produce `3`.
- Casos: texto vacío o formado solo por espacios en blanco devuelve `0`.
- Primera versión: recorre el texto sin usar `split()`.
- Variante: contar las apariciones de cada palabra.

### Bloque C. Listas y vectores

**8. Encontrar el máximo** · `listas/e01_maximo`

- Firma: `encontrar_maximo(numeros: list[int]) -> int`.
- Devuelve el mayor valor. Para una lista vacía, lanza `ValueError`.
- Ejemplos: `[3, 8, 2]` produce `8`; `[-5, -2, -9]` produce `-2`.
- Primera versión: sin `max()` ni ordenamiento; conserva la lista original.
- Variante: devolver también la posición de la primera aparición del máximo.

**9. Segundo mayor distinto** · `listas/e02_segundo_mayor`

- Firma: `segundo_mayor(numeros: list[int]) -> int | None`.
- Devuelve el segundo mayor valor distinto. Si existen menos de dos valores distintos, devuelve `None`.
- Ejemplos: `[5, 5, 3, 1]` produce `3`; `[4, 4]` produce `None`; `[-1, -3, -2]` produce `-2`.
- Casos: lista vacía y lista de un solo elemento devuelven `None`.
- Primera versión: un recorrido, sin ordenar ni convertir a conjunto; conserva la entrada.
- Variante: obtener el tercer mayor distinto.

**10. Invertir una lista** · `listas/e03_invertir_lista`

- Firma: `invertir_lista(numeros: list[int]) -> None`.
- Modifica la misma lista para invertir sus elementos y devuelve `None`.
- Ejemplo: después de llamar la función con `[1, 2, 3]`, esa lista contiene `[3, 2, 1]`.
- Casos: lista vacía y lista de un elemento.
- Primera versión: sin `reverse()`, `reversed()` ni slices; usa espacio auxiliar constante.
- Variante: devolver una lista invertida nueva y conservar la entrada.

**11. Mover ceros al final** · `listas/e04_mover_ceros`

- Firma: `mover_ceros(numeros: list[int]) -> None`.
- Modifica la lista para dejar los ceros al final y conservar el orden relativo de los demás valores. Devuelve `None`.
- Ejemplo: `[0, 1, 0, 3, 12]` pasa a `[1, 3, 12, 0, 0]`.
- Casos: lista vacía, todos ceros, ningún cero y números negativos.
- Meta: tiempo lineal y espacio auxiliar constante.
- Variante: trasladar al final cualquier valor recibido como parámetro.

### Bloque D. Diccionarios y conjuntos

**12. Frecuencias de caracteres** · `diccionarios_sets/e01_frecuencias`

- Firma: `contar_frecuencias(texto: str) -> dict[str, int]`.
- Cuenta cada carácter, distinguiendo mayúsculas e incluyendo espacios.
- Ejemplo: `"casa"` produce `{"c": 1, "a": 2, "s": 1}`.
- Caso: una cadena vacía devuelve `{}`. El orden de las claves no forma parte del resultado exigido.
- Primera versión: usa un diccionario, sin `collections.Counter`.
- Variante: contar palabras con una normalización acordada.

**13. Primer carácter único** · `diccionarios_sets/e02_primer_caracter_unico`

- Firma: `primer_caracter_unico(texto: str) -> str | None`.
- Devuelve el primer carácter, según el orden del texto, que aparece exactamente una vez. Distingue mayúsculas e incluye espacios.
- Ejemplos: `"swiss"` produce `"w"`; `"aabb"` produce `None`.
- Caso: una cadena vacía devuelve `None`.
- Variante: devolver su índice en lugar del carácter.

**14. Anagramas** · `diccionarios_sets/e03_anagramas`

- Firma: `son_anagramas(a: str, b: str) -> bool`.
- Dos textos son anagramas si contienen los mismos caracteres con las mismas frecuencias. En la primera versión, espacios y mayúsculas cuentan exactamente.
- Ejemplos: `("amor", "roma")` produce `True`; `("a", "A")` produce `False`; `("aa", "ab")` produce `False`.
- Caso: dos cadenas vacías devuelven `True`.
- Primera versión: usa conteos, sin ordenar ni usar `Counter`.
- Variante: ignorar espacios y mayúsculas.

**15. Two Sum** · `diccionarios_sets/e04_two_sum`

- Firma: `two_sum(numeros: list[int], objetivo: int) -> tuple[int, int] | None`.
- Devuelve dos índices distintos `i < j` cuyos valores sumen el objetivo. Las entradas de esta versión tendrán como máximo una pareja válida. Si no existe, devuelve `None`.
- Ejemplos: `([2, 7, 11, 15], 9)` produce `(0, 1)`; `([3, 3], 6)` produce `(0, 1)`; `([3], 6)` produce `None`.
- Conserva la lista original. Empieza con una solución correcta y después busca una de tiempo lineal promedio con un diccionario. 
- Variante: devolver todas las parejas de índices válidas.

**16. Detectar duplicados** · `diccionarios_sets/e05_duplicados`

- Firma: `tiene_duplicados(numeros: list[int]) -> bool`.
- Devuelve si algún valor aparece más de una vez; conserva la entrada.
- Ejemplos: `[1, 2, 1]` produce `True`; `[1, 2, 3]` produce `False`; `[]` produce `False`.
- Variante: devolver los valores que se repiten, sin repetirlos en la salida.

**17. Eliminar duplicados conservando el orden** · `diccionarios_sets/e06_eliminar_duplicados`

- Firma: `eliminar_duplicados(numeros: list[int]) -> list[int]`.
- Devuelve una lista nueva con la primera aparición de cada valor y conserva la entrada.
- Ejemplo: `[3, 1, 3, 2, 1]` produce `[3, 1, 2]`.
- Casos: lista vacía y lista formada por un único valor repetido.
- Variante: escribir otra versión que modifique la lista original.

**18. Intersección sin duplicados** · `diccionarios_sets/e07_interseccion`

- Firma: `interseccion(a: list[int], b: list[int]) -> list[int]`.
- Devuelve los valores presentes en ambas listas, una sola vez cada uno y en el orden de su primera aparición en `a`. Conserva las entradas.
- Ejemplo: `([3, 1, 3, 2], [2, 3])` produce `[3, 2]`.
- Casos: alguna lista vacía y listas sin elementos comunes devuelven `[]`.
- Variante: conservar repeticiones hasta la menor frecuencia que tenga cada valor entre ambas listas.

### Bloque E. Pilas

**19. Implementar una pila** · `pilas_colas/e01_pila`

- Implementa una clase `Pila` con estos métodos: `push(valor)`, `pop()`, `peek()`, `is_empty()` y `size()`.
- `push()` agrega un valor y devuelve `None`; `pop()` retira y devuelve el último; `peek()` consulta el último sin retirarlo; `is_empty()` devuelve un booleano; `size()` devuelve la cantidad de elementos.
- Si la pila está vacía, `pop()` y `peek()` deben lanzar `IndexError`.
- Puedes usar internamente una lista con `append()` y `pop()`; crea una lista independiente para cada instancia.
- Prueba: una pila nueva está vacía; después de agregar 10 y 20, `peek()` devuelve 20, `pop()` devuelve 20 y el tamaño queda en 1. Verifica que dos instancias no compartan elementos.
- Variante: representar una secuencia de acciones y deshacer la más reciente.

**20. Delimitadores balanceados** · `pilas_colas/e02_delimitadores_balanceados`

- Firma: `delimitadores_balanceados(texto: str) -> bool`.
- Comprueba que cada `(`, `[` y `{` se cierre con el tipo correcto y en el orden adecuado. Ignora los demás caracteres. Cada delimitador cuenta, incluso si aparece entre comillas: este ejercicio no analiza la sintaxis de un lenguaje.
- Ejemplos: `"([{}])"` produce `True`; `"(]"` produce `False`; `"([)]"` produce `False`; `"a+(b*c)"` produce `True`.
- Casos: `""` devuelve `True`; `"("` y `")"` devuelven `False`.
- Variante: devolver también la posición del primer cierre incorrecto; acuerda qué reportar si quedan aperturas pendientes.

## 8. Cómo escribir y ejecutar pruebas

Las pruebas deben comprobar resultados y contratos: qué devuelve la función, qué modifica y qué errores debe producir. Evita depender de las variables internas del algoritmo.

Para comenzar, copia este esqueleto en `ejercicios/cadenas/e01_invertir_cadena/solucion.py`:

```python
def invertir_cadena(texto: str) -> str:
    raise NotImplementedError("Implementa el ejercicio")
```

En `ejercicios/cadenas/e01_invertir_cadena/test_solucion.py`, agrega:

```python
import unittest

from .solucion import invertir_cadena


class TestInvertirCadena(unittest.TestCase):
    def test_casos(self):
        casos = [
            ("", ""),
            ("a", "a"),
            ("backend", "dnekcab"),
            ("Hola!", "!aloH"),
            ("a b", "b a"),
        ]

        for entrada, esperado in casos:
            with self.subTest(entrada=entrada):
                self.assertEqual(invertir_cadena(entrada), esperado)
```

Cómo leer el ejemplo: `unittest.TestCase` es la clase base que ofrece herramientas para escribir pruebas. Un método cuyo nombre empieza por `test_` se descubre como prueba. `assertEqual()` comprueba que dos valores sean iguales, y `subTest()` identifica qué entrada falló. `from .solucion import ...` importa desde `solucion.py` en la misma carpeta. [Guía de unittest](https://docs.python.org/es/3/library/unittest.html#basic-example).

Ejecuta las pruebas desde la raíz del repositorio. Para este ejercicio:

```powershell
.\.venv\Scripts\python.exe -m unittest ejercicios.cadenas.e01_invertir_cadena.test_solucion -v
```

Para todas las pruebas del directorio:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s ejercicios -t . -v
```

`discover` busca las pruebas; `-s ejercicios` indica dónde empezar, `-t .` identifica la raíz para las importaciones y `-v` muestra más detalle. `.` representa la carpeta actual.

Con el esqueleto, las pruebas producirán errores por `NotImplementedError`. Implementa la función y ejecútalas otra vez. Los archivos de pruebas vacíos aún no comprueban nada: al revisar la salida, confirma cuántas pruebas se ejecutaron.

En los demás ejercicios agrega los casos que correspondan:

- Entrada típica y entrada mínima.
- Entrada vacía, cuando esté permitida.
- Duplicados, negativos, mayúsculas o espacios, según el contrato.
- Resultado inexistente y errores definidos por el enunciado.
- Conservación o modificación de la entrada, según se haya solicitado.

Por ejemplo, para comprobar un error esperado puedes usar `with self.assertRaises(ValueError): ...`. Para una operación que modifica una lista, revisa la misma lista después de la llamada y el valor devuelto.

## 9. Plantillas para documentar

Puedes usar esta estructura para el `README.md` de cada ejercicio:

```markdown
# Nombre del ejercicio

## Enunciado
Explica qué hay que resolver y qué entradas se permiten.

## Firma
Escribe el nombre, parámetros y tipo de retorno.

## Ejemplos
Incluye entrada y salida esperada.

## Condiciones y casos límite
Define vacíos, repeticiones, errores y si se modifica la entrada.

## Restricciones de la primera versión
Registra las herramientas permitidas y el objetivo didáctico.

## Ejecución de pruebas
Escribe el comando para este ejercicio.
```

Y esta estructura para `notas.md`:

```markdown
# Notas del ejercicio

## Mi estrategia
Explica los pasos y por qué llegan al resultado correcto.

## Traza de un ejemplo
Muestra cómo cambian las variables en una entrada pequeña.

## Complejidad
- n representa:
- Tiempo y justificación:
- Espacio auxiliar y justificación:
- Memoria de la salida, si aplica:

## Errores y ayuda utilizada
Anota qué falló, cómo lo detectaste y qué pistas consultaste.

## Variante
Describe la nueva condición, tu solución y qué cambió.
```

En `PROGRESO.md` puedes registrar:

| Tema y ejercicio | Estado | Ayuda utilizada | Último intento | Próximo repaso | Variante |
| --- | --- | --- | --- | --- | --- |
| Cadenas / invertir cadena | Pendiente | — | — | — | Pendiente |

Estados sugeridos: **pendiente**, **en práctica**, **resuelto con ayuda**, **resuelto solo** y **dominado**. Registra el resultado real de cada intento.

## 10. Script opcional para preparar las carpetas

Copia el siguiente código en `crear_estructura.py`, en la raíz del repositorio. Ejecútalo desde PowerShell con:

```powershell
.\.venv\Scripts\python.exe .\crear_estructura.py
```

Creará las carpetas de los 20 ejercicios, archivos de teoría y plantillas de documentación. **Conserva el contenido de los archivos que ya existan.** El script utiliza `pathlib` para construir las rutas en Windows.

`pathlib` es un módulo de la biblioteca estándar para trabajar con rutas; no debes instalarlo. Puedes ejecutar este script de preparación y volver a estudiar sus detalles cuando domines funciones. [Referencia de pathlib](https://docs.python.org/es/3/library/pathlib.html).

Los archivos `solucion.py` y `test_solucion.py` se crean vacíos para que tú los completes. Al terminar de usar el script puedes conservarlo como herramienta del repositorio.

```python
from pathlib import Path


RAIZ = Path(__file__).resolve().parent

TEMAS = {
    "fundamentos": [
        "e01_fizzbuzz",
        "e02_sumar_digitos",
        "e03_numero_primo",
    ],
    "cadenas": [
        "e01_invertir_cadena",
        "e02_contar_vocales",
        "e03_palindromo",
        "e04_contar_palabras",
    ],
    "listas": [
        "e01_maximo",
        "e02_segundo_mayor",
        "e03_invertir_lista",
        "e04_mover_ceros",
    ],
    "diccionarios_sets": [
        "e01_frecuencias",
        "e02_primer_caracter_unico",
        "e03_anagramas",
        "e04_two_sum",
        "e05_duplicados",
        "e06_eliminar_duplicados",
        "e07_interseccion",
    ],
    "pilas_colas": [
        "e01_pila",
        "e02_delimitadores_balanceados",
    ],
}

PLANTILLA_EJERCICIO = """# {nombre}

## Enunciado

## Firma

## Ejemplos

## Condiciones y casos limite

## Restricciones de la primera version

## Ejecucion de pruebas
"""

PLANTILLA_NOTAS = """# Notas

## Mi estrategia

## Traza de un ejemplo

## Complejidad
- n representa:
- Tiempo y justificacion:
- Espacio auxiliar y justificacion:
- Memoria de la salida, si aplica:

## Errores y ayuda utilizada

## Variante
"""


def crear_si_falta(ruta: Path, contenido: str = "") -> None:
    try:
        with ruta.open("x", encoding="utf-8") as archivo:
            archivo.write(contenido)
    except FileExistsError:
        pass


def main() -> None:
    ejercicios = RAIZ / "ejercicios"
    ejercicios.mkdir(exist_ok=True)
    crear_si_falta(ejercicios / "__init__.py")

    for tema, nombres in TEMAS.items():
        carpeta_tema = ejercicios / tema
        carpeta_tema.mkdir(exist_ok=True)
        crear_si_falta(carpeta_tema / "__init__.py")
        crear_si_falta(
            carpeta_tema / "teoria.md",
            f"# Teoria: {tema}\n\nEscribe conceptos, ejemplos y costos.\n",
        )

        for nombre in nombres:
            carpeta = carpeta_tema / nombre
            carpeta.mkdir(exist_ok=True)
            crear_si_falta(carpeta / "__init__.py")
            crear_si_falta(carpeta / "solucion.py")
            crear_si_falta(carpeta / "test_solucion.py")
            crear_si_falta(
                carpeta / "README.md",
                PLANTILLA_EJERCICIO.format(nombre=nombre),
            )
            crear_si_falta(carpeta / "notas.md", PLANTILLA_NOTAS)

    crear_si_falta(
        RAIZ / "PROGRESO.md",
        "# Progreso\n\n"
        "| Tema y ejercicio | Estado | Ayuda | Ultimo intento | Proximo repaso | Variante |\n"
        "| --- | --- | --- | --- | --- | --- |\n",
    )

    print("Estructura lista. Los archivos existentes conservaron su contenido.")


if __name__ == "__main__":
    main()
```

## 11. Cómo revisar avances con tu mentor

Para cada revisión prepara el ejercicio, sus pruebas y tus notas. Debes poder responder:

1. ¿Qué recibe tu función y cuál es su contrato?
2. ¿Por qué funciona tu algoritmo? ¿Qué se mantiene cierto mientras avanza?
3. ¿Qué caso te hizo fallar y cómo lo corregiste?
4. ¿Cuánto tiempo y memoria necesita al crecer la entrada?
5. ¿Qué cambiarías si se modifica una condición del problema?

### Qué son los comandos de Git y un commit

Un **commit** es un registro local de cambios seleccionados, acompañado de un mensaje que explica qué hiciste. Una **rama** es una línea de trabajo dentro del repositorio. Usa la rama que acuerdes con tu mentor. [Guardar cambios en Git](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Guardando-cambios-en-el-Repositorio).

Cuando termines un ejercicio, sigue estos pasos desde la raíz del proyecto. Este ejemplo corresponde a invertir una cadena:

```powershell
git status
git add ejercicios/cadenas/e01_invertir_cadena
git diff --staged
git commit -m "Resuelve inversion de cadenas y agrega pruebas"
```

- `git status` muestra los archivos nuevos o modificados y los cambios preparados.
- `git add ruta` selecciona los cambios de esa ruta para el próximo commit; en Git se llama área de preparación o staging.
- `git diff --staged` muestra el contenido seleccionado para que lo revises.
- `git commit -m "mensaje"` registra esos cambios seleccionados en el historial local. El commit incluye todo lo que esté preparado; compruébalo antes de confirmarlo.

El commit se guarda en tu computadora. **Push** significa enviar commits a un repositorio remoto, alojado en otro lugar. Tu mentor te indicará cómo compartirlos según la configuración que ya tenga el proyecto. [Trabajar con repositorios remotos](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Trabajar-con-Remotos).

**Tu primera entrega:** entorno funcionando, estructura inicial, teoría de fundamentos escrita con tus palabras y FizzBuzz con pruebas. Después continúa con sumar dígitos y número primo.

## 12. Qué estudiar después

Avanza cuando puedas resolver y adaptar los básicos correspondientes. Acuerda el ritmo con tu mentor; puedes empezar a aplicar fundamentos en problemas de backend antes de completar todos los temas siguientes.

| Tema y carpeta sugerida | Teoría esencial | Ejercicios |
| --- | --- | --- |
| Dos punteros / `dos_punteros` | Dos índices avanzan según una condición; debes justificar cuándo mover cada uno. | Combinar listas ordenadas; encontrar una pareja que sume un objetivo en una lista ordenada. |
| Ventana deslizante / `ventana_deslizante` | Mantener información de un segmento contiguo y actualizarla al avanzar. | Máxima suma de `k` elementos consecutivos; subcadena más larga sin repetidos. |
| Búsqueda y ordenamiento / `busqueda_ordenamiento` | Comparar búsqueda lineal y binaria; comprender que la binaria requiere datos ordenados. | Búsqueda lineal, búsqueda binaria e insertion sort. |
| Colas / `pilas_colas` | Atender elementos en orden FIFO. | Cola de atención con `deque`; simular procesamiento de tareas. |
| Recursión / `recursion` | Resolver una versión más pequeña y detenerse con un caso base. Cada llamada también puede consumir memoria. | Factorial y suma recursiva de una lista. |
| Listas enlazadas / `listas_enlazadas` | Nodos con valor y referencia al siguiente. Acceder a una posición exige recorrer nodos. | Invertir una lista enlazada y encontrar su nodo central. |
| Árboles y grafos / `arboles_grafos` | Nodos conectados; recorridos DFS y BFS. En grafos con ciclos debes evitar revisitar indefinidamente. | Altura de un árbol, recorrido por niveles y comprobar si existe un camino. |

En esta tabla, un **nodo** es un elemento con un valor y conexiones; una **referencia** permite llegar a otro objeto. Un **árbol** organiza nodos de forma jerárquica y un **grafo** representa conexiones más generales. **DFS** recorre primero en profundidad; **BFS**, por niveles. Un **ciclo** en un grafo es una ruta que vuelve al nodo de inicio; un **caso base** es la condición que detiene las llamadas recursivas. Estudia cada tema con tu mentor al llegar a ese bloque.

Para acercar lo aprendido a backend, agrega después una carpeta `aplicaciones_backend/` y resuelve tareas como:

- Leer un archivo JSON y validar campos obligatorios.
- Contar peticiones por usuario o por código de respuesta.
- Detectar identificadores duplicados conservando el primer registro.
- Agrupar transacciones por cuenta y calcular totales.
- Paginar una lista de resultados definiendo los casos vacíos y los límites.

**JSON** es un formato de texto para intercambiar datos; **validar** es comprobar que cumplan reglas, como tener un campo obligatorio; una **petición** es una solicitud que recibe una aplicación; un **código de respuesta** indica su resultado; y **paginar** consiste en dividir una colección de resultados en partes. Cuando llegues a esos ejercicios, consulta el [módulo json de Python](https://docs.python.org/es/3/library/json.html).

## 13. Documentación para consultar

Usa estas referencias para comprobar el comportamiento de Python. La secuencia de ejercicios y los tiempos de estudio de esta guía son una propuesta de práctica que puedes ajustar con tu mentor.

- [Tutorial oficial: estructuras de datos](https://docs.python.org/es/3/tutorial/datastructures.html).
- [Tipos incorporados: cadenas, listas, diccionarios y conjuntos](https://docs.python.org/es/3/library/stdtypes.html).
- [Implementación de listas en CPython](https://docs.python.org/3/faq/design.html#how-are-lists-implemented-in-cpython).
- [Costos de operaciones de tipos incorporados en CPython](https://docs.python.org/3/builtins/time-complexity.html).
- [Pruebas con unittest](https://docs.python.org/es/3/library/unittest.html).
- [collections y deque](https://docs.python.org/es/3/library/collections.html#collections.deque).
- [Python en Windows](https://docs.python.org/3/using/windows.html).
- [Entornos virtuales y uso sin activación](https://docs.python.org/3/library/venv.html#how-venvs-work).
- [Git: conceptos iniciales](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Fundamentos-de-Git).
- [Git: archivo .gitignore](https://git-scm.com/docs/gitignore).
- [Microsoft: qué es PowerShell](https://learn.microsoft.com/es-es/powershell/scripting/overview).

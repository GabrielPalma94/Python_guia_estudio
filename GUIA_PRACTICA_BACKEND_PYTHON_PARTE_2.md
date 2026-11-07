# Guía de práctica, parte 2: patrones, estructuras enlazadas y primeros problemas de backend

Esta guía continúa `GUIA_PRACTICA_BACKEND_PYTHON.md`. Usa el mismo repositorio, el mismo entorno `.venv`, la misma forma de organizar carpetas y el mismo método de estudio. Aquí no se repiten esas instrucciones; si tienes dudas sobre cómo crear un ejercicio, ejecutar pruebas o hacer un commit, vuelve a la parte 1.

En esta etapa vas a estudiar los temas de la sección 12 de la parte 1; después harás un bloque de problemas parecidos a los que resuelve un desarrollador backend en su trabajo diario (leer y validar datos, contar, agrupar, eliminar duplicados y paginar) y cerrarás con un bloque de preparación para entrevistas y coding assessments.

La numeración de los ejercicios continúa: la parte 1 terminó en el 20 y esta empieza en el 21.

**Avanza bloque por bloque. Un bloque está terminado cuando sus ejercicios están dominados, no solo resueltos.**

## 0. Antes de empezar

Comprueba que puedes hacer lo siguiente sin consultar la solución. Si alguno falla, repásalo antes de continuar:

- [ ] Resolver desde cero FizzBuzz, Two Sum y delimitadores balanceados.
- [ ] Explicar la diferencia entre modificar una lista y devolver una lista nueva.
- [ ] Escribir una clase con `__init__`, atributos y métodos, como la `Pila`.
- [ ] Escribir pruebas con `unittest`, `subTest()` y `assertRaises()`.
- [ ] Ejecutar todas las pruebas con `unittest discover` y leer su salida.
- [ ] Justificar la complejidad en tiempo y espacio de una solución.

### Conceptos nuevos

| Concepto | Definición breve |
| --- | --- |
| Puntero o índice de trabajo | Variable que guarda una posición dentro de una secuencia. En Python no manejas punteros de memoria; aquí la palabra se usa para un índice que avanza. |
| Invariante | Condición que se mantiene cierta en cada paso del algoritmo. Sirve para explicar por qué el resultado es correcto. |
| Ventana | Segmento contiguo de una secuencia, delimitado por un índice de inicio y uno de fin. |
| Estable (ordenamiento) | Un ordenamiento es estable si los elementos con la misma clave conservan su orden relativo original. |
| Función `key` | Función que indica a `sorted()` o `sort()` qué valor comparar de cada elemento. |
| `lambda` | Forma corta de escribir una función de una sola expresión, por ejemplo `lambda usuario: usuario["edad"]`. |
| Recursión | Técnica en la que una función se llama a sí misma con un problema más pequeño. |
| Caso base | Condición que detiene la recursión y devuelve un resultado directo. |
| Pila de llamadas | Registro que guarda Python de cada llamada en curso. Cada llamada recursiva ocupa un espacio en ella. |
| Nodo | Objeto con un valor y una o más referencias a otros nodos. |
| Cabeza | Primer nodo de una lista enlazada. Si la lista está vacía, la cabeza es `None`. |
| Raíz | Nodo inicial de un árbol, desde el que se llega a todos los demás. |
| Hoja | Nodo de un árbol que no tiene hijos. |
| Lista de adyacencia | Forma de representar un grafo: cada nodo se asocia con la lista de nodos a los que está conectado. En Python suele ser un `dict[str, list[str]]`. |
| Entrada/salida (E/S) | Operaciones que leen o escriben fuera del programa, como archivos, red o bases de datos. |
| Función pura | Función cuyo resultado depende solo de sus argumentos y que no lee ni modifica nada externo. Es la parte más fácil de probar. |
| Centavos | Representación de dinero como entero en la unidad mínima (`1999` en lugar de `19.99`). Evita errores de redondeo de `float`. |

## 1. Cómo estudiar en esta etapa

El proceso de la parte 1 sigue vigente: leer, resolver a mano, intentar, comprender, reconstruir, probar y repetir. En esta etapa agrega dos pasos:

1. **Escribe la invariante antes del código.** Por ejemplo: “todo lo que está a la izquierda de `escritura` ya no tiene duplicados”. Si no puedes escribirla, todavía no entiendes el algoritmo.
2. **Dibuja las referencias.** En listas enlazadas, árboles y grafos, dibuja cajas y flechas en papel. Actualiza el dibujo en cada línea que cambia una referencia. La mayoría de los errores de estos temas se ven en el dibujo antes que en el código.

Una sesión típica puede ser: 10 minutos de repaso de un ejercicio anterior, 40 minutos de ejercicio nuevo y 10 minutos de notas. Ajusta el ritmo con tu mentor.

## 2. Nuevas carpetas

Agrega estos temas dentro de `ejercicios/`. Las colas se agregan a la carpeta `pilas_colas/` que ya existe.

```text
ejercicios/
    dos_punteros/
    ventana_deslizante/
    busqueda_ordenamiento/
    pilas_colas/            (ya existe; agregas e03 y e04)
    recursion/
    listas_enlazadas/
    arboles_grafos/
    aplicaciones_backend/
    entrevistas/
```

Cada tema lleva su `__init__.py` y su `teoria.md`; cada ejercicio, los mismos cinco archivos de la parte 1: `__init__.py`, `README.md`, `solucion.py`, `test_solucion.py` y `notas.md`. El script de la sección 14 crea toda la estructura.

## 3. Bloque F. Dos punteros

### Teoría

La técnica de dos punteros usa dos índices sobre una o varias secuencias. En cada paso decides cuál mover según una condición. Funciona bien cuando los datos están **ordenados** o cuando necesitas leer y escribir en la misma lista.

Hay dos formas comunes:

- **Extremos opuestos:** un índice empieza al inicio y otro al final; se acercan hasta encontrarse. Ejemplo: buscar una pareja que sume un objetivo en una lista ordenada.
- **Misma dirección:** un índice de lectura recorre todo y un índice de escritura marca dónde colocar el siguiente valor válido. Ejemplo: eliminar duplicados dentro de la misma lista. Ya lo usaste sin ese nombre en “mover ceros al final”.

Lo importante es justificar cada movimiento. En la pareja que suma un objetivo: si la suma es menor que el objetivo, mover el índice izquierdo es la única forma de aumentarla, porque la lista está ordenada. Si no puedes explicar por qué un movimiento no descarta una respuesta válida, el algoritmo no está justificado.

Costo habitual: tiempo `O(n)`, porque cada índice avanza como máximo `n` veces, y espacio auxiliar `O(1)`.

### Ejercicios

**21. Combinar listas ordenadas** · `dos_punteros/e01_combinar_ordenadas`

- Firma: `combinar_ordenadas(a: list[int], b: list[int]) -> list[int]`.
- Recibe dos listas ordenadas de menor a mayor y devuelve una lista nueva, también ordenada, con todos los elementos de ambas. Conserva las entradas.
- Ejemplos: `([1, 3, 5], [2, 3, 6])` produce `[1, 2, 3, 3, 5, 6]`; `([], [4])` produce `[4]`.
- Casos: ambas vacías, una vacía, listas de distinto tamaño, valores repetidos y negativos.
- Primera versión: sin `sorted()`, `sort()` ni `heapq`. Meta: tiempo `O(n + m)`.
- Variante: combinar sin repetir valores en la salida.

**22. Pareja que suma un objetivo en una lista ordenada** · `dos_punteros/e02_pareja_suma_ordenada`

- Firma: `pareja_suma_ordenada(numeros: list[int], objetivo: int) -> tuple[int, int] | None`.
- La lista está ordenada de menor a mayor. Devuelve dos índices `i < j` cuyos valores sumen el objetivo, o `None` si no existen. Las entradas tendrán como máximo una pareja válida.
- Ejemplos: `([1, 2, 4, 7, 11], 9)` produce `(1, 3)`; `([1, 2, 3], 10)` produce `None`.
- Casos: lista vacía, un elemento, negativos y una pareja formada por valores iguales, como `([2, 3, 3, 8], 6)`, que produce `(1, 2)`.
- Meta: espacio auxiliar `O(1)`, sin diccionario. Compara con tu Two Sum de la parte 1: ¿qué ganas y qué condición necesitas?
- Variante: devolver todas las parejas de valores distintos que suman el objetivo, sin repetir parejas.

**23. Eliminar duplicados de una lista ordenada** · `dos_punteros/e03_duplicados_ordenada`

- Firma: `eliminar_duplicados_ordenada(numeros: list[int]) -> int`.
- La lista está ordenada. Modifica la misma lista para que contenga cada valor una sola vez, en el mismo orden, y devuelve la cantidad de valores que quedaron.
- Ejemplo: con `[1, 1, 2, 3, 3, 3]`, la función devuelve `3` y la lista queda `[1, 2, 3]`.
- Casos: lista vacía, sin duplicados y todos iguales.
- Primera versión: un índice de lectura y uno de escritura. Al final puedes recortar con `del numeros[escritura:]`. No uses `set`, `dict` ni una lista auxiliar.
- Variante: permitir como máximo dos apariciones de cada valor.

## 4. Bloque G. Ventana deslizante

### Teoría

Una ventana deslizante mantiene información sobre un segmento contiguo de la secuencia y la actualiza al avanzar, en lugar de recalcularla desde cero.

- **Ventana fija:** siempre tiene `k` elementos. Al avanzar una posición, suma el elemento que entra y resta el que sale. Recalcular la suma de cada ventana cuesta `O(n · k)`; actualizarla cuesta `O(n)`.
- **Ventana variable:** el fin avanza en cada paso y el inicio avanza solo cuando la ventana deja de cumplir una condición. Necesitas una estructura que describa el contenido de la ventana, como un `set` o un `dict`.

Pregunta clave en una ventana variable: ¿qué condición debe cumplir la ventana y qué haces cuando deja de cumplirla? Escríbelo en tus notas antes de programar.

En backend esta técnica aparece en límites de peticiones (rate limiting), métricas de los últimos minutos y detección de picos.

### Ejercicios

**24. Máxima suma de `k` elementos consecutivos** · `ventana_deslizante/e01_maxima_suma_k`

- Firma: `maxima_suma_k(numeros: list[int], k: int) -> int`.
- Devuelve la mayor suma de `k` elementos consecutivos.
- Ejemplos: `([2, 1, 5, 1, 3, 2], 3)` produce `9`; `([-1, -2, -3], 2)` produce `-3`.
- Errores: si `k <= 0` o `k > len(numeros)`, lanza `ValueError`.
- Meta: tiempo `O(n)`. Escribe primero la versión `O(n · k)`, pruébala y úsala para comparar resultados con la versión eficiente.
- Variante: devolver también el índice donde empieza la mejor ventana.

**25. Subcadena más larga sin caracteres repetidos** · `ventana_deslizante/e02_subcadena_sin_repetidos`

- Firma: `subcadena_sin_repetidos(texto: str) -> int`.
- Devuelve la longitud de la subcadena contigua más larga que no repite caracteres. Distingue mayúsculas e incluye espacios.
- Ejemplos: `"abcabcbb"` produce `3`; `"bbbbb"` produce `1`; `"pwwkew"` produce `3`; `"aA"` produce `2`.
- Caso: `""` produce `0`.
- Meta: tiempo `O(n)` con una ventana variable y un `set` o un `dict` de últimas posiciones.
- Variante: devolver la subcadena en lugar de su longitud; si hay empate, la que aparece primero.

**26. Máximo de peticiones en una ventana de tiempo** · `ventana_deslizante/e03_peticiones_en_ventana`

- Firma: `max_peticiones_en_ventana(tiempos: list[int], segundos: int) -> int`.
- `tiempos` contiene los segundos en que llegaron peticiones a un servidor, ordenados de menor a mayor; puede haber repetidos. Devuelve el mayor número de peticiones que caen dentro de una ventana de `segundos` de duración. Dos peticiones caben en la misma ventana si la diferencia entre sus tiempos es menor que `segundos`.
- Ejemplos: `([1, 2, 3, 10, 11], 3)` produce `3`; `([1, 2, 3, 10, 11], 2)` produce `2`; `([5, 5, 5], 1)` produce `3`.
- Casos: lista vacía produce `0`. Si `segundos <= 0`, lanza `ValueError`.
- Meta: tiempo `O(n)`.
- Variante: dado un límite `maximo`, devolver los tiempos de las peticiones que un rate limiter rechazaría.

## 5. Bloque H. Búsqueda y ordenamiento

### Teoría

**Búsqueda lineal:** revisa los elementos uno por uno. Funciona con cualquier lista y cuesta `O(n)`.

**Búsqueda binaria:** requiere datos ordenados. Compara el objetivo con el elemento central y descarta la mitad donde no puede estar. Cuesta `O(log n)`: con un millón de elementos necesita unas 20 comparaciones. Los errores típicos están en los límites: decide si trabajas con el intervalo `[izquierda, derecha]` o `[izquierda, derecha)` y respétalo en todo el código.

**Insertion sort:** recorre la lista y coloca cada elemento en su lugar dentro de la parte ya ordenada, desplazando los mayores hacia la derecha. Cuesta `O(n²)` en el peor caso y `O(n)` si la lista ya está casi ordenada. Es estable y no usa memoria adicional proporcional a `n`.

**Ordenamiento incorporado:** `sorted()` y `list.sort()` usan un algoritmo llamado Timsort: `O(n log n)` en el peor caso y estable. En el trabajo real usarás estas funciones; implementar algoritmos a mano sirve para comprender sus costos y sus invariantes.

Para ordenar registros usa el parámetro `key`:

```python
usuarios = [
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Ana", "edad": 25},
]

por_edad = sorted(usuarios, key=lambda usuario: usuario["edad"])
```

Cuando `key` devuelve una tupla, Python compara el primer elemento y, si empatan, el segundo, y así sucesivamente. `reverse=True` invierte el orden. Como el ordenamiento es estable, también puedes ordenar en varias pasadas: primero por el criterio secundario y después por el principal.

Python incluye el módulo `bisect` para búsqueda binaria en listas ordenadas. Úsalo para comparar tus resultados cuando termines tu implementación.

### Ejercicios

**27. Búsqueda lineal** · `busqueda_ordenamiento/e01_busqueda_lineal`

- Firma: `busqueda_lineal(numeros: list[int], objetivo: int) -> int | None`.
- Devuelve el índice de la primera aparición del objetivo o `None`.
- Ejemplos: `([4, 2, 7, 2], 2)` produce `1`; `([4, 2], 9)` produce `None`.
- Primera versión: sin `index()` ni `in`.
- Variante: devolver todos los índices donde aparece.

**28. Búsqueda binaria** · `busqueda_ordenamiento/e02_busqueda_binaria`

- Firma: `busqueda_binaria(numeros: list[int], objetivo: int) -> int | None`.
- La lista está ordenada y no tiene duplicados. Devuelve el índice del objetivo o `None`.
- Ejemplos: `([1, 3, 5, 7, 9], 7)` produce `3`; `([1, 3, 5], 4)` produce `None`.
- Casos: lista vacía, un elemento, objetivo en el primer y último índice, menor que todos y mayor que todos.
- Primera versión: iterativa, sin `bisect` ni slices. Escribe en tus notas qué intervalo representan tus dos índices.
- Variante: con duplicados, devolver la primera aparición. Compara tu resultado con `bisect.bisect_left`.

**29. Insertion sort** · `busqueda_ordenamiento/e03_insertion_sort`

- Firma: `insertion_sort(numeros: list[int]) -> None`.
- Ordena la misma lista de menor a mayor y devuelve `None`.
- Ejemplo: `[5, 2, 4, 6, 1, 3]` queda `[1, 2, 3, 4, 5, 6]`.
- Casos: vacía, un elemento, ya ordenada, en orden inverso, con repetidos y negativos.
- Primera versión: sin `sort()` ni `sorted()`. Prueba tu resultado contra `sorted()` con varias listas.
- Variante: ordenar de mayor a menor recibiendo un parámetro `descendente: bool`.

**30. Ordenar registros por varios criterios** · `busqueda_ordenamiento/e04_ordenar_usuarios`

- Firma: `ordenar_usuarios(usuarios: list[dict]) -> list[dict]`.
- Cada usuario es un diccionario con `"nombre"` (`str`) y `"edad"` (`int`). Devuelve una lista nueva ordenada por edad de menor a mayor; si hay empate, por nombre en orden alfabético. Conserva la entrada.
- Ejemplo: `[{"nombre": "Luis", "edad": 30}, {"nombre": "Ana", "edad": 30}, {"nombre": "Eva", "edad": 22}]` produce `Eva`, `Ana`, `Luis`.
- Aquí sí debes usar `sorted()` con `key`. `list[dict]` indica una lista de diccionarios sin detallar sus claves.
- Prueba que la lista original no cambió.
- Variante: ordenar por edad de mayor a menor y, en empate, por nombre de menor a mayor. Explica por qué `reverse=True` solo no resuelve esta variante.

## 6. Bloque I. Colas

### Teoría

Una cola sigue FIFO: el primero que entra es el primero que sale. La estudiaste en teoría en la parte 1; ahora la implementarás.

Una lista de Python no es buena cola: `lista.pop(0)` cuesta `O(n)` porque desplaza todos los elementos restantes. `collections.deque` permite agregar y retirar en ambos extremos en `O(1)`:

```python
from collections import deque

cola = deque()
cola.append("tarea 1")
cola.append("tarea 2")
primera = cola.popleft()
```

En backend las colas aparecen en todas partes: trabajos en segundo plano, mensajes entre servicios, correos pendientes de enviar y peticiones esperando a ser atendidas. Herramientas como RabbitMQ, Kafka o SQS son colas a escala de sistema; la idea es la misma.

### Ejercicios

**31. Implementar una cola** · `pilas_colas/e03_cola`

- Implementa una clase `Cola` con `enqueue(valor)`, `dequeue()`, `peek()`, `is_empty()` y `size()`.
- `enqueue()` agrega al final y devuelve `None`; `dequeue()` retira y devuelve el primero; `peek()` consulta el primero sin retirarlo.
- Si la cola está vacía, `dequeue()` y `peek()` lanzan `IndexError`.
- Usa internamente un `deque`, uno independiente por instancia.
- Prueba: después de encolar 10, 20 y 30, `dequeue()` devuelve 10, `peek()` devuelve 20 y el tamaño es 2. Verifica que dos instancias no compartan elementos.
- Variante: agrega una capacidad máxima recibida en `__init__`; `enqueue()` lanza `OverflowError` si la cola está llena.

**32. Simular procesamiento de tareas por turnos** · `pilas_colas/e04_procesar_tareas`

- Firma: `procesar_tareas(tareas: list[tuple[str, int]], turno: int) -> list[str]`.
- Cada tarea es un nombre y su duración en unidades de tiempo, un entero positivo. Un trabajador atiende la tarea del frente durante como máximo `turno` unidades. Si termina, la tarea sale; si no, vuelve al final de la cola con la duración restante. Devuelve los nombres en el orden en que terminaron. Conserva la entrada.
- Ejemplo: `([("A", 3), ("B", 1), ("C", 2)], 2)` produce `["B", "C", "A"]`.
- Casos: lista vacía produce `[]`; un turno mayor que todas las duraciones conserva el orden original.
- Errores: si `turno <= 0`, lanza `ValueError`.
- Haz la traza del ejemplo a mano en tus notas, mostrando la cola después de cada turno.
- Variante: devolver también el instante en que terminó cada tarea.

## 7. Bloque J. Recursión

### Teoría

Una función recursiva tiene dos partes:

1. **Caso base:** una entrada tan pequeña que la respuesta es directa.
2. **Caso recursivo:** reduce el problema y confía en que la llamada con la entrada más pequeña devuelve la respuesta correcta.

```python
def cuenta_regresiva(n: int) -> list[int]:
    if n == 0:
        return [0]
    return [n] + cuenta_regresiva(n - 1)
```

Cada llamada que todavía no termina ocupa espacio en la pila de llamadas, así que una recursión de profundidad `n` usa espacio `O(n)`. Python limita la profundidad (normalmente alrededor de 1000; consúltalo con `sys.getrecursionlimit()`). Si la superas, obtienes `RecursionError`. Por eso en Python, para recorrer listas largas, se prefiere un ciclo. La recursión es natural para estructuras anidadas: árboles, carpetas dentro de carpetas o JSON con objetos dentro de objetos.

Cuidado con los slices en recursión: `suma(numeros[1:])` copia la lista en cada llamada, y el total pasa a ser `O(n²)`. Pasar un índice evita esas copias.

Para trazar una recursión, escribe cada llamada en una línea con sangría según su profundidad y anota lo que devuelve al regresar.

### Ejercicios

**33. Factorial** · `recursion/e01_factorial`

- Firma: `factorial(n: int) -> int`.
- `factorial(0) == 1`; `factorial(5) == 120`.
- Errores: para `n < 0`, lanza `ValueError`.
- Primera versión: recursiva. Segunda versión: con un ciclo. Compara su espacio.
- Variante: prueba qué ocurre con `factorial(5000)` en la versión recursiva y explica el error.

**34. Suma recursiva de una lista** · `recursion/e02_suma_recursiva`

- Firma: `suma_recursiva(numeros: list[int], inicio: int = 0) -> int`.
- Devuelve la suma de los elementos desde la posición `inicio` hasta el final. Quien llama a la función normalmente omite `inicio`.
- Ejemplos: `suma_recursiva([1, 2, 3])` produce `6`; `suma_recursiva([])` produce `0`.
- Restricción: sin `sum()`, sin ciclos y sin slices.
- Variante: escribe una versión con slices y explica en tus notas por qué su costo es `O(n²)`.

**35. Aplanar una lista anidada** · `recursion/e03_aplanar`

- Firma: `aplanar(datos: list) -> list[int]`.
- Recibe una lista cuyos elementos son enteros u otras listas con la misma forma, a cualquier profundidad. Devuelve una lista nueva con todos los enteros en el orden en que aparecen.
- Ejemplos: `[1, [2, [3, 4]], 5]` produce `[1, 2, 3, 4, 5]`; `[[], [[]]]` produce `[]`.
- Usa `isinstance(elemento, list)` para distinguir una lista de un entero.
- Variante: recibir un diccionario anidado, como un JSON, y devolver sus claves con la ruta completa: `{"a": {"b": 1}, "c": 2}` produce `["a.b", "c"]`.

## 8. Bloque K. Listas enlazadas

### Teoría

Una lista enlazada está formada por nodos. Cada nodo guarda un valor y una referencia al siguiente; el último apunta a `None`.

```text
cabeza
  |
  v
[1 | •] --> [2 | •] --> [3 | None]
```

```python
class Nodo:
    def __init__(self, valor: int, siguiente: "Nodo | None" = None) -> None:
        self.valor = valor
        self.siguiente = siguiente
```

La anotación `"Nodo | None"` va entre comillas porque la clase todavía no termina de definirse en esa línea.

Comparación con `list`:

| Operación | `list` | Lista enlazada |
| --- | --- | --- |
| Acceder a la posición `i` | `O(1)` | `O(i)`: hay que recorrer |
| Insertar al inicio | `O(n)` | `O(1)` |
| Insertar después de un nodo que ya tienes | `O(n)` | `O(1)` |
| Memoria por elemento | Una referencia | Un objeto nodo con valor y referencia |

En Python casi nunca usarás listas enlazadas en producción, pero el razonamiento sobre referencias es el mismo que necesitarás con objetos relacionados, árboles, grafos y caches. También son un tema frecuente en entrevistas técnicas.

Errores típicos: perder la referencia al resto de la lista antes de cambiar `siguiente`, olvidar el caso `cabeza is None` y acceder a `nodo.siguiente.valor` cuando `nodo.siguiente` puede ser `None`.

La técnica de **dos punteros a distinta velocidad** (lento avanza uno, rápido avanza dos) resuelve varios problemas en una sola pasada: cuando el rápido llega al final, el lento está en el centro; y si hay un ciclo, el rápido termina alcanzando al lento.

### Ejercicios

En este bloque, el primer ejercicio define la clase `Nodo` y dos funciones auxiliares. Los demás ejercicios las importan con una importación absoluta, por ejemplo:

```python
from ejercicios.listas_enlazadas.e01_construir_lista.solucion import Nodo, a_lista, desde_lista
```

Esta forma funciona porque las pruebas se ejecutan desde la raíz del repositorio con `-t .`.

**36. Construir y convertir una lista enlazada** · `listas_enlazadas/e01_construir_lista`

- Define la clase `Nodo` de la teoría.
- Firma: `desde_lista(valores: list[int]) -> Nodo | None`: construye una lista enlazada con los valores en el mismo orden y devuelve su cabeza.
- Firma: `a_lista(cabeza: Nodo | None) -> list[int]`: recorre la lista enlazada y devuelve sus valores en una `list`.
- Ejemplos: `a_lista(desde_lista([1, 2, 3]))` produce `[1, 2, 3]`; `desde_lista([])` produce `None`.
- Variante: `insertar_en(cabeza, posicion, valor) -> Nodo | None`, que devuelve la cabeza resultante y lanza `IndexError` si la posición no existe.

**37. Invertir una lista enlazada** · `listas_enlazadas/e02_invertir`

- Firma: `invertir_enlazada(cabeza: Nodo | None) -> Nodo | None`.
- Invierte las referencias de los mismos nodos, sin crear nodos nuevos, y devuelve la nueva cabeza.
- Ejemplo: `1 -> 2 -> 3` queda `3 -> 2 -> 1`.
- Casos: lista vacía y un solo nodo.
- Meta: iterativa, tiempo `O(n)` y espacio auxiliar `O(1)`. Dibuja las tres referencias que necesitas en cada paso.
- Variante: versión recursiva. ¿Cuál es su espacio?

**38. Nodo central** · `listas_enlazadas/e03_nodo_central`

- Firma: `nodo_central(cabeza: Nodo | None) -> Nodo | None`.
- Devuelve el nodo central. Si la cantidad de nodos es par, devuelve el segundo de los dos centrales.
- Ejemplos: `1 -> 2 -> 3 -> 4 -> 5` devuelve el nodo con valor `3`; `1 -> 2 -> 3 -> 4` devuelve el nodo con valor `3`.
- Caso: lista vacía devuelve `None`.
- Meta: una sola pasada con un puntero lento y uno rápido, sin contar primero los nodos.
- Variante: devolver el primero de los dos centrales cuando la cantidad es par.

**39. Detectar un ciclo** · `listas_enlazadas/e04_detectar_ciclo`

- Firma: `tiene_ciclo(cabeza: Nodo | None) -> bool`.
- Una lista tiene un ciclo si al seguir `siguiente` vuelves a un nodo ya visitado.
- Para probarlo, construye la lista con `desde_lista()` y después crea el ciclo a mano: recorre hasta el último nodo y asigna `ultimo.siguiente = segundo`.
- Casos: lista vacía, un nodo sin ciclo, un nodo que apunta a sí mismo y un ciclo que empieza a la mitad.
- Primera versión: con un `set` de nodos visitados. Segunda versión: dos punteros a distinta velocidad con espacio `O(1)`. ¿Por qué un `set` puede guardar nodos aunque `Nodo` no defina `__hash__`?
- Variante: devolver el nodo donde empieza el ciclo.

## 9. Bloque L. Árboles y grafos

### Teoría

Un **árbol binario** está formado por nodos con hasta dos hijos, izquierdo y derecho:

```python
class NodoArbol:
    def __init__(
        self,
        valor: int,
        izquierdo: "NodoArbol | None" = None,
        derecho: "NodoArbol | None" = None,
    ) -> None:
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
```

```text
        1
       / \
      2   3
     / \
    4   5
```

Ese árbol se construye así:

```python
raiz = NodoArbol(1, NodoArbol(2, NodoArbol(4), NodoArbol(5)), NodoArbol(3))
```

Dos formas de recorrer:

- **DFS (profundidad):** baja por una rama hasta el final antes de pasar a la siguiente. Se escribe con recursión o con una pila. El recorrido **preorden** visita nodo, izquierdo y derecho: en el ejemplo, `1, 2, 4, 5, 3`.
- **BFS (niveles):** visita todos los nodos de un nivel antes del siguiente. Se escribe con una cola. En el ejemplo, `[[1], [2, 3], [4, 5]]`.

Un **grafo** generaliza el árbol: cualquier nodo puede conectarse con cualquier otro y puede haber ciclos. En esta guía usarás grafos dirigidos representados como listas de adyacencia:

```python
grafo = {
    "api": ["auth", "pagos"],
    "auth": ["db"],
    "pagos": ["db", "api"],
    "db": [],
}
```

En un grafo con ciclos debes guardar los nodos visitados en un `set`; si no, el recorrido puede no terminar. Recorrer todo el grafo cuesta `O(V + E)`, donde `V` es el número de nodos y `E` el de conexiones.

En backend aparecen grafos en dependencias entre servicios o paquetes, permisos heredados, relaciones entre usuarios y rutas de red. Los árboles aparecen en el sistema de archivos, en documentos JSON y en los índices de las bases de datos.

### Ejercicios

En este bloque, cada `solucion.py` que lo necesite define `NodoArbol` o lo importa del ejercicio 40 con una importación absoluta, igual que en listas enlazadas.

**40. Altura de un árbol** · `arboles_grafos/e01_altura`

- Define `NodoArbol` en este ejercicio.
- Firma: `altura(raiz: NodoArbol | None) -> int`.
- La altura es la cantidad de nodos en el camino más largo desde la raíz hasta una hoja. Un árbol vacío tiene altura `0` y un solo nodo, `1`.
- Ejemplo: el árbol de la teoría tiene altura `3`.
- Casos: árbol vacío, un nodo y un árbol en el que todos los nodos tienen solo hijo derecho.
- Variante: contar las hojas.

**41. Recorrido en preorden** · `arboles_grafos/e02_preorden`

- Firma: `preorden(raiz: NodoArbol | None) -> list[int]`.
- Devuelve los valores en orden nodo, izquierdo, derecho.
- Ejemplo: el árbol de la teoría produce `[1, 2, 4, 5, 3]`.
- Primera versión: recursiva. Segunda versión: iterativa con una pila. ¿En qué orden debes apilar los hijos?
- Variante: recorrido inorden (izquierdo, nodo, derecho).

**42. Recorrido por niveles** · `arboles_grafos/e03_por_niveles`

- Firma: `recorrido_por_niveles(raiz: NodoArbol | None) -> list[list[int]]`.
- Devuelve una lista por nivel, de izquierda a derecha.
- Ejemplo: el árbol de la teoría produce `[[1], [2, 3], [4, 5]]`.
- Caso: árbol vacío produce `[]`.
- Usa un `deque` como cola.
- Variante: devolver solo el último valor de cada nivel (lo que se vería mirando el árbol desde la derecha).

**43. ¿Existe un camino?** · `arboles_grafos/e04_existe_camino`

- Firma: `existe_camino(grafo: dict[str, list[str]], origen: str, destino: str) -> bool`.
- El grafo es dirigido y todos sus nodos aparecen como clave, aunque no tengan conexiones. Devuelve si se puede llegar de `origen` a `destino` siguiendo las conexiones.
- Ejemplos con el grafo de la teoría: `("api", "db")` produce `True`; `("db", "api")` produce `False`; `("pagos", "auth")` produce `True`.
- Casos: `origen == destino` produce `True`; un grafo con ciclos debe terminar.
- Errores: si `origen` o `destino` no están en el grafo, lanza `ValueError`.
- Primera versión: BFS con un `deque` y un `set` de visitados. Segunda versión: DFS.
- Variante: devolver el camino con menos saltos como `list[str]`, o `None` si no existe.

## 10. Bloque M. Aplicaciones de backend

### Teoría

Un servicio backend recibe datos, los valida, aplica reglas de negocio y devuelve o guarda un resultado. Los ejercicios de este bloque practican esas piezas con estructuras que ya conoces.

**Separa la lógica de la entrada/salida.** Leer un archivo, una base de datos o una petición HTTP es E/S. Validar, contar o agrupar es lógica. Si la lógica vive en funciones puras que reciben datos ya cargados, puedes probarla con listas y diccionarios sin depender de archivos ni de red. La función que hace E/S queda pequeña y solo carga datos y llama a la lógica.

**JSON.** Es el formato habitual para intercambiar datos entre servicios. El módulo `json` convierte texto JSON en objetos de Python y al revés:

| JSON | Python |
| --- | --- |
| objeto `{...}` | `dict` |
| arreglo `[...]` | `list` |
| texto `"..."` | `str` |
| número entero / con decimales | `int` / `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

```python
import json
from pathlib import Path

texto = Path("usuarios.json").read_text(encoding="utf-8")
usuarios = json.loads(texto)
```

Si el texto no es JSON válido, `json.loads()` lanza `json.JSONDecodeError`, que es una subclase de `ValueError`.

**Validar es no confiar.** Todo dato que entra al sistema puede venir incompleto o con tipos equivocados. Valida en la frontera, reporta errores claros (qué registro y qué campo) y no continúes con datos inválidos. Ten en cuenta que en Python `bool` es subclase de `int`: `isinstance(True, int)` devuelve `True`. Si un campo debe ser entero, decide con tu mentor si `True` debe aceptarse.

**Dinero.** No uses `float` para montos: `0.1 + 0.2` produce `0.30000000000000004`. Representa el dinero como un entero en centavos o usa `decimal.Decimal`. En estos ejercicios usarás centavos.

**Paginación.** Una API no devuelve millones de registros en una sola respuesta: los divide en páginas. Debes definir desde qué número empiezan las páginas, qué pasa con una página fuera de rango y cómo informas el total.

### Ejercicios

**44. Cargar y validar usuarios desde JSON** · `aplicaciones_backend/e01_cargar_usuarios`

- Firma: `validar_usuario(usuario: dict) -> list[str]`. Función pura. Devuelve la lista de errores del registro; una lista vacía significa que es válido. Reglas: `"id"` debe existir y ser `int` positivo; `"email"` debe existir, ser `str` y contener exactamente un `@` con texto antes y después. Usa mensajes como `"id: campo obligatorio"` o `"email: formato invalido"`.
- Firma: `cargar_usuarios(ruta: Path) -> list[dict]`. Lee el archivo con `encoding="utf-8"`, lo convierte con `json.loads()`, comprueba que el contenido sea una lista y valida cada elemento con `validar_usuario()`. Si hay errores, lanza `ValueError` con un mensaje que incluya la posición del registro, por ejemplo `"registro 2: email: campo obligatorio"`. Si todo es válido, devuelve la lista.
- Prueba `validar_usuario()` con diccionarios escritos en la prueba. Prueba `cargar_usuarios()` creando archivos temporales con `tempfile.TemporaryDirectory()` (ver sección 12).
- Casos: archivo con JSON inválido, contenido que no es lista, lista vacía, `id` negativo, `id` como texto y `email` sin `@`.
- Variante: en lugar de detenerse en el primer registro inválido, devolver una tupla con los válidos y los errores de todos los inválidos.

**45. Contar peticiones por usuario y por código de respuesta** · `aplicaciones_backend/e02_contar_peticiones`

- Firma: `contar_peticiones(peticiones: list[dict]) -> tuple[dict[str, int], dict[int, int]]`.
- Cada petición tiene `"usuario"` (`str`) y `"codigo"` (`int`, como `200`, `404` o `500`). Devuelve dos diccionarios: peticiones por usuario y peticiones por código.
- Ejemplo: `[{"usuario": "ana", "codigo": 200}, {"usuario": "luis", "codigo": 500}, {"usuario": "ana", "codigo": 404}]` produce `({"ana": 2, "luis": 1}, {200: 1, 500: 1, 404: 1})`.
- Caso: lista vacía produce `({}, {})`.
- Primera versión: con `dict` y `get()`. Segunda versión: con `collections.Counter`.
- Variante: devolver los usuarios cuyo porcentaje de respuestas `5xx` (de 500 a 599) supere un umbral recibido como parámetro.

**46. Detectar registros con identificador duplicado** · `aplicaciones_backend/e03_deduplicar_por_id`

- Firma: `deduplicar_por_id(registros: list[dict]) -> tuple[list[dict], list[int]]`.
- Cada registro tiene un `"id"` entero. Devuelve los registros conservando solo la primera aparición de cada `id`, en el orden original, y la lista de `id` que estaban repetidos, cada uno una vez, en el orden en que se detectó su primera repetición. Conserva la entrada.
- Ejemplo: registros con `id` `[3, 1, 3, 2, 1, 3]` producen registros con `id` `[3, 1, 2]` y repetidos `[3, 1]`.
- Casos: lista vacía y ningún duplicado.
- Meta: tiempo `O(n)` promedio.
- Variante: conservar la última aparición de cada `id` en lugar de la primera, manteniendo el orden de primera aparición.

**47. Agrupar transacciones y calcular saldos** · `aplicaciones_backend/e04_saldos_por_cuenta`

- Firma: `saldos_por_cuenta(transacciones: list[dict]) -> dict[str, int]`.
- Cada transacción tiene `"cuenta"` (`str`), `"tipo"` (`"deposito"` o `"retiro"`) y `"monto_centavos"` (`int` positivo). Los depósitos suman y los retiros restan. Devuelve el saldo en centavos de cada cuenta que aparece.
- Ejemplo: depósito de `10000` y retiro de `2550` en `"A"`, depósito de `500` en `"B"` producen `{"A": 7450, "B": 500}`.
- Errores: un `"tipo"` desconocido o un monto que no sea entero positivo lanza `ValueError` indicando la posición de la transacción.
- Caso: lista vacía produce `{}`.
- Variante: rechazar con `ValueError` cualquier retiro que deje la cuenta con saldo negativo en ese momento.

**48. Paginar resultados** · `aplicaciones_backend/e05_paginar`

- Firma: `paginar(elementos: list[int], pagina: int, tamano: int) -> dict`.
- Las páginas empiezan en `1`. Devuelve un diccionario con `"elementos"` (los de esa página), `"pagina"`, `"tamano"`, `"total_elementos"` y `"total_paginas"`. Conserva la entrada.
- Ejemplo: `paginar(list(range(1, 11)), 2, 3)` produce `{"elementos": [4, 5, 6], "pagina": 2, "tamano": 3, "total_elementos": 10, "total_paginas": 4}`.
- Casos: la última página puede estar incompleta (`pagina=4` del ejemplo devuelve `[10]`); una página mayor que `total_paginas` devuelve `"elementos": []`; una lista vacía tiene `total_paginas` igual a `0`.
- Errores: `pagina < 1` o `tamano < 1` lanzan `ValueError`.
- Calcula `total_paginas` sin `math.ceil()`, solo con división entera, y explica la fórmula en tus notas.
- Variante: paginación por cursor: recibe el último `id` visto en lugar del número de página y devuelve los siguientes `tamano` elementos de una lista ordenada por `id`.

## 11. Bloque N. Preparación para entrevistas y coding assessments

### Qué es un coding assessment

En los procesos de contratación de backend casi siempre hay una o varias pruebas de programación:

- **Assessment en línea:** una plataforma como HackerRank, CodeSignal o Codility te da entre 1 y 4 problemas con un límite de tiempo (60–90 minutos). Tu código se evalúa con pruebas ocultas, incluidas entradas grandes y casos límite.
- **Entrevista en vivo:** resuelves 1 o 2 problemas en 45–60 minutos mientras explicas tu razonamiento a un entrevistador, a veces en inglés.

Los ejercicios de las partes 1 y 2 ya son la base de estas pruebas. Este bloque los conecta con el formato real: identificar el patrón sin que te lo digan, trabajar con tiempo limitado y explicar en voz alta.

### Método para resolver un problema de entrevista

Practica estos pasos hasta que salgan solos:

1. **Aclara (2–5 min).** Repite el problema con tus palabras. Pregunta por tamaños de entrada, valores negativos, duplicados, entrada vacía y qué devolver si no hay respuesta. En un assessment en línea no puedes preguntar: lee las restricciones del enunciado (por ejemplo `1 <= n <= 10^5`) y escribe tus supuestos.
2. **Ejemplos (2–3 min).** Resuelve un ejemplo pequeño a mano y piensa uno difícil.
3. **Fuerza bruta (2–3 min).** Describe la solución más simple y su complejidad. Aunque no la programes, demuestra que entiendes el problema y te da un punto de comparación.
4. **Optimiza (5–10 min).** Busca el patrón con la tabla de abajo. Explica la idea y su complejidad **antes** de escribir código.
5. **Programa (15–20 min).** Nombres claros, funciones pequeñas. Habla mientras escribes.
6. **Prueba (5 min).** Recorre tu código a mano con el ejemplo y con un caso límite. Corrige sin borrar todo.
7. **Cierra.** Di la complejidad final en tiempo y espacio, y qué mejorarías.

Las restricciones del enunciado te dicen qué complejidad se espera:

| Tamaño de `n` | Complejidad que suele pasar |
| --- | --- |
| `n <= 20` | `O(2^n)`, probar combinaciones |
| `n <= 1 000` | `O(n²)` |
| `n <= 100 000` | `O(n log n)` u `O(n)` |
| `n <= 10 000 000` | `O(n)` u `O(log n)` |

### Reconocer el patrón

| Si el enunciado dice o sugiere... | Piensa primero en... |
| --- | --- |
| “¿Ya vi este valor?”, contar, agrupar, buscar complemento | `dict` o `set` |
| Lista **ordenada**, pareja o tripleta, extremos | Dos punteros |
| Subarreglo o subcadena **contigua**, “los últimos k” | Ventana deslizante |
| Lista ordenada y buscar rápido, “mínimo valor que cumple...” | Búsqueda binaria |
| Paréntesis, deshacer, “el más reciente”, evaluar expresiones | Pila |
| Orden de llegada, por niveles, camino más corto sin pesos | Cola / BFS |
| Árbol, estructura anidada, explorar todas las opciones | Recursión / DFS |
| Cuadrícula, conexiones, dependencias | Grafo con BFS o DFS y `set` de visitados |
| Intervalos que se cruzan, horarios | Ordenar por inicio y recorrer |
| “Los k más grandes / frecuentes” | Ordenar, o `heapq` |

### Tus ejercicios anteriores con su nombre en inglés

Muchos ejercicios que ya resolviste son problemas clásicos de entrevista. Busca su nombre en inglés en LeetCode o NeetCode para practicar con pruebas ocultas y ver otras soluciones **después** de resolverlos tú:

| Ejercicio | Nombre habitual |
| --- | --- |
| 14. Anagramas | Valid Anagram |
| 15. Two Sum | Two Sum |
| 16. Detectar duplicados | Contains Duplicate |
| 11. Mover ceros | Move Zeroes |
| 13. Primer carácter único | First Unique Character in a String |
| 20. Delimitadores balanceados | Valid Parentheses |
| 21. Combinar listas ordenadas | Merge Sorted Array |
| 22. Pareja suma ordenada | Two Sum II – Input Array Is Sorted |
| 23. Duplicados en lista ordenada | Remove Duplicates from Sorted Array |
| 25. Subcadena sin repetidos | Longest Substring Without Repeating Characters |
| 28. Búsqueda binaria | Binary Search |
| 37. Invertir lista enlazada | Reverse Linked List |
| 38. Nodo central | Middle of the Linked List |
| 39. Detectar ciclo | Linked List Cycle |
| 40. Altura de un árbol | Maximum Depth of Binary Tree |
| 42. Recorrido por niveles | Binary Tree Level Order Traversal |

### Leer la entrada en un assessment

Algunas plataformas te piden completar una función; otras te dan la entrada por **entrada estándar** (stdin) y esperan la respuesta impresa en **salida estándar** (stdout). Practica este formato:

```python
import sys


def main() -> None:
    datos = sys.stdin.read().split()
    n = int(datos[0])
    numeros = [int(x) for x in datos[1 : 1 + n]]
    print(max(numeros))


if __name__ == "__main__":
    main()
```

Prueba un programa así en PowerShell escribiendo la entrada en un archivo `entrada.txt` y ejecutando `Get-Content entrada.txt | .\.venv\Scripts\python.exe .\programa.py`. Mantén la lógica en una función separada de la lectura, como en el bloque M: así también la puedes probar con `unittest`.

### Ejercicios

Estos enunciados **no dicen qué patrón usar**: descubrirlo es parte del ejercicio. Escribe en `notas.md` qué patrón elegiste y qué señal del enunciado te lo indicó. Para cada uno, mide tu tiempo; la meta es resolverlo en menos de 30 minutos sin ayuda.

**49. Agrupar anagramas** · `entrevistas/e01_agrupar_anagramas` · *Group Anagrams*

- Firma: `agrupar_anagramas(palabras: list[str]) -> list[list[str]]`.
- Agrupa las palabras que son anagramas entre sí. Los grupos aparecen en el orden en que apareció su primera palabra y, dentro de cada grupo, las palabras conservan su orden original.
- Ejemplo: `["eat", "tea", "tan", "ate", "nat", "bat"]` produce `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`.
- Casos: lista vacía produce `[]`; `[""]` produce `[[""]]`.
- Pregunta de entrevista: ¿qué clave usas para el diccionario y cuánto cuesta calcularla?

**50. Mejor momento para comprar y vender** · `entrevistas/e02_mejor_ganancia` · *Best Time to Buy and Sell Stock*

- Firma: `mejor_ganancia(precios: list[int]) -> int`.
- `precios[i]` es el precio en el día `i`. Compras un día y vendes un día posterior. Devuelve la mayor ganancia posible, o `0` si no se puede ganar.
- Ejemplos: `[7, 1, 5, 3, 6, 4]` produce `5`; `[7, 6, 4, 3, 1]` produce `0`.
- Casos: lista vacía y un solo día producen `0`.
- Meta: una pasada, espacio `O(1)`.

**51. Producto de la lista excepto el propio elemento** · `entrevistas/e03_producto_excepto_propio` · *Product of Array Except Self*

- Firma: `producto_excepto_propio(numeros: list[int]) -> list[int]`.
- Devuelve una lista donde la posición `i` es el producto de todos los elementos excepto `numeros[i]`.
- Ejemplos: `[1, 2, 3, 4]` produce `[24, 12, 8, 6]`; `[2, 0, 3]` produce `[0, 6, 0]`.
- Restricción: sin división, tiempo `O(n)`.
- Pista para cuando te bloquees: ¿qué sabes si conoces el producto de todo lo que está a la izquierda y de todo lo que está a la derecha?

**52. Contenedor con más agua** · `entrevistas/e04_contenedor_agua` · *Container With Most Water*

- Firma: `max_area(alturas: list[int]) -> int`.
- Cada valor es la altura de una línea vertical en la posición `i`. Elige dos líneas que, junto con el eje horizontal, formen un recipiente con la mayor área: `min(alturas[i], alturas[j]) * (j - i)`.
- Ejemplos: `[1, 8, 6, 2, 5, 4, 8, 3, 7]` produce `49`; `[1, 1]` produce `1`.
- Caso: menos de dos líneas produce `0`.
- Meta: `O(n)`. Justifica por qué mover la línea más baja nunca descarta la respuesta.

**53. Subarreglo de suma máxima** · `entrevistas/e05_subarreglo_suma_maxima` · *Maximum Subarray*

- Firma: `suma_maxima_subarreglo(numeros: list[int]) -> int`.
- Devuelve la mayor suma de un subarreglo contiguo no vacío.
- Ejemplos: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` produce `6` (`[4, -1, 2, 1]`); `[-3, -1, -2]` produce `-1`.
- Errores: lista vacía lanza `ValueError`.
- Meta: `O(n)`. La idea se conoce como algoritmo de Kadane: en cada posición decides si extender el subarreglo actual o empezar uno nuevo.

**54. Fusionar intervalos** · `entrevistas/e06_fusionar_intervalos` · *Merge Intervals*

- Firma: `fusionar_intervalos(intervalos: list[tuple[int, int]]) -> list[tuple[int, int]]`.
- Cada intervalo es `(inicio, fin)` con `inicio <= fin`. Fusiona los que se superponen o se tocan y devuelve el resultado ordenado por inicio. Conserva la entrada.
- Ejemplos: `[(1, 3), (2, 6), (8, 10), (15, 18)]` produce `[(1, 6), (8, 10), (15, 18)]`; `[(1, 4), (4, 5)]` produce `[(1, 5)]`; `[(5, 6), (1, 2)]` produce `[(1, 2), (5, 6)]`.
- Caso: lista vacía produce `[]`.
- Contexto backend: unir franjas ocupadas de una agenda o reservas.
- Variante: dada una lista de reservas, decidir si una nueva reserva `(inicio, fin)` choca con alguna.

**55. Los `k` elementos más frecuentes** · `entrevistas/e07_k_mas_frecuentes` · *Top K Frequent Elements*

- Firma: `k_mas_frecuentes(numeros: list[int], k: int) -> list[int]`.
- Devuelve los `k` valores que más se repiten, de mayor a menor frecuencia; en empate, el valor menor primero.
- Ejemplos: `([1, 1, 1, 2, 2, 3], 2)` produce `[1, 2]`; `([4, 4, 5, 5, 6], 2)` produce `[4, 5]`.
- Errores: si `k` es menor que 1 o mayor que la cantidad de valores distintos, lanza `ValueError`.
- Primera versión: contar y ordenar. Investiga después `heapq.nlargest` y explica cuándo conviene.

**56. Buscar en una lista ordenada y rotada** · `entrevistas/e08_busqueda_rotada` · *Search in Rotated Sorted Array*

- Firma: `buscar_en_rotada(numeros: list[int], objetivo: int) -> int | None`.
- La lista estaba ordenada de menor a mayor, sin duplicados, y luego se rotó en una posición desconocida. Devuelve el índice del objetivo o `None`.
- Ejemplos: `([4, 5, 6, 7, 0, 1, 2], 0)` produce `4`; `([4, 5, 6, 7, 0, 1, 2], 3)` produce `None`; `([1], 1)` produce `0`.
- Meta: `O(log n)`. En cada paso, una de las dos mitades está ordenada: ¿cómo lo detectas?

**57. Contar islas** · `entrevistas/e09_contar_islas` · *Number of Islands*

- Firma: `contar_islas(mapa: list[list[str]]) -> int`.
- `"1"` es tierra y `"0"` es agua. Una isla es un grupo de tierra conectado horizontal o verticalmente. Devuelve cuántas islas hay. Conserva la entrada.
- Ejemplo: `[["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]]` produce `2`.
- Casos: mapa vacío produce `0`; todo agua produce `0`; todo tierra produce `1`.
- Pista: cada celda es un nodo y sus vecinos son las celdas de arriba, abajo, izquierda y derecha.

**58. Evaluar notación polaca inversa** · `entrevistas/e10_notacion_polaca_inversa` · *Evaluate Reverse Polish Notation*

- Firma: `evaluar_rpn(tokens: list[str]) -> int`.
- En notación polaca inversa el operador va después de sus operandos: `["2", "1", "+", "3", "*"]` significa `(2 + 1) * 3` y produce `9`. Operadores: `+`, `-`, `*` y `/`. La división trunca hacia cero: usa `int(a / b)`, no `a // b`.
- Ejemplos: `["4", "13", "5", "/", "+"]` produce `6`; `["7", "-2", "/"]` produce `-3`.
- Errores: expresión incompleta o con operandos sobrantes lanza `ValueError`.
- Explica por qué `-7 // 2` y `int(-7 / 2)` dan resultados distintos.

**59. Combinar dos listas enlazadas ordenadas** · `entrevistas/e11_combinar_enlazadas` · *Merge Two Sorted Lists*

- Firma: `combinar_enlazadas(a: Nodo | None, b: Nodo | None) -> Nodo | None`.
- Importa `Nodo`, `desde_lista` y `a_lista` del ejercicio 36. Combina dos listas enlazadas ordenadas reutilizando sus nodos y devuelve la cabeza del resultado.
- Ejemplo: `1 -> 2 -> 4` y `1 -> 3 -> 4` producen `1 -> 1 -> 2 -> 3 -> 4 -> 4`.
- Casos: una o ambas vacías.
- Pista: un nodo inicial ficticio (en inglés, *dummy node*) evita tratar aparte la primera posición.

**60. Cache LRU** · `entrevistas/e12_cache_lru` · *LRU Cache*

- Implementa una clase `CacheLRU` con `__init__(capacidad: int)`, `get(clave: str) -> int | None` y `put(clave: str, valor: int) -> None`.
- LRU significa *least recently used*: cuando la cache está llena y llega una clave nueva, se elimina la que lleva más tiempo sin usarse. Tanto `get()` como `put()` cuentan como uso.
- Ejemplo con capacidad 2: `put("a", 1)`, `put("b", 2)`, `get("a")` devuelve `1`, `put("c", 3)` elimina `"b"`, y `get("b")` devuelve `None`.
- Errores: capacidad menor que 1 lanza `ValueError`.
- Meta: `get()` y `put()` en `O(1)`. Primera versión: con `collections.OrderedDict`. Segunda versión: con un `dict` y una lista doblemente enlazada propia; esta es la que suelen pedir en entrevistas.
- Contexto backend: Redis y muchas caches de aplicaciones usan políticas parecidas para decidir qué datos descartar.

### Práctica con tiempo y simulacros

- **Repaso mezclado.** Una vez por semana, elige al azar tres ejercicios ya dominados de las partes 1 y 2, sin mirar el tema, y resuélvelos en un archivo vacío con 25 minutos cada uno.
- **Assessment simulado.** Cada dos semanas, resuelve dos problemas nuevos de nivel fácil o medio en LeetCode o HackerRank en 70 minutos seguidos, sin ayuda ni IA. Anota cuántas pruebas ocultas pasaste.
- **Entrevista simulada con tu mentor.** 45 minutos: tu mentor elige el problema y tú sigues el método en voz alta. Al final, tu mentor evalúa comunicación, enfoque, código correcto, pruebas y complejidad.
- **En inglés.** Muchas entrevistas de backend son en inglés. Practica explicar al menos una solución por semana en inglés usando los nombres de la tabla anterior y términos como *edge case*, *time complexity*, *hash map* y *two pointers*.
- **Registro.** En `PROGRESO.md`, para cada problema de este bloque anota el tiempo que tardaste, si identificaste el patrón solo y si pasaste todas las pruebas al primer intento.

## 12. Herramientas nuevas de prueba

Además de lo aprendido en la parte 1, en esta etapa vas a necesitar:

**Comprobar el mensaje de un error.** `assertRaises` como contexto te deja revisar la excepción:

```python
with self.assertRaises(ValueError) as contexto:
    paginar([1, 2], 0, 10)

self.assertIn("pagina", str(contexto.exception))
```

**Comprobar identidad de objetos.** En listas enlazadas importa devolver el mismo nodo, no uno con el mismo valor. Usa `assertIs(resultado, nodo_esperado)`.

**Preparar datos comunes.** Si varias pruebas usan el mismo árbol o grafo, constrúyelo en `setUp()`, que se ejecuta antes de cada prueba:

```python
class TestPorNiveles(unittest.TestCase):
    def setUp(self):
        self.raiz = NodoArbol(1, NodoArbol(2, NodoArbol(4), NodoArbol(5)), NodoArbol(3))

    def test_arbol_de_ejemplo(self):
        self.assertEqual(recorrido_por_niveles(self.raiz), [[1], [2, 3], [4, 5]])
```

**Archivos temporales.** Para probar funciones que leen archivos, crea una carpeta temporal que se borra sola al terminar:

```python
import json
import tempfile
import unittest
from pathlib import Path

from .solucion import cargar_usuarios


class TestCargarUsuarios(unittest.TestCase):
    def test_archivo_valido(self):
        datos = [{"id": 1, "email": "ana@ejemplo.com"}]

        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "usuarios.json"
            ruta.write_text(json.dumps(datos), encoding="utf-8")

            self.assertEqual(cargar_usuarios(ruta), datos)
```

**Comparar con una versión de referencia.** En búsqueda y ordenamiento, compara tu implementación con la de Python en muchas entradas:

```python
import random

for _ in range(200):
    numeros = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
    esperado = sorted(numeros)
    insertion_sort(numeros)
    self.assertEqual(numeros, esperado)
```

Si una de esas pruebas falla, imprime la lista que la hizo fallar y conviértela en un caso fijo de tu prueba.

**Comprobar que la entrada no cambió.** Guarda una copia antes de llamar a la función y compárala después:

```python
original = [{"nombre": "Luis", "edad": 30}]
copia = [dict(usuario) for usuario in original]
ordenar_usuarios(original)
self.assertEqual(original, copia)
```

[Referencia de unittest](https://docs.python.org/es/3/library/unittest.html) · [Referencia de tempfile](https://docs.python.org/es/3/library/tempfile.html).

## 13. Complejidad de los temas nuevos

Agrega esta tabla a tus notas y verifica cada fila con tus propias implementaciones:

| Algoritmo u operación | Tiempo | Espacio auxiliar |
| --- | --- | --- |
| Dos punteros sobre una lista | `O(n)` | `O(1)` |
| Ventana fija de tamaño `k` actualizada | `O(n)` | `O(1)` |
| Ventana variable con `set` o `dict` | `O(n)` promedio | `O(k)`, contenido de la ventana |
| Búsqueda lineal | `O(n)` | `O(1)` |
| Búsqueda binaria iterativa | `O(log n)` | `O(1)` |
| Insertion sort | `O(n²)` peor caso, `O(n)` casi ordenada | `O(1)` |
| `sorted()` / `sort()` | `O(n log n)` | `O(n)` |
| `deque.append()` / `deque.popleft()` | `O(1)` | — |
| `list.pop(0)` | `O(n)` | — |
| Recursión de profundidad `d` | depende del trabajo por llamada | `O(d)` por la pila de llamadas |
| Recorrer una lista enlazada | `O(n)` | `O(1)` |
| DFS / BFS en un árbol de `n` nodos | `O(n)` | `O(h)` DFS (altura) / `O(w)` BFS (nivel más ancho) |
| DFS / BFS en un grafo | `O(V + E)` | `O(V)` |

## 14. Script opcional para preparar las carpetas

Copia este código en `crear_estructura_parte_2.py`, en la raíz del repositorio, y ejecútalo:

```powershell
.\.venv\Scripts\python.exe .\crear_estructura_parte_2.py
```

Igual que el script de la parte 1, **conserva el contenido de los archivos que ya existan**. Puedes ejecutarlo aunque `pilas_colas/` ya tenga tus ejercicios: solo agregará lo que falte.

```python
from pathlib import Path


RAIZ = Path(__file__).resolve().parent

TEMAS = {
    "dos_punteros": [
        "e01_combinar_ordenadas",
        "e02_pareja_suma_ordenada",
        "e03_duplicados_ordenada",
    ],
    "ventana_deslizante": [
        "e01_maxima_suma_k",
        "e02_subcadena_sin_repetidos",
        "e03_peticiones_en_ventana",
    ],
    "busqueda_ordenamiento": [
        "e01_busqueda_lineal",
        "e02_busqueda_binaria",
        "e03_insertion_sort",
        "e04_ordenar_usuarios",
    ],
    "pilas_colas": [
        "e03_cola",
        "e04_procesar_tareas",
    ],
    "recursion": [
        "e01_factorial",
        "e02_suma_recursiva",
        "e03_aplanar",
    ],
    "listas_enlazadas": [
        "e01_construir_lista",
        "e02_invertir",
        "e03_nodo_central",
        "e04_detectar_ciclo",
    ],
    "arboles_grafos": [
        "e01_altura",
        "e02_preorden",
        "e03_por_niveles",
        "e04_existe_camino",
    ],
    "aplicaciones_backend": [
        "e01_cargar_usuarios",
        "e02_contar_peticiones",
        "e03_deduplicar_por_id",
        "e04_saldos_por_cuenta",
        "e05_paginar",
    ],
    "entrevistas": [
        "e01_agrupar_anagramas",
        "e02_mejor_ganancia",
        "e03_producto_excepto_propio",
        "e04_contenedor_agua",
        "e05_subarreglo_suma_maxima",
        "e06_fusionar_intervalos",
        "e07_k_mas_frecuentes",
        "e08_busqueda_rotada",
        "e09_contar_islas",
        "e10_notacion_polaca_inversa",
        "e11_combinar_enlazadas",
        "e12_cache_lru",
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

## Invariante o idea principal

## Mi estrategia

## Traza o dibujo de un ejemplo

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

    print("Estructura de la parte 2 lista. Los archivos existentes conservaron su contenido.")


if __name__ == "__main__":
    main()
```

Agrega las filas de los ejercicios 21 a 60 a tu `PROGRESO.md` conforme los empieces.

## 15. Cómo revisar avances con tu mentor

Las cinco preguntas de la parte 1 siguen aplicando. Agrega estas según el bloque:

1. **Dos punteros y ventanas:** ¿qué invariante mantienes? ¿Por qué mover ese índice no descarta una respuesta válida?
2. **Búsqueda binaria:** ¿qué intervalo representan tus índices y por qué el ciclo siempre termina?
3. **Recursión:** ¿cuál es el caso base? ¿Qué profundidad alcanza y qué pasa con una entrada muy grande?
4. **Listas enlazadas, árboles y grafos:** dibuja las referencias antes y después de tu operación. ¿Qué pasa con `None`? ¿Cómo evitas visitar dos veces un nodo?
5. **Aplicaciones backend:** ¿qué parte de tu código es lógica pura y cuál es E/S? ¿Qué dato inválido podría llegar y qué haría tu función con él?

**Entregas sugeridas:**

- Entrega 1: bloques F y G.
- Entrega 2: bloques H e I.
- Entrega 3: bloques J y K.
- Entrega 4: bloque L.
- Entrega 5: bloque M.
- Entrega 6: bloque N, más un assessment simulado y una entrevista simulada con tu mentor. Todas las pruebas del repositorio deben pasar con `unittest discover`.

Haz un commit por ejercicio terminado, como en la parte 1.

## 16. Qué estudiar después

Al terminar esta parte ya tienes la base de algoritmos y estructuras de datos que se usa a diario en backend. La siguiente etapa deja de ser solo funciones y pasa a construir servicios:

| Tema | Qué vas a aprender |
| --- | --- |
| Módulos, paquetes y dependencias | Organizar un proyecto real, `pip`, `requirements.txt` o `pyproject.toml`. |
| Tipado y modelado de datos | `dataclasses`, anotaciones más precisas y validación de datos con modelos. |
| Errores y logging | Definir excepciones propias, cuándo capturarlas y registrar eventos con el módulo `logging`. |
| HTTP y APIs REST | Métodos, rutas, códigos de respuesta, cabeceras y JSON. Consumir una API con un cliente HTTP. |
| Un framework web | Construir tu primera API, por ejemplo con FastAPI o Flask, aplicando la paginación y validación de esta guía. |
| Bases de datos SQL | Tablas, consultas, índices y transacciones. Empezar con SQLite, que viene con Python. |
| Pruebas de servicios | `pytest`, pruebas de endpoints y separación entre pruebas unitarias y de integración. |
| Configuración y despliegue | Variables de entorno, Docker y nociones de cómo se ejecuta un servicio en un servidor. |

## 17. Documentación para consultar

- [Tutorial oficial: clases](https://docs.python.org/es/3/tutorial/classes.html).
- [Ordenamiento en Python: `key`, estabilidad y varios criterios](https://docs.python.org/es/3/howto/sorting.html).
- [Módulo bisect](https://docs.python.org/es/3/library/bisect.html).
- [collections: deque y Counter](https://docs.python.org/es/3/library/collections.html).
- [Límite de recursión: `sys.getrecursionlimit`](https://docs.python.org/es/3/library/sys.html#sys.getrecursionlimit).
- [Módulo json](https://docs.python.org/es/3/library/json.html).
- [Módulo pathlib](https://docs.python.org/es/3/library/pathlib.html).
- [Módulo tempfile](https://docs.python.org/es/3/library/tempfile.html).
- [Módulo decimal](https://docs.python.org/es/3/library/decimal.html).
- [Problemas de punto flotante](https://docs.python.org/es/3/tutorial/floatingpoint.html).
- [Costos de operaciones de tipos incorporados en CPython](https://docs.python.org/3/builtins/time-complexity.html).
- [Pruebas con unittest](https://docs.python.org/es/3/library/unittest.html).

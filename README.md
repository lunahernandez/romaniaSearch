# Práctica 1 - Búsqueda por Ramificación y Acotación

## Descripción

La práctica 1 tiene como objetivo implementar la búsqueda por Ramificación y Acotación (B&B) y la búsqueda por Ramificación y Acotación con Subestimación (B&B Subestimación) utilizando como problema el grafo de las ciudades de Rumanía.

## Conteo de Nodos Generados y Visitados

Antes de abordar las implementaciones de B&B y B&B Subestimación, se realizó el conteo de nodos generados y visitados. En la función `graph_search` (líneas 95-126 en `search.py`), se añadieron líneas de código para llevar un registro preciso de estos nodos. Además, se implementó el conteo sin repetición para mejorar la eficiencia.

## Implementación de Búsquedas

A continuación, se presentan las implementaciones de B&B y B&B Subestimación en `search.py` (líneas 139-146):

```python
def branch_and_bound_graph_search(problem):
   """Search using a priority queue (PriorityQueue) based on path cost."""
   return graph_search(problem, PriorityQueue())

def branch_and_bound_with_subestimation_graph_search(problem):
   """Search using a priority queue (PriorityQueueWithSubestimation) based on path cost and subestimation heuristic."""
   return graph_search(problem, PriorityQueueWithSubestimation(problem))
```
Ambos métodos utilizan la función `graph_search`, que toma como primer parámetro el problema de Rumanía y como segundo la definición del comportamiento de la lista abierta `fringe`. En el caso de B&B, se utiliza `PriorityQueue()`, mientras que para B&B Subestimación, se utiliza `PriorityQueueWithSubestimation(problem)`.

## Implementación de Clases

En el archivo `utils.py`, se añadieron las clases `PriorityQueue` y `PriorityQueueWithSubestimation`. 

- `PriorityQueue` se comporta de manera similar a `FIFOQueue`, pero con una función lambda llamada `lt` que compara `x < y`. Esto permite ordenar la lista abierta de menor a mayor coste acumulado, como se requiere en B&B.

- `PriorityQueueWithSubestimation` incluye un nuevo parámetro `problem`, que pertenece a la clase `GPSProblem` y contiene la función de la heurística. Esto permite ordenar los nodos en la lista abierta según su coste acumulado más su heurística, como se hace en B&B Subestimación.

## Comparación de Estrategias

Se completó una tabla de comparación de estrategias de búsqueda, realizando llamadas con nodos inicial y final específicos para las cuatro búsquedas: en amplitud, en profundidad, B&B y B&B Subestimación (líneas 24-80 en `run.py`).

La tabla se puede encontrar en el archivo `FSITablaComparativa.pdf` que se encuentra en el zip.

## Apartados Opcionales
Se pueden encontrar en el archivo `FSITrabajoOpcional.pdf` que se encuentra en el zip.
### Traza de Búsqueda

En el primer apartado opcional, se realizó a mano la traza de una búsqueda de B&B, determinando un nuevo nodo inicial y un nodo objetivo en el grafo de Rumanía. A través del árbol de expansión, se determinó el camino seguido, su costo total y el número de nodos generados y visitados.

### Consistencia de Heurística

En el segundo apartado opcional, se cuestiona la consistencia de la heurística para asegurar el carácter óptimo de la búsqueda. Para abordar este interrogante, se creó un grafo junto a dos heurísticas. La búsqueda que cuenta con una heurística no consistente generará más nodos, ya que sigue un camino que en un principio era mejor pero luego resulta que tiene más costo a largo plazo que siguiendo otra trayectoria. 
Por otro lado, la otra búsqueda cuenta con una heurística consistente que subestima y asegura el carácter óptimo de la búsqueda.


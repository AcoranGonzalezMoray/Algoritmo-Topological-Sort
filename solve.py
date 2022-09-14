import networkx as nx

def dfs_topological_sort(graph):
    """
    Compute one topological sort of the given directed graph.
    """
    
    # La solucion que retorna esta función es un diccionario de Python.
    #   * La clave del diccionario es el número del nodo
    #   * El valor es el orden topologico asignado a ese nodo
    # 
    # Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
    #                    3 ---> 2 ---> 1
    # ... el orden topologico es:
    #                El vértice 3 va en la primera posición
    #                El vértice 2 en la segunda posición
    #                El vértice 1 en la tercera posición
    # Se devuelve
    #     {1: 3, 2: 2, 3: 1}

    solution = dict()


    Visitado = []
    Pila = []
    Comienzo = [x for x in graph.nodes if graph.in_degree(x) == 0]#metemos los nodos donde su adyacente sea solo de salida, y no de entrada
    
    
    
    def dfs(graph, inicial, Visitado, Pila):
        if inicial in Visitado:
            return Pila, Visitado
    
        if graph.out_degree(inicial) == 0:
            # nodo y todas sus ramas han sido visitadas
            Pila.append(inicial)
            Visitado.append(inicial)
            return Pila, Visitado
    
        # recorre todas las ramas
        for node in graph[inicial]:
            if node in Visitado:
                continue
            Pila, Visitado = dfs(graph, node, Visitado, Pila)
    
        # ahora insertamos en pila, si no esta visitiado
        if inicial not in Visitado:
            Pila.append(inicial)
            Visitado.append(inicial)
    
        return Pila, Visitado
    
    
    for i in Comienzo:
        Pila, Visitado = dfs(graph, i, Visitado, Pila)
    
    for i in graph.nodes():
        solution[i]=Pila.pop()

    return solution

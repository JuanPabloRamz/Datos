# Primero creamos la "cajita" que guardará nuestra información
class Nodo:
    def __init__(self, dato):
        self.dato = dato           # Guardamos el valor (número, texto, etc.)
        self.siguiente = None      # Esta es la "flecha" que por ahora no apunta a nadie

# --- LISTA ENLAZADA SIMPLE ---
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None         # La lista empieza vacía, la "cabeza" no apunta a nada

    def insertar_inicio(self, dato):
        # Complejidad: O(1) porque es un paso rápido, no importa si hay 1 o 1 millón de nodos.
        nuevo = Nodo(dato)         # Creamos la nueva cajita
        nuevo.siguiente = self.cabeza # La flecha del nuevo ahora apunta a lo que antes era el primero
        self.cabeza = nuevo        # Ahora el nuevo nodo es oficialmente el primero (la cabeza)

    def insertar_final(self, dato):
        # Complejidad: O(n) porque si la lista es larga, hay que caminar mucho hasta el final.
        nuevo = Nodo(dato)
        if not self.cabeza:        # Si la lista está vacía...
            self.cabeza = nuevo    # El nuevo se vuelve la cabeza
            return
        temporal = self.cabeza     # Empezamos a caminar desde el principio
        while temporal.siguiente:  # Mientras haya alguien después del actual...
            temporal = temporal.siguiente # ...seguimos saltando al siguiente
        temporal.siguiente = nuevo # Cuando llegamos al último, le decimos que ahora apunte al nuevo

    def eliminar(self, valor):
        # Complejidad: O(n) porque hay que buscar el valor nodo por nodo.
        actual = self.cabeza
        anterior = None            # Necesitamos saber quién está antes para no romper la cadena
        
        while actual and actual.dato != valor: # Caminamos mientras no encontremos el dato
            anterior = actual
            actual = actual.siguiente
            
        if not actual: return      # Si llegamos al final y no estaba el dato, no hacemos nada
        
        if not anterior:           # Si el que vamos a borrar es el primero...
            self.cabeza = actual.siguiente # ...la cabeza ahora salta al segundo
        else:
            # El de atrás ahora apunta al de adelante del que vamos a borrar ("puente")
            anterior.siguiente = actual.siguiente 

# --- PILA (STACK) - Imaginalo como una pila de platos ---
class Pila:
    def __init__(self):
        self.cima = None           # El plato que está arriba de todo

    def push(self, dato):
        # Operación: Poner un plato arriba. Complejidad: O(1)
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cima # El nuevo plato apunta hacia el que estaba abajo
        self.cima = nuevo          # Ahora el nuevo es el que está arriba

    def pop(self):
        # Operación: Quitar el plato de arriba. Complejidad: O(1)
        if not self.cima: return None
        valor = self.cima.dato
        self.cima = self.cima.siguiente # La cima ahora es el plato que estaba abajo
        return valor

# --- COLA (QUEUE) - Como la fila del banco ---
class Cola:
    def __init__(self):
        self.frente = None         # El primero de la fila
        self.final = None          # El último de la fila

    def enqueue(self, dato):
        # Operación: Alguien nuevo llega a la fila. Complejidad: O(1)
        nuevo = Nodo(dato)
        if not self.final:         # Si no hay nadie en la fila...
            self.frente = self.final = nuevo
            return
        self.final.siguiente = nuevo # El que era último ahora apunta al que acaba de llegar
        self.final = nuevo         # El recién llegado es ahora el nuevo último

    def dequeue(self):
        # Operación: Atender al primero de la fila. Complejidad: O(1)
        if not self.frente: return None
        valor = self.frente.dato
        self.frente = self.frente.siguiente # El segundo ahora es el primero
        if not self.frente: self.final = None # Si ya no queda nadie, el final también es None
        return valor
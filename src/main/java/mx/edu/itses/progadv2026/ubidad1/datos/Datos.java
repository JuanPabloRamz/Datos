/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package mx.edu.itses.progadv2026.ubidad1.datos;

// Definimos la clase Nodo 
class Nodo {
    int dato;           // El valor que guardamos
    Nodo siguiente;     // El "puntero" o referencia para conectar con el siguiente Nodo

    public Nodo(int dato) {
        this.dato = dato;
        this.siguiente = null; // Al nacer, el nodo no está conectado a nadie
    }
}

//LISTA ENLAZADA SIMPLE
class ListaEnlazada {
    Nodo cabeza; // El primer nodo de la lista

    // O(1): Meter un dato al principio es muy rápido
    public void insertarInicio(int dato) {
        Nodo nuevo = new Nodo(dato);    // Creamos el nodo
        nuevo.siguiente = cabeza;       // Lo conectamos a lo que antes era el inicio
        cabeza = nuevo;                 // Decimos que el inicio ahora es este nuevo nodo
    }

    // O(n): Hay que recorrer toda la lista hasta encontrar el hueco al final
    public void insertarFinal(int dato) {
        Nodo nuevo = new Nodo(dato);
        if (cabeza == null) {           // Si la lista no tiene nada:
            cabeza = nuevo;             // El nuevo es el primero
            return;
        }
        Nodo aux = cabeza;              // Usamos un "auxiliar" para caminar sin perder la cabeza
        while (aux.siguiente != null) { // Mientras el nodo actual tenga alguien después
            aux = aux.siguiente;        // pasamos al siguiente
        }
        aux.siguiente = nuevo;          // Al llegar al final, lo conectamos
    }

    public void recorrer() {
        Nodo aux = cabeza;
        while (aux != null) {           // Mientras no lleguemos al vacío (null)
            System.out.print(aux.dato + " -> ");
            aux = aux.siguiente;        // Avanzamos
        }
        System.out.println("null");
    }
}

// PILA (STACK)
class Pila {
    private Nodo cima; // El elemento de hasta arriba

    // O(1): Solo movemos la referencia de la cima
    public void push(int dato) {
        Nodo nuevo = new Nodo(dato);
        nuevo.siguiente = cima; // El nuevo se apoya sobre el que ya estaba
        cima = nuevo;           // El nuevo ahora es el jefe de la pila
    }

    // O(1): Quitamos el de arriba y el de abajo toma el mando
    public int pop() {
        if (cima == null) return -1;
        int valor = cima.dato;
        cima = cima.siguiente; // La cima baja un nivel
        return valor;
    }

    public int peek() {
        return (cima != null) ? cima.dato : -1; // Solo miramos, no tocamos nada
    }
}

// COLA (QUEUE)
class Cola {
    private Nodo frente, ultimo; // Necesitamos saber quién es el primero y quién el último

    // O(1): Como sabemos quién es el último, lo pegamos ahí directamente
    public void enqueue(int dato) {
        Nodo nuevo = new Nodo(dato);
        if (ultimo == null) {           // Si la cola está vacía:
            frente = ultimo = nuevo;    // El nuevo es el primero y el último a la vez
            return;
        }
        ultimo.siguiente = nuevo;       // El que era último ahora tiene a alguien detrás
        ultimo = nuevo;                 // El nuevo se convierte en el último de la fila
    }

    // O(1): Atendemos al primero y el que seguía pasa al frente
    public int dequeue() {
        if (frente == null) return -1;
        int valor = frente.dato;
        frente = frente.siguiente;      // El segundo de la fila ahora es el primero
        if (frente == null) ultimo = null; // Si ya no hay nadie, el último también es null
        return valor;
    }
}

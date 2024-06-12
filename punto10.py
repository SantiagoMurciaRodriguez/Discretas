class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self, valor_raiz):
        self.raiz = Nodo(valor_raiz)
    
    def insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.insertar(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.insertar(nodo.derecha, valor)
    
    def insertar_lista(self, lista):
        for valor in lista:
            self.insertar(self.raiz, valor)
    
    def inorden_fibo(self):
        fibo_order = self._fibonacci(len(self))
        self._inorden_fibo(self.raiz, fibo_order)
    
    def _inorden_fibo(self, nodo, fibo_order):
        if nodo:
            self._inorden_fibo(nodo.izquierda, fibo_order)
            
            if nodo.valor in fibo_order:
                print(nodo.valor, end=' ')
            
            self._inorden_fibo(nodo.derecha, fibo_order)
    
    def encontrar_maximo(self):
        return self._encontrar_maximo(self.raiz)
    
    def _encontrar_maximo(self, nodo):
        if nodo is None:
            return float('-inf')
        
        maximo = nodo.valor
        actual = maximo
        
        if nodo.izquierda:
            izq_max = self._encontrar_maximo(nodo.izquierda)
            if izq_max > maximo:
                maximo = izq_max
        
        if nodo.derecha:
            der_max = self._encontrar_maximo(nodo.derecha)
            if der_max > maximo:
                maximo = der_max
        
        return maximo
    
    def _fibonacci(self, n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib
    
    def __len__(self):
        return self._contar_nodos(self.raiz)
    
    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierda) + self._contar_nodos(nodo.derecha)

# Función para generar la secuencia de Fibonacci
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Crear un árbol binario con la secuencia de Fibonacci
fib_sequence = fibonacci(10)  # Por ejemplo, obtener los primeros 10 números de Fibonacci
arbol_fibonacci = Arbol(fib_sequence[0])
arbol_fibonacci.insertar_lista(fib_sequence[1:])

# Imprimir los valores de los nodos en orden Fibonacci
print("Valores de los nodos en orden Fibonacci:")
arbol_fibonacci.inorden_fibo()

# Encontrar el valor máximo en el árbol
maximo = arbol_fibonacci.encontrar_maximo()
print(f"\nEl valor máximo en el árbol es: {maximo}")

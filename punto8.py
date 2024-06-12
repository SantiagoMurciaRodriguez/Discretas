class Nodo:
    def __init__(self, valor, es_pregunta=True):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.es_pregunta = es_pregunta

class Arbol:
    def __init__(self, valor_raiz):
        self.raiz = Nodo(valor_raiz, es_pregunta=True)

    def insertar(self, nodo, nueva_pregunta, nueva_respuesta, respuesta_correcta):
        valor_antiguo = nodo.valor  # Guardar el valor antiguo antes de actualizar
        nodo.valor = nueva_pregunta
        nodo.es_pregunta = True
        if respuesta_correcta == "si":
            nodo.izquierda = Nodo(nueva_respuesta, es_pregunta=False)
            nodo.derecha = Nodo(valor_antiguo, es_pregunta=False)
        else:
            nodo.izquierda = Nodo(valor_antiguo, es_pregunta=False)
            nodo.derecha = Nodo(nueva_respuesta, es_pregunta=False)

    def adivinar(self, nodo):
        while nodo and nodo.es_pregunta:
            respuesta = input(nodo.valor + " (si/no): ").strip().lower()
            while respuesta not in ["si", "no"]:
                respuesta = input("Por favor responde con 'si' o 'no': ").strip().lower()
            if respuesta == "si":
                if nodo.izquierda is None:
                    nodo.izquierda = Nodo("animal desconocido", es_pregunta=False)
                nodo = nodo.izquierda
            else:
                if nodo.derecha is None:
                    nodo.derecha = Nodo("animal desconocido", es_pregunta=False)
                nodo = nodo.derecha

        if nodo is None:
            print("Error: nodo inesperadamente vacío.")
            return

        respuesta = input("Es un " + nodo.valor + "? (si/no): ").strip().lower()
        while respuesta not in ["si", "no"]:
            respuesta = input("Por favor responde con 'si' o 'no': ").strip().lower()
        if respuesta == "si":
            print("¡Soy el más grande!")
        else:
            nuevo_animal = input("Cómo se llama el animal? ").strip()
            nueva_pregunta = input("Qué pregunta distinguiría a un " + nuevo_animal + " de un " + nodo.valor + "? ").strip()
            respuesta_correcta = input("Si el animal fuera un " + nuevo_animal + ", cuál sería la respuesta? (si/no): ").strip().lower()
            while respuesta_correcta not in ["si", "no"]:
                respuesta_correcta = input("Por favor responde con 'si' o 'no': ").strip().lower()
            self.insertar(nodo, nueva_pregunta, nuevo_animal, respuesta_correcta)

def main():
    print("¡Bienvenido al juego de adivinanza de animales!")
    arbol = Arbol("Es un pájaro?")

    while True:
        respuesta = input("Estás pensando en un animal? (si/no): ").strip().lower()
        while respuesta not in ["si", "no"]:
            respuesta = input("Por favor responde con 'si' o 'no': ").strip().lower()
        if respuesta == "no":
            break
        arbol.adivinar(arbol.raiz)

if __name__ == "__main__":
    main()

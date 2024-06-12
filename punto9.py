class TreeNode:
    def __init__(self, value, type):
        self.value = value
        self.type = type
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None
        
    def build_tree(self, postfix):
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for token in postfix:
            if token not in operators:
                # Es un operando (número)
                node = TreeNode(float(token), 'VALUE')
                stack.append(node)
            else:
                # Es un operador
                right = stack.pop()
                left = stack.pop()
                node = TreeNode(token, 'OPERATOR')
                node.left = left
                node.right = right
                stack.append(node)
        
        self.root = stack.pop()
    
    def evaluate_tree(self, node):
        if node.type == 'VALUE':
            return node.value
        else:
            left_val = self.evaluate_tree(node.left)
            right_val = self.evaluate_tree(node.right)
            
            if node.value == '+':
                return left_val + right_val
            elif node.value == '-':
                return left_val - right_val
            elif node.value == '*':
                return left_val * right_val
            elif node.value == '/':
                return left_val / right_val
            else:
                raise ValueError("Operador desconocido")
    
    def evaluate_expression(self, expression):
        postfix = self.infix_to_postfix(expression)
        self.build_tree(postfix)
        return self.evaluate_tree(self.root)
    
    def infix_to_postfix(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []
        operators = set(['+', '-', '*', '/'])
        tokens = expression.replace(" ", "")
        
        i = 0
        while i < len(tokens):
            if tokens[i].isdigit() or tokens[i] == '.':
                # Si el token es un número, lo agregamos directamente a la salida
                num = ''
                while i < len(tokens) and (tokens[i].isdigit() or tokens[i] == '.'):
                    num += tokens[i]
                    i += 1
                output.append(num)
                continue
            elif tokens[i] in operators:
                # Si el token es un operador, lo manejamos según la precedencia
                while (stack and stack[-1] != '(' and
                       precedence.get(stack[-1], 0) >= precedence[tokens[i]]):
                    output.append(stack.pop())
                stack.append(tokens[i])
            elif tokens[i] == '(':
                # Si el token es '(' lo añadimos a la pila
                stack.append(tokens[i])
            elif tokens[i] == ')':
                # Si el token es ')', desapilamos hasta encontrar el '('
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Sacamos el '(' de la pila
            i += 1
        
        # Vaciamos la pila
        while stack:
            output.append(stack.pop())
        
        return output

# Función principal para ejecutar el programa
def main():
    expression = "((3+4)*5)+((2-5)+(8*2))"
    tree = ExpressionTree()
    result = tree.evaluate_expression(expression)
    
    # Imprimir el árbol de expresión y el resultado
    print(f"Expresión: {expression}")
    print(f"Resultado: {result}")

if __name__ == "__main__":
    main()

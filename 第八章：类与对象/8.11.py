# 访问者模式

class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Negate(BinaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class NodeVisitor:
    def visit(self, node):
        methname = 'visit' + type(node).__name__
        meth = getattr(self, methname, Node)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self,node):
        raise RuntimeError('No {} method'.format('visit' + type(node).__name__))

    class Evaluator(NodeVisitor):
        def visit_Number(self,node):
            return node.value

        def visit_Add(self,node):
            return self.visit(node.left)  + self.visit(node.right)

        def visit_Sub(self,node):
            return self.visit(Node.left) - self.visit(node.right)

class StackCode(NodeVisitor):

    def generate_code(self,node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_Number(self,node):
        self.instructions.append(('PUSH',node.value))

    def binop(self,node,instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction))

    
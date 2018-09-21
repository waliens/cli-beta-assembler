from parsing.nodes import *


class BetaAssemblyVisitor(object):
    def _visitChildren(self, node: Node):
        for child in node.children:
            child.accept(self)

    def visitBetaTree(self, node: BetaTree):
        self._visitChildren(node)

    def visitNumber(self, node: Number):
        self._visitChildren(node)

    def visitDot(self, node: Dot):
        self._visitChildren(node)

    def visitUnaryOperator(self, node: UnaryOperator):
        self._visitChildren(node)

    def visitNegateOp(self, node: NegateOp):
        self._visitChildren(node)

    def visitBitwiseComplementOp(self, node: BitwiseComplementOp):
        self._visitChildren(node)

    def visitBinaryOperator(self, node: BinaryOperator):
        self._visitChildren(node)

    def visitPlusOp(self, node: PlusOp):
        self._visitChildren(node)

    def visitMinusOp(self, node: MinusOp):
        self._visitChildren(node)

    def visitMultOp(self, node: MultOp):
        self._visitChildren(node)

    def visitDivOp(self, node: DivOp):
        self._visitChildren(node)

    def visitModuloOp(self, node: ModuloOp):
        self._visitChildren(node)

    def visitShiftLeftOp(self, node: ShiftLeftOp):
        self._visitChildren(node)

    def visitShiftRightOp(self, node: ShiftRightOp):
        self._visitChildren(node)

    def visitIdentifier(self, node: Identifier):
        self._visitChildren(node)

    def visitAssignment(self, node: Assignment):
        self._visitChildren(node)

    def visitMacro(self, node: Macro):
        self._visitChildren(node)

    def visitMacroInvocation(self, node: MacroInvocation):
        self._visitChildren(node)

    def visitAlign(self, node: Align):
        self._visitChildren(node)
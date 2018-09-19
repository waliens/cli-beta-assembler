// Grammar for Beta assembly
// Compilation command: java -jar antlr-4.7.1-complete.jar assembler/BetaAssembly.g4 -o assembler -no-listener -no-visitor
grammar BetaAssembly;

options { language=Python3; }

@header {
from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation

def extend_if_exists(l, child, access_fn):
    if child.ctx is not None:
        l.extend(access_fn(child))
    return l
}

// Parser rules
start returns[BetaTree beta_tree]
    : NEWLINE* beta_block NEWLINE* EOF {$beta_tree = BetaTree($beta_block.nodes) }
      | NEWLINE* EOF                   {$beta_tree = BetaTree([]) }
;

// A beta block is a block of beta language elements (possibly starting with a unary expression)
beta_block returns[list nodes]
    : unary (NEWLINE* beta_items) ? {
$nodes = [$unary.node]
if $beta_items.ctx is not None:
    $nodes.extend($beta_items.nodes)
}
      | beta_items {$nodes = $beta_items.nodes }
;

// Sequence of beta language elements
beta_items returns[list nodes]
    : beta (NEWLINE* beta_items) ? {
$nodes = $beta.nodes
if $beta_items.ctx is not None:
    $nodes.extend($beta_items.nodes)
}
;

// A beta element can be an expression, an assignment or a non expression (possibly followed by a unary expression)
beta returns[list nodes]
    : expression                {$nodes = [$expression.node] }
      | assignment              {$nodes = [$assignment.assign] }
      | non_expression (unary)? {
$nodes = [$non_expression.node]
if $unary.ctx is not None:
    $nodes.append($unary.node)
}
;

non_expression returns[Node node]
    : macro_def_body          {$node = $macro_def_body.macro }
//      | macro_call             {$node = $macro_call.call }
//      | macro_def_line NEWLINE {$node = $macro_def_line.macro }
//      | macro_def_line EOF     {$node = $macro_def_line.macro }
;

// Identifier definition (regular identifiers + labels)
assignment returns[Assignment assign]
    : IDENTIFIER EQUAL expression {$assign = Assignment($IDENTIFIER.text, $expression.node) }
      | IDENTIFIER EQUAL unary    {$assign = Assignment($IDENTIFIER.text, $unary.node) }
      | IDENTIFIER ':'            {$assign = Assignment($IDENTIFIER.text, Dot()) }
;

// Expression with parenthesis
expression returns[Node node]
    : '(' expression ')'                              {$node = $expression.node }
      | atom                                          {$node = $atom.a }
      | <assoc=right> a=expression MOD b=expression   {$node = ModuloOp($a.node, $b.node) }
      |               a=expression MULT  b=expression {$node = MultOp($a.node, $b.node) }
      |               a=expression DIV   b=expression {$node = DivOp($a.node, $b.node) }
      |               a=expression PLUS  b=expression {$node = PlusOp($a.node, $b.node) }
      |               a=expression MINUS b=expression {$node = MinusOp($a.node, $b.node) }
      |               a=expression SHL   b=expression {$node = ShiftLeftOp($a.node, $b.node) }
      |               a=expression SHR   b=expression {$node = ShiftRightOp($a.node, $b.node) }
      | '(' unary ')'                                 {$node = $unary.node }
;

// Atoms: numbers, dot and identifier
atom returns[Atom a]
    : NB_BINARY     {$a = Number(binary=$NB_BINARY.text) }
      | NB_HEXA     {$a = Number(hexadecimal=$NB_HEXA.text) }
      | NB_DECIMAL  {$a = Number(decimal=$NB_DECIMAL.text) }
      | DOT         {$a = Dot() }
      | IDENTIFIER  {$a = Identifier($IDENTIFIER.text) }
;

// Unary operators
unary returns[Node node]
    : MINUS expression   {$node = NegateOp($expression.node) }
      | COMPL expression {$node = BitwiseComplementOp($expression.node) }
;

//// Macro definition (e.g. `.macro ADD(Ra, Rb, Rc) `)
//macro_def_line returns[Macro macro]
//    : MACRO IDENTIFIER '(' macro_params ')' macro_def {$macro = Macro($IDENTIFIER.text, $macro_params.params, $macro_def.definition) }
//;
//
macro_def_body returns[Macro macro]
    : MACRO IDENTIFIER '(' macro_params ')' '{' NEWLINE* beta_block NEWLINE* '}' {$macro = Macro($IDENTIFIER.text, $macro_params.params, $beta_block.nodes) }
;

macro_params returns[list params]
    : IDENTIFIER (',' macro_params) ? {
$params = [Identifier($IDENTIFIER.text)]
if $macro_params.ctx is not None:
    $params.extend($macro_params.params)
}
;

//macro_def returns[list definition]
//    : expression (macro_def) ?   {
//$definition = [$expression.node]
//if $macro_def.ctx is not None:
//    $definition.extend($macro_def.definition)
//}
//      | macro_call (macro_def) ? {
//$definition = [$macro_call.call]
//if $macro_def.ctx is not None:
//    $definition.extend($macro_def.definition)
//}
//;

//// Macro calls (e.g. ADD(R1, r3, R4), LD(R1, 0x4, R6),...)
//macro_call returns[MacroInvocation call]
//    : IDENTIFIER '(' macro_call_params ')' {$call = MacroInvocation($IDENTIFIER.text, $macro_call_params.params) }
//;
//
//macro_call_params returns[list params]
//    : expression (',' macro_call_params) ? {
//$params = [$expression.node]
//if $macro_call_params.ctx is not None:
//    $params.extend($macro_call_params.params)
//}
//;

// Lexer rules
COMMENT   : '|' ~[\r\n]* -> skip;
IDENTIFIER: [a-zA-Z][a-zA-Z0-9_]* ;
NB_DECIMAL: [0-9]+('.'[0-9]+|'e''-'?[0-9]+)? ;
NB_BINARY : '0b'[01]+ ;
NB_HEXA   : '0x'[0-9A-Fa-f]+ ;
MACRO     : '.macro' ;
INCLUDE   : '.include' ;
DOT       : '.' ;
WSPACE    : [ \t\f]+ -> channel(HIDDEN) ;
NEWLINE   : '\r'? '\n' ;
EXP       : '^' ;
DIV       : '/' ;
MULT      : '*' ;
PLUS      : '+' ;
MINUS     : '-' ;
EQUAL     : '=' ;
SHR       : '>>' ;
SHL       : '<<' ;
MOD       : '%' ;
COMPL     : '~' ;

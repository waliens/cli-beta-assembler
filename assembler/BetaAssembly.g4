// Grammar for Beta assembly
// Compilation command: java -jar antlr-4.7.1-complete.jar assembler/BetaAssembly.g4 -o assembler -no-listener -no-visitor
grammar BetaAssembly;

options { language=Python3; }

@header {
from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, Assignment, Macro, MacroCall
}

// Parser rules
start returns[BetaTree beta_tree]
    : NEWLINE* beta NEWLINE* EOF {$beta_tree = BetaTree($beta.nodes) }
      | NEWLINE* EOF {$beta_tree = BetaTree([]) }
;

// beta
beta returns[list nodes]
    : beta_node (NEWLINE* beta) ? {
$nodes = [$beta_node.node]
if $beta.ctx is not None:
    $nodes.extend($beta.nodes)
}
;

// beta node
beta_node returns[Node node]
    :
//      macro_call             {$node = $macro_call.call }
//      | macro_inline NEWLINE {$node = $macro_inline.macro }
//      | macro_inline EOF     {$node = $macro_inline.macro }
//      | macro_block          {$node = $macro_block.macro }
       expression           {$node = $expression.node }
//      | atom                 {$node = $atom.a            }
//      | assignment           {$node = $assignment.assign }
;

// Identifier definition (regular identifiers + labels)
//assignment returns[Assignment assign]
//    : IDENTIFIER EQUAL expression {$assign = Assignment($IDENTIFIER.text, $expression.node) }
//      | IDENTIFIER ':'            {$assign = Assignment($IDENTIFIER.text, Dot()) }
//;


// Expression with parenthesis
//expression returns[Node node]
//    :   a=expression MOD   b=expression {$node = ModuloOp($a.node, $b.node) }
//      | a=expression DIV   b=expression {$node = DivOp($a.node, $b.node) }
//      | a=expression MULT  b=expression {$node = MultOp($a.node, $b.node) }
//      | a=expression PLUS  b=expression {$node = PlusOp($a.node, $b.node) }
//      | a=expression MINUS b=expression {$node = MinusOp($a.node, $b.node) }
//      | a=expression SHL   b=expression {$node = ShiftLeftOp($a.node, $b.node) }
//      | a=expression SHR   b=expression {$node = ShiftRightOp($a.node, $b.node) }
//;


// Expression with parenthesis
expression returns[Node node]
    : '(' expression ')'                              {$node = $expression.node }
      | atom                                          {$node = $atom.a }
      | <assoc=right> a=expression MOD   b=expression {$node = ModuloOp($a.node, $b.node) }
      |               a=expression DIV   b=expression {$node = DivOp($a.node, $b.node) }
      |               a=expression MULT  b=expression {$node = MultOp($a.node, $b.node) }
      |               a=expression PLUS  b=expression {$node = PlusOp($a.node, $b.node) }
      |               a=expression MINUS b=expression {$node = MinusOp($a.node, $b.node) }
      |               a=expression SHL   b=expression {$node = ShiftLeftOp($a.node, $b.node) }
      |               a=expression SHR   b=expression {$node = ShiftRightOp($a.node, $b.node) }
//      | '(' MINUS expression ')'                      {$node = NegateOp($expression.node) }
;

// Atoms: numbers, dot and identifier
atom returns[Atom a]
    : NB_BINARY     {$a = Number(binary=$NB_BINARY.text) }
      | NB_HEXA     {$a = Number(hexadecimal=$NB_HEXA.text) }
      | NB_DECIMAL  {$a = Number(decimal=$NB_DECIMAL.text) }
      | DOT         {$a = Dot() }
      | IDENTIFIER  {$a = Identifier($IDENTIFIER.text) }
;

//// Macro definition (e.g. `.macro ADD(Ra, Rb, Rc) `)
//macro_inline returns[Macro macro]
//    : MACRO IDENTIFIER '(' macro_params ')' macro_def {$macro = Macro($IDENTIFIER.text, $macro_params.params, $macro_def.definition) }
//;
//
//macro_block returns[Macro macro]
//    : MACRO IDENTIFIER '(' macro_params ')' '{' NEWLINE* beta '}' {$macro = Macro($IDENTIFIER.text, $macro_params.params, $beta.nodes) }
//;
//
//macro_params returns[list params]
//    : IDENTIFIER (',' macro_params) ? {
//$params = [Identifier($IDENTIFIER.text)]
//if $macro_params.ctx is not None:
//    $params.extend($macro_params.params)
//}
//;
//
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
//macro_call returns[MacroCall call]
//    : IDENTIFIER '(' macro_call_params ')' {$call = MacroCall($IDENTIFIER.text, $macro_call_params.params) }
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

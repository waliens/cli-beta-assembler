// Grammar for Beta assembly
// Compilation command: java -jar antlr-4.7.1-complete.jar assembler/BetaAssembly.g4 -o assembler -no-listener -no-visitor
grammar BetaAssembly;

options { language=Python3; }

@header {
from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, Assignment, Macro, MacroCall
}

// Parser rules
start returns[BetaTree beta_tree]
    : beta {$beta_tree = BetaTree($beta.nodes) }
;

// beta
beta returns[list nodes]
    : beta_node (beta) ? {
$nodes = [$beta_node.node]
if $beta.ctx is not None:
    $nodes.extend($beta.nodes)
}
;

// beta node
beta_node returns[Node node]
    : macro_call NEWLINE*    {$node = $macro_call.call }
      | macro_inline NEWLINE {$node = $macro_inline.macro }
      | macro_block NEWLINE* {$node = $macro_block.macro }
      | expression NEWLINE*  {$node = $expression.expr }
      | assignment NEWLINE*  {$node = $assignment.assign }
;

// Identifier definition (regular identifiers + labels)
assignment returns[Assignment assign]
    : IDENTIFIER EQUAL expression {$assign = Assignment($IDENTIFIER.text, $expression.expr) }
      | IDENTIFIER ':'            {$assign = Assignment($IDENTIFIER.text, Dot()) }
;

// Expression
expression returns[Expression expr]
    : '(' expression ')'                             {$expr = $expression.expr }
      |<assoc=right> a=expression MOD   b=expression {$expr = ModuloOp($a.expr, $b.expr) }
      |              a=expression DIV   b=expression {$expr = DivOp($a.expr, $b.expr) }
      |              a=expression MULT  b=expression {$expr = MultOp($a.expr, $b.expr) }
      |              a=expression PLUS  b=expression {$expr = PlusOp($a.expr, $b.expr) }
      |              a=expression MINUS b=expression {$expr = MinusOp($a.expr, $b.expr) }
      |              a=expression SHL   b=expression {$expr = ShiftLeftOp($a.expr, $b.expr) }
      |              a=expression SHR   b=expression {$expr = ShiftRightOp($a.expr, $b.expr) }
      | atom                                         {$expr = Atom($atom.a) }
      | IDENTIFIER                                   {$expr = Identifier($IDENTIFIER.text) }
;

// Atoms: numbers and dot identifier
atom returns[Atom a]
    : NB_BINARY     {$a = Number(binary=$NB_BINARY.text) }
      | NB_HEXA     {$a = Number(hexadecimal=$NB_HEXA.text) }
      | NB_DECIMAL  {$a = Number(decimal=$NB_DECIMAL.text) }
      | DOT         {$a = Dot() }
;

// Macro definition (e.g. `.macro ADD(Ra, Rb, Rc) `)
macro_inline returns[Macro macro]
    : MACRO IDENTIFIER '(' macro_params ')' macro_def {$macro = Macro($IDENTIFIER.text, $macro_params.params, $macro_def.definition) }
;

macro_block returns[Macro macro]
    : MACRO IDENTIFIER '(' macro_params ')' '{' NEWLINE* beta '}' {$macro = Macro($IDENTIFIER.text, $macro_params.params, $beta.nodes) }
;

macro_params returns[list params]
    : IDENTIFIER (',' macro_params) ? {
$params = [Identifier($IDENTIFIER.text)]
if $macro_params.ctx is not None:
    $params.extend($macro_params.params)
}
;

macro_def returns[list definition]
    : expression (macro_def) ?   {
$definition = [Expression($expression.expr)]
if $macro_def.ctx is not None:
    $definition.extend($macro_def.definition)
}
      | macro_call (macro_def) ? {
$definition = [Expression($macro_call.call)]
if $macro_def.ctx is not None:
    $definition.extend($macro_def.definition)
}
;

// Macro calls (e.g. ADD(R1, r3, R4), LD(R1, 0x4, R6),...)
macro_call returns[MacroCall call]
    : IDENTIFIER '(' macro_call_params ')' {$call = MacroCall($IDENTIFIER.text, $macro_call_params.params) }
;

macro_call_params returns[list params]
    : IDENTIFIER (',' macro_call_params) ? {
$params = [Identifier($IDENTIFIER.text)]
if $macro_call_params.ctx is not None:
    $params.extend($macro_call_params.params)
}
        | expression (',' macro_call_params) ? {
$params = [$expression.expr]
if $macro_call_params.ctx is not None:
    $params.extend($macro_call_params.params)
}
;

// Lexer rules
IDENTIFIER: [a-zA-Z][a-zA-Z0-9_]* ;
NB_DECIMAL: [\-]?[0-9]+('.'[0-9]+|'e''-'?[0-9]+)? ;
NB_BINARY : '0b'[01]+ ;
NB_HEXA   : '0x'[0-9A-Fa-f]+ ;
MACRO     : '.macro' ;
INCLUDE   : '.include' ;
DOT       : '.' ;
WSPACE    : [ \t]+ -> channel(HIDDEN) ;
NEWLINE  : [\r\n]+ ;
COMMENT   : '|'';'? .*? ~[\r\n]* -> skip ;
EXP       : '^' ;
DIV       : '/' ;
MULT      : '*' ;
PLUS      : '+' ;
MINUS     : '-' ;
EQUAL     : '=' ;
SHR       : '>>' ;
SHL       : '<<' ;
MOD       : '%' ;

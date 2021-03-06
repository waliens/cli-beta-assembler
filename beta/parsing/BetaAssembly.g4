// Grammar for Beta assembly
// Compilation command: java -jar antlr-4.7.1-complete.jar assembler/BetaAssembly.g4 -o assembler -no-listener -no-visitor
grammar BetaAssembly;

options { language=Python3; }

@header {
import os
from .nodes import BetaTree, Node, Align, Breakpoint, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation
from .exceptions import IncludeFileNotFoundError, CircularInclusionError
}

@parser::members {

@property
def symbol_table(self):
    return self._symbol_table

@symbol_table.setter
def symbol_table(self, t):
    self._symbol_table = t

@property
def parsed_files(self):
    return self._parsed_files

@parsed_files.setter
def parsed_files(self, t):
    self._parsed_files = t

@property
def current_file_path(self):
    return self._parsed_files[-1] if len(self._parsed_files) > 0 else None
}


//@lexer::members {
//def nextToken(self):
//    token = super().nextToken()
//    if token.type != 17:
//        print("Token: {} [{}] [{}]".format(self.ruleNames[token.type - 1], token.type, token.text))
//    return token
//}

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
      | ALIGN expression        {$nodes = [Align($expression.node, line=$ALIGN.line, pos=$ALIGN.pos, source=self.current_file_path)] }
      | non_expression (unary)? {
$nodes = $non_expression.nodes
if $unary.ctx is not None:
    $nodes.append($unary.node)
}
;

non_expression returns[list nodes]
    : multiline_macro              {$nodes = [$multiline_macro.macro] }
      | macro_call                 {$nodes = [$macro_call.call] }
      | inline_macro (NEWLINE|EOF) {$nodes = [$inline_macro.macro] }
      | BREAKPOINT                 {$nodes = [Breakpoint(line=$BREAKPOINT.line, pos=$BREAKPOINT.pos, source=self.current_file_path)] }
      | INCLUDE                    {
from .parse_util import parse_file
filepath = $INCLUDE.text[8:].strip()
current_file_path = self.current_file_path

# if relative path, make it relative to the including file
if not os.path.isabs(filepath):
    corrected_filepath = os.path.join(os.path.dirname(current_file_path), filepath)
else:
    corrected_filepath = filepath

# check included file exists
if not os.path.isfile(corrected_filepath):
    raise IncludeFileNotFoundError(current_file_path, $INCLUDE.line, $INCLUDE.pos, filepath)

realpath = os.path.realpath(corrected_filepath)
if realpath in set(self.parsed_files):
    raise CircularInclusionError(self.current_file_path, self.parsed_files[-1], $INCLUDE.line, $INCLUDE.pos, filepath)
tree, _ = parse_file(realpath, parsed_files=self.parsed_files + [realpath], symbol_table=self.symbol_table)
$nodes = tree.children
}
;

// Identifier definition (regular identifiers + labels)
assignment returns[Assignment assign]
    : IDENTIFIER EQUAL assignment_rhs {
$assign = Assignment(Identifier($IDENTIFIER.text, line=$IDENTIFIER.line, pos=$IDENTIFIER.pos, source=self.current_file_path), $assignment_rhs.node)
self.symbol_table.add_variable($IDENTIFIER.text)
}
      | DOT EQUAL assignment_rhs  {$assign = Assignment(Dot(line=$DOT.line, pos=$DOT.pos, source=self.current_file_path), $assignment_rhs.node) }
      | IDENTIFIER ':'            {$assign = Assignment(Identifier($IDENTIFIER.text, line=$IDENTIFIER.line, pos=$IDENTIFIER.pos, source=self.current_file_path), Dot()) }
;

assignment_rhs returns[Node node]
    : expression {$node = $expression.node }
      | unary    {$node = $unary.node }
;

// Expression
expression returns[Node node]
    : '(' expression ')'                              {$node = $expression.node }
      | atom                                          {$node = $atom.a }
      | <assoc=right> a=expression MOD b=expression   {$node = ModuloOp($a.node, $b.node, line=$MOD.line , pos=$MOD.pos, source=self.current_file_path) }
      |               a=expression MULT  b=expression {$node = MultOp($a.node, $b.node, line=$MULT.line, pos=$MULT.pos, source=self.current_file_path) }
      |               a=expression DIV   b=expression {$node = DivOp($a.node, $b.node, line=$DIV.line, pos=$DIV.pos, source=self.current_file_path) }
      |               a=expression PLUS  b=expression {$node = PlusOp($a.node, $b.node, line=$PLUS.line, pos=$PLUS.pos, source=self.current_file_path) }
      |               a=expression MINUS b=expression {$node = MinusOp($a.node, $b.node, line=$MINUS.line, pos=$MINUS.pos, source=self.current_file_path) }
      |               a=expression SHL   b=expression {$node = ShiftLeftOp($a.node, $b.node, line=$SHL.line, pos=$SHL.pos, source=self.current_file_path) }
      |               a=expression SHR   b=expression {$node = ShiftRightOp($a.node, $b.node, line=$SHR.line, pos=$SHR.pos, source=self.current_file_path) }
      | '(' unary ')'                                 {$node = $unary.node }
;

// Atoms: numbers, dot and identifier
atom returns[Atom a]
    : NB_BINARY     {$a = Number(binary=$NB_BINARY.text, line=$NB_BINARY.line, pos=$NB_BINARY.pos, source=self.current_file_path) }
      | NB_HEXA     {$a = Number(hexadecimal=$NB_HEXA.text, line=$NB_HEXA.line, pos=$NB_HEXA.pos, source=self.current_file_path) }
      | NB_DECIMAL  {$a = Number(decimal=$NB_DECIMAL.text, line=$NB_DECIMAL.line, pos=$NB_DECIMAL.pos, source=self.current_file_path) }
      | DOT         {$a = Dot(line=$DOT.line, pos=$DOT.pos, source=self.current_file_path) }
      | IDENTIFIER  {$a = Identifier($IDENTIFIER.text, line=$IDENTIFIER.line, pos=$IDENTIFIER.pos, source=self.current_file_path) }
;

// Unary operators
unary returns[Node node]
    : MINUS expression   {$node = NegateOp($expression.node, line=$MINUS.line, pos=$MINUS.pos, source=self.current_file_path) }
      | COMPL expression {$node = BitwiseComplementOp($expression.node, line=$COMPL.line, pos=$COMPL.pos, source=self.current_file_path) }
;

// Macro definition (e.g. `.macro ADD(Ra, Rb, Rc) `)
multiline_macro returns[Macro macro]
    : MACRO macro_def_identifier '(' macro_params? ')' '{' NEWLINE* beta_block NEWLINE* '}' {
params = [] if $macro_params.ctx is None else $macro_params.params
$macro = Macro($macro_def_identifier.name, params, BetaTree($beta_block.nodes), line=$MACRO.line, pos=$MACRO.pos, source=self.current_file_path)
self.symbol_table.add_macro($macro_def_identifier.name)
}
;

macro_def_identifier returns[str name]
    : IDENTIFIER {$name = $IDENTIFIER.text }
      | MACRO_ID {$name = $MACRO_ID.text   } ;

macro_params returns[list params]
    : IDENTIFIER (',' macro_params) ? {
$params = [Identifier($IDENTIFIER.text)]
if $macro_params.ctx is not None:
    $params.extend($macro_params.params)
}
;

// Inline macro
inline_macro returns[Macro macro]
    : MACRO macro_def_identifier '(' macro_params? ')' unary? beta_items_inline {
nodes = []
if $unary.ctx is not None:
    nodes.append($unary.node)
nodes.extend($beta_items_inline.nodes)
params = [] if $macro_params.ctx is None else $macro_params.params
$macro = Macro($macro_def_identifier.name, params, BetaTree(nodes), line=$MACRO.line, pos=$MACRO.pos, source=self.current_file_path)
self.symbol_table.add_macro($macro_def_identifier.name)
}
;

// Sequence of beta language elements (reduced set) on the same line
beta_items_inline returns[list nodes]
    : reduced_beta beta_items_inline? {
$nodes = [$reduced_beta.node]
if $beta_items_inline.ctx is not None:
    $nodes.extend($beta_items_inline.nodes)
}
;

reduced_beta returns[Node node]
    : expression   {$node = $expression.node }
      | macro_call {$node = $macro_call.call }
      | assignment {$node = $assignment.assign }
;

// Macro calls (e.g. ADD(R1, r3, R4), LD(R1, 0x4, R6),...)
macro_call returns[MacroInvocation call]
    : MACRO_ID '(' macro_call_params? ')' {
params = [] if $macro_call_params.ctx is None else $macro_call_params.params
$call = MacroInvocation($MACRO_ID.text, params, line=$MACRO_ID.line, pos=$MACRO_ID.pos, source=self.current_file_path)
}
;

macro_call_params returns[list params]
    : macro_param (',' macro_call_params) ? {
$params = [$macro_param.node]
if $macro_call_params.ctx is not None:
    $params.extend($macro_call_params.params)
}
;

macro_param returns[Node node]
    : expression {$node = $expression.node }
      | unary    {$node = $unary.node }
;

// Lexer rules
COMMENT   : '|' ~[\r\n]* -> skip;
INCLUDE   : '.include' [ \t\f]+ ~[ \n\r\f\t]+ ;
MACRO     : '.macro' ;
ALIGN     : '.align' ;
BREAKPOINT: '.breakpoint' ;
IDENTIFIER: [a-zA-Z][a-zA-Z0-9_]* {
val = self.text
if self.symbol_table.has_macro(val):
    self.type = self.MACRO_ID
else:
    self.type = self.IDENTIFIER
};
NB_DECIMAL: [0-9]+('.'[0-9]+|'e''-'?[0-9]+)? ;
NB_BINARY : '0b'[01]+ ;
NB_HEXA   : '0x'[0-9A-Fa-f]+ ;
DOT       : '.' ;
WSPACE    : [ \t\f]+ -> skip ;
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



MACRO_ID  : '_/xx';
VAR_ID    : '_/xy';

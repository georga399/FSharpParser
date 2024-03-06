grammar Tokenize;

WHITE_SPACE: [ \t\r\n]+ -> skip ;
COMMENT:( ('//'.*?([\n]| EOF))  | ('(*' .*? '*)') )-> skip ;

IDENTIFIER: [a-zA-Z_0-9]+ ;

INT: [0-9]+('uy'|'y'|'s'|'us'|'u'|'L')?;

FLOAT: [0-9]+'.'[0-9]+ ('f'|'m')?;

INTERPOLATIONSIGN: ('%s'|'%d'|'%f'|'%c');

CHAR: '\'' (ESC | ~[\n\t\r .]) '\'' ;

ESC: '\\' [0-9]{3} | '\\' 'u' [0-9a-zA-Z]{4} ;

BOOL: 'true' | 'false';

UNIT: '(' ' '* ')';

REC: 'rec';

PUBLIC: 'public';

PRIVATE: 'private';

INTERNAL: 'internal';

MUTABLE: 'mutable';

LET: 'let';

FUN: 'fun';

WHILE: 'while';

DO: 'do';

FOR: 'for';

TO: 'to';

DOWNTO: 'downto';

IN: 'in';

DOLLAR: '$';

TYPE: 'type';

MODULE: 'module';

OPEN: 'open';

NAMESPACE: 'namespace';

CLASS: 'class';

END: 'end';

STRUCT: 'struct';

WITH_AND: 'and';

INTERFACE: 'interface';

GET: 'get';

INHERIT: 'inherit';

OVERRIDE: 'override';

DEFAULT: 'default';

ABSTRACT: 'abstract';

BASE: 'base';

ASYNC: 'async';

TASK: 'task';

NEW: 'new';

THEN: 'then';

THIS: 'this';

MEMBER: 'member';

SEQ: 'seq';

MAP: 'Map';

SET: 'set';

RAISE: 'raise';

RERAISE: 'reraise';

FAILWITH: 'failwith';

INVALIDARG: 'invalidArg';

VAL: 'val';

TRY: 'try';

FINALLY: 'finally';

MATCH: 'match';

WITH: 'with';

USE: 'use';

USING: 'using';

EXCEPTION: 'exception';

OF: 'of';

DOT: '.';

DOTDOT: '..';

EXCLAMATION_MARK: '!';

COMMA: ',';

SEMICOLON: ';';

COLON: ':';

ASSIGN: '<-';

PIPE: '|>';

MISSING_ARG: '_';

RIGHT_ARROW: '->';

COMPOS: '>>';

ADD: '+';

MINUS: '-';

MUL: '*';

DIV: '/';

POW: '**';

MOD: '%';

EQUAL: '=';

NOT_EQUAL: '<>';

LESS: '<';

GREATER: '>';

LESS_EQUAL: '<=';

GREATER_EQUAL: '>=';

AND:'&&';

OR:'||';

LSHIFT: '<<<';

RSHIFT: '>>>';

LOG_MUL: '&&&';

LOG_ADD: '|||';

LOG_XOR: '^^^';

LOG_NOT: '~~~';

NOT: 'not';

COLON_Q: ':?';



// rules
dot:DOT;

dotIentifier: IDENTIFIER (dot IDENTIFIER)*;

int: INT;

float: FLOAT;

unit: UNIT;

bool: BOOL;

char: CHAR;

missing_arg: MISSING_ARG;

interpolationSign: INTERPOLATIONSIGN; // don't add to expr

dollar: DOLLAR; //don't add

string: dollar? '"' (('{'expression '}')|interpolationSign | CHAR)* '"';

attribute: '[' '<' dotIentifier '>' ']';

round_brackets: '(' expression+ ')';

rec: REC;

public: PUBLIC;

private: PRIVATE;

internal: INTERNAL;

mutable: MUTABLE;

let: LET ;

fun: FUN expression+ RIGHT_ARROW expression;

fun_type: dotIentifier (RIGHT_ARROW dotIentifier)+;

typezation: COLON (round_brackets|dotIentifier);

if_then_elif_else: 'if' expression+ 'then' expression+ 
    ('elif' expression+ 'then' expression+)*
    ('else' expression)?;

while_do: WHILE expression+ DO; 

for: FOR expression+ (TO|DOWNTO|IN) expression+ DO;

add: ADD;

mul: MUL;

div: DIV;

minus: MINUS;

pow: POW;

mod: MOD;

not_equal: NOT_EQUAL;

less: LESS;

less_equal: LESS_EQUAL;

greater: GREATER;

greater_equal: GREATER_EQUAL;

equal: EQUAL;

and: AND;

or: OR;

lshift: LSHIFT;

rshift: RSHIFT;

log_mul: LOG_MUL;

log_add: LOG_ADD;

log_xor: LOG_XOR;

log_not: LOG_NOT;
not: NOT;

pipe: PIPE;

compos: COMPOS;

assign: ASSIGN;

type: TYPE expression+ EQUAL expression;

module: MODULE dotIentifier;

open: OPEN dotIentifier;

namespace: NAMESPACE dotIentifier;

class: CLASS expression+ END;

do: DO;

new: NEW expression;

then: THEN;

seq: SEQ '{' expression+ (SEMICOLON expression+)* '}';

list: '[' expression+ (SEMICOLON expression+)*']';

array: '[|' expression+ (SEMICOLON expression+)*'|]';

map: MAP '[' expression+ COMMA expression+ (SEMICOLON expression+ COMMA expression+)* ']';

generator: (INT|FLOAT) DOTDOT (INT|FLOAT) ((DOTDOT) (INT|FLOAT))?;

set: SET expression;

async_rule: ASYNC '{' expression* '}' ;

task: TASK '{' expression* '}' ;

exclamation_mark: EXCLAMATION_MARK;

match_with: MATCH expression+ WITH
('|' expression+ RIGHT_ARROW expression+ '\n')+;

try_with_finally: TRY expression* (WITH ('|' expression* RIGHT_ARROW expression*)*)? 
   (FINALLY expression)?; 

use: USE expression* EQUAL expression;

using: USING round_brackets expression;

raise: RAISE;

reraise: RERAISE;

failwith: FAILWITH;

invalidArg: INVALIDARG;

exception_of: EXCEPTION expression* OF expression;

member: MEMBER (THIS|MISSING_ARG) dot dotIentifier+ equal expression;

val: VAL mutable? (internal|public|private)? dotIentifier COLON dotIentifier;

struct: STRUCT expression* END;

with_get_set: (WITH ((private|internal|public)? GET UNIT EQUAL expression) 
    (AND ((private|internal|public)? SET expression* EQUAL expression)?) 
    | (WITH (private|internal|public)? expression* EQUAL expression));

tuple: '(' expression (COMMA expression)+ ')';

with: WITH;

record: '{' (((expression COLON dotIentifier) *)| (expression* with expression*))'}';

of:OF;

enum: ('|' dotIentifier (equal|of) dotIentifier)+;

inherit: INHERIT;

default: DEFAULT;

override: OVERRIDE;

abstract: ABSTRACT;

base: BASE;

colon_q: COLON_Q;

interface: INTERFACE;


expression: dotIentifier
            |dot
            |int
            |float
            |bool
            |char
            |unit
            |missing_arg
            |string
            |attribute
            |let
            |round_brackets
            |rec
            |public
            |private
            |internal
            |mutable
            |fun
            |typezation
            |if_then_elif_else
            |while_do
            |for
            |add
            |mul
            |div
            |minus
            |pow
            |mod
            |not_equal
            |less
            |less_equal
            |greater
            |greater_equal
            |equal
            |and
            |or
            |lshift
            |rshift
            |log_mul
            |log_add
            |log_xor
            |log_not
            |not
            |pipe
            |compos
            |assign
            |fun_type
            |type
            |module
            |open
            |namespace
            |class
            |do
            |new
            |then
            |seq
            |generator
            |list
            |array
            |map
            |async_rule
            |task
            |exclamation_mark
            |match_with
            |try_with_finally
            |use
            |using
            |raise
            |reraise
            |failwith
            |invalidArg
            |exception_of
            |member
            |val
            |struct
            |with_get_set
            |tuple
            |with
            |record
            |enum
            |inherit
            |default
            |override
            |abstract
            |base
            |colon_q
            |interface
            ;

exprs: expression* EOF;
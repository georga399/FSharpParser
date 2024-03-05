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

DOLLAR: '$';

// TYPE: 'type';

// MODULE: 'module';

// OPEN: 'open';

// NAMESPACE: 'namespace';

// MOD_ACCESS: PUBLIC|PRIVATE|INTERNAL;

// ASYNC: 'async';

// TASK: 'task';

// NEW: 'new';

// THIS: 'this';

// MEMBER: 'member';

// SEQ: 'seq';

// MAP: 'Map';

// SET: 'set';

// RAISE: 'raise';

// RERAISE: 'reraise';

// FAILWITH: 'failwith';

// INVALIDARG: 'invalidArg';

// VAL: 'val';

// type of vars
// literals
// async await
// open namespace using
//mutable
// DOT: '.';

// EXCLAMATION_MARK: '!';
// COMMA: ',';
// SEMICOLON: ';'
COLON: ':';
// ASSIGN: '<-';
// PIPE: '|>';
MISSING_ARG: '_';
RIGHT_ARROW: '->';
// COMPOS: '>>';

ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
POW: '**';
MOD: '%';

EQUAL: '=';
// NOT_EQUAL: '<>';
// LESS: '<';
// GREATER: '>';
// LESS_EQUAL: '<=';
// GREATER_EQUAL: '>=';

// AND:'&&';
// OR:'||';
// LSHIFT: '<<<';
// RSHIFT: '>>>';
// LOG_MUL: '&&&';
// LOG_ADD: '|||';
// LOG_XOR: '^^^';
// LOG_NOT: '~~~';
// NOT: 'not';



// rules
dotIentifier: IDENTIFIER ('.'IDENTIFIER)*;

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

typezation: COLON (round_brackets|dotIentifier);

if_then_elif_else: 'if' expression+ 'then' expression+ 
    ('elif' expression+ 'then' expression+)*
    ('else' expression)?;

add: ADD;

mul: MUL;

div: DIV;

minus: MINUS;

pow: POW;

mod: MOD;

equal: EQUAL;

expression: dotIentifier
            |int
            |unit
            |attribute
            ;

exprs: expression* EOF;
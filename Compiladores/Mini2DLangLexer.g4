lexer grammar Mini2DLangLexer;

// Palabras reservadas
SPRITE: 'sprite';
AT: 'at';
MOVE: 'move';
JUMP: 'jump';
RUN: 'run';
CROUCH: 'crouch';
STOP: 'stop';
SET_ANIMATION: 'set_animation';
IF: 'if';
ELSE: 'else';
LOOP: 'loop';
SET: 'set';
GRAVITY: 'gravity';
WORLD_WIDTH: 'world_width';
WORLD_HEIGHT: 'world_height';
PLAYER_SPEED: 'player_speed';

// Operadores y delimitadores
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';
DOT: '.';
ASSIGN: '=';
SEMICOLON: ';';

// Operadores de comparación
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

// Operadores aritméticos
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

// Literales
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n])* '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Comentarios
COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// Espacios en blanco
WS: [ \t\r\n]+ -> skip;

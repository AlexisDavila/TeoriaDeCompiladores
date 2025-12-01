parser grammar Mini2DLangParser;

options {
    tokenVocab=Mini2DLangLexer;
}

// Regla principal
program: statement* EOF;

// Declaraciones y comandos
statement
    : spriteDeclaration
    | environmentSetting
    | action
    | controlFlow
    ;

// Declaración de sprite
spriteDeclaration
    : SPRITE IDENTIFIER AT LPAREN expr COMMA expr RPAREN
    ;

// Configuración del entorno
environmentSetting
    : SET GRAVITY ASSIGN expr
    | SET WORLD_WIDTH ASSIGN expr
    | SET WORLD_HEIGHT ASSIGN expr
    | SET PLAYER_SPEED ASSIGN expr
    ;

// Acciones del sprite
action
    : IDENTIFIER DOT MOVE LPAREN expr COMMA expr RPAREN
    | IDENTIFIER DOT JUMP LPAREN RPAREN
    | IDENTIFIER DOT RUN LPAREN expr RPAREN
    | IDENTIFIER DOT CROUCH LPAREN RPAREN
    | IDENTIFIER DOT STOP LPAREN RPAREN
    | IDENTIFIER DOT SET_ANIMATION LPAREN STRING RPAREN
    ;

// Control de flujo
controlFlow
    : ifStatement
    | loopStatement
    ;

ifStatement
    : IF condition LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?
    ;

loopStatement
    : LOOP expr LBRACE statement* RBRACE
    ;

// Condiciones
condition
    : expr comparator expr
    | expr
    ;

comparator
    : EQ
    | NEQ
    | LT
    | GT
    | LTE
    | GTE
    ;

// Expresiones
expr
    : expr (MULT | DIV) expr          # MulDiv
    | expr (PLUS | MINUS) expr        # AddSub
    | NUMBER                           # Number
    | IDENTIFIER                       # Identifier
    | LPAREN expr RPAREN              # Parens
    ;

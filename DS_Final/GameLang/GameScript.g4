grammar GameScript;

script: (command)+ EOF;

command:
      moveCommand
    | jumpCommand
    | attackCommand
    | waitCommand
    ;

moveCommand: 'move' direction amount (NEWLINE | ';')+;
jumpCommand: 'jump' (NEWLINE | ';')+;
attackCommand: 'attack' target (NEWLINE | ';')+;
waitCommand: 'wait' amount 'seconds' (NEWLINE | ';')+;

direction: 'left' | 'right' | 'up' | 'down';
target: 'enemy' | 'boss' | 'object';
amount: INT;

INT: [0-9]+;
NEWLINE: ('\r'? '\n')+;
WS: [ \t]+ -> skip;

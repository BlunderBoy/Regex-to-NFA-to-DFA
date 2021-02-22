grammar Regex;

 /*
    Parser
    regex = regexAtom or regexAtom | reuniune
            (regex)(regex) concatenare
            regexAtom * | kleenstar
            (regexAtom) | paranteze
  */

regex : regex KLEENSTAR #regexStar |
        '('regex')' #regexParanth |
        regex regex #regexConcat |
        regex OR regex #regexOr |
        REGEX_ATOM #regexAtom;

/*
    Lexer
    regexAtom = ([a-zA-Z] | [A-Za-z])*
 */

REGEX_ATOM : [a-z]; //un caracter
OR : '|';
KLEENSTAR : '*';
import sys
from antlr4 import *
from RegexLexer import RegexLexer
from RegexParser import RegexParser
from RegexVisitor import RegexVisitor
from nfa import *
import pprint

def filePrint(nfa: NFA, fileToPrint):

    # numar stari
    #print(nfa.numberOfStates)
    print(nfa.numberOfStates, file=fileToPrint)

    # starea finala
    for i in nfa.finalStates:
        #print(i)
        print(i,  file=fileToPrint)

    # tranzitii

    lista = list(nfa.tabelTranzitii.items())
    lista.sort()
    #print(lista)

    for (stare, simbol), nextState in lista:
        #print(str(stare), simbol, end="")
        print(str(stare), simbol, end="", file=fileToPrint)

        #print(" ", end="")
        print(" ", end="", file=fileToPrint)
        
        
        for i in nextState:
            #print(i, " ", end="", sep="")
            print(i, " ", end="", sep="", file=fileToPrint)
        
        
        #print()    
        print(file=fileToPrint) 

def main(argv):

    # antlr
    input = FileStream(sys.argv[1])
    nfaFile = open(argv[2], "w")
    dfaFile = open(argv[3], "w")

    lexer = RegexLexer(input)
    stream = CommonTokenStream(lexer)
    parser = RegexParser(stream)

    tree = parser.regex()    
    visitor = RegexVisitor()
    visitor.visit(tree)

    # dupa ce am facut partea de parsare NFA-ul se gaseste in RegexVisitor.stiva
    nfa = RegexVisitor.stivaNFA.pop()
    filePrint(nfa, nfaFile)
    #print(nfa)

    (stari, tabel) = NFA2DFA(nfa)
    pp = pprint.PrettyPrinter()
    printOutput(stari, tabel, nfa.finalStates, dfaFile)

if __name__ == "__main__":
    main(sys.argv)
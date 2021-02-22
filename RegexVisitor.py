from antlr4 import *
import pprint
if __name__ is not None and "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

from nfa import NFA

def mergeNFAConcat(nfa1 : NFA, nfa2 : NFA):

    # calculam numarul de stari la final
    numarStariTotal = nfa1.numberOfStates + nfa2.numberOfStates
    
    # instantiem un nfa nou
    newNfa = NFA(numarStariTotal)
    
    # setam starea finala ca fiind numar total de stari - 1 (ultima stare din nfa2)
    newNfa.finalStates.append(numarStariTotal - 1)

    # setam tranzitiile
    # adaugam fiecare tranzitie din nfa1 asa cum e
    newNfa.tabelTranzitii = nfa1.tabelTranzitii.copy()

    # adaugam fiecare tranzitie din nfa2 cu starile shiftate
    # facem un map + numarStariNfa1 peste stari
    for (state, simbol), nextState in nfa2.tabelTranzitii.items():
        newNfa.tabelTranzitii[(state + (nfa1.numberOfStates), simbol)] = [i + nfa1.numberOfStates for i in nextState]

    # adaugam "podul (bridge)" intre cele 2 nfa-uri (o tranzitie pe eps)
    # tranzitia este intre starea cu numarul nfa1.numarStari - 1 si nf1.numarStari
    try:
        newNfa.tabelTranzitii[(nfa1.numberOfStates - 1, "eps")] = newNfa.tabelTranzitii[(nfa1.numberOfStates - 1, "eps")] + [nfa1.numberOfStates]
    except:
        newNfa.tabelTranzitii[(nfa1.numberOfStates - 1, "eps")] = [nfa1.numberOfStates]

    # print("concat")
    # print(newNfa)
    # print()

    return newNfa

def changeNFAStar(nfa : NFA):

    # se creeaza un nfa nou cu 2 stari in plus
    newNfa = NFA(nfa.numberOfStates + 2)

    # adaugam starea finala
    newNfa.finalStates.append(nfa.numberOfStates - 1)

    # adaugam starile celuilalt nfa cu +1 la stare
    for (state, simbol), nextState in nfa.tabelTranzitii.items():
        newNfa.tabelTranzitii[(state + 1, simbol)] = [i + 1 for i in nextState]

    # adaugam starile ajutatoare cu tranzitii pe eps

    # de la 0 la nfa
    newNfa.tabelTranzitii[(0, "eps")] = [1]

    # de la nfa la finala
    try:
        newNfa.tabelTranzitii[((newNfa.numberOfStates - 2), "eps")] = newNfa.tabelTranzitii[((newNfa.numberOfStates - 2), "eps")] + [newNfa.numberOfStates - 1]
    except:
        newNfa.tabelTranzitii[((newNfa.numberOfStates - 2), "eps")] = [newNfa.numberOfStates - 1]

    # de la finala la initiala si invers
    newNfa.tabelTranzitii[(0, "eps")] = newNfa.tabelTranzitii[(0, "eps")] + [newNfa.numberOfStates - 1]

    try:
        newNfa.tabelTranzitii[(newNfa.numberOfStates - 1, "eps")] = [0]
    except:
        newNfa.tabelTranzitii[(newNfa.numberOfStates - 1, "eps")] = newNfa.tabelTranzitii[(newNfa.numberOfStates - 1, "eps")] + [0]

    # print("star")
    # print(newNfa)
    # print()

    return newNfa

def mergeNFAOR(nfa1 : NFA, nfa2 : NFA):
    
    # calculam numarul de stari la final
    numarStariTotal = nfa1.numberOfStates + nfa2.numberOfStates + 2
    
    # instantiem un nfa nou
    newNfa = NFA(numarStariTotal)
    
    # setam starea finala ca fiind numar total de stari - 1 (ultima stare din nfa2)
    newNfa.finalStates.append(numarStariTotal - 1)

    # setam tranzitiile
    # adaugam fiecare tranzitie din nfa1 cu stare +1
    for (state, simbol), nextState in nfa1.tabelTranzitii.items():
        newNfa.tabelTranzitii[(state + 1, simbol)] = [i + 1 for i in nextState]

    # adaugam fiecare tranzitie din nfa2 cu starile shiftate
    # facem un map + numarStariNfa1 peste stari
    for (state, simbol), nextState in nfa2.tabelTranzitii.items():
        newNfa.tabelTranzitii[(state + nfa1.numberOfStates + 1, simbol)] = [i + nfa1.numberOfStates + 1 for i in nextState]

    # adaugam tranzitii de pe starile ajutatoare la cele 2 nfa-uri

    # de pe 0 pe cele 2 nfa-uri
    newNfa.tabelTranzitii[(0, "eps")] = [nfa1.numberOfStates + 1, 1]

    # de pe starile finale ale celor 2 nfa-uri pe finala
    try:
        newNfa.tabelTranzitii[(nfa1.numberOfStates, "eps")] = newNfa.tabelTranzitii[(nfa1.numberOfStates, "eps")] + [newNfa.numberOfStates - 1]
    except:
        newNfa.tabelTranzitii[(nfa1.numberOfStates, "eps")] = [newNfa.numberOfStates - 1]

    try:
        newNfa.tabelTranzitii[(newNfa.numberOfStates - 2, "eps")] = newNfa.tabelTranzitii[(newNfa.numberOfStates - 2, "eps")] + [newNfa.numberOfStates - 1] 
    except:
        newNfa.tabelTranzitii[(newNfa.numberOfStates - 2, "eps")] = [newNfa.numberOfStates - 1] 

    # print("or")
    # print(newNfa)
    # print()

    return newNfa

# Botom up aproach
class RegexVisitor(ParseTreeVisitor):
    
    count = 0
    debug = 0

    # stiva ce contine nfa-urile
    stivaNFA = []

    # Visit a parse tree produced by RegexParser#regexOr.
    def visitRegexOr(self, ctx:RegexParser.RegexOrContext):
        returnValue = self.visitChildren(ctx)

        #debug information
        if self.debug:
            print(self.count)
            self.count += 1
            print("or", ctx.getText())
        
        #actual operations

        # obtinem nfa1 si nfa2
        nfa2 = self.stivaNFA.pop()
        nfa1 = self.stivaNFA.pop()

        # merge the nfas
        newNFA = mergeNFAOR(nfa1, nfa2)

        # push the new nfa
        self.stivaNFA.append(newNFA)

        return returnValue


    # Visit a parse tree produced by RegexParser#regexStar.
    def visitRegexStar(self, ctx:RegexParser.RegexStarContext):
        returnValue = self.visitChildren(ctx)

        #debug information
        if self.debug:
            print(self.count)
            self.count += 1
            print("regex star", ctx.getText())
        
        #actual operations

        # get the nfa
        nfa = self.stivaNFA.pop()

        # change the nfa
        newNFA = changeNFAStar(nfa)

        # push the new nfa
        self.stivaNFA.append(newNFA)

        return returnValue


    # Visit a parse tree produced by RegexParser#regexParanth.
    def visitRegexParanth(self, ctx:RegexParser.RegexParanthContext):
        returnValue = self.visitChildren(ctx)

        #debug information
        if self.debug:
            print(self.count)
            self.count += 1
            print("paranth", ctx.getText())
        
        #actual operations
        return returnValue

    # Visit a parse tree produced by RegexParser#regexConcat.
    def visitRegexConcat(self, ctx:RegexParser.RegexConcatContext):
        returnValue = self.visitChildren(ctx)

        #debug information
        if self.debug:
            print(self.count)
            self.count += 1
            print("concat", ctx.getText())
        
        #actual operations

        # obtinem nfa1 si nfa2
        nfa2 = self.stivaNFA.pop()
        nfa1 = self.stivaNFA.pop()

        # merge the nfas
        newNfa = mergeNFAConcat(nfa1, nfa2)

        # push the new NFA
        self.stivaNFA.append(newNfa)

        return returnValue


    # Visit a parse tree produced by RegexParser#regexAtom.
    def visitRegexAtom(self, ctx:RegexParser.RegexAtomContext):
        returnValue = self.visitChildren(ctx)

        #debug information
        if self.debug:
            print(self.count)
            self.count += 1
            print("atom ", ctx.getText())
        
        #actual operations

        # se creeaza un dfa nou cu 2 stari
        newNfa = NFA(2)

        # adaugam 1 ca stare finala
        newNfa.finalStates.append(1)

        # adaugam tranzitia de pe 0 pe 1 pe simbolul din atom
        newNfa.tabelTranzitii[(0, str(ctx.getText()))] =  [1]

        # adaugam nfa-ul in stiva
        self.stivaNFA.append(newNfa)

        return returnValue

del RegexParser
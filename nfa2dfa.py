#Macarie Razvan Cristian 332CB
import sys
import pprint

def readNFA(file):
        lines = list(map(lambda b : b.split(" "),map(lambda a : a.strip("\n"), file.readlines())))
        return lines

class NFA():
    def __init__(self, file):
        lines = readNFA(file)
        self.numberOfStates = int(lines[0][0])
        self.finalStates = [int(i) for i in lines[1]]
        self.tabelTranzitii = dict()

        for curent in lines[2::]:
            self.tabelTranzitii[(int(curent[0]), curent[1])] = list(map(int, curent[2::]))

    def __str__(self):
        pp = pprint.PrettyPrinter()
        return "NFA cu " + str(self.numberOfStates) + " stari dintre care " + str(self.finalStates) + " finale " + "\ntranzitiile sunt: \n" + pp.pformat(self.tabelTranzitii)

    # am folosit o abordare pseudo recursiva pentru ca aveam nevoie sa nu adaug in set
    # daca ceva este deja in set si avea nevoie de un set global, asa ca am folosit o stiva
    # primeste o lista de stari sau o stare
    # intoarce o lista de stari care reprezinta e tranzitii
    def epsilonClosure(self, stari):
        rezultat = set()
        stiva = []

        #verificam daca e int sau lista si initializam stiva cum trebuie
        if isinstance(stari, int):
            stiva.append(stari)
        else:
            stiva = stiva + stari
        
        while stiva != []:
            # adaugam in rezultat elementul curent
            elementCurent = stiva.pop(0)
            rezultat.add(elementCurent)

            # avem nevoie de un if deoarece atunci cand se uita la starile care nu au tranzitii
            # care pleaca din ele genereaza un KeyError(stare, 'eps') pentru ca tranzitia nu exista
            if (elementCurent, "eps") in self.tabelTranzitii:
                # pentru starea curenta din stiva adaugam in stiva starile in care ajungem in e tranzitii
                nextStates = self.tabelTranzitii[(elementCurent, "eps")]
                for stare in nextStates:
                    if stare not in rezultat:
                        stiva.append(stare)
        return rezultat

    # introace toate simbolurile pe care sunt tranzitii din NFA
    # adaugam toate simbolurile intr-un set 
    # intoarcem la final o lista sortata fara "eps"
    def availableSimbols(self):
        simboluri = set()
        # pattern matching in python super nice
        for (_, simbol) in self.tabelTranzitii.keys():
            simboluri.add(simbol)
        try:
            simboluri.remove("eps")
        except:
            pass
        simboluri = list(simboluri)
        simboluri.sort()
        return simboluri

#scoate duplicatele dintr-o lista
def removeDupes(lista):
    listaNoua = []
    for elem in lista:
        if elem not in listaNoua:
            listaNoua.append(elem)
    return listaNoua

# functie(numeVariabila: numeClasa) pentru control al tiparii
def NFA2DFA(nfa: NFA):
    stariRezultate = set()
    simboluriValabile = nfa.availableSimbols()

    stari = []

    coada = []
    coada.append(tuple(nfa.epsilonClosure(0)))

    tabelNouTranzitii = dict()

    while coada != []:
        subsetCurent = coada.pop(0)
        stariRezultate.add(tuple(subsetCurent))
        stari.append(list(subsetCurent))
    
        for simbol in simboluriValabile:
            subset = set()
            for stare in subsetCurent:
                if (stare, simbol) in nfa.tabelTranzitii.keys():

                    # tranzitia in alta stare pe un simbol
                    tranzitie = nfa.tabelTranzitii[(stare, simbol)]

                    # verificam daca avem o singura stare urmatoare sau o lista de stari urmatoare
                    if isinstance(tranzitie, int):
                        subset.add(nfa.tabelTranzitii[(stare, simbol)])
                    else:
                        for i in tranzitie:
                            subset.add(i)
            
            # adaugam epsilon tranzitia starilor in care pot ajunge intr-un alt tabel de tranzitii
            stariInCarePotAjunge = nfa.epsilonClosure(list(subset))
            tabelNouTranzitii[(tuple(subsetCurent), simbol)] = list(stariInCarePotAjunge)
            
            # adaugam subsetul in coada
            if tuple(stariInCarePotAjunge) not in stariRezultate:
                if stariInCarePotAjunge != set():
                    coada.append(tuple(stariInCarePotAjunge))

    stari = removeDupes(stari)
    return (stari, tabelNouTranzitii) 

def printOutput(stari, tabel, stariFinale, fileToPrint):
    #printam numarul de stari
    print(len(stari), file=fileToPrint)

    stariFinaleDFA = set()
    index = -1
    for stare in stari:
        index += 1
        for stareFinala in stariFinale:
            if stareFinala in stare:
                stariFinaleDFA.add(index)

    #printam starile finale
    # map (++" ") (map show lista)
    print("".join(list(map(lambda a: a + " ", map(str, stariFinaleDFA)))), file=fileToPrint)

    tranzitiiFinale = dict()
    for (tuplu, simbol), nextState in tabel.items():
        tranzitiiFinale[(stari.index(list(tuplu)), simbol)] = stari.index(nextState)

    lista = list(tranzitiiFinale.items())
    lista.sort(key = lambda tup: tup[0][0])
    for (stare, simbol), nextState in lista:
        print(str(stare), simbol, str(nextState), file=fileToPrint)
        print(str(stare), simbol, str(nextState))
    

def main(argv):
    nfa = NFA(fileToRead)
    (stari, tabel) = NFA2DFA(nfa)
    printOutput(stari, tabel, nfa.finalStates ,fileToPrint)

if __name__ == "__main__":
    main(sys.argv)

   
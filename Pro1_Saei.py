from collections import defaultdict


class NFA():
    transition = []

    def __init__(self, grammar):
        counter = 0
        for key in grammar.keys():
            indexMap[key] = counter
            for value in grammar[key]:
                if value[-1].isupper():
                    self.transition.append(f"{key}->{value[:-1]}->{value[-1]}")
                else:
                    self.transition.append(f"{key}->{value}->Final")
            counter += 1
        indexMap["Final"] = counter

    def buildMatrix(self):
        matrix = [[""] * len(indexMap) for i in range(len(indexMap))]
        for x in G.keys():
            matrix[indexMap[x]][indexMap[x]] = "λ"
        for x in self.transition:
            a, b, c = map(str, x.split("->"))
            if matrix[indexMap[a]][indexMap[c]] == "":
                matrix[indexMap[a]][indexMap[c]] = b
            else:
                matrix[indexMap[a]][indexMap[c]] += f"+{b}"

        matrix[len(indexMap)-1][len(indexMap)-1] = "λ"
        return matrix


def printAdjMatrix():
    print("Adjacnecy Matrix: ")
    for x in adj_matrix:
        print(x)


def printGrammar():
    print("Right Linear Grammar: ")
    for key in G.keys():
        for item in G[key]:
            print(key, " -> ", item)


def trim():
    x = G.keys()
    for key in x:
        temp = []
        for item in G[key]:
            if not (item[-1] in x) and (item[-1].isupper()):
                temp.append(item)
        li = G[key]

        for i in temp:
            if i in li:
                li.remove(i)

        G[key] = li


if __name__ == "__main__":
    G = defaultdict()
    indexMap = defaultdict()

    while (True):
        try:
            # get lines of # sepreated right linear grammar
            grammar = input()
            if not grammar[0] in G:
                temp = list()
                temp.append(grammar[2:])
                G[grammar[0]] = temp
            else:
                li = G[grammar[0]]
                li.append(grammar[2:])
                G[grammar[0]] = li
        except Exception:
            break

    trim()
    printGrammar()
    nfa = NFA(G)
    adj_matrix = nfa.buildMatrix()
    print(indexMap)
    printAdjMatrix()

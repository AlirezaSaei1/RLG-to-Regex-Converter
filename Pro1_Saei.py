from collections import defaultdict


class FA():
    states = []

    def __init__(self) -> None:
        for key in G.keys():
            state = State(key)
            self.states.append(state)

            if "Start" in key:
                self.startState = state

        self.finalState = State("Final")
        self.states.append(self.finalState)

    # def p(self):
    #     for x in self.states:
    #         print(x.stateName)
    #         for i in x.transitions.keys():
    #             print("Ts:")
    #             print(i, x.transitions[i])


class State():
    def __init__(self, name):
        self.stateName = name
        self.transitions = defaultdict()

        if name != "Final":
            for x in G[name]:
                if x[-1].isupper():
                    self.transitions[x[:-1]] = x[-1]
                else:
                    self.transitions[x] = "Final"


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
    adj_matrix = defaultdict(dict)

    li1 = []
    li1.append("λS")
    G["Start"] = li1

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

    fa = FA()
    # fa.p()

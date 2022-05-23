from collections import defaultdict


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
                print("Deleted", key, item)
                temp.append(item)
        li = G[key]

        for i in temp:
            if i in li:
                li.remove(i)

        G[key] = li


G = defaultdict()
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

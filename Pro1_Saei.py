from collections import defaultdict


def printGrammar():
    for key in G.keys():
        for item in G[key]:
            print(key, " -> ", item)


G = defaultdict()
while (True):
    try:
        # get lines of # sepreated right linear grammar
        grammar = input()
        if(not grammar[-1].isupper()):
            raise ValueError("Grammar Is Not Right Linear")
        if not grammar[0] in G:
            temp = list()
            temp.append(grammar[2:])
            G[grammar[0]] = temp
        else:
            li = G[grammar[0]]
            li.append(grammar[2:])
            G[grammar[0]] = li
    except (Exception) as e:
        print(e)
        break

printGrammar()

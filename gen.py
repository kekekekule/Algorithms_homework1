import networkx as nx
import random as rnd

test_number = 31

DIRECTORY = 'tests/'

for _ in range(30):
    test = open('{}{}.in'.format(DIRECTORY, test_number), 'w')

    n = rnd.randint(100, 300)

    m = min(rnd.randint(4, 6) * n, 850)

    g = nx.gnm_random_graph(n, m)

    print(n, len(g.edges), file=test)
    for edge in g.edges:
        print(edge[0] + 1, edge[1] + 1, file=test)

    test_number += 1
    test.close()

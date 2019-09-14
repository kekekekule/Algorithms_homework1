import networkx as nx
import random as rnd


# gnp = [nx.gnp_random_graph, nx.fast_gnp_random_graph, nx.erdos_renyi_graph] * 2
# gn = [nx.cycle_graph, nx.complete_graph, nx.ladder_graph, nx.star_graph, nx.wheel_graph] * 2
gnm = [nx.gnm_random_graph] * 30

funcs = (gnm,)

test_number = 31

DIRECTORY = 'tests/'

for pack in funcs:
    for func in pack:
        test = open('{}{}.in'.format(DIRECTORY, test_number), 'w')

        prob = rnd.random()
        n = rnd.randint(100, 300)

        if func == nx.complete_graph:
            n = rnd.randint(30, 35)

        m = min(rnd.randint(4, 6) * n, 850)

        g = func(n, m)

        print(n, len(g.edges), file=test)
        for edge in g.edges:
            print(edge[0] + 1, edge[1] + 1, file=test)

        test_number += 1
        test.close()
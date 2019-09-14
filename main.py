from pysat.solvers import Glucose3
import sys
import time

begin = time.clock()

NUMBER = sys.argv[1]
DIRECTORY = 'tests/'
INPUT_FILE = DIRECTORY + NUMBER + '.in'
OUTPUT_FILE = DIRECTORY + NUMBER + '.out'

fin = open(INPUT_FILE, 'r')
fout = open(OUTPUT_FILE, 'w')

n, m = map(int, fin.readline().rstrip().split())

print('running ' + INPUT_FILE + ', n = {}, m = {}'.format(n, m), file=sys.stderr)

# n * k vertices in CNF, vertices
# with numbers [i * k, (i + 1) * k)
# stand for i-th vertex in graph

edges = []

for i in range(m):
    edges.append(tuple(sorted(list(map(int, fin.readline().rstrip().split())))))

# bruteforcing number of colors

answer = None

for colors in range(1, n + 1):
    g = Glucose3()
    for i in range(n):
        current_clause = []
        for c in range(colors):

            # for each vertex adding clause (vi_c1 or ... or vi_ck)
            # meaning each vertex should be colored somehow

            current_clause.append(i * colors + c + 1)
        g.add_clause(current_clause)
    for v, u in edges:
        for c in range(colors):
            # for each edge (u, v) adding clause (~u or ~v) where ~ stands for "not"
            g.add_clause([-((v - 1) * colors + c) - 1, -((u - 1) * colors + c) - 1])
    ok = g.solve()
    if ok:
        answer = colors
        print(colors, file=fout)
        model = g.get_model()

        vertex_color = []
        for i in range(n):
            one_counter = 0
            for c in range(colors):
                if model[i * colors + c] > 0:

                    # Glucose3 sometimes puts one more than
                    # for one color for some vertices
                    # however we can just ignore it

                    if one_counter == 1:
                        continue

                    vertex_color.append(c + 1)
                    one_counter += 1
        print(*vertex_color, file=fout)

        break

fin.close()
fout.close()

end = time.clock()

assert(answer is not None)

print('test #{} complete in {} seconds with answer = {}'.format(NUMBER, end - begin, answer), file=sys.stderr)

import sys

OK = '\033[92m'
WRONG = '\033[91m'
END = '\033[0m'

DIRECTORY = 'tests/'
input_file = DIRECTORY + sys.argv[1]
output_file = DIRECTORY + sys.argv[2]
answer_file = DIRECTORY + sys.argv[3] if len(sys.argv) >= 4 else None

with open(input_file, 'r') as f:
    n, m = [int(x) for x in next(f).split()]
    edges = []
    for _ in range(m):
        u, v = [int(x) for x in next(f).split()]
        edges.append((u - 1, v - 1))

with open(output_file, 'r') as f:
    chromatic_number = int(next(f))
    coloring = [int(x) for x in next(f).split()]
    if len(coloring) != n:
        print(WRONG, 'Wrong:', END, 'expected {} colors, got {}'.format(n, len(coloring)))
        sys.exit()

    for index, color in enumerate(coloring):
        if color <= 0:
            print(WRONG, 'Wrong:', END, 'c[{}] <= 0'.format(index + 1))
            sys.exit()
        if color > chromatic_number:
            print(WRONG, 'Wrong:', END, 'c[{}] > {}'.format(index + 1, chromatic_number))
            sys.exit()

for u, v in edges:
    if coloring[u] == coloring[v]:
        print(WRONG, 'Wrong:', END, 'vertices {} and {} are connected by an edge but colored with the same color'.format(u + 1, v + 1))
        sys.exit()

if answer_file is not None:
    with open(answer_file, 'r') as f:
        answer = int(next(f))
        if chromatic_number != answer:
            print(WRONG, 'Wrong:', END, 'your chromatic number is {} but the real chromatic number is {}'.format(chromatic_number, answer))
            sys.exit()

print(OK + 'Ok!' + END)

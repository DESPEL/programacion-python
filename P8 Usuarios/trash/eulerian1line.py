find_eulerian_path = [lambda graph: (lambda graph, numbers: [(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda get_path: (lambda args: args[2] if len(args[2]) == len(args[0]) else [[get_path([args[0], n[0] if n[1] == args[1] else n[1], args[2]+[n]]) for n in filter(lambda x: args[1] in x and x not in args[2], args[0])] or [None, ]][0][-1]))([graph, node, []])for node in numbers][0])(graph, list(set(sum(graph, []))))][0]

print(find_eulerian_path([
    [0, 1], [0, 2], [0, 3], [0, 4], [0, 5],
    [1, 2], [1, 3], [1, 4], [1, 5],
    [2, 3], [2, 4], [2, 5],
    [3, 4], [3, 5],
    [4, 5]
]))
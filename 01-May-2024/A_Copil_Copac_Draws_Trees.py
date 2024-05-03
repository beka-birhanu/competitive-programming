def count_reads(g, curr_node, drawn_at, visited):
    # max_read = 0

    # for edge_idx, nbr in g[curr_node]:
    #     curr_read = 0
    #     # print(nbr, visited)
    #     if nbr not in visited:
    #         # print(edge_idx, drawn_at)
    #         if edge_idx < drawn_at:
    #             curr_read += 1

    #         visited.add(nbr)
    #         curr_read += count_reads(g, nbr, edge_idx, visited)

    #         max_read = max(max_read, curr_read)
    # # print(curr_node, max_read, g[curr_node])
    st = [(1, n, 0)]
    max_read = 0

    while st:
        curr_node, drawn_at, curr_read = st.pop()
        max_read = max(max_read, curr_read)
        for edge_idx, nbr in g[curr_node]:
            # print(nbr, visited)
            curr_read_n = curr_read
            if nbr not in visited:
                # print(edge_idx, drawn_at)
                if edge_idx < drawn_at:
                    curr_read_n += 1

                visited.add(nbr)
                st.append((nbr, edge_idx, curr_read_n))

    return max_read


for _ in range(int(input())):
    n = int(input())
    edges = [list(map(int, input().split())) for i in range(n-1)]
    g = [[] for i in range(n+1)]

    for i, (x, y) in enumerate(edges):

        g[x].append((i, y))
        g[y].append((i, x))
    # print(g)
    print(count_reads(g, 1, n, set([1])))

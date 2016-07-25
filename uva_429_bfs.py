# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

429 Word Transformation

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/4/429.pdf
http://luckycat.kshs.kh.edu.tw/homework/q429.htm

"""

import sys
from collections import deque


def bfs(src, tgt, graph):
    """
    src: string
    tgt: string, the same length as src
    graph: the nodes in the graph has the same length as src and tgt.
    """

    n_node = len(graph.keys())
    visited = {k: False for k in graph.keys()}
    queue = deque([(src, 0), ])
    visited[src] = True
    # print (graph)

    while queue:
        node, depth = queue.popleft()
        if node == tgt:
            return depth

        for child in graph[node]:
            if not visited[child]:
                queue.append((child, depth + 1))
                visited[child] = True


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        try:
            # the length of a word is from 1 to 10
            len_sets = [set() for _ in range(10)]
            graphs = [dict() for _ in range(10)]

            while True:
                # dictionary
                data = (next(recs)).strip()
                if data:
                    if data == '*':
                        break
                    else:
                        len_sets[len(data) - 1].add(data)

            # build graph
            for idx, words in enumerate(len_sets):
                if not words:
                    continue
                # node
                for word in words:
                    graphs[idx][word] = []

                # edge
                word_len = idx + 1
                for jdx, word1 in enumerate(words):
                    for kdx, word2 in enumerate(words):
                        if jdx == kdx:
                            continue
                        n_diff = sum(1 for tdx in range(word_len)
                                     if word1[tdx] != word2[tdx])
                        if n_diff == 1:
                            graphs[idx][word1].append(word2)
                            graphs[idx][word2].append(word1)
            # print (graphs)

            if tdx:
                print()

            # query
            while True:
                query = next(recs).strip()
                if not query:
                    break
                src, tgt = query.split()

                ans = bfs(src, tgt, graphs[len(src) - 1])
                if ans is None:
                    ans = -1
                print("{} {} {}".format(src, tgt, ans))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()

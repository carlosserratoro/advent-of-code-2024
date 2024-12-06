# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from collections import deque


class DAG:
    """Directed Acyclic Graph.

    - No check for cycles, thus no real DAG ─ although expected to be.
    - Implementation uses adjacency sets.
    """

    def __init__(self):
        self._g = dict()
        self._g_inv = dict()

    def add_edge(self, v, w):
        if v not in self._g:
            self._g[v] = set()
        if w not in self._g:
            self._g[w] = set()
        self._g[v].add(w)

    def edge_exists(self, v, w):
        return w in self._g.get(v, set())

    # Note on the methods successors and predecessors for Day 5:
    # At first I misunderstood what the problem required and thought
    # that we had to consider elements that came after or before a
    # given one, no matter if there wasn't an explicit rule (i.e. edge)
    # between two elements (i.e. nodes). For this assumption, the
    # successors and predecessors were needed. After realising that
    # this worked only for the test input, but not the final input, I
    # noticed the mistake. I however keep these methods and their
    # implementations (which are tested) just in case I can reuse them
    # on a later Day.
    def successors(self, v):
        return self._successors(self._g, v)

    def predecessors(self, v):
        if not self._g_inv:
            self._compute_inverse()
        return self._successors(self._g_inv, v)

    def _compute_inverse(self):
        """Compute the inverse directed graph.

        Will be in hand when computing the predecessors of a node.
        """
        self._g_inv = dict()
        for node, neighbours in self._g.items():
            if node not in self._g_inv:
                self._g_inv[node] = set()
            for neighbour in neighbours:
                if neighbour not in self._g_inv:
                    self._g_inv[neighbour] = set()
                self._g_inv[neighbour].add(node)

    def _successors(self, g, v):
        """Compute the successors for a node, using the internal representation."""
        visited = set()
        dq = deque([v])
        while dq:
            node = dq.popleft()
            if node not in visited:
                visited.add(node)
                dq.extend(g[node])
        visited.remove(v)
        return visited

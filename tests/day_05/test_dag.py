# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

# We want to access protected members in these tests.
# pylint: disable=W0212
from aoc.day_05.dag import DAG


def test_add_edge():
    dag = DAG()
    assert dag._g == dict()
    assert dag._g_inv == dict()
    dag.add_edge(1, 2)
    assert dag._g == {1: {2}, 2: set()}
    assert dag._g_inv == dict()
    dag.add_edge(2, 3)
    assert dag._g == {1: {2}, 2: {3}, 3: set()}
    assert dag._g_inv == dict()
    dag.add_edge(2, 4)
    assert dag._g == {1: {2}, 2: {3, 4}, 3: set(), 4: set()}
    assert dag._g_inv == dict()


def test_successors():
    dag = DAG()
    dag.add_edge(1, 2)
    dag.add_edge(2, 3)
    dag.add_edge(2, 4)
    assert dag.successors(1) == {2, 3, 4}
    assert not dag._g_inv
    assert dag.successors(2) == {3, 4}
    assert not dag.successors(3)
    assert not dag.successors(4)


def test_predecessors():
    dag = DAG()
    dag.add_edge(1, 2)
    dag.add_edge(2, 3)
    dag.add_edge(2, 4)
    assert not dag.predecessors(1)
    assert dag._g_inv == {1: set(), 2: {1}, 3: {2}, 4: {2}}
    assert dag.predecessors(2) == {1}
    assert dag.predecessors(3) == {1, 2}
    assert dag.predecessors(4) == {1, 2}


def test_edge_exists():
    dag = DAG()
    dag.add_edge(1, 2)
    assert dag.edge_exists(1, 2)
    assert not dag.edge_exists(2, 1)


def test_get_nodes():
    dag = DAG()
    assert not list(dag.get_nodes())
    dag.add_edge(1, 2)
    dag.add_edge(2, 3)
    assert list(dag.get_nodes()) == [1, 2, 3]


def test_get_neighbours():
    dag = DAG()
    dag.add_edge(1, 2)
    assert dag.get_neighbours(1) == (2,)
    assert not dag.get_neighbours(2)
    dag.add_edge(1, 3)
    assert dag.get_neighbours(1) == (2, 3)
    assert not dag.get_neighbours(2)
    assert not dag.get_neighbours(3)


def test_paths():
    dag = DAG()
    dag.add_edge(1, 2)
    dag.add_edge(2, 3)
    dag.add_edge(2, 4)
    dag.add_edge(4, 5)
    dag.add_edge(6, 7)
    dag.add_edge(3, 5)
    assert set(dag.paths(1, 2, valid_nodes={1, 2})) == {(1, 2)}
    assert set(dag.paths(1, 5, valid_nodes={1, 2, 3, 5})) == {(1, 2, 3, 5)}
    assert set(dag.paths(1, 5, valid_nodes={1, 2, 4, 5})) == {(1, 2, 4, 5)}
    assert set(dag.paths(1, 5, valid_nodes={1, 2, 5, 7})) == set()
    assert set(dag.paths(1, 7, valid_nodes={1, 2, 3, 4, 5, 6, 7})) == set()

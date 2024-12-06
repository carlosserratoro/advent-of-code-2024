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

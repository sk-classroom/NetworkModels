import unittest
import networkx as nx
import igraph
import numpy as np
from scipy import sparse

from scripts.network_robustness import *
from scripts.k_core_decomposition import *


class Test(unittest.TestCase):
    def setUp(self, **params):
        G = nx.karate_club_graph()
        A = nx.adjacency_matrix(G)
        src, trg, _ = sparse.find(sparse.triu(A, 1))
        self.g = igraph.Graph(tuple(zip(src, trg)))

    def test_random_attack(self):
        x, y = random_attack(self.g)

        assert np.all(np.isclose(np.diff(x), 1.0 / self.g.vcount()))
        assert len(x) == len(y)

        rindex = np.mean(y)

        assert rindex >= 0.3
        assert rindex <= 0.5

    def test_targeted_attack(self):
        x, y = degree_targeted_attack(self.g)
        assert np.all(np.isclose(np.diff(x), 1.0 / self.g.vcount()))
        assert len(x) == len(y)
        rindex = np.mean(y)
        assert np.isclose(rindex, 0.16050420168067225)

    def test_betweenness_attack(self):
        x, y = betweenness_targeted_attack(self.g)
        assert np.all(np.isclose(np.diff(x), 1.0 / self.g.vcount()))
        assert len(x) == len(y)
        rindex = np.mean(y)
        assert np.isclose(rindex, 0.1588235294117647)

    def test_kcore(self):
        node_indices = kcore_decomposition(self.g, k=4)

        assert np.all(
            np.sort(node_indices)
            == np.sort(np.where(np.array(self.g.coreness()) == 4)[0])
        )

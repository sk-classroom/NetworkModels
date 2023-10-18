In this assignment, we will break a network into pieces. Many empirical networks are hard to break if we randomly attack it. However, by strategically attacking a specific part of the network, we can break it very easily. This leads to the idea of "importance," i.e., a node is "important" for the network if removing the node breaks the network.

# Exercise
- See the notebook under `notebook` folder

# Task

Your task is to implement some functions in the Python scripts under `./scripts` folder.

You can check the correctness of your implementation by `git push` the scripts. It will trigger the auto-grading on the GitHub server. You can see the correctness in GitHub Actions.

### Example data

You can use an airport network to test your implementation. The data can be loaded by
```python
import pandas as pd
import igraph
import numpy as np

node_table = pd.read_csv(
    "https://raw.githubusercontent.com/skojaku/adv-net-sci-course/main/data/airport_network_v2/node_table.csv"
)
edge_table = pd.read_csv(
    "https://raw.githubusercontent.com/skojaku/adv-net-sci-course/main/data/airport_network_v2/edge_table.csv"
)
src, trg = tuple(edge_table[["src", "trg"]].values.T)
edge_list = tuple(zip(src, trg))

# node_id and name dictionary
n_nodes = node_table.shape[0]
id2name = np.array([""] * n_nodes, dtype="<U64")
id2name[node_table["node_id"]] = node_table["Name"].values

g = igraph.Graph(
    edge_list,
    vertex_attrs=dict(Name=id2name, node_id=node_table["node_id"].values),
)

# You can retrieve the airport names by
print(g.vs[0]["Name"], ",", g.vs[1]["Name"], ", ...")
```

## Task 1: Robustness

Open the script `scripts/network_robustness.py` and implement the following functions to draw the robustness profile curve.


```python
def random_attack(g):
    """Random attack
    g: igraph.Graph object

    Return:
    x: the proportion of nodes to be removed
    y: the proportion of nodes in the giant component
    """
    return x, y

def degree_targeted_attack(g):
    """Targeted attach by degree.

    Return:
    x: the proportion of nodes to be removed
    y: the proportion of nodes in the giant component
    """

    return x, y

def betweenness_targeted_attack(g):
    """Targeted attach by betweenness centrality.

    Return:
    x: the proportion of nodes to be removed
    y: the proportion of nodes in the giant component
    """

    return x, y
```

The robustness profile curve can be computed as follows.
1. Remove one node from the network. The node is chosen by random, or based on degree, or betweenness centrality.
2. Compute the proportion of nodes in the giant connected component.
3. Repeat steps 1 and 2 until no node is left in the network.

To test your code, you can draw and see the robustness profile by using the example data by running a notebook in `./notebooks/draw_robustness_profile.ipynb`


## Task 2: k-core decomposition

Implement the $k$-core decomposition algorithm.
The algorithm identifies the $k$-core as follows:

1. Calculate the degree of nodes in the network
2. Remove the nodes with degree less than degree $k$ in the network.
3. Recalculate the degree
4. If all nodes have a degree less than $k$ in the removed network, terminate the algorithm. Otherwise, go back to step 2.

Do not use the APIs that directly compute the $k$-core.

```python

def kcore_decomposition(g, k):
    """K-core decomposition

    Return:
    node_indiced: Indices of nodes in the k-core
    """

    return node_indices
```

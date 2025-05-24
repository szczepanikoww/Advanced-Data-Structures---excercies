import networkx as nx
import matplotlib.pyplot as plt

# WRITE YOUR CODE HERE
G = ...

pos = {
    # WRITE YOUR CODE HERE
}

nx.draw(
    G,
    positions=pos,
    with_labels=True,
    node_color="#1f78b4",
    node_size=1500,
    font_size=12,
    font_color="white",
    edge_color="gray",
    arrows=True
)
plt.show()

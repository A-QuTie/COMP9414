import sys

import networkx as nx
from PyQt5.QtWidgets import QApplication

# Import the Visualiser from your week1 subdirectory
from week1.visualiser import Visualiser


def main():
    # 1. Create the Graph as defined in the Tutorial PDF/Notebook
    G = nx.Graph()
    edges = [
        ("A", "B", 1),
        ("A", "C", 10),
        ("B", "D", 2),
        ("C", "D", 1),
        ("B", "E", 5),
        ("C", "F", 2),
        ("D", "E", 3),
        ("D", "F", 8),
        ("E", "G", 1),
        ("F", "G", 1),
        ("F", "H", 2),
        ("G", "H", 1),
    ]

    # Add weighted edges to the NetworkX graph
    for from_node, to_node, weight in edges:
        G.add_edge(from_node, to_node, weight=weight)

    print(G.neighbours("A"))

    # 2. Define the Heuristic values (Straight-line distance to goal 'H')
    heuristic = {
        "A": 10,
        "B": 8,
        "C": 5,
        "D": 7,
        "E": 3,
        "F": 6,
        "G": 1,
        "H": 0,
    }

    # 3. Initialize the PyQt5 Application
    app = QApplication(sys.argv)

    # 4. Create and show the Visualiser
    # We set 'A' as the start and 'H' as the goal node
    v = Visualiser(G, edges, heuristic, fixed_start="A", fixed_end="H")

    # Optional: Fill your Samsung G8 21:9 monitor
    v.showMaximized()

    sys.exit(app.exec_())

    # edges = [
    #     ("A", "B", 1),
    #     ("A", "C", 10),
    #     ("B", "D", 2),
    #     ("C", "D", 1),
    #     ("B", "E", 5),
    #     ("C", "F", 2),
    #     ("D", "E", 3),
    #     ("D", "F", 8),
    #     ("E", "G", 1),
    #     ("F", "G", 1),
    #     ("F", "H", 2),
    #     ("G", "H", 1),
    # ]

    # G = nx.Graph()
    # for n1, n2, dis in edges:
    #     G.add_edge(n1, n2, weight=dis)

    # for node, weight in G["A"].items():
    #     print(node, weight["weight"])
    # print(G["A"])


if __name__ == "__main__":
    main()

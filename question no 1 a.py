#Refernece Link: https://www.youtube.com/watch?v=EJKdmEbGre8

import numpy as np

from ant_colony import AntColony

distances = np.array([[1, 2, 2, 5, 7],
                      [2, 1, 4, 8, 2],
                      [2, 4, 1, 1, 3],
                      [5, 8, 1, 1, 2],
                      [7, 2, 3, 2, 1],
                      [2, 1, 4, 8, 2]])

ant_colony = AntColony(distances, 1, 1, 5, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print ("\nshorted_path: {}".format(shortest_path))


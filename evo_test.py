from evolve import Evolution
from creature import Creature
import matplotlib.pyplot as plt
from tqdm import tqdm

progress = []


def fitness_rankings(in_list):
    return sorted(in_list, key=lambda f: sum(f.traits))


a = Evolution(population_size=100)
population = [Creature() for i in range(0, 100)]

for i in tqdm(range(0, 100)):
    population = fitness_rankings(population)
    progress.append(sum(population[0].traits))
    children_traits = a.evolve(population)

    population = [Creature(children_traits[index]) for index, x in enumerate(population, 0)]

plt.plot(progress)
plt.show()

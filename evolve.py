
import random
from creature import Creature


class Evolution:
    def __init__(self, population_size=100, survival_percent=0.50, luck_percent=0.05, mutation_percent=0.05):
        self.population_size = population_size
        self.survival_num = int(population_size * survival_percent)
        self.luck_num = int(population_size * luck_percent)
        self.mutation_num = int(population_size * mutation_percent)

    def selection(self, ranked_population):
        cutoff = self.survival_num - self.luck_num
        survivors = ranked_population[:cutoff]
        survivors += random.sample(ranked_population[cutoff:], self.luck_num)
        return survivors

    def breeding(self, population):
        children = []

        population_sequences = int(self.population_size/(len(population)/2))
        population = population * population_sequences

        random.shuffle(population)
        parents = [population[i:i+2]
                   for i in range(0, len(population), 2)][:self.population_size]

        for couple in parents:
            splitter = random.randint(0, len(couple[0].traits))
            child = couple[0].traits[splitter:] + couple[1].traits[:splitter]
            children.append(child)

        return children

    def mutation(self, population):
        indexes = [random.randint(0, self.population_size-1) for i in range(0, self.mutation_num)]
        for i in indexes:
            index_choice = random.randint(0, len(population[i])-1)
            population[i][index_choice] = random.random()

        return population

    def evolve(self, population):
        return self.mutation(self.breeding(self.selection(population)))


if __name__ == "__main__":
    a = Evolution(population_size=10)
    b = a.evolve([Creature(), ]*100)
    print(b)

from Graph import Graph
import random


def generate_initial_population(graph):
    population = []
    for i in range(50000):
        candidate = set(random.sample(graph.get_vertices(), 18))
        population.append(candidate)
    return population


def fitness_function(candidate, graph):
    for v1 in candidate:
        for v2 in candidate:
            if v1 != v2 and graph.is_edge(v1, v2):
                return 0
    return len(candidate)


def tournament_selection(graph, population, fitness_fn, num_parents, tournament_size=2):
    parents = []
    for i in range(num_parents):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=lambda x: fitness_fn(x, graph))
        parents.append(winner)

    return parents


def crossover(parent1, parent2):
    subset = set(random.sample(parent1,
                 random.randint(1, len(parent1)-1)))
    offspring1 = subset.union(
        set(v for v in parent2 if v not in subset))
    return offspring1


def mutation(candidate, graph):
    if random.random() < 0.5:
        candidate.add(random.choice(list(graph.get_vertices())))
    else:
        candidate.remove(random.choice(list(candidate)))

    return candidate


def main():
    with open("members.txt", "r") as f:
        g = Graph()
        for memeber in f.readlines():
            g.add_vertex(memeber.strip())

    with open("friends05.txt", "r") as f:
        for edge in f.readlines():
            p1, p2 = edge.strip().split(" ")
            g.add_edge(p1, p2)

    population = generate_initial_population(g)

    generations = 10
    for i in range(generations):
        parents = tournament_selection(g,
                                       population, fitness_function, len(population)//2)

        offspring = []
        for i in range(len(parents)//2):
            offspring1 = crossover(parents[2*i], parents[(2*i)+1])
            offspring2 = crossover(parents[(2*i)+1], parents[2*i])
            offspring.append(mutation(offspring1, g))
            offspring.append(mutation(offspring2, g))

        population = parents + offspring

    max_fitness = 0
    max_candidate = None
    for candidate in population:
        candidate_fitness = fitness_function(candidate, g)
        if candidate_fitness > max_fitness:
            max_fitness = candidate_fitness
            max_candidate = candidate

    print("Clique: {}".format(max_candidate))
    print("Size: {}".format(max_fitness))


main()

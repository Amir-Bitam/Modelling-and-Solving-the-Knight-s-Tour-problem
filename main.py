import time

from config import POPULATION_SIZE, MAX_FITNESS
from population import Population
from gui import show_solution


def main():
    population_size = POPULATION_SIZE

    # Création de la population initiale
    population = Population(population_size)

    start = time.time()
    while True:
        # Vérifier (et corriger) la validité des déplacements de chaque cavalier
        population.check_population()

        # Evaluer la génération et récupérer le meilleur cavalier
        maxFit, bestSolution = population.evaluate()

        # TODO : afficher la progression dans le terminal
        #        (ex : tous les 10 générations -> génération, meilleure fitness)
        if maxFit == MAX_FITNESS:
            break

        # Générer la nouvelle population
        population.create_new_generation()

    elapsed = time.time() - start

    # TODO : afficher le résumé (générations, temps) et la liste des 64 positions
    print("Solution trouvée à la génération", population.generation, "en", round(elapsed, 2), "s")

    # Interface : afficher la solution
    show_solution(bestSolution.path, generation=population.generation,
                  fitness=maxFit, elapsed=elapsed)


if __name__ == "__main__":
    main()

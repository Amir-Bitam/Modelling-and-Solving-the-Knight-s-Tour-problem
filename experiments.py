

import time

from config import MAX_FITNESS
from population import Population


def run_once(population_size, mutation_rate, tournament_size=3, max_generations=5000):

    pop = Population(population_size,mutation_rate,tournament_size)
    
   

    start_time = time.perf_counter()

    while True:
        pop.check_population()
        max_fit, best = pop.evaluate()
        if max_fit == MAX_FITNESS or pop.generation > max_generations:
            break
        pop.create_new_generation()

    end_time = time.perf_counter()

    seconds = end_time - start_time
    
    found = max_fit == MAX_FITNESS

    return (pop.generation,seconds,max_fit,found)


def average_over_runs(population_size, mutation_rate,tournament_size=3, nb_runs=20):
    average_generation = 0
    average_time = 0
    successful_runs= 0
    for i in range(nb_runs): 
        generation,seconds,_,found = run_once(population_size,mutation_rate,tournament_size)

        if found:
            successful_runs = successful_runs + 1
            average_generation = average_generation + generation
            average_time = average_time + seconds  #on compte seulement les moyenne pour les run reussi
    if successful_runs == 0:
        return (None,None,0)
    else:
        return (average_generation/successful_runs,average_time/successful_runs,successful_runs)    
     
def print_row(label, result):
    mean_gen, mean_time, successes = result
    if mean_gen is None:
        print(label, "-> successes:", successes, "/ 20, no tour found")
    else:
        print(label, "-> successes:", successes, "/ 20, generations:", round(mean_gen), ", seconds:", round(mean_time, 2))


def main():
    print("Population size (mutation 0.02, tournament 3)")
    for size in [10, 25, 50, 100, 200]:
        print_row(size, average_over_runs(size, 0.02, 3))

    print()
    print("Mutation rate (population 50, tournament 3)")
    for rate in [0.005, 0.01, 0.02, 0.05, 0.1]:
        print_row(rate, average_over_runs(50, rate, 3))


if __name__ == "__main__":
    main()



import random

from config import MUTATION_RATE, TOURNAMENT_SIZE
from knight import Knight


class Population:

    def __init__(self, population_size, mutation_rate=MUTATION_RATE, tournament_size=TOURNAMENT_SIZE):

        self.population_size = population_size
        self.generation = 1
        self.knights=[]
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size

        for _ in range(population_size):
            self.knights.append(Knight())

           
    def check_population(self):
        for k in self.knights:
            k.check_moves()


    def evaluate(self):
        best_score = 0 
        best_knight = None
        for k in self.knights:
            current = k.evaluate_fitness()

            if  best_score < current :

                best_score = current
                best_knight = k

        return (best_score,best_knight)

    def tournament_selection(self, size = None):

        if size is None:
            size = self.tournament_size
        

        tournament = random.sample(self.knights,size)
        tournament.sort(key=lambda k: k.fitness,reverse=True)

        
        first_parent = tournament[0]
        second_parent = tournament[1]

        return(first_parent,second_parent)


    def create_new_generation(self):

        new_knights = []

        while len(new_knights) < self.population_size:

            parent1,parent2 = self.tournament_selection()
            child1,child2 = parent1.chromosome.crossover(parent2.chromosome)

            child1.mutation(self.mutation_rate)
            child2.mutation(self.mutation_rate)

            knight1 = Knight(child1)
            knight2 = Knight(child2)

            new_knights.append(knight1)
            new_knights.append(knight2)

     
        self.knights = new_knights[:self.population_size]
        self.generation+=1





            


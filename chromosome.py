"""
chromosome.py : le chromosome d'un cavalier = la liste de ses 63 déplacements.
Responsable : MEMBRE 1
"""

import random
import copy
from config import NB_GENES, MUTATION_RATE


class Chromosome:

    def __init__(self, genes=None):
        if genes is not None :
            self.genes = copy.copy(genes)
        else:
            self.genes = [ random.randint(1,8) for _ in range(NB_GENES)]
                
        

    def crossover(self, partner):

        cut = random.randint(1 , NB_GENES -1)

        enfant1 = self.genes[:cut]    + partner.genes[cut:]
        enfant2 = partner.genes[:cut] + self.genes[cut:]

        return (Chromosome(enfant1),Chromosome(enfant2))
       


    def mutation(self, rate=MUTATION_RATE):

        for i in range(NB_GENES):
            if random.random() < rate:
                self.genes[i] = random.randint(1,8)


"""
chromosome.py : le chromosome d'un cavalier = la liste de ses 63 déplacements.
Responsable : MEMBRE 1
"""

import random

from config import NB_GENES, MUTATION_RATE


class Chromosome:

    def __init__(self, genes=None):
        """
        genes : liste de 63 entiers entre 1 et 8 (voir MOVES dans config.py).

        - Si genes est None (population initiale) : générer 63 gènes aléatoires
          avec random.randint(1, 8).
        - Sinon : garder une COPIE de la liste (genes[:]), pour que deux
          chromosomes ne partagent jamais la même liste en mémoire.

        Attribut obligatoire (CONTRAT) : self.genes
        """
        raise NotImplementedError

    def crossover(self, partner):
        """
        Croisement à un point entre self et partner (un autre Chromosome).

        TODO :
            1. tirer un point de coupure : cut = random.randint(1, NB_GENES - 1)
            2. enfant 1 = self.genes[:cut]    + partner.genes[cut:]
               enfant 2 = partner.genes[:cut] + self.genes[cut:]
            3. retourner les DEUX enfants sous forme de Chromosome :
                   return (Chromosome(genes1), Chromosome(genes2))

        CONTRAT : retourne un tuple (enfant1, enfant2). Ne modifie ni self ni partner.
        """
        raise NotImplementedError

    def mutation(self, rate=MUTATION_RATE):
        """
        Mutation : chaque gène a la probabilité 'rate' d'être remplacé par une
        direction aléatoire (random.randint(1, 8)).

        TODO : boucle sur les 63 gènes ; si random.random() < rate, nouveau gène.

        CONTRAT : modifie self.genes EN PLACE et ne retourne rien.
        (Le paramètre rate permet de faire varier le taux dans les expériences.)
        """
        raise NotImplementedError

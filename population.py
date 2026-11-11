"""
population.py : la population de cavaliers et les opérateurs de sélection.
Responsable : MEMBRE 1
(Dépend de Knight du membre 2 : seulement via le contrat décrit dans le README.)
"""

import random

from config import MUTATION_RATE, TOURNAMENT_SIZE
from chromosome import Chromosome
from knight import Knight


class Population:

    def __init__(self, population_size, mutation_rate=MUTATION_RATE, tournament_size=TOURNAMENT_SIZE):
        """
        Attributs obligatoires (CONTRAT) :
            self.population_size
            self.generation = 1
            self.knights    = liste de population_size Knight() aléatoires
        Garder aussi self.mutation_rate et self.tournament_size
        (valeurs par défaut de config.py, modifiables pour les expériences).
        """
        raise NotImplementedError

    def check_population(self):
        """
        Pour chaque cavalier de la population : appeler knight.check_moves().
        """
        raise NotImplementedError

    def evaluate(self):
        """
        Pour chaque cavalier : appeler knight.evaluate_fitness().
        Retourner le tuple (maxFit, bestKnight) : la meilleure fitness de la
        génération et le cavalier correspondant.
        CONTRAT : retourne (int, Knight).
        """
        raise NotImplementedError

    def tournament_selection(self, size):
        """
        Sélection par tournoi.

        TODO :
            1. tirer 'size' cavaliers DIFFERENTS au hasard : random.sample(self.knights, size)
            2. les trier par fitness décroissante
            3. retourner les deux meilleurs : (parent1, parent2)

        CONTRAT : retourne deux objets Knight (pas des chromosomes).
        Les fitness doivent déjà être calculées (evaluate() appelée avant).
        """
        raise NotImplementedError

    def create_new_generation(self):
        """
        Remplace self.knights par la génération suivante (même taille).

        TODO :
            nouveaux = []
            tant que len(nouveaux) < self.population_size :
                parent1, parent2 = self.tournament_selection(self.tournament_size)
                enfant1, enfant2 = parent1.chromosome.crossover(parent2.chromosome)
                enfant1.mutation(self.mutation_rate)
                enfant2.mutation(self.mutation_rate)
                ajouter Knight(enfant1) et Knight(enfant2) à 'nouveaux'
            si la taille dépasse population_size (taille impaire) : couper la fin
            self.knights = nouveaux
            self.generation += 1

        Attention : créer de NOUVEAUX Knight pour les enfants (ne pas réutiliser
        les anciens objets, sinon leur path / fitness resteraient ceux du parent).
        """
        raise NotImplementedError

"""
knight.py : le cavalier. Il applique les gènes de son chromosome pour
construire un chemin (path) sur l'échiquier et en calcule la fitness.
Responsable : MEMBRE 2
"""

import random

from config import BOARD_SIZE, MAX_FITNESS, MOVES, START
from chromosome import Chromosome


class Knight:

    def __init__(self, chromosome=None):
        """
        chromosome : un objet Chromosome. S'il est None (population initiale),
        créer un nouveau Chromosome() aléatoire.

        Attributs obligatoires (CONTRAT) :
            self.position   = START, c'est-à-dire (0, 0)
            self.chromosome = le chromosome
            self.path       = [START]   (liste des positions visitées, départ inclus)
            self.fitness    = 0
        """
        raise NotImplementedError

    def move_forward(self, direction):
        """
        Applique la direction (1 à 8) : MOVES[direction] = (dx, dy).

        TODO :
            - self.position = (x + dx, y + dy)
            - ajouter la nouvelle position à self.path
        Cette méthode NE vérifie PAS si le mouvement est valide (c'est le rôle
        de check_moves). La nouvelle position peut donc être hors de l'échiquier.
        """
        raise NotImplementedError

    def move_backward(self, direction):
        """
        Annule move_forward(direction) :
            - retirer la dernière position de self.path (pop)
            - remettre self.position = position précédente (celle qui est
              maintenant en dernière place de self.path)
        """
        raise NotImplementedError

    def is_last_move_valid(self):
        """
        (Méthode d'aide, utilisée par check_moves.)
        Vérifie la DERNIERE position de self.path :
            - elle est dans l'échiquier : 0 <= x < BOARD_SIZE et 0 <= y < BOARD_SIZE
            - elle n'a pas déjà été visitée : absente de self.path[:-1]
        Retourne True / False.
        """
        raise NotImplementedError

    def check_moves(self, cycle=None):
        """
        Vérifie et CORRIGE les 63 gènes du chromosome, un par un.

        cycle : +1 (cycle vers l'avant : d, d+1, d+2 ...) ou -1 (cycle vers
        l'arrière : d, d-1, d-2 ...). Si None : choisir au hasard UNE seule fois
        au début (random.choice([1, -1])), puis garder le même sens pour tous
        les gènes de ce chromosome. (Le paramètre existe pour pouvoir tester.)

        TODO :
            0. repartir de zéro : self.position = START ; self.path = [START]
            1. pour chaque indice i de 0 à 62 :
                 d = self.chromosome.genes[i]
                 essayer d, puis les directions suivantes du cycle (8 essais max) :
                     move_forward(essai)
                     si is_last_move_valid() -> garder, écrire essai dans
                         self.chromosome.genes[i] (la correction est mémorisée
                         dans le chromosome), passer au gène suivant
                     sinon -> move_backward(essai), essayer la direction suivante
                         essai = (essai - 1 + cycle) % 8 + 1
                 si AUCUNE des 8 directions n'est valide (cul-de-sac) :
                     garder le mouvement d'origine : move_forward(d), laisser
                     le gène inchangé, puis ARRETER la boucle (break). La position
                     invalide reste dans self.path ; c'est evaluate_fitness qui
                     s'en servira pour arrêter le comptage.

        Exemple (cycle vers l'avant) : le gène 4 est illégal -> on essaie
        5, 6, 7, 8, 1, 2, 3. Vers l'arrière : 3, 2, 1, 8, 7, 6, 5.

        CONTRAT : modifie self.chromosome.genes EN PLACE, remet à jour
        self.position et self.path. Peut être rappelée plusieurs fois.
        """
        raise NotImplementedError

    def evaluate_fitness(self):
        """
        Parcourt self.path et compte les positions valides jusqu'à la première
        position invalide (hors échiquier OU déjà vue plus tôt dans le chemin).

        TODO :
            fitness = 0 ; vues = ensemble vide
            pour chaque pos de self.path :
                si pos hors échiquier ou pos dans vues -> arrêter
                sinon ajouter pos à vues, fitness += 1
            self.fitness = fitness

        La case de départ compte : un tour complet donne MAX_FITNESS = 64.
        CONTRAT : met à jour self.fitness ET le retourne.
        """
        raise NotImplementedError

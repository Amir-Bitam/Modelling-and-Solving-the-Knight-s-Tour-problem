"""
experiments.py : mesures pour le rapport (sans interface graphique).
Responsable : MEMBRE 1

Objectif : voir comment la taille de la population et le taux de mutation
influencent le nombre de générations nécessaires pour trouver un tour complet.

Usage :  python experiments.py
"""

import time

from config import MAX_FITNESS
from population import Population


def run_once(population_size, mutation_rate, tournament_size=3, max_generations=5000):
    """
    Lance UN run de l'algorithme génétique (même boucle que main.py, sans GUI).

    Retourne (generations, temps_en_secondes, trouve)
        trouve = True si fitness 64 atteinte avant max_generations, sinon False
        (le max_generations évite une boucle infinie).
    """
    raise NotImplementedError


def average_over_runs(population_size, mutation_rate, nb_runs=20):
    """
    Lance nb_runs runs et retourne (moyenne des générations, moyenne du temps,
    nombre de runs réussis). Ne compter dans les moyennes que les runs réussis.
    """
    raise NotImplementedError


def main():
    """
    TODO : tester plusieurs valeurs, par exemple
        population_size dans [20, 50, 100, 200]       (mutation_rate = 0.02)
        mutation_rate   dans [0.005, 0.01, 0.02, 0.05, 0.1]   (population_size = 50)
    et afficher un tableau :
        taille | taux | générations moyennes | temps moyen | réussites / 20
    Copier ce tableau dans le rapport et commenter (quelle combinaison est la meilleure ?).
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()

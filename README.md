# Projet 2 : Problème du cavalier avec algorithme génétique

## Lancer
```
python -m pip install -r requirements.txt
python main.py
```

## Répartition

| Membre | Fichiers | Contenu |
|---|---|---|
| 1 | `chromosome.py`, `population.py`, `experiments.py` | Chromosome (init, crossover, mutation), Population (init, check_population, evaluate, tournament_selection, create_new_generation), expériences pour le rapport |
| 2 | `knight.py` | Knight (init, move_forward, move_backward, check_moves, evaluate_fitness) |
| 3 | `gui.py`, `main.py` (+ `ART/knight.png`) | Interface Pygame (Figure 2 du PDF) et fonction main |

`config.py` est partagé : constantes communes, personne ne le modifie sans prévenir (seuls les paramètres de la section 3 servent aux expériences).

## Contrat entre les classes

- Gène : entier de **1 à 8** (clé de `MOVES`). Chromosome : liste `genes` de 63 gènes.
- Position : `(x, y)`, x = colonne, y = ligne (0 en haut). Départ `(0, 0)`.
- `Chromosome(genes=None)` ; `crossover(partner)` -> **tuple de 2 Chromosome** ; `mutation(rate)` modifie en place.
- `Knight(chromosome=None)` : attributs `position`, `chromosome`, `path` (départ inclus), `fitness`.
- `Knight.check_moves(cycle=None)` corrige `chromosome.genes` **en place**, reconstruit `path` depuis zéro.
- `Knight.evaluate_fitness()` met à jour et retourne `fitness` (64 = tour complet, la case de départ compte).
- `Population(size)` : `knights`, `generation` (commence à 1). `evaluate()` -> `(maxFit, bestKnight)`. `tournament_selection(size)` -> **2 Knight**.
- `show_solution(path, generation, fitness, elapsed)` dans `gui.py`.

## Valeurs de contrôle

- Direction 8 en (0, 0) : corrigée en **3** (cycle avant) ou en **4** (cycle arrière).
- Avec population 50, 3 chromosomes de tournoi et mutation 0.02 par gène, un run complet doit trouver un tour en quelques dizaines à quelques centaines de générations, en moins de 2 secondes (prototype de référence : 19 à 76 générations sur 3 essais).
  Si votre run dépasse plusieurs milliers de générations, cherchez un bug (gènes non réécrits après correction, `path` non remis à zéro, listes partagées entre chromosomes).

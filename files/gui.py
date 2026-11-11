"""
gui.py : interface Pygame qui affiche la solution (comme la Figure 2 de l'énoncé).
Responsable : MEMBRE 3

Ce que l'on doit voir (Figure 2 du PDF) :
    - un échiquier 8 x 8 avec cases claires / foncées alternées (vert et crème)
    - les numéros de colonnes (1 à 8) en haut et en bas, les numéros de lignes
      (1 à 8) à gauche et à droite
    - le cavalier qui se déplace case par case le long de la solution
    - chaque case déjà visitée est colorée (plus claire) et affiche son numéro
      d'ordre de passage (1, 2, 3 ... 64)
    - à côté (ou en bas) : numéro de génération, fitness, temps de calcul

Pour tester sans attendre l'algorithme génétique : utiliser un tour complet
connu (voir KNOWN_TOUR_GENES dans test_knight.py) ou construire un path à la main.
"""

import os
import time

import pygame

from config import BOARD_SIZE

WIDTH = 800
HEIGHT = 800
ART_DIR = os.path.join(os.path.dirname(__file__), "ART")   # mettre knight.png ici

# Couleurs suggérées (à ajuster selon la Figure 2)
LIGHT_SQUARE = (238, 238, 210)
DARK_SQUARE = (118, 150, 86)
VISITED_LIGHT = (214, 224, 127)
VISITED_DARK = (160, 190, 70)
TEXT = (60, 70, 50)


def load_knight_image(tile):
    """
    Charge ART/knight.png redimensionnée à (tile, tile).
    Si l'image n'existe pas : retourner None, et draw_board dessinera à la place
    un cercle noir avec la lettre "N" (solution de secours).
    """
    raise NotImplementedError


def draw_board(screen, path, step, tile, ox, oy, font, knight_img):
    """
    Dessine l'échiquier tel qu'il est après 'step' déplacements.

    path : liste des positions (x, y) du cavalier (path[0] = (0, 0)).
    step : indice dans path ; le cavalier est en path[step].
    tile : taille d'une case en pixels ; (ox, oy) : coin haut-gauche de l'échiquier.
    font : police pour les numéros.

    TODO :
        1. pour chaque case (x, y) : couleur claire/foncée selon (x + y) % 2
        2. pour chaque indice k de 0 à step : colorer path[k] en "visitée" et
           écrire le numéro k + 1 au centre de la case
        3. dessiner le cavalier en path[step]
        4. écrire les numéros de colonnes (haut et bas) et de lignes (gauche et droite)
    Attention : y = ligne (0 en haut), x = colonne (voir config.py).
    """
    raise NotImplementedError


def show_solution(path, generation=0, fitness=0, elapsed=0.0, delay_ms=300):
    """
    Ouvre la fenêtre et anime la solution (bloquant jusqu'à fermeture de la fenêtre).

    path : best_knight.path (64 positions pour un tour complet).

    TODO :
        - pygame.init(), créer la fenêtre (WIDTH x HEIGHT), titre "Knight's Tour"
        - boucle : gérer pygame.QUIT (et la touche Echap) ; toutes les delay_ms
          millisecondes, passer à l'étape suivante jusqu'à la dernière position
        - afficher generation / fitness / temps (texte)
        - à la fin : le dernier état reste affiché
        - bonus : touche ou bouton "Rejouer" qui recommence l'animation
        - pygame.quit() à la fermeture
    """
    raise NotImplementedError

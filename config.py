"""
config.py : constantes partagées par TOUS les fichiers (le "contrat").
A valider ensemble à la réunion de départ, puis personne ne modifie
sans prévenir les autres. (Seuls les paramètres de la section 3 peuvent
être ajustés pour les expériences.)
"""

# ----------------------------------------------------------------------
# 1) L'échiquier
# ----------------------------------------------------------------------
BOARD_SIZE = 8          # échiquier 8 x 8
NB_GENES = 63           # 64 cases - la case de départ = 63 déplacements
MAX_FITNESS = 64        # fitness d'un tour complet (nombre de cases)
START = (0, 0)          # position de départ du cavalier (coin haut-gauche)

# Convention de coordonnées : position = (x, y)
#   x = colonne (0 à 7, de gauche à droite)
#   y = ligne   (0 à 7, de HAUT en BAS)  -> "down" veut dire y + 1
# Dans l'interface, on affiche x + 1 et y + 1 (les cases sont numérotées de 1 à 8).

# ----------------------------------------------------------------------
# 2) Les 8 directions (numérotées comme dans l'énoncé)
#    direction -> (dx, dy)
# ----------------------------------------------------------------------
MOVES = {
    1: (1, -2),    # up-right    : 2 en haut, 1 à droite
    2: (2, -1),    # right-up    : 2 à droite, 1 en haut
    3: (2, 1),     # right-down  : 2 à droite, 1 en bas
    4: (1, 2),     # down-right  : 2 en bas, 1 à droite
    5: (-1, 2),    # down-left   : 2 en bas, 1 à gauche
    6: (-2, 1),    # left-down   : 2 à gauche, 1 en bas
    7: (-2, -1),   # left-up     : 2 à gauche, 1 en haut
    8: (-1, -2),   # up-left     : 2 en haut, 1 à gauche
}
# Un gène = un entier de 1 à 8 (la clé de MOVES). Jamais 0 !
# Pour "avancer d'un cran" dans le cycle des directions (8 -> 1, 1 -> 8) :
#   nouvelle_dir = (dir - 1 + sens) % 8 + 1      avec sens = +1 (avant) ou -1 (arrière)

# ----------------------------------------------------------------------
# 3) Paramètres de l'algorithme génétique (modifiables pour les expériences)
# ----------------------------------------------------------------------
POPULATION_SIZE = 50    # taille de la population (énoncé : 50)
TOURNAMENT_SIZE = 3     # taille de l'échantillon du tournoi (énoncé : 3)
MUTATION_RATE = 0.02    # probabilité de mutation PAR GENE

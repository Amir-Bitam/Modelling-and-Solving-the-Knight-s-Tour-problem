"""
test_knight.py : tests de Knight / Chromosome (utile aussi aux membres 1 et 3).
Responsable : MEMBRE 2

Usage :  python test_knight.py
Ecrire les tests dans le style "if ... : print('OK') else : print('ERREUR ...')".
"""

from chromosome import Chromosome
from knight import Knight

# Un tour complet valide depuis (0, 0) : 63 gènes (vérifié : fitness 64, aucune
# correction nécessaire).
KNOWN_TOUR_GENES = [
    3, 2, 3, 4, 5, 4, 7, 2, 5, 7, 6, 7, 1, 8, 1, 3, 2, 3, 5, 7, 8, 6, 5, 2,
    7, 2, 5, 5, 2, 5, 5, 2, 1, 7, 5, 4, 1, 4, 7, 2, 4, 2, 8, 7, 1, 2, 5, 5,
    5, 3, 2, 7, 2, 8, 1, 6, 3, 5, 7, 6, 1, 3, 5,
]


def test_known_tour():
    """
    Knight(Chromosome(KNOWN_TOUR_GENES)) ; check_moves() ; evaluate_fitness()
    -> fitness == 64, len(path) == 64, et les gènes n'ont pas changé.
    """
    raise NotImplementedError


def test_forward_correction():
    """
    Chromosome dont TOUS les gènes valent 8 (up-left). Depuis (0, 0) le 1er
    mouvement sort de l'échiquier.
    check_moves(cycle=+1) : le 1er gène doit être corrigé en 3
        (essais : 1 -> (1,-2) invalide, 2 -> (2,-1) invalide, 3 -> (2,1) valide).
    check_moves(cycle=-1) : le 1er gène doit être corrigé en 4
        (essais : 7, 6, 5 invalides, 4 -> (1,2) valide).
    """
    raise NotImplementedError


def test_move_forward_backward():
    """
    Depuis (0, 0) : move_forward(3) -> position (2, 1) et path de longueur 2 ;
    move_backward(3) -> position (0, 0) et path de longueur 1.
    """
    raise NotImplementedError


def test_revisit_detection():
    """
    Un chemin qui repasse sur une case déjà visitée (par exemple gènes 3 puis 7
    qui ramènent en (0, 0)) : sans correction, evaluate_fitness s'arrête avant
    la case répétée. Avec check_moves, le gène est corrigé et la case n'est
    plus répétée.
    """
    raise NotImplementedError


def test_dead_end():
    """
    Cul-de-sac : le mouvement d'origine est gardé (invalide) et le calcul
    s'arrête. fitness < 64 et la dernière position de path est invalide.
    (Fabriquer le cas en construisant à la main un path presque complet.)
    """
    raise NotImplementedError


def test_check_moves_twice():
    """
    Appeler check_moves() deux fois de suite sur le même cavalier ne doit pas
    allonger path : len(path) <= 64 et path[0] == (0, 0).
    """
    raise NotImplementedError


if __name__ == "__main__":
    test_known_tour()
    test_forward_correction()
    test_move_forward_backward()
    test_revisit_detection()
    test_dead_end()
    test_check_moves_twice()

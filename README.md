# Knight's Tour Solver

This project models and solves the Knight's Tour problem with a genetic
algorithm.

The goal is to find a sequence of 63 legal knight moves that visits every
square of an 8×8 chessboard exactly once. The search starts from the
top-left corner, `(0, 0)`. Once a complete tour is found, the solution is
displayed as an animated Pygame board.

## Features

- Generates an initial population of candidate tours.
- Evaluates candidates using the number of unique squares visited.
- Uses tournament selection, one-point crossover, and per-gene mutation.
- Repairs invalid moves by trying the neighboring directions in a cyclic order.
- Animates the best solution on an 8×8 board.
- Provides experiments for comparing population sizes and mutation rates.

## Requirements

- Python 3
- `pygame-ce`

Install the dependency with:

```bash
python -m pip install -r requirements.txt
```

## Running the solver

From this directory, run:

```bash
python main.py
```

The program searches until it finds a complete tour, then opens the
visualization window. In the visualization:

- Press `R` to replay the tour.
- Press `Esc` or close the window to exit.

## Running experiments

To run the predefined experiments for population size and mutation rate:

```bash
python experiments.py
```

The experiment script performs multiple runs and reports the average number
of generations, average runtime, and number of successful runs.

## Algorithm overview

Each candidate solution is represented by a chromosome containing 63 genes.
Each gene is an integer from `1` to `8`, representing one of the eight
possible knight-move directions.

For every generation, the solver:

1. Builds a valid path from each chromosome.
2. Calculates its fitness, where `64` means that all board squares were
   visited.
3. Selects parents using tournament selection.
4. Creates children with one-point crossover.
5. Mutates each child according to the configured mutation rate.
6. Repeats until a complete tour is found.

The default parameters are defined in [`config.py`](config.py):

| Parameter | Default |
|---|---:|
| Board size | 8 × 8 |
| Population size | 50 |
| Tournament size | 3 |
| Mutation rate | 0.02 per gene |
| Maximum fitness | 64 |

## Project structure

| File | Description |
|---|---|
| [`main.py`](main.py) | Runs the solver and displays the solution. |
| [`config.py`](config.py) | Stores board dimensions and algorithm parameters. |
| [`chromosome.py`](chromosome.py) | Defines genes, crossover, and mutation. |
| [`knight.py`](knight.py) | Builds paths and calculates candidate fitness. |
| [`population.py`](population.py) | Manages evaluation and new generations. |
| [`experiments.py`](experiments.py) | Runs parameter-comparison experiments. |
| [`gui.py`](gui.py) | Provides the Pygame visualization. |
| [`ART/`](ART/) | Contains the board and knight image assets. |

# Machine Problem 1

## How to use

To run the solver, run this command in your terminal:

```bash
./main.py Mazes/*.lay.txt
```

To solve only a specific maze run:

```bash
./main.py location_of_file
```

For Windows user, be sure to add `python` at the start of the command and remove `./`.

Example:

```bash
python main.py location_of_file
```

To specify heuristic method, add `-m` or `-s` before specifying the location of your maze.

Manhattan Heuristic: `-m`
Straight Heuristic: `-s`

Default heuristic method is Manhattan.

Example:

```bash
# To use Straight heuristic method.
./main.py -s location_of_file

# To use Manhattan heuristic method.
./main.py -m location_of_file

# or simply
./main.py location_of_file
```

## Python Version:

 - Python 3.6.1

# Description: Command line arguments for the program
from argparse import ArgumentParser, Namespace

# Zorgt voor een argument parser die de argumenten van de command line kan parsen en de beschrijving van de argumenten kan weergeveb
parser = ArgumentParser(description="Command line arguments for the program")
parser.add_argument("square", help="Squares a given number", type=int, default=0)
parser.add_argument("-v", "--verbose", help="Increase output verbosity", type=int, choices=[0, 1, 2])

# definiëren van de argumenten doormiddel van de parse_args() functie
args: Namespace = parser.parse_args()

if args.verbose == 0:
    print("option 1")
elif args.verbose == 1:
    # py __name__.py 10 -v 1
    print("option 2")
elif args.verbose == 2:
    print("option 3")

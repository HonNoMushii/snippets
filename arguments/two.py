from argparse import ArgumentParser,Namespace

parser = ArgumentParser()

parser.usage = "This program calculates the power of a number"

parser.add_argument("a", type=int, help="The base value")
parser.add_argument("b", type=int, help="The exponent value")
parser.add_argument("-v", "--verbose",
                    help="Provides verbose description. use -vv for extra verbose",
                    action="count", default=0)

args: Namespace = parser.parse_args()
result: int = args.a ** args.b

# Handeling extra verbose -v, -vv
match args.verbose:
    case 1:
        print(f"The result is: {result}")
    case 2:
        print(f"{args.a} ** {args.b} = {result}")
    case _:
        print(result)

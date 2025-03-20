from argparse import ArgumentParser,Namespace

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group() # makes a group of mutually exclusive arguments

# parser.usage = "This program calculates the power of a number"

parser.add_argument("a", type=int, help="The base value")
parser.add_argument("b", type=int, help="The exponent value")

# So instead of parser we use group
group.add_argument("-v", "--verbose",
                    help="Provides verbose description. use -vv for extra verbose",
                    action="count", default=0)
group.add_argument("-s", "--silent", action="store_true", help="Generate a silent version of the output")

args: Namespace = parser.parse_args()
result: int = args.a ** args.b

# Handeling extra verbose -v, -vv
if args.silent:
    print("Silent mode!")
else:
    match args.verbose:
        case 1:
            print(f"The result is: {result}")
        case 2:
            print(f"{args.a} ** {args.b} = {result}")
        case _:
            print(result)
            

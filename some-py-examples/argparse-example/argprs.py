import argparse
# https://docs.python.org/3/library/argparse.html

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('integers',
                        nargs='+',
                        type=int,
                        help='an integer for the accumulator',
                        metavar='N',)

    parser.add_argument('--sum',
                        action='store_const',
                        const=sum,
                        default=max,
                        help='sum the integers (default: find the max)',
                        dest='accumulate',
                        )

    '''
    name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
    action - The basic type of action to be taken when this argument is encountered at the command line.
    nargs - The number of command-line arguments that should be consumed.
    const - A constant value required by some action and nargs selections.
    default - The value produced if the argument is absent from the command line.
    type - The type to which the command-line argument should be converted.
    choices - A container of the allowable values for the argument.
    required - Whether or not the command-line option may be omitted (optionals only).
    help - A brief description of what the argument does.
    metavar - A name for the argument in usage messages.
    dest - The name of the attribute to be added to the object returned by parse_args().
    '''

    # args = parser.parse_args(["13 43 645".split()])  # debug
    args = parser.parse_args()
    print(args.accumulate(args.integers))

# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: docopt.py <arg1> [<newarg>] --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg>             Takes any value (this is a required positional argument)
[<newarg>]        Takes any value (optional positional arg)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
"""

from docopt import docopt
opt = docopt(__doc__)

def main(opt):
    print(opt)
    print(type(opt))
    print(opt.get('<newarg>', None))

if __name__ == '__main__':
    main(opt)
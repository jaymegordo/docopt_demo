# author: Tiffany Timbers
# date: 2020-01-15

"This script prints out docopt args.
Usage: demo.R <arg1> [<newarg>] --arg2=<arg2> [--arg3=<arg3>]
Options:
<arg>             Takes any value (this is a required positional argument)
[<newarg>]          Takes any value (optional positional arg)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)

" -> doc

library(docopt)
opt <- docopt(doc)

main <- function(opt) {
    print(opt)
    print(typeof(opt))
    print(opt$newarg)
}

main(opt)
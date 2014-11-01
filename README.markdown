# `rere`: regex redone

## Usage

    from rere import *

    regex = Exactly('$23.') + Anything + Exactly('\n')

    regex.match('$23.bl@h\n') # => True

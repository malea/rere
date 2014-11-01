# `rere`: regex redone

```python
from rere import *

money_regex = Exactly('$') + Digit*2 + (Exactly('.') + Digit*2).zero_or_one

regex.match('$23.95') # ==> True
```

Isn't this better than `regex.compile('\\$\\d\\d(\\.\\d\\d)?')`?

## Installation

Run the following command to install:

    pip install rere

This may require root (`sudo`).

Python 2.7+ and 3.3+ are supported.

## Usage

To get started using `rere`, you need to know the logic of the regular
expression pattern that you wish to build. To learn more about regular
expressions and their usage, please visit [Wikipedia: Regular
Expression](http://en.wikipedia.org/wiki/Regular_expression).

Once you know what sort of pattern you wish to match strings against, you can
use `rere` to automatically generate the string patterns that you wish to use.
Additionally, there is functionality built in to `rere` to call Python's
built-in `re` library to do the matching for you (`match()` or
`match\_prefix`).

See above for the example.

## API

### Regex Components

The following components can be used individually, or added together (with `+`)
create compound regexes.

#### `Exactly`

```python
Exactly(string)
```

-   `string`: the string that is exactly what you want to match against

Use exactly to describe a part of a regex that you wish to be the exact
string of your choosing.

For example, if you want to match for the exact string, 'cat',

```python
regex = Exactly('cat')
regex.match('cat') # ==> True
regex.match('Cat') # ==> False
regex.prefix_match('catapult') # ==> True
regex.prefix_match('bobcat') # ==> False
```

`Exactly` takes care of any required escaping, so you can do things like: 

```python
regex = Exactly('$2.00\n')
regex.match('$2.00\n') # ==> True
````

(If you had to write a raw regex for the above, it might look something
like `re.compile('\\$2\\.00\\\n')`. Ew.)

#### `AnyChar`

```python
AnyChar
```

Use `AnyChar` when you want to match any single character (special or
otherwise, including newlines). 

```python
regex = Exactly('hello') + AnyChar
regex.match('hello!') # ==> True
regex.match('hello1') # ==> True
regex.match('hello!!') # ==> False
regex.match('hello\n') # ==> True
```

#### `Digit`

```python
Digit
```

Use `Digit` when you want to match any single digit (from 0 to 9).

```python
regex = Exactly('hello') + Digit
regex.match('hello!') # ==> False 
regex.match('hello1') # ==> True
regex.match('hello09') # ==> False 
```

#### `Letter`

```python
Letter
```

Use `Letter` when you want to match any English letter (case insensitive). 

```python
regex = Exactly('hello') + Letter 
regex.match('helloB') # ==> True 
regex.match('hellob') # ==> True
regex.match('hello9') # ==> False 
regex.match('hello\n') # ==> False
regex.match('helloBb') # ==> False
```
#### `Whitespace`

```python
Whitespace
```

Use `Whitespace` when you want to match whitespace (`[ \t\n\r\f\v]`).

```python
regex = Exactly('hi') + Whitespace
regex.match('hi ') # ==> True
regex.match('hi\n') # ==> True
regex.match('hi b') # ==> False
```

#### `Anything`

```python
Anything
```

Use `Anything` when you want to match absolutely anything (special or
otherwise, including newlines). The empty string will also be matched.

```python
regex = Exactly('hello') + Anything
regex.match('hello!') # ==> True
regex.match('hello!!') # ==> True 
regex.match('hello\n') # ==> True
regex.match('Hellohello') #==> False
```

#### `RawRegex`

```python
RawRegex(pattern)
```

-   `pattern`: a string containing a raw regex (using the syntax from `re`)

Simply match the provided regular expression. This allows you to use legacy
regexes within `rere` expressions.

For example, if you have an existing regex for phone numbers (like
`r"\(\d\d\d\) \d\d\d-\d\d\d\d"`), and you want to match one or more of
them:

```python
regex = RawRegex(r"\(\d\d\d\) \d\d\d-\d\d\d\d").one_or_more
```

### Combining Components

All regex components implement several common functions. They can be combined
and nested in many ways, such as:

```python
regex = (Exactly('cat') + Exactly('dog').zero_or_one).one_or_more
regex.match('catcatdogcatdogcatdog') # ==> True
regex.match('catdogdog') # ==> False
```

#### `regex.zero_or_one`

Use the `zero_or_one` property to describe how many repetitions of a string are
required to match the pattern, in this case, only zero or one.

```python
regex = Exactly('ab').zero_or_one
regex.match('aba') # ==> False
regex.match('ab') # ==> True
regex.match('') # ==> True
```

#### `regex.zero_or_more`

Use the `zero_or_more` property to describe how many repetitions of a string are
required to match the pattern, in this case, any number (zero or more).

```python
regex = Exactly('ab').zero_or_more 
regex.match('ababab') # ==> True
regex.match('ab') # ==> True
regex.match('') # ==> True
regex.match('aba') # ==> False 
```

#### `regex.one_or_more`

Use the `one_or_more` function to describe how many repetitions of a string are
required to match the pattern, in this case, at least one.

```python
regex = Exactly('ab').one_or_more 
regex.match('ababab') # ==> True
regex.match('ab') # ==> True
regex.match('') # ==> False
regex.match('aba') # ==> False 
```

#### Addition (`+`)

You can form a regex from separate parts and combine them together with the
`+` sign.

```python
regex = Exactly('cat') + Exactly('dog')
regex.match('catdog') # ==> True
```

#### Multiplication (`*`)

If you want a part (or a full) regex to be repeated a specified number of times,
use the `*` sign.

```python
regex = Exactly('cat') * 2
regex.match('catcat') # ==> True
```

#### Or (`|`)

If need "Either or" logic for your regex, use `|`.

```python
regex = Exactly('cat') | Exactly('dog')
regex.match('cat') # ==> True
regex.match('dog') # ==> True
regex.match('fish') # ==> False
```

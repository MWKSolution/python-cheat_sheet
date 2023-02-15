# regex

---

## Metacharacters
### Basic
```regexp
.   single character except newline   
^   anchors at the start of a string,
    complements a character class
$   anchors at the end of a string
*   zero or more repetitions
+   one or more repetitions
?   zero or one repetition
    non-greedy versions of *, +, and ?
    lookahead or lookbehind assertion
    a named group
{2} explicitly specified number of repetitions
\   escapes a metacharacter of its special meaning
    special character class
    grouping backreference
[x] character class, Specifies a specific set of characters to match.
    [a-z][A-Z][0-9],  [^abc] - not [abc]
|  alternation
() group
(:  # = !)	specialized group
<>  named group
```
### Special
```regexp
\w  character is a word character. [a-zA-Z0-9_]:
\W  not \w
\d  decimal digit [0-9]
\D  not \d
\s  whitespace
\S not \s
```
### Anchors
```regexp
\A  start of the string, same as ^
\Z  end of the string, same as $
\b  word boundary - part of string with  [a-zA-Z0-9_]
\B  not \b
```
### Non-greedy
```regexp
*?
+?
?? 
greedy - longest possible, non-greedy - shortest possible
```
### Repetition
```regexp
{3}   3 repetitions of precicing regex
{2,3} 2 to 3 repetitions
{,3} - {0,3} 
{2,} - 2 or more repetitions
{,}  - {0,} any number of repetition
{2,3}? - non-greedy version
```
### Grouping, capturing
```regexp
(abc)
(\d\d\d)? - zero or one ocurance of 3 digit str
\2  - match sth like previously described 2nd group
(?P<name>...) - named group
(?P=<name>) - as previously named group
(?:...) - don't catch that group
```
### Alternative, conditional
```regexp
abc | def - match one of them
(?(name)...|...) conditional based on existence of group name
```
### Lookahead and Lookbehind
```regexp
(?=...) - what follows
(?!...) - what doesn't follow
(?<=...) - what precedes
(?<!...) what doesn't predede
```
### Comments
```regexp
(?#this is comment)
```
## Python re
### Searching functions
```python
import re
re.search(regex, string, flags)     # anywhere
re.match(regex, string, flags)      # at the beginning
re.fullmatch(regex, string, flags)  # whole string
re.findall(regex, string, flags)    # all non-overlaping matches with tupled groups
re.finiter(regex, string, flags)    # same but returns iterator - but not string but match objects
#  all with pos and endpos for string !!!
```
### Substitution functions
```python
import re
re.sub(regex, repl, string, count, flags) # replace matches by repl count times, with groups and functions !!!
re.subn()  # same but return also nuber of substitutions
```
### Utility functions
```python
import re
re.split(regex, string, maxsplit, flags)  # splits using regex as delimiter, with groups!!!
re.escape(regex)  # escape characters in regex - anything other than \w
```
### Precompile
```python
import re
regcomp = re.compile(regex, flags)
result = re.search(regcomp, string)
```
```python
import re
regcomp = re.compile(regex, flags)
result = regcomp.search(string)
```
### Regex attributes
```python
import re
regcomp = re.compile(regex, flags)
regcomp.flags       # set flags
regcomp.groups      # number of defined groups
regcomp.groupindex  # dictionary of named groups
regcomp.pattern     # regex itself
```
### Match object
```python
import re
r = re.compile(r'\w')
m = r.match('abc cdf')  # match !!!! only !!!
m.group(1)       # concrete captured group
m.groups(default='1')      # all captured groups, when None returns default !!!
m.groupdict(default=None)  # dictionary with named groups
m.expand()                 # substituting strings, some like f'{}' strings ut with groups
m.start()                  # start index
m.end()                    # end index
m.span()                   # span: (start, end))
```

```python
import timeit

m.pos         # 
m.endpos      # pos and endpos arguments for match
m.lastindex   # index of the last captured group
m.lastgroup   # name of the last captued group
m.re          # compiled regex
m.string      # used string
```
### Flags
```python
import re
re.IGNORECASE  # case insensitive
re.MULTILINE   # anchor start and stop at lines
re.DEBUG       # display debug information
re.DOTALL      # make . matching all characters
re.VERBOSE     # make regex more readable by ignoring whitespacec in them
re.ASCII       # specify encoding for string...
re.UNICODE
re.LOCALE
```


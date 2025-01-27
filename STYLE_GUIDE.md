# Tech Stack Guide

This guide gives coding conventions that must be used when building this project (**Colorful Test**).  The main idea behind this guide is to ensure we write consistent code that can easily be understood by every member of the team.

## How to use this style guide

You are requested to read the guide before you start writing any code, so you know what is accepted and what is not. When refactoring your code, you must also use the guide to ensure your solution complies with what is expected. **Ensure you do not push code to GitHub that is considered bad design by the guide.**

Most of these conventions are in compliance with [PEP-8.](https://peps.python.org/pep-0008/)

**Indentation.**

Use 4 spaces per indentation level.

*Correct:*

```python
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

*Incorrect:*

```python
# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

When the conditional part of an `if`-statement is long enough to require that it be written across multiple lines

```python
# Correct

# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

*Incorrect:*

```python
# Incorrect

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```

*Correct:*

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

**Maximum Line Length.**

The line length of comments and docstrings should be limited to 72 characters.

**Should a line break before or after the binary operator?**

*Incorrect:*

```python
# Wrong:
# operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

*Correct:*

```python
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

**Blank Lines.**

Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank line.

Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners.

Use blank lines in functions, sparingly, to indicate logical sections.

**Imports.**

Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

Imports should be grouped in the following order:

1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.

You should put a blank line between each group of imports.

Avoid importing the whole package/library when you only need a few functions from it.

Imports should be on separate lines: 

*Incorrect:*

```python
# Correct:
import os
import sys
```

*Correct:*

```python
# Wrong:
import sys, os
```

*It’s okay to say this though:*

```python
# Correct:
from subprocess import Popen, PIPE
```

**String Quotes.**

Strings - ‘single quotes must be used for strings.’

Docstrings - “”” Double quotes must be used for docstrings.”””

**Whitespace in expressions and statements.**

Avoid extraneous whitespace in the following situations:

- Immediately inside parentheses, brackets or brace
    
    ```python
    # Correct:
    spam(ham[1], {eggs: 2})
    
    # Wrong:
    spam( ham[ 1 ], { eggs: 2 } )
    ```
    

- Between a trailing comma and a following close parenthesis
    
    ```python
    # Correct:
    foo = (0,)
    
    # Wrong:
    bar = (0, )
    ```
    
- Immediately before a comma, semicolon, or colon
    
    ```python
    # Correct:
    if x == 4: print(x, y); 
    x, y = y, x
    
    # Wrong:
    if x == 4 : print(x , y) ; 
    x , y = y , x
    ```
    
- However, in a slice the colon acts like a binary operator and should have equal amounts on either side (treating it as the operator with the lowest priority). In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted
    
    ```python
    # Correct:
    ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
    ham[lower:upper], ham[lower:upper:], ham[lower::step]
    ham[lower+offset : upper+offset]
    ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
    ham[lower + offset : upper + offset]
    
    # Wrong:
    ham[lower + offset:upper + offset]
    ham[1: 9], ham[1 :9], ham[1:9 :3]
    ham[lower : : upper]
    ham[ : upper]
    ```
    
- Immediately before the open parenthesis that starts the argument list of a function call
    
    ```python
    # Correct:
    spam(1)
    
    # Wrong:
    spam (1)
    ```
    
- Immediately before the open parenthesis that starts an indexing or slicing
    
    ```python
    # Correct:
    dct['key'] = lst[index]
    
    # Wrong:
    dct ['key'] = lst [index]
    ```
    
- More than one space around an assignment (or other) operator to align it with another
    
    ```python
    # Correct:
    x = 1
    y = 2
    long_variable = 3
    
    # Wrong:
    x             = 1
    y             = 2
    long_variable = 3
    ```
    
- Avoid trailing whitespace anywhere.
- Always surround these binary operators with a single space on either side: assignment (`=`), augmented assignment (`+=`, `-=` etc.), comparisons (`==`, `<`, `>`, `!=`, `<>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`), Booleans (`and`, `or`, `not`).
- If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator:
    
    ```python
    # Correct:
    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)
    
    # Wrong:
    i=i+1
    submitted +=1
    x = x * 2 - 1
    hypot2 = x * x + y * y
    c = (a + b) * (a - b)
    ```
    
- Don’t use spaces around the `=` sign when used to indicate a keyword argument, or when used to indicate a default value for an *unannotated* function parameter.
    
    ```python
    # Correct:
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)
    
    # Wrong:
    def complex(real, imag = 0.0):
        return magic(r = real, i = imag)
    ```
    
    When combining an argument annotation with a default value, however, do use spaces around the `=` sign:
    
    ```python
    # Correct:
    def munge(sep: AnyStr = None): ...
    def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
    
    # Wrong:
    def munge(input: AnyStr=None): ...
    def munge(input: AnyStr, limit = 1000): ...
    ```
    
- Multiple statements on the same line should not be used.
    
    ```python
    # Correct:
    if foo == 'blah':
        do_blah_thing()
    do_one()
    do_two()
    do_three()
    
    # Wrong:
    if foo == 'blah': do_blah_thing()
    do_one(); do_two(); do_three()
    ```
    
- Avoid these when using if/for/while statements.
    
    ```python
    # Wrong:
    if foo == 'blah': do_blah_thing()
    for x in lst: total += x
    while t < 10: t = delay()
    
    # Wrong:
    if foo == 'blah': do_blah_thing()
    else: do_non_blah_thing()
    
    try: something()
    finally: cleanup()
    
    do_one(); do_two(); do_three(long, argument,
                                 list, like, this)
    
    if foo == 'blah': one(); two(); three()
    ```
    

**Comments.**

Comments should ***always*** be written in English.

Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!

Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).

Comments should short and concise. They should be easy to understand. Take your time when writing your comments.

Write short comments that describes what a module/function does. Try to make this just one line but if it’s necessary it can be a multi-line comment. This comment should be after the `def` line. For example:

```python
def get_random_code():
	# Generates a 4-digit random number

	code goes here...
```

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

Inline comments are unnecessary and in fact distracting if they state the obvious.

**Documentation strings.**

Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods.

**Naming Conventions.**

Try to use self-explanatory names. If you feel like people will find it hard to understand a name, just ask a friend or a colleague to help you come up with a better name or leave a comment explaining that name.

```python
# Naming Conventions

# Start names with a lowercase
number = 5

# Use an underscore for a space
def get_random_num():
	code goes here...

# Use camel case for classes
class LookupError(BaseException):
	code goes here...

# Use all caps for constants
DONT_CHANGE_ME = 100
```

**More rules!**

- Comparisons to singletons like None should always be done with `is` or `is not`, never the equality operators. For example:
    
    ```python
    # Correct
    if abc is None:
    	pass # Pythonic way to say 'do nothing'
    
    # Wrong
    if abc == None:
    	pass
    ```
    
- Use `is not` operator rather than `not ... is`. While both expressions are functionally identical, the former is more readable and preferred.
    
    ```python
    # Correct:
    if foo is not None:
    
    # Wrong:
    if not foo is None:
    ```
    
- Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier:
    
    ```python
    # Correct:
    def f(x): return 2*x
    
    # Wrong:
    f = lambda x: 2*x
    ```
    
- When catching exceptions, mention specific exceptions instead of using a bare `except:`
    
    ```python
    try:
        import platform_specific_module
    except ImportError:
        platform_specific_module = None
    ```
    
- For all try/except clauses, limit the `try` clause to the absolute minimum amount of code necessary.
    
    ```python
    # Correct:
    try:
        value = collection[key]
    except KeyError:
        return key_not_found(key)
    else:
        return handle_value(value)
    
    # Wrong:
    try:
        # Too broad!
        return handle_value(collection[key])
    except KeyError:
        # Will also catch KeyError raised by handle_value()
        return key_not_found(key)
    ```
    
- Be consistent in return statements. Either all return statements in a function should return an expression, or none of them should.
    
    ```python
    # Correct:
    def foo(x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return None
    
    def bar(x):
        if x < 0:
            return None
        return math.sqrt(x)
    
    # Wrong:
    def foo(x):
        if x >= 0:
            return math.sqrt(x)
    
    def bar(x):
        if x < 0:
            return
        return math.sqrt(x)
    ```
    
- Use `' '.startswith()` and `' '.endswith()` instead of string slicing to check for prefixes or suffixes. `startswith()` and `endswith()` are cleaner and less error prone:
    
    ```python
    # Correct:
    if foo.startswith('bar'):
    
    # Wrong:
    if foo[:3] == 'bar':
    ```
    
- For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
    
    ```python
    # Correct:
    if not seq:
    if seq:
    
    # Wrong:
    if len(seq):
    if not len(seq):
    ```
    
- Don’t compare `boolean` values to True or False using `==`.
    
    ```python
    # Correct:
    if greeting:
    
    # Wrong:
    if greeting == True:
    
    # Wrong:
    if greeting is True:
    ```
    
- Use of the flow control statements `return`/`break`/`continue` within the `finally` suite of a `try...finally`, where the flow control statement would jump outside the `finally` suite, is discouraged.
    
    ```python
    # Wrong:
    def foo():
        try:
            1 / 0
        finally:
            return 42
    ```
    

**Additional Python Conveniences**

Conditional Expressions

```python
# Discouraged
if n > 0:
	sign = 'positive'
else:
	sign = 'negative'

# Encouraged
sign = 'positive' if n > 0 else 'negative'
```

Comprehension Syntax

```python
# Discouraged
new_list = []
for x in old_list:
	if x > 1:
		new_list.append(x*2)

# Encouraged
new_list = [x*2 for x in old_list if x > 1]

# Format
[expression for value in iterable if condition] # Condition is optional

[] => List Compression
{} => Set Compression
() => Generator Compression
{k: } => Dictionary Compression

```

Simultaneous Assignments

- Technique whereby we explicitly assign a series of values to a series of identifiers, using this syntax:
    
    ```python
    x, y, z = 1, 2, 3
    ```
    
- In effect, the right-hand side of this assignment is automatically packed into a tuple and then automatically unpacked with its elements assigned to the two identifies on the left-hand side.

```python
j, k = k, j
```
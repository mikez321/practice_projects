# Notes from Udemy Python Course:
* All python functions end with parenthesis

### Strings and Variables
* Get input from user with `input()` method.  Pretty slick.
* The 'escape' character `\`

__Naming Variables__
* Must begin with a letter (upper or lower case) or a _
* They can contain numbers
* They are case sensitive
* They are assigned using an `=`
* You would say that 'this string (or whatever) is bound to the variable (whatever)'

__Types in Python__
* find a data type with the `type()` method.
* variables can easily be reassigned just like in Ruby (apparently that's not the case for languages like C or Java... weird... who knew)

__Python is a 'strongly typed' language__

What does that even mean???

In this example we try to concatenate a string and an int.  It generates an error saying it can't do that.  _Oh, and one nice thing here... it has a semi useful error message with a line number and everything!_

### Python Types:
Numeric:
* The 3 kinds are: int, float, complex
* Integers = int
* This is all the same as Ruby with int and float
* There's basically no limit to how big ints can be
* Floats work the same
* They can have 308 places to the right of a decimal
* There is a 'decimal' data type but that's not covered in the course

__A bit of vocab now: Expression__

An expression is anything that can be calculated to return a value.  Probably pretty stright forward, but I am not used to hearing that term soooo.... there  ya go.

__Slicing Strings__
`[start:end]`

Slicing will cut a word up through a range... start:end.  It __does not__ include the last number!  "Up to but not including"

__Python Idioms__

To reverse a string: `[::-1]`

To print the last character of a sequence: `[-1:]`

To print the last n characters of a sequence: `[-n:]`

To print the first n characters of a sequence: `[:n]`

To print the first in a string:
`[:1]` or `[0]`

### Sequences:

What is a sequence?

An __ordered__ set of items.... Strings are sequences, and so are arrays

stuff = ['computer', 'monitor', 'mouse']

stuff[0] => 'computer'

stuff[0][0] => 'c'

### Fun to know!
Any data type can be 'coerced' into a string in Python!

### Replacement Fields
This is called 'String Interpolation' in Ruby.  It is done with curly braces and a number, and then `.format(num1, num2, num3 ....)`

These numbers don't have to be in order in the string.... just as long as they are referenced properly.

`"Jan: {1}, Feb: {0}, Mar: {1}, Apr: {2}".format(28, 31, 30)`

### F Strings
F Strings are a little newer of a feature and really get close to Ruby string interpolation.  Instead of using `.format("whatever")` you would do something like this:
```
word = "whatever"

print(f"Tim's age is {word}".)
=> Tim's age is whatever.
```

Basically you prepend an 'f' before the double quotes

And you can put whatever you want in the curly braces.  You can totally do something like:
```
num1 = 3
num2 = 1

print(f"The sum of {num1} and {num2} is {num1 + num2}.")

=> The sum of 3 and 1 is 4.
```

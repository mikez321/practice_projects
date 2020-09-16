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

## Onto Python Programming!
Now that we've gone through how to manipulate things and do data calculations, lets look at programming in Python...

Python uses indentation to define blocks of code

Convention is to indent 4 spaces per block

To start a code block you'll always have a : and then the line below will be indented.

### Booleans!
True and False (Yep, I knew that!)
True and False will always be capitalized.  I also came across None, which is also capitalized.

Precedence of booleans.... I covered this back in Mod1, but let's go over it again.
```
Precedence of boolean
()
if/else
or
and
not
>,<, >=, <=, !=, ==
```

So, there are 'bitwise' and/or represented by & and |, but these don't seem to work right in my code.  Just stick with words unlike Ruby here.

### Truthy
This seems like it might be a little bit different than Ruby....

* None and False == False
* 0 of any numeric type (int, float, fraction, etc) == False
* Empty strings == False

### In and Not In
I think this has been covered already, but it just checks to see if something is contained in a string.  It can be whole words or just letters or whatever (for strings).  `not in` is the opposite of `in`.

### A bit of reference:
Check out methods at [Python Docs](https://docs.python.org)

### For Loops
This is like an each loop in Ruby.

```
for VARIABLE in THING:
  do something until the THING has nothing else to do something with
```

When using for loops and ranges, remember that ranges go from the first number, up to BUT NOT INCLUDING the last number in the range (just like string slice).

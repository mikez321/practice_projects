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

### Continue and Break
`continue` works like `next` in ruby where if a condition is true it is skipped.

`break` works like `return` in ruby where the method stops running where its at.

### Heads up!
Guard clauses are a thing in Python just like they are in Ruby.

```
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
```

This can also be written as:
```
if item_to_find in shopping_list:
  found_at = shopping_list.index(item_to_find)
  break
```

### Pass Statement
If you put `pass` in a code block, it will run, just not do anything

In Python, you can't have blanks inside flow control statements, but pass will work.

### Augmented Assignment
"The combination in a single statement of a binary operation and an assignment statement."

This means `guesses = guesses + 1` == `guesses += 1`

In Python augmented assignment is faster than assigning and then adding

### Style in Python Code
PEP8 is the Python style guide.

"Python Enhancement Proposal"

There might be unique style guides for your own projects, so be aware.  __DO NOT__ just change things because it follows the style guide.  Stick to what your application is written with so you don't introduce problems into the code.

Your IDE might tab differently so be careful with spaces and tabs when indenting

Line lengths should be limited to 72 characters.

_Naming Conventions_
* Functions and Variables should be written in lower_snake_case
* Classes should be named in UpperCamelCase
* Always use `self` as the first arg for instance methods
* Always use `cls` as the first arg for class methods

### Else in a Loop
Else can run with a FOR loop is kinda weird.  It goes with the same indentation as the for part, and is just code that runs at the end of the for loop.

```
for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")
```

In this code, if any of the numbers are divisible by 8 it will reject the list and the loop will break.  If none of that code breaks, the for loop will terminate by running what's in the else block.

To make it seem a little more straightforward... else in a for or while loop could have simply been called something like `completed` or `loop_end` since it will run that if a loop successfully ends or completes.

You don't need to use else in for and while loops but it can be handy sometimes.

### Sequence Types:
What is a sequence type?
```
lists, tuples, and range objects are sequences
A sequence is an ordered collection of items
If a sequence wasn't ordered you couldn't refer to their items by an index position

If you iterate over a sequence you'll always get the results in the same order

Anything you can use in a for loop is an iterable.
```

### Lists:
You can slice lists and look at their content just like you can with a string because strings and lists are both sequences.

BUT, strings are _immutable_ where as lists are _mutable_.

When an object is immutable that means it cannot be changed.  The following are immutable types built into Python:

* int
* float
* bool
* str
* tuple
* frozenset
* bytes

A 5 will always be a 5.  You can do arithmetic to it, but a 5 will always be a 5.

### Method Vs. Function
When you call a function you just type in the name of the function and any args it might need.  `len('hello')` is an example of a function.

You call a method on an object.  You'll specify an object that you want to run a function on.  `list = ['hello']` gives you an object called list.  Then you can do something like call the append method to list.  `list.append('world')`


### Enumerate function:
The enumerate() function returns each item in a list with its index number

### Tricky here... sorted() or .sort()
They both can both sort lists (or strings or ints or floats etc)... but be careful! `.sort()` returns `None` where `sorted()` returns a sorted version of that list.

Oh, and one more bit on this.  sorted() will __create a new list__ from your existing list and return it.  You will still be able to access your original list.  .sort() will mutate your current list, and then return `None`.  __Instead of creating a new, sorted list, your list has been mutated into a sorted list.__

### If you want to sort case insensitive:
You can use a 2nd argument to the sorted() function.  Just add `, key=str.casefold` as a 2nd arg.

### Style guide for nested lists:
Multi line lists can be broken up as such with the closing bracket in line with the items.
```
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
```

Or the closing bracket can line up on space zero... like this:
```
my_list = [
    1, 2, 3,
    4, 5, 6,
]
```
Both are acceptable.
_Also of note... the lists can end with a comma, and Python will just ignore it.  It might make things a little easier in the future._

### Interesting thing about print()
The first argument of `print()` is `*Object`.  `*Object` means it can take as many args to print as you would like.  They will be separated by a comma.  I think in Ruby this was called 'splat operator'.

### Tuples
Tuples are like lists, but they are immutable.  Tuples are ordered lists. They also share the same methods as lists.

Visually, tuples are encased in `()`, not `[]`.  A tuple can be created by code similar to the following:
```
t = 'a', 'b', 'c'
# or t = ('a', 'b', 'c')

print(t)

=> ('a', 'b', 'c')
```

The parenthesis while declaring a tuple aren't required, but maybe just go ahead and alway use them

__Tuples must be encased in parenthesis when they are being passed as an arg in a function/method.__

```
name = 'Mike'
keyboard = 'HHKB'

print(name, 20, keyboard, 99)

# the above != below!

print((name, 20, keyboard, 99))
```

You can access indexes just like in a list using square brackets.  But remember that tuples are immutable, so you can't reassign at an index value.

Because tuples are immutable they don't carry all the extra overhead and methods of lists and take up less memory.  Also, if you don't want your data to change you could store it in a tuple.

Because tuples are immutable, you can _always_ successfully unpack a tuple, where as a list, you could potentially run into issues.

And one last bit about unpacking tuples... if you're writing code and need to reference things in a tuple (or list) and find yourself referencing a lot of index positions you can just unpack the tuple or list into variables and it might make things easier for you in the future.

### Import Data from other Python Files:
You can import other python files into your python files and save yourself from having to copy-paste everything in there.  Do this the same way you'd import other modules or how you'd do it in Ruby.

But, unlike Ruby, you can import just a single piece of a file.

```
from nested_data import albums
```

This will import the variable 'albums' (which was a nested list of tuples) from the file nested_data.py and allow access to it.

_It does appear the whole file will run, so if you have rando code hanging out in there it will output in your input_

### Constants
A constant is a value that is fixed and does not change.  Python doesn't have any data type that you can set like in C or Java.  So, you use an ALL_CAPS name to remind people... 'don't change that.'  Remember tho, its still a variable, and you can still change it.  It is just convention that constant variables that should not change are going to be named in all caps.

### Functions
Function names start with `def` and follow the same rules as variables: start with lower case, separated by _ and then has a `():`

You will always need to add the () to the end of functions when you write or call them.

You will use `return` to tell what the result of the function is.  When a function hits a return it stops running!

If you don't have a return, the return value of the function will be `None`.

Functions don't _need_ to return anything tho... maybe they just need to do something to a piece of data, ya know?  Functions might alter data and not return a value.

### Errors
If you want to generate an error, make sure it is descriptive and you can then add it by something like:
```
raise ValueError("Whatever the error is going to say.")
```

There are many different types of errors and you can find them in the python docs under 'exceptions'.

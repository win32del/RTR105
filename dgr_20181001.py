Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __built

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __built
NameError: name '__built' is not defined
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."__builtins__.__doc__)
SyntaxError: invalid syntax
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> a = 12312
>>> b = 1.666
>>> c = 'Z'
>>> vars()
{'a': 12312, 'c': 'Z', 'b': 1.666, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(a)
<type 'int'>
>>> type(b)
<type 'float'>
>>> type(c)
<type 'str'>
>>> 

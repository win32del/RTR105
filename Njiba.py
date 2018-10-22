Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def thing():
	print("Hello")
	print("Fun")

	
>>> thing()
Hello
Fun
>>> thing()
Hello
Fun
>>> print("Zip")
Zip
>>> thing():
	
SyntaxError: invalid syntax
>>> thing()
Hello
Fun
>>> thing():
	
SyntaxError: invalid syntax
>>> def thing()
SyntaxError: invalid syntax
>>> def thing():
	print("Hello")
	print("Fun")
thing()
SyntaxError: invalid syntax
>>> def thing():
    print("hello")
    print("Fun")

thing()
print("Zip")
thing()
SyntaxError: invalid syntax
>>> 
================ RESTART: /home/birthrepelant/RTR105/nuuug.py ================
hello
Fun
Zip
hello
Fun
>>> big = max("Hello world")
>>> print(big)
w
>>> tiny = min("hello world")
>>> print(tiny)
 
>>> 
================ RESTART: /home/birthrepelant/RTR105/njaag.py ================
>>> 
================ RESTART: /home/birthrepelant/RTR105/njaag.py ================
>>> print(1 + 2 * float(3) / 4 - 5)
-2.5
>>> sval = "123"
>>> type(sval)
<class 'str'>
>>> ival = int(sval)
>>> type(ival)
<class 'int'>
>>> fval = ival + 1
>>> print(fval)
124
>>> def print_lyrics():
	print("Es black bullet")
	print("Netaisos tik atri iet gulet")

	
>>> print_lyrics()
Es black bullet
Netaisos tik atri iet gulet
>>> 
========== RESTART: /home/birthrepelant/RTR105/guido wrote this.py ==========
hello
Traceback (most recent call last):
  File "/home/birthrepelant/RTR105/guido wrote this.py", line 4, in <module>
    print_lyrics()
NameError: name 'print_lyrics' is not defined
>>> 
========== RESTART: /home/birthrepelant/RTR105/guido wrote this.py ==========
hello
Yo
7
>>> 
========== RESTART: /home/birthrepelant/RTR105/guido wrote this.py ==========
hello
Yo
Es black bullet
Netaisos tik atri eit gulet
7
>>> 
======== RESTART: /home/birthrepelant/RTR105/guido also wrote this.py ========
>>> greet("en")
hello
>>> greet("es")
Hola
>>> greet("fr")
Bonjour
>>> 
====== RESTART: /home/birthrepelant/RTR105/guido did not write this.py ======
Hello Glenn
Hello sally
>>> print(greet("en"), "Glenn")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(greet("en"), "Glenn")
TypeError: greet() takes 0 positional arguments but 1 was given
>>> 
====== RESTART: /home/birthrepelant/RTR105/maybe guido was involved.py ======
Hello Glenn
Hola sally
Bonjour Michael
>>> 
============= RESTART: /home/birthrepelant/Guido does it all.py =============
8
>>> history > history_20181022_17_05
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    history > history_20181022_17_05
NameError: name 'history' is not defined
>>> 

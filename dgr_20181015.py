Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> 
>>> 
>>> x = 5
>>> if x < 10:
	print("smaller")
	if x > 20:
		print("Bigger")

		
smaller
>>> print("finis")
finis
>>> if x < 10:
	print("smaller")
	if x > 20:
		print("BIgger")
		print("finis")

		
smaller
>>>  if x < 10:
	print("smaller")
	if x > 20:
		print("BIgger")
			print("finis")


SyntaxError: unexpected indent
>>> if x < 10:
	print("smaller")
	if x > 20:
		print("BIgger")
			print("finis")

SyntaxError: unexpected indent
>>> 
>>> if x < 10:
	print("smaller")
	if x > 20:
		print("BIgger")
			print("finis")
			
SyntaxError: unexpected indent
>>> 
>>> if x < 10:
	print("smaller")
	if x > 20:
		print("BIgger")

									print("finis")

SyntaxError: unexpected indent
>>> x = 5
>>> if x < 10:
	print("smaller")
	if x > 20:
		print("BIgger")



								   	print("finis")
								   	
SyntaxError: unexpected indent
>>> if x < 10:
	print("smaller")
	if x > 20:
		print("BIgger")
									 print("finis")

SyntaxError: unexpected indent
>>> x = 5
>>> if x == 5:
	print("Equals 5")
	if x > 4:
		print("Greater than 4")
		if x >= 5:
			print("Greater than or equals 5")
			if x < 6: print("Less than 6")
			if x <= 5: print("less than or equals 5")
			if x != 6 : print("not equal 6")

			
Equals 5
Greater than 4
Greater than or equals 5
Less than 6
less than or equals 5
not equal 6
>>> print("before 5")
before 5
>>> if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5")
    
SyntaxError: unindent does not match any outer indentation level
>>> if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5")
    print("before 6")
    if x == 6 :
        print("Is 6")
        print("is still 6")
        print("Third 6")
    print("afterwards 6")

SyntaxError: unindent does not match any outer indentation level
>>> 
>>> if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5"):
    print("before 6")
    if x == 6 :
        print("Is 6")
        print("is still 6")
        print("Third 6")
    print("afterwards 6")
    
SyntaxError: unindent does not match any outer indentation level
>>> if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5") :
    print("before 6")
    if x == 6 :
        print("Is 6")
        print("is still 6")
        print("Third 6")
    print("afterwards 6")

SyntaxError: unindent does not match any outer indentation level
>>> if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5") :
        print("before 6")
    if x == 6 :
        print("Is 6")
        print("is still 6")
        print("Third 6")
    print("afterwards 6")

SyntaxError: unindent does not match any outer indentation level
>>> if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5")
    print("before 6")
    if x == 6 :
        print("Is 6")
        print("is still 6")
        print("Third 6")
    print("afterwards 6")

SyntaxError: unindent does not match any outer indentation level
>>> 	if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5"):print("before 6")
    if x == 6 :
        print("Is 6")
        print("is still 6")
        print("Third 6")
    print("afterwards 6")

SyntaxError: unexpected indent
>>> if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5"):print("before 6")
    if x == 6 :
        print("Is 6")
        print("is still 6")
        print("Third 6")
    print("afterwards 6")

SyntaxError: unindent does not match any outer indentation level
>>> if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5"):print("before 6")

if x == 6 :
        print("Is 6")
        print("is still 6")
        print("Third 6")
    print("afterwards 6")

SyntaxError: unindent does not match any outer indentation level
>>> for i in range(5) :
	print(i)
	if i > 2 :
		print("bigger than 2")
	print("done with i", i)
print("all done")
SyntaxError: invalid syntax
>>> if x == 5 :
	print("Is 5")
	print("Is still 5")
	print("third 5")
    print("Afterwards 5"):print("before 6")

if x == 6 :
        print("Is 6")
        print("is still 6")
        print("Third 6")
    print("afterwards 6")

SyntaxError: unindent does not match any outer indentation level
>>> for i in range(5) :
	print(i)
	if i > 2 :
		print("bigger than 2")
	     print("done with i", i)
	print("all done")
	
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(5) :
	print(i)
	if i > 2 :
	     print("bigger than 2")
	print("done with i", i)
print("all done")
SyntaxError: invalid syntax
>>> for i in range(5) :
	print(i)
	if i > 2 :
		print("bigger than 2")
	print("done with i", i)
print("all done")
SyntaxError: invalid syntax
>>> 
================ RESTART: /home/birthrepelant/RTR105/bb_p.py ================
Traceback (most recent call last):
  File "/home/birthrepelant/RTR105/bb_p.py", line 1, in <module>
    if x == 5 :
NameError: name 'x' is not defined
>>> 
================ RESTART: /home/birthrepelant/RTR105/bb_p.py ================
Is 5
Is still 5
third 5
Afterwards 5
before 6
>>> 
================ RESTART: /home/birthrepelant/RTR105/bb_a.py ================
0
done with i 0
1
done with i 1
2
done with i 2
3
bigger than 2
done with i 3
4
bigger than 2
done with i 4
all done
>>> 
================= RESTART: /home/birthrepelant/RTR105/ass.py =================
More than one
Less than 100
all done
>>> 
================ RESTART: /home/birthrepelant/RTR105/hole.py ================
bigger
all done
>>> 
================ RESTART: /home/birthrepelant/RTR105/fuck.py ================
Traceback (most recent call last):
  File "/home/birthrepelant/RTR105/fuck.py", line 1, in <module>
    if x < 2:
NameError: name 'x' is not defined
>>> 
================ RESTART: /home/birthrepelant/RTR105/fuck.py ================
small
alle done
>>> 
================ RESTART: /home/birthrepelant/RTR105/fuck.py ================
small
alle done
>>> 
================ RESTART: /home/birthrepelant/RTR105/fuck.py ================
medium
alle done
>>> 
================ RESTART: /home/birthrepelant/RTR105/fuck.py ================
LAAAAAAARGE
alle done
>>> 
============ RESTART: /home/birthrepelant/RTR105/aaaaaaaaaafu.py ============
medium
>>> 
================ RESTART: /home/birthrepelant/RTR105/nuuug.py ================
Hekko
Done -1
>>> 

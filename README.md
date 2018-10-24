# RTR105
Datormācibas kursa elektroniskā klade
    1  man uname - parāda lietotāja komandas
    2  uname - Operētājsistēmas nosaukums
    3  echo $0 - programmēšanas valodas dialekts
    4  echo 0$ - programmēšanas valoda
    5  whoami - parāda kas es esmu datorā
    6  who - parāda kas man atrodas blakus
    7  pwd - atrašanās vieta datorā
    8  ls - parāda publiski pieejamās mapes un failus
    9  man ls - manuālās grāmatas skaidrojums ls funkcijai
   10  ls -l - parāda plaši izklāstītu failu un mapju aprakstu
   11  ls -a - parāda visas mapes, kuras ir pieejamas uz datora.
   12  ls -la - parāda detalizētu informāciju par mapēm, to saturu, izveidošanas datumu, īpašnieku.
   13  clear - notīrīt darba virsmu
   history >> history_20180912.txt - izveidot teksta failu ar šodienas vēsturi
    
    

    9  cd Music - Mainit direktoriju
   17  cd . - solis direktorijaa uz vietas
   19  cd .. - pariet uz augstak stavosu mapi
   32  cd Home/Birthrepelant
   33  cd home
   35  cd home/user
   36  cd /home/birthrepelant/
   38  cd / - parvietoties uz pasu sakumu
   43  cd ~ - tikt uz majam
   50  mkdir rib - izveidot direktoriju
   58  rmdir rib/ - izdzest mapi
   70  rm -r - izdzest direktoriju neskatoties uz to, ka mape ir saturs
   77  echo  "text" - terminali pasaka ievadito tekstu
   79  echo "teksts
teksts
teksts" - pasaka tekstu vairakas rindas
   81  man echo
   82  echo -e "es\nes\nes" - pasaka tekstu vairakas rindas
   86  echo "best" > fails1.txt
   88  cat fails1.txt - pasaka faila saturu
   89  less fails1.txt  - pasaka faila saturu
   90  echo "best" > fails1.txt redige faila saturu uz ievadito
   95  more fails1.txt  - pasaka faila saturu
  103  nano fails1.txt - atver teksta redaktoru
  106  chmod 540 fails1.txt - izmaina faila pieejamibu
  118  mv *1*.txt Music/ - parvieto visus failus kas satur ierakstito simbolu uz noradito mapi
    4  nano skripts_mans_skripts.sh - izveidot sava skripta failu
    5  cat skripts_mans_skripts.sh parbaudit sava skripta faila saturu
   13  echo $PATH - parada visus celus uz galvenajam direktorijam
   14  ./skripts_mans_skripts.sh - palaist skriptu
   15  /home/user/skripts_mans_skripts.sh
   19  chmod 764 skripts_mans_skripts.sh - izmainit skripta faila ipasibas
   21  echo $PATH
   22  PATH=$PATH:/home/user - pievienot jaunu galveno celu
   27  git clone https://github.com/win32del/RTR105 - lejupieladet githuba repozitariju

print(123) - parāda ievadīto iekavās
print("yeeee") - Ar pēdiņām parāda tekstu
float(a) - pārveido nodefinēto simbolu par decimālou
int(a) - ārveido nodefinēto simbolu par skaitli
str(a) - ārveido nodefinēto simbolu par  vārdu vai burtu
10 % 9 = 1 - parāda atlikumu no dalījuma
2 ** 3 - kāpinājums
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

=========== RESTART: /home/birthrepelant/RTR105/who wrote this.py ===========
5
4
3
2
1
Blastoff!
0
>>> 
===== RESTART: /home/birthrepelant/RTR105/maybe i know who wrote this.py =====
>hello there
hello there
>finished
finished
>done
done!
>>> 
========== RESTART: /home/birthrepelant/RTR105/it was not guido.py ==========
>hello there
hello there
># don't print this
>print this!
print this!
>done
done!
>>> for i in [5, 4, 3, 2, 1]:
	print(i)
print("Blastoff")
SyntaxError: invalid syntax
>>> 
============= RESTART: /home/birthrepelant/RTR105/yeye right.py =============
5
4
3
2
1
Blastoff!
>>> 
================== RESTART: /home/birthrepelant/RTR105/G.py ==================
Traceback (most recent call last):
  File "/home/birthrepelant/RTR105/G.py", line 3, in <module>
    print("Happy new year", friend)
NameError: name 'friend' is not defined
>>> 
================== RESTART: /home/birthrepelant/RTR105/G.py ==================
Happy new year Joseph
Happy new year Glenn
Happy new year Sally
Done!
>>> 
============= RESTART: /home/birthrepelant/RTR105/guido loopy.py =============
Before
9
41
12
3
74
15
After
>>> 
============== RESTART: /home/birthrepelant/RTR105/heavy guy.py ==============
before -1
Traceback (most recent call last):
  File "/home/birthrepelant/RTR105/heavy guy.py", line 6, in <module>
    print(larfest_so_far, the_num)
NameError: name 'larfest_so_far' is not defined
>>> 
============== RESTART: /home/birthrepelant/RTR105/heavy guy.py ==============
before -1
9 9
After 9
41 41
After 41
41 12
After 41
41 3
After 41
74 74
After 74
74 15
After 74
>>> 
===== RESTART: /home/birthrepelant/RTR105/yikes guido youre a genius.py =====
Before 0
1 9
2 41
3 12
4 3
5 74
6 15
After 6
>>> 
======= RESTART: /home/birthrepelant/RTR105/hey thats pretty guido.py =======
Before 0
9 9
50 41
62 12
65 3
139 74
154 15
After 154
>>> 
===== RESTART: /home/birthrepelant/RTR105/the era of guido has dusked.py =====
Before 0 0
1 9 9
After 1 9 9.0
2 50 41
After 2 50 25.0
3 62 12
After 3 62 20.666666666666668
4 65 3
After 4 65 16.25
5 139 74
After 5 139 27.8
6 154 15
After 6 154 25.666666666666668
>>> 
======= RESTART: /home/birthrepelant/RTR105/seeeeduced by the guid.py =======
Before
After
Large number 41
After
After
After
Large number 74
After
After
>>> 
============ RESTART: /home/birthrepelant/RTR105/boy in the pc.py ============
Before False
False 9
False 41
False 12
True 3
True 74
True 15
After True
>>> 
=============== RESTART: /home/birthrepelant/RTR105/ye man.py ===============
Traceback (most recent call last):
  File "/home/birthrepelant/RTR105/ye man.py", line 1, in <module>
    smallest = none
NameError: name 'none' is not defined
>>> 
=============== RESTART: /home/birthrepelant/RTR105/ye man.py ===============
Before
9 9
9 41
9 12
3 3
3 74
3 15
After 3
>>> 


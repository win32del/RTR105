#!/usr/bin/python
#!-*- coding: utf-8 -*-

a = input("cien. liet., lūdzu, ievadi skaitli: ")
#3. python'ā visi input rezultāti ir ar str datu tipu
# tapēc ievadītā lieluma datu tips vēlāk ir jāpārveido
a = int(a)

# python valodā balstās uz C valodas => print strādā līdzīgi print
print("Liet., Tu esi ievadījis skaitli: %d"%(a))
aa = a * a
print("tavs skaitlis kvadrātā ir: %d"%(aa))

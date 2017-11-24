# PicoCTF 2017 "So random"
# Ireneusz "ircykk" Kierkowski (ircykk@gmail.com)

import random, string

flag = "BNZQ:1l36de9583w5516fv3b8691102224f3e" 

decflag = ""
random.seed("random")
for c in flag:
	if c.islower():
		decflag += chr((ord(c)-97-random.randrange(0,26))%26 + 97)
	elif c.isupper():
		decflag += chr((ord(c)-65-random.randrange(0,26))%26 + 65)
	elif c.isdigit():
		decflag += chr((ord(c)-48-random.randrange(0,10))%10 + 48)
	else:
		decflag += c

print "Decoded flag: "+decflag

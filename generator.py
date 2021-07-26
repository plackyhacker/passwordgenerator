#!/usr/bin/env python3
from random import seed
from random import randint

count = 160
min_word_length = 5
file = "/usr/share/wordlists/wfuzz/general/common.txt"
l = []

f = open(file, "r")

for line in f:
	if len(line.replace("\n", "")) >= min_word_length:
		l.append(line.replace("\n", ""))

f.close

length_of_array = len(l)

for y in range(count):
	password = ""

	for x in range(3):
		rnd = randint(0, length_of_array - 1)
		password = password + str(l[rnd]) + "-"

	password = password + str(rnd)
	
	print(password)

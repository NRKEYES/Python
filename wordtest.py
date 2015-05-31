Letter_frequencies = {'A': 0.0955948121645796, 'C': 0.027728085867620753, 'B': 0.030523255813953487, 'E': 0.10084973166368515, 'D': 0.040697674418604654, 'G': 0.025380143112701252, 'F': 0.01967799642218247, 'I': 0.057356887298747765, 'H': 0.026721824686940968, 'K': 0.023255813953488372, 'J': 0.0063729874776386405, 'M': 0.03175313059033989, 'L': 0.0637298747763864, 'O': 0.07166815742397138, 'N': 0.053220035778175315, 'Q': 0.0007826475849731664, 'P': 0.03354203935599284, 'S': 0.0802772808586762, 'R': 0.05858676207513417, 'U': 0.03924418604651163, 'T': 0.05254919499105545, 'W': 0.02169051878354204, 'V': 0.010286225402504472, 'Y': 0.020013416815742396, 'X': 0.0038014311270125225, 'Z': 0.004695885509838999}

# look at a 4 character string and test if it is a english word or not. Return a boolean or an integer indicating this.

#test character to see if it is a vowel
def isVowel(test_char):
	if test_char in'aeiou':
		return True
	return False

#Word function returns true if input is a word within 15% precision
def isWord (test_string):
	word_probablily = Letter_frequencies[test_string[0].upper()]*Letter_frequencies[test_string[1].upper()]*Letter_frequencies[test_string[2].upper()]*Letter_frequencies[test_string[3].upper()]
	if word_probablily < .00000206:
		return False

	# for i in range(0,3):
	# 	if i <=1 and not isVowel(test_string[i]) and not isVowel(test_string[i+1]) and not isVowel(test_string[i+2]):
	# 		return False
	# 	if i <=1 and isVowel(test_string[i]) and isVowel(test_string[i+1]) and isVowel(test_string[i+2]):
	# 		return False

	return True


#Test function,
#Submit known strings to the function, calculates acuracy.
def testIsWord():
	words = open('words.txt', 'r')
	not_words = open('notwords.txt', 'r')
	word_right = 0
	word_wrong = 0
	not_word_right = 0
	not_word_wrong = 0

	for line in words:
		if isWord(line):
			word_right+=1
			continue
		word_wrong+=1
	print "Fake Words"
	for line in not_words:
		if not isWord(line):
			not_word_right += 1
			continue
		not_word_wrong += 1

	print "number right:", word_right
	print "number wrong:", word_wrong
	percent =float(word_wrong)/(word_right+word_wrong)*100
	print "percent mistaking a real word as fake:",percent
	print "number right:", not_word_right
	print "number wrong:", not_word_wrong
	percent = float(not_word_wrong)/(not_word_wrong+not_word_right)*100
	print "Percent mistaking a fake word as real:", percent

testIsWord();
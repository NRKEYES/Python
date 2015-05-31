#Letter_frequencies = {'E':0.120195499, 'T':0.090985886, 'A':0.081238378, 'O':0.076811682, 'I':0.073054201, 'N':0.069477738, 'S':0.062807524, 'R':0.060212942, 'H':0.059214604, 'D':0.043191829, 'L':0.039785412, 'U':0.028776268, 'C':0.0271142, 'M':0.026115862, 'F':0.023038568, 'Y':0.021135143, 'W':0.02094864, 'G':0.020257483, 'P':0.018189498, 'B':0.014892788, 'V':0.011074969, 'K':0.006895114, 'X':0.001727893, 'Q':0.001124502, 'J':0.00103125, 'Z':0.000702128}
Letter_frequencies = {'A': 0.0955948121645796, 'C': 0.027728085867620753, 'B': 0.030523255813953487, 'E': 0.10084973166368515, 'D': 0.040697674418604654, 'G': 0.025380143112701252, 'F': 0.01967799642218247, 'I': 0.057356887298747765, 'H': 0.026721824686940968, 'K': 0.023255813953488372, 'J': 0.0063729874776386405, 'M': 0.03175313059033989, 'L': 0.0637298747763864, 'O': 0.07166815742397138, 'N': 0.053220035778175315, 'Q': 0.0007826475849731664, 'P': 0.03354203935599284, 'S': 0.0802772808586762, 'R': 0.05858676207513417, 'U': 0.03924418604651163, 'T': 0.05254919499105545, 'W': 0.02169051878354204, 'V': 0.010286225402504472, 'Y': 0.020013416815742396, 'X': 0.0038014311270125225, 'Z': 0.004695885509838999}
def isWord (test_string, number):
	word_probablily = Letter_frequencies[test_string[0].upper()]*Letter_frequencies[test_string[1].upper()]*Letter_frequencies[test_string[2].upper()]*Letter_frequencies[test_string[3].upper()]
	if word_probablily < number:
		return False
	return True

def testIsWord(number):
	words = open('words.txt', 'r')
	not_words = open('notwords.txt', 'r')
	word_right = 0
	word_wrong = 0
	not_word_right = 0
	not_word_wrong = 0
	

	for line in words:
		if isWord(line, number):
			word_right+=1
			continue
		word_wrong+=1

	for line in not_words:
		if not isWord(line, number):
			not_word_right += 1
			continue
		not_word_wrong += 1

	total_wrong = not_word_wrong+word_wrong;
#	print total_wrong
	return total_wrong

wrong = 10000
best_number = 0
for i in range(1,1000):

	number_to_pass = i/float(100000000)
	t = testIsWord(number_to_pass)
	if t < wrong:
		wrong = t
		best_number = number_to_pass	
print wrong
print best_number

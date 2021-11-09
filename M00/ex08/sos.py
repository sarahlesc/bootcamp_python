import sys

morse = {
					'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/'
}

if len(sys.argv) < 2:
    exit()
i = 2
sentence = sys.argv[1]
while i < len(sys.argv):
    sentence = sentence + " " + sys.argv[i]
    i += 1
sentence = sentence.upper()
if all(x.isalnum() or x.isspace() for x in sentence):
	for i in sentence:
		for key, value in morse.items():
			if i == key:
				print(value, end =' ')
	print('')
else:
	print('ERROR')
	exit()

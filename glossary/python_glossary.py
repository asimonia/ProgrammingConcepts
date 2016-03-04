from random import choice
from os import system

def create_glossary():
	word = dict()
	defined = ''
	with open('glossary.txt', 'r') as f:
		for line in f:
			line = line.strip()
			if line.endswith(':'):
				defined = line[:(len(line) - 1)]
			else:
				word[defined] = line

	f.close()

	return word


def main():
	while True:
		your_word = choice(d.keys())

		print("Define the word: {0} ".format(your_word))
		raw_input('>>> ')
		print
		print("The answer is: \n{0}".format(d[your_word]))
		print
		raw_input('<more>')
		cls()


if __name__ == '__main__':
	# Define globals
	cls = lambda : system('cls')
	d = create_glossary()
	
	main()
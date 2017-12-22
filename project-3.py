
#Base text from wiki: https://en.wikipedia.org/wiki/Python_(programming_language)
#Retrieved 27 Sep 2017.

#For the easy quiz, the text is from the header, the replaced words have been defined as the values of easy_words below:

easy_words = ['language', 'programming', 'whitespace', 'readability']

easy_string = """
Python is a widely used high-level __word_2__ __word_1__ for general-purpose __word_2__,
created by Guido van Rossum and first released in 1991. An interpreted __word_1__, Python has a 
design philosophy that emphasizes code __word_4__ (notably using __word_3__ indentation to delimit 
code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express 
concepts in fewer lines of code than might be used in __word_1__s such as C++ or Java. The __word_1__ provides 
constructs intended to enable writing clear programs on both a small and large scale."""


#For the medium quiz, the text is from the History box:

medium_words = ['paradigm', 'garbage', 'Beautiful', 'implicit', 'Complicated']

medium_string = '''
Python is a multi-(word 1) programming language: object-oriented programming and structured programming are fully 
supported, and many language features support functional programming and aspect-oriented programming (including by
metaprogramming and metaobjects (magic methods)). Many other (word 1)s are supported via extensions, including design 
by contract and logic programming.

Python uses dynamic typing and a mix of reference counting and a cycle-detecting (word 2) collector for memory management. 
An important feature of Python is dynamic name resolution (late binding), which binds method and variable names during program execution.

The design of Python offers some support for functional programming in the Lisp tradition. The language has filter(), map(), 
and reduce() functions; list comprehensions, dictionaries, and sets; and generator expressions. The standard library has 
two modules (itertools and functools) that implement functional tools borrowed from Haskell and Standard ML.

The core philosophy of the language is summarized by the document The Zen of Python (PEP 20), which includes aphorisms such as:

    (word 3) is better than ugly
    Explicit is better than (word 4)
    Simple is better than complex
    Complex is better than (word 5)
    Readability counts

'''

#For the hard quiz, the text is again from the History box:

hard_words = ['functionality', 'core', 'optimization', 'Cython', 'Monty Python', 'pythonic', 'unpythonic']

hard_string = '''
Rather than requiring all desired (word 1) to be built into the language's (word 2), Python was designed to be highly extensible. 
Python can also be embedded in existing applications that need a programmable interface. This design of a small core language 
with a large standard library and an easily extensible interpreter was intended by Van Rossum from the start because of his 
frustrations with ABC, which espoused the opposite mindset.

While offering choice in coding methodology, the Python philosophy rejects exuberant syntax, such as in Perl, in favor of a 
sparser, less-cluttered grammar. As Alex Martelli put it: "To describe something as clever is not considered a compliment in the 
Python culture." Python's philosophy rejects the Perl "there is more than one way to do it" approach to language design in favor 
of "there should be one - and preferably only one - obvious way to do it".

Python's developers strive to avoid premature (word 3), and moreover, reject patches to non-critical parts of CPython that 
would offer a marginal increase in speed at the cost of clarity. When speed is important, a Python programmer can move time-critical 
functions to extension modules written in languages such as C, or try using PyPy, a just-in-time compiler. (word 4) is also available, 
which translates a Python script into C and makes direct C-level API calls into the Python interpreter.

An important goal of Python's developers is making it fun to use. This is reflected in the origin of the name, which comes from 
(word 5), and in an occasionally playful approach to tutorials and reference materials, such as using examples that refer to 
spam and eggs instead of the standard foo and bar.

A common neologism in the Python community is (word 6), which can have a wide range of meanings related to program style. To say 
that code is (word 6) is to say that it uses Python idioms well, that it is natural or shows fluency in the language, that it 
conforms with Python's minimalist philosophy and emphasis on readability. In contrast, code that is difficult to understand or 
reads like a rough transcription from another programming language is called (word 7).

Users and admirers of Python, especially those considered knowledgeable or experienced, are often referred to as Pythonists, 
Pythonistas, and Pythoneers.

'''

string_dict = {'easy' : easy_string, 'medium' : medium_string, 'hard' : hard_string}
words_dict = {'easy' : easy_words, 'medium' : medium_words, 'hard' : hard_words}


def user_tries():
#Asks user whether they are happy with 5 tries
	print 'Are you happy with 5 tries?'
	tries_choice = ''
	while tries_choice != 'y' or 'n':
			
			tries_choice = raw_input ('Please enter y or n:')
			if tries_choice == 'y':
				print 'You have selected the standard 5 tries.'
				return 5
				
			elif tries_choice == 'n':
			#Gets user to input manual number of tries, ensures input is a positive integer
				custom_tries = raw_input('Please enter how many tries you would like:')
				while custom_tries.isdigit() != True:
					custom_tries = raw_input('Please enter an integer number')
				print 'You have selected', custom_tries , 'tries.'
				return int(custom_tries)
	

def user_difficulty():
#prompts user to select a difficulty from easy, medium or hard
	print '\nPlease select your difficulty, options are easy, medium or hard.'
	difficulty_choice = ''
	acceptable_difficulties = ['easy', 'medium', 'hard']
	
	while difficulty_choice not in acceptable_difficulties:
			difficulty_choice = raw_input ('Please enter easy, medium or hard: ')
			
			if difficulty_choice in acceptable_difficulties:
				print '\nYou have selected ', difficulty_choice, ' difficulty.'
				return difficulty_choice



def check_word(user_input,answer_list,position):
#Passes in word input by user, removes capitalisation and then checks if word is equal to active element in selected list
#If OK, returns word input, otherwise, returns None.
	user_compare = user_input.lower()
	answer_index = position - 1
	answer_compare = answer_list[answer_index]

	if user_compare == answer_compare:
		
		return True
	return None


def split_string(selected_string, maxsplit = 0):
# Passes in the selected string and splits along selected delimiters
	import re
	delimiters = '__',
	regexPattern = '|'.join(map(re.escape, delimiters))
	return re.split(regexPattern, selected_string, maxsplit)


def sub_words(split_string, selected_words, selected_string, tries_left):
#Main function:
#	Initialises with an empty, unsubstituted list
#	For every element of the selected answer list:
#
#		1. Joins current state of selected_list into a string, prints string,
#		2. Asks user for next word (starting at 0)
#		3. Calls check_word function
#		4. If word matches, (i.e. return not None) replaces all instances of active word placeholders in selected_list
#			with correct capitalisation
#		5. Joins the substituted list back into a string
#		6. Prints new substituted string, moves onto next word
#	If at any step the user input does not match the active element in the answer list:
#		1. Subtracts 1 from number of tries left
#		2. If resultant tries left > 0, goes back to the main loop
#		3. Else, prints 'game over' string asks user for raw input y/n if they want to start again
#				If y, calls difficulty function which resets the selected string, the number of tries left
#				and then re-initialises the list
#	
	
	
	#result_list = []

	for position, value in enumerate(selected_words,1):
		answer_position = 'word ' + str(position)
		
		printed_string = "".join(split_string)
		
		print "---------------------------------------------------------------\n\
The current paragraph reads:\n\n", printed_string
		
		user_input = raw_input('\n\nType in your answer for ' + answer_position + ': ')
		
		while check_word(user_input,selected_words,position) == None:
			print check_word(user_input,selected_words,position)
			if tries_left > 1:
				tries_left = tries_left -1
				print '\nPlease try again, you have', tries_left, 'tries left.'
				user_input = raw_input('\n\nType in your answer for ' + answer_position + ': ')
			else:
				print 'That was incorrect and you have no tries left, goodbye!'
				return None
		if check_word(user_input,selected_words,position) != None:
			'''
			result_list = [n.replace(answer_position, ) for n in split_string]
			for n in split_string:
				
				if n == answer_position:
					n = n.replace(answer_position, selected_words[0])
					result_list.append(n)
				else:
					result_list.append(n)
			print "".join(result_list)'''
			print '\nThat is correct!'
			


		



tries_left = user_tries()
user_difficulty = user_difficulty()

selected_string = string_dict[user_difficulty]
selected_words = words_dict[user_difficulty]
print selected_string

sub_words(split_string, selected_words,selected_string, tries_left)


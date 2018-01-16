
#Base text from wiki: https://en.wikipedia.org/wiki/Python_(programming_language)
#Retrieved 27 Sep 2017.

#For the easy quiz, the text is from the header, the replaced words have been defined as the values of easy_words below:

easy_words = ['programming', 'language', 'whitespace', 'readability']

easy_string = """
Python is a widely used high-level __word_1__ __word_2__ for general-purpose 
__word_1__, created by Guido van Rossum and first released in 1991. An 
interpreted __word_2__, Python has a design philosophy that emphasizes code 
__word_4__ (notably using __word_3__ indentation to delimit code blocks rather 
than curly brackets or keywords), and a syntax that allows programmers to 
express concepts in fewer lines of code than might be used in __word_1__s such 
as C++ or Java. The __word_2__ provides constructs intended to enable writing 
clear programs on both a small and large scale."""


#For the medium quiz, the text is from the History box:

medium_words = ['paradigm', 'garbage', 'Beautiful', 'implicit', 'Complicated']

medium_string = '''
Python is a multi-__word_1__ programming language: object-oriented programming 
and structured programming are fully supported, and many language features 
support functional programming and aspect-oriented programming (including by
metaprogramming and metaobjects (magic methods)). Many other __word_1__s are 
supported via extensions, including design by contract and logic programming.

Python uses dynamic typing and a mix of reference counting and a 
cycle-detecting __word_2__ collector for memory management. An important 
feature of Python is dynamic name resolution (late binding), which binds 
method and variable names during program execution.

The design of Python offers some support for functional programming in the 
Lisp tradition. The language has filter(), map(), and reduce() functions; list 
comprehensions, dictionaries, and sets; and generator expressions. The 
standard library has two modules (itertools and functools) that implement 
functional tools borrowed from Haskell and Standard ML.

The core philosophy of the language is summarized by the document The Zen of 
Python (PEP 20), which includes aphorisms such as:

    __word_3__ is better than ugly
    Explicit is better than __word_4__
    Simple is better than complex
    Complex is better than __word_5__
    Readability counts

'''

#For the hard quiz, the text is again from the History box:

hard_words = ['functionality', 'core', 'optimization', 'Cython', 'Monty Python', 'pythonic', 'unpythonic']

hard_string = '''
Rather than requiring all desired __word_1__ to be built into the language's 
__word_2__, Python was designed to be highly extensible. Python can also be 
embedded in existing applications that need a programmable interface. This 
design of a small core language with a large standard library and an easily 
extensible interpreter was intended by Van Rossum from the start because of 
his frustrations with ABC, which espoused the opposite mindset.

While offering choice in coding methodology, the Python philosophy rejects 
exuberant syntax, such as in Perl, in favor of a sparser, less-cluttered 
grammar. As Alex Martelli put it: "To describe something as clever is not 
considered a compliment in the Python culture." Python's philosophy rejects 
the Perl "there is more than one way to do it" approach to language design 
in favor of "there should be one - and preferably only one - obvious way to 
do it".

Python's developers strive to avoid premature __word_3__, and moreover, 
reject patches to non-critical parts of CPython that would offer a marginal 
increase in speed at the cost of clarity. When speed is important, a Python 
programmer can move time-critical functions to extension modules written in 
languages such as C, or try using PyPy, a just-in-time compiler. __word_4__ 
is also available, which translates a Python script into C and makes direct 
C-level API calls into the Python interpreter.

An important goal of Python's developers is making it fun to use. This is 
reflected in the origin of the name, which comes from __word_5__, and in an 
occasionally playful approach to tutorials and reference materials, such as 
using examples that refer to spam and eggs instead of the standard foo and bar.

A common neologism in the Python community is __word_6__, which can have a 
wide range of meanings related to program style. To say that code is 
__word_6__ is to say that it uses Python idioms well, that it is natural or 
shows fluency in the language, that it conforms with Python's minimalist 
philosophy and emphasis on readability. In contrast, code that is difficult 
to understand or reads like a rough transcription from another programming 
language is called __word_7__.

Users and admirers of Python, especially those considered knowledgeable or 
experienced, are often referred to as Pythonists, Pythonistas, and Pythoneers.

'''

string_dict = {'easy' : easy_string, 'medium' : medium_string, 'hard' : hard_string}
words_dict = {'easy' : easy_words, 'medium' : medium_words, 'hard' : hard_words}


def user_tries():
#Asks user whether they are happy with 5 tries
	print 'Are you happy with 5 tries?'
	tries_choice = ''
	default_tries = 5
	while tries_choice != 'y' or 'n':
			
			tries_choice = raw_input ('Please enter y or n:')
			if tries_choice == 'y':
				print 'You have selected the standard ', default_tries,' tries.'
				return default_tries
				
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



def check_word(user_input,answer_list,position, answer_position):
#
	'''
Inputs:
		1. user_input:	raw input by user, passed in from external function
		2. answer_list:	answer list used for quiz, has correct answers expected
		3. position:	active position in answer list, note this starts from 1 due to enumerate but list
						index starts from 0. Therefore, assigned with 1 subtracted to answer_index

Behaviour:
		Passes in word input by user, removes capitalisation and then checks if word is equal to active 
		element in selected list. If OK, returns word input, otherwise, returns None.

Outputs:
		True or None, if the user input matches the expected answer or not, respectively
'''	
	user_compare = user_input.lower()
	answer_index = position - 1
	answer_compare = answer_list[answer_index].lower()
	if user_compare == answer_compare:		
		return True
	return False
	'''
		print tries_left
		tries_left = tries_left -1
		if tries_left == 0:
			print 'That was incorrect and you have no tries left, goodbye!'
			return False
			
		print '\nPlease try again, you have', tries_left, 'tries left.'
		print tries_left
		user_input = raw_input('\n\nType in your answer for ' + answer_position + ': ')'''




def string_tosplit(selected_string, maxsplit = 0):
	'''
	Inputs:
		1.	selected_string:	active string used for quiz

	Behaviour:
		Passes in the selected string and splits along selected delimiters

	Outputs:
		1. split string (later assigned to split_string)

	'''
 
	import re
	delimiters = '__',
	regexPattern = '|'.join(map(re.escape, delimiters))
	return re.split(regexPattern, selected_string, maxsplit)

def check_tries(tries_left, answer_position, user_input):
	'''
	Inputs:
			1. tries_left:		number of tries left at active position in answer list
			2. answer_position:	current word count being checked against
			3. user_input:		raw input by user, passed in from external function

	Behaviour:
			Function only called if check_word gives None i.e. user makes a mistake. Function then checks number of
			tries left and if >1, subtracts 1. If the number of tries left is 1, triggers lose condition.
			If user gets correct input, moves on.
	Outputs:
			Nothing, or returns lose condition if no more tries left 
	'''
	'''	if tries_left > 1:
		tries_left = tries_left -1
		print '\nPlease try again, you have', tries_left, 'tries left.'
		user_input = raw_input('\n\nType in your answer for ' + answer_position + ': ')
	else:
		print 'That was incorrect and you have no tries left, goodbye!'
		return None
	'''

def run_replace(split_string,answer_position,selected_words,position, result_list):

	for elements in split_string:
		if elements == answer_position:
			elements = elements.replace(answer_position, selected_words[position-1])					
			result_list.append(elements)
		else:
			result_list.append(elements)
	return result_list


def sub_words(selected_words, selected_string, tries_left):
	'''
Inputs:
	1.	selected_words:		Answer list chosen for quiz
	2.	selected_string:	Answer string being tested against
	3.	tries_left:			Number of tries left (starting), also used as input to check_tries

Behaviour:
	Initialises with an empty, unsubstituted list
	For every element of the selected answer list:

		1. Joins current state of selected_list into a string, prints string,
		2. Asks user for next word (starting at 1)
		3. Calls check_word function
		4. If word matches, (i.e. return true) replaces all instances of active word placeholders in split_string
			with correct capitalisation
		5. Joins the substituted list back into a string
		6. Moves onto next word
	If at any step the user input does not match the active element in the answer list:
		1. Subtracts 1 from number of tries left
		2. If resultant tries left > 0, goes back to the main loop
		3. Else, prints 'game over' string asks user for raw input y/n if they want to start again
				If y, calls difficulty function which resets the selected string, the number of tries left
				and then re-initialises the list
		
		Prints final string
Outputs:
	1.	Printed string on every iteration
	2.	Counts tries left
	3.	Prints substituted (joined) string

	'''
	split_string = string_tosplit(selected_string)
	for position, value in enumerate(selected_words,1):
		result_list = []
		answer_position = 'word_' + str(position)
		
		print "---------------------------------------------------------------\nThe current string reads:\n\n", "".join(split_string)
		user_input = raw_input('\n\nPlease read the text above and then type in your answer for ' + answer_position + ': ')
		
		while check_word(user_input, selected_words, position, answer_position) == False:
			if tries_left > 1:
				tries_left = tries_left - 1
				print '\nPlease try again, you have', tries_left, 'tries left.'
				user_input = raw_input('\n\nType in your answer for ' + answer_position + ': ')
			else:
				print 'That was incorrect and you have no tries left, goodbye!'
				return None	
		result_list[:] = run_replace(split_string,answer_position,selected_words,position, result_list)				
		split_string[:] = result_list

		print '\nThat is correct!\n'
	print "---------------------------------------------------------------\nThe complete string reads:\n\n", "".join(split_string), '\n\n Well done!'


user_difficulty = user_difficulty()
tries_left = user_tries()

selected_string = string_dict[user_difficulty]
selected_words = words_dict[user_difficulty]


sub_words(selected_words,selected_string, tries_left)


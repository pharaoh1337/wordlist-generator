#!/usr/bin/python3.6

import sys
import os
import getopt

ver = 1.0
license = """ 
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
		http://www.apache.org/licenses/LICENSE-2.0
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License."""


def main(argv):
	wordlength = 0
	alphabets = []
	file_path = ''

	if len(sys.argv) == 1:
		help()

	try:
		opts, args = getopt.getopt(argv, "hl:L:a:A:f:F:", ["help", "version", "length=", "alphabets=", "file="])
	except getopt.GetoptError:
		print("Invalid arguments")
		print("Usage\n./wordlist_generator.py -l <length> -a <alphabets> -f <file>")
		sys.exit(2)

	for opt, arg in opts:
		if opt == '--help':
			help()
		if opt == '--version':
			version()
		elif opt in ('-a', '-A', '--alphabets'):
			alphabets = list(arg)
		elif opt in ('-f', '-F', '--file'):
			file_path = arg
		elif opt in ('-l', '-L', '--length'):
			wordlength = int(arg)

	try:
		file = open(file_path, 'w')
		RADIX = len(alphabets)
		MAX_WORDS = pow(RADIX, wordlength)
		print("This will generate", MAX_WORDS, "passwords")
		print("[", end='', flush=True)
		p = 1
		for n in range(0, MAX_WORDS):
			if p == int((1+n)/MAX_WORDS*10):
				print("==========", end='', flush=True)
				p += 1
			indices = convert_to_radix(RADIX, n, wordlength)
			word = ''
			for i in indices:
				word += (alphabets[i])
			file.write(word)
			file.write('\n')
		print(']')
	except Exception as e:
		print("can't open this file")
		os._exit(1)
	except (KeyboardInterrupt, SystemExit):
		os._exit(1)
	finally:
		file.close()


def convert_to_radix(radix, number, wordlength):
	for n in range(wordlength-1, -1, -1):
		if number > 0:
			rest = int(number % radix)
			number /= radix
			yield rest
		else:
			yield 0


def help():
	banner()
	print("Usage\n./wordlist_generator.py -l <length> -a <alphabets> -f <file>\n")
	print("Options\n")
	print("-a, -A, --alphabets   alphabets which your passwords will generate from")
	print("-f, -F, --file        file which will contain of your passwords")
	print("-l, -L, --length      length of your passwords")
	print("      --help display this help and exit")
	print("      --version output version information and exit\n")
	print("Note:")
	print(" recommended use absolute path for output file or\n relative path if you know what are you do")
	print(" i'm irresponsible if it use for illegal purpose\n")
	print("\033[1;38;5;1mWARRING:")
	print(" THIS SCRIPT RESOURCE INTENSIVE \n BE SURE YOUR MACHINE HAVE GOOD AIRCONDITION AND AVAILABLE STORAGE " \
		"IN YOUR HARD DISK \033[0m\n")
	print("Exit status:")
	print(" 0  if OK,\n 1  if minor problems (e.g., cannot access subdirectory),\n" \
		" 2  if serious trouble (e.g., cannot access command-line argument).")
	sys.exit(0)


def version():
	print("wordlist generator " + str(ver) + " \nCopyright (C) 2017 Pharaoh." + license +"\nWritten by Pharaoh")
	sys.exit(0)

def banner():
	author = """
		 _____  _                           _
		|  __ \| |                         | |    
		| |__) | |__   __ _ _ __ __ _  ___ | |__  
		|  ___/| '_ \ / _` | '__/ _` |/ _ \| '_ \ 
		| |    | | | | (_| | | | (_| | (_) | | | |
		|_|    |_| |_|\__,_|_|  \__,_|\___/|_| |_|

	"""
	print(author)

if __name__ == "__main__":
	main(sys.argv[1:])

Simple python script for password list generation

WHAT IS THIS ?


This is a python script for generating password-lists for bruteforce and dictionnary attacks It is best used for default passwords as they tend to follow a strict pattern and people tend to be too lazy to change them

HOW TO USE :

open commandprompt enter:
  python passwordlist.py letterset number_of_const_strings filename parsestring [ const strings depending on number_of_const_strings]

letterset:

  fixed set of characters for bruteforce used by "q" in parsestring

number_of_const_strings:

  say password has constant substring you can create upto 9 such const substrings used by "0" "1" "2" ... in parse string

filename :

  enter name of text file to be save DONT SAVE AS FILENAME.txt eg test -> test.txt

parsestring :

  Enter string from which list is to be generated -I integer from 0-9 -a lowerclass letters a-z -A CapitalLetters A-Z -S special characters -q letterset set -[0-9] const string to be used -W (a-z) & (A-Z) EXAMPLE : Fall@6723!!! ,Fall@1892!!! ,Fall@2133!!! ... code :python _____.py - 1 passlist 0IIII1 Fall@ !!! output file named passlist.txt with list of passwords

passwordlist.py name of file in git forgot to see before hand


EXAMPLE:
  password be like Fall@1231!!! Fall@1232!!! Fall@9212!!!
  
  command :
    python passwordlist.py - 2 passlist 0IIII1 Fall@ !!!

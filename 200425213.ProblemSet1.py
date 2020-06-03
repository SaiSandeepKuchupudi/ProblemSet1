{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "1. What data type is each of the following?\n",
    "5 - INTEGER\n",
    "5.0 - FLOAT\n",
    "5>1 - BOOLEAN\n",
    "'5' - STRING\n",
    "5*2 - LONG\n",
    "'5'*2 - \n",
    "'5'+'2'- \n",
    "5/2 - \n",
    "5//2 - \n",
    "[5,2,1] - LIST\n",
    "5 in [1,4,6] - \n",
    "math.pi - "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number of letters in the strings are: 34\n"
     ]
    }
   ],
   "source": [
    "2. Write (and evaluate) Python expressions that answer these questions: \n",
    "a.How many letters are there in 'Supercalifragilisticexpialidocious'?\n",
    "b.Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? \n",
    "c.Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus,  \n",
    "  or Bababadalgharaghtakamminarronnkonn? \n",
    "d.Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'.\n",
    "Which one comes last?\n",
    "\n",
    "# Solution (a):\n",
    "\n",
    "str_super = 'Supercalifragilisticexpialidocious'\n",
    "count = int(len(str_super))\n",
    "print('The number of letters in the strings are: {}'.format(count))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Does string contains \"ice\": True\n"
     ]
    }
   ],
   "source": [
    "# Solution (b): \n",
    "\n",
    "find = bool(\"ice\" in str_super)\n",
    "print('Does string contains \"ice\": {}'.format(find))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "longest string is: Supercalifragilisticexpialidocious\n"
     ]
    }
   ],
   "source": [
    "# SOlution (c): \n",
    "\n",
    "str_honor = \"Honorificabilitudinitatibus\"\n",
    "str_baba = \"Bababadalgharaghtakamminarronnkon\"\n",
    "count = str(max(str_super,str_honor, str_baba))\n",
    "print('longest string is: {}'.format(count))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First composer in the dictionary is: Bartok \n",
      "Last composer in the dictionary is: Buxtehude\n"
     ]
    }
   ],
   "source": [
    "# Solution (d):\n",
    "\n",
    "Composers = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']\n",
    "Composers.sort()\n",
    "First_composer = str(Composers[0])\n",
    "Last_composer = str(Composers[-1])\n",
    "print('First composer in the dictionary is: {} '.format(First_composer))\n",
    "print('Last composer in the dictionary is: {}'.format(Last_composer))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "3.(a). Write a function inside(x,y,x1,y1,x2,y2) that returns True or False\n",
    "depending on whether the point (x,y) lies in the rectangle with lower left\n",
    "corner (x1,y1) and upper right corner (x2,y2).\n",
    ">>> inside(1,1,0,0,2,3)\n",
    "True\n",
    ">>> inside(-1,-1,0,0,2,3)\n",
    "False\n",
    "\n",
    "# Solution (a):\n",
    ">>>\n",
    "Enter x1: 1\n",
    "Enter y1: 1\n",
    "Enter x2: 0\n",
    "Enter y2: 0\n",
    "Enter x: 2\n",
    "Enter y: 3\n",
    "True\n",
    "\n",
    "Enter x1: -1\n",
    "Enter y1: -1\n",
    "Enter x2: 0\n",
    "Enter y2: 0\n",
    "Enter x: 2\n",
    "Enter y: 3\n",
    "False\"\"\"\n",
    "\n",
    "x1 = (input(\"Enter x1: \"))\n",
    "y1 = (input(\"Enter y1: \"))\n",
    "x2 = (input(\"Enter x2: \"))\n",
    "y2 = (input(\"Enter y2: \"))\n",
    "x = (input(\"Enter x: \"))\n",
    "y = (input(\"Enter y:\"))\n",
    "if (x >= x1 and x< = x2) and (y >= y1 and y <= y2):\n",
    "    print(True)\n",
    "else:\n",
    "    print(False)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "3.(b). Use function inside() from part a. to write an expression that tests whether\n",
    "the point (1,1) lies in both of the following rectangles: one with lower left\n",
    "corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower\n",
    "left corner (0.5, 0.2) and upper right corner (1.1, 2). \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "4. You can turn a word into pig-Latin using the following two rules (simplified):\n",
    "• If the word starts with a consonant, move that letter to the end and append\n",
    "'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.\n",
    "• If the word starts with a vowel, simply append 'way' to the end of the word.\n",
    "For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For\n",
    "our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).\n",
    "Write a function pig() that takes a word (i.e., a string) as input and returns its pigLatin form. Your function should still work if the input word contains upper case\n",
    "characters. Your output should always be lower case however.\n",
    ">>> pig('happy')\n",
    "'appyhay\n",
    "\n",
    "## solution:\n",
    "pyg = 'ay'\n",
    "#display 'Enter a word..' then take the input and set as original\n",
    "original = raw_input('Enter any word...')\n",
    "#word  = original lower case\n",
    "word = original.lower()\n",
    "#first = 1st letter of word\n",
    "first = word[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "5.File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic.\n",
    "Write a function bldcount() that reads the file with name name and reports (i.e.,\n",
    "prints) how many patients there are in each bloodtype.\n",
    ">>> bldcount('bloodtype.txt')\n",
    "There are 10 patients of blood type A.\n",
    "There is one patient of blood type B.\n",
    "There are 10 patients of blood type AB.\n",
    "There are 12 patients of blood type O.\n",
    "There are no patients of blood type OO.\n",
    "\n",
    "## solution\n",
    "\n",
    "def bldcount(filename):\n",
    "    file=open(filename, 'r')\n",
    "    bloodGroup=(file.read()).split()\n",
    "    file.close()\n",
    "    a,b,aB,o,oO=0,0,0,0,0\n",
    "    for word in bloodGroup:\n",
    "        if word=='A':\n",
    "            a+=1\n",
    "        elif word=='B':\n",
    "            b+=1\n",
    "        elif word=='AB':\n",
    "            aB+=1\n",
    "        elif word=='O':\n",
    "            o+=1\n",
    "        else:\n",
    "            oO+=1\n",
    "    \n",
    "    print('There are '+str(a)+' patients of blood type A')\n",
    "    print('There are '+str(b)+' patients of blood type B')\n",
    "    print('There are '+str(aB)+' patients of blood type AB')\n",
    "    print('There are '+str(o)+' patients of blood type O')\n",
    "    print('There are '+str(oO)+' patients of blood type OO')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "6. Write a function curconv() that takes as input:\n",
    "1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or\n",
    "'EUR' for the Euro)\n",
    "2. an amount\n",
    "and then converts and returns the amount in US dollars.\n",
    ">>> curconv('EUR', 100)\n",
    "122.96544\n",
    ">>> curconv('JPY', 100)\n",
    "1.241401\n",
    "\n",
    "def curcon(currency, amount):\n",
    "    file = open(\"D:/Sandeep/DataProgramming//currencies.txt\", \"r\")\n",
    "    content = file.readlines()\n",
    "    for line in content:\n",
    "        if currency in line:      \n",
    "            conversion = line.split()[1]    \n",
    "            convertedAmt = float(conversion)*amount\n",
    "            return convertedAmt\n",
    "       \n",
    "amount = float(input(\"Enter the amount to want to convert: \"))\n",
    "currency = input(\"Enter the currency you want to convert to USD: \")\n",
    "print(curcon(currency, amount))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "7. Each of the following will cause an exception (an error). Identify what type of\n",
    "exception each will cause.\n",
    "\n",
    "A. Trying to add incompatible variables, as in\n",
    "adding 6 + ‘a’\n",
    " ##TypeError is thrown when an operation is applied to an object of an inappropriate type.\n",
    "    \n",
    "B.Using a value that is out of range for a function’s\n",
    "input, such as calling math.sqrt(-1.0)\n",
    "\n",
    "## ValueError is thrown when a function's argument is of an inappropriate type.\n",
    "\n",
    "c. Using an undeclared variable, such as print(x)\n",
    "when x has not been defined \n",
    "## NameError is thrown when an object could not be found.\n",
    "\n",
    "D. Trying to open a file that does not exist, such as\n",
    "mistyping the file name or looking in the wrong\n",
    "directory. \n",
    "\n",
    "## file = open(\"DoesNotExist.txt\")\n",
    "print(file.Readlines())\n",
    "# This Error is trown when file does not exist in the content.\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "8. Encryption is the process of hiding the meaning of a text by substituting letters in the\n",
    "message with other letters, according to some system. If the process is successful, no\n",
    "one but the intended recipient can understand the encrypted message. Cryptanalysis\n",
    "refers to attempts to undo the encryption, even if some details of the encryption are\n",
    "unknown (for example, if an encrypted message has been intercepted). The first step\n",
    "of cryptanalysis is often to build up a table of letter frequencies in the encrypted text.\n",
    "Assume that the string letters is already defined as\n",
    "'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies()\n",
    "that takes a string as its only parameter, and returns a list of integers, showing the\n",
    "number of times each character appears in the text. Your function may ignore any\n",
    "characters that are not in letters.\n",
    ">>> frequencies('The quick red fox got bored and went home.')\n",
    "[1, 1, 1, 3, 5, 1, 1, 2, 1, 0, 1, 0, 1, 2, 4, 0, 1, 2, 0, 2,\n",
    "1, 0, 1, 1, 0, 0]\n",
    ">>> frequencies('apple')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "9. The Sieve of Erastophenes is an algorithm -- known to ancient Greeks -- that finds\n",
    "all prime numbers up to a given number n. It does this by first creating a list L from\n",
    "2 to n and an (initially empty) list primeL. The algorithm then takes the first number\n",
    "in list L (2) and appends it to list primeL, and then removes 2 and all its multiples\n",
    "(4,6,8,10,12, ...) from L. The algorithm then takes the new first number in L (3) and\n",
    "appends it to list primeL, and then removes from L 3 and all its remaining multiples\n",
    "(9,15,21,...). So, in every iteration, the first number of list L is appended to list\n",
    "primeL and then it and its multiples are removed from list L. The iterations stop\n",
    "when list L becomes empty. Write a function sieve() that takes as input a positive\n",
    "integer n, implements the above algorithm, and returns a list of all prime numbers up\n",
    "to n.\n",
    ">>> sieve(56)\n",
    "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,\n",
    "43, 47, 53]\n",
    ">>> sieve(368)\n",
    "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,\n",
    "43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,\n",
    "101, 103, 107, 109, 113, 127, 131, 137, 139, 149,\n",
    "151, 157, 163, 167, 173, 179, 181, 191, 193, 197,\n",
    "199, 211, 223, 227, 229, 233, 239, 241, 251, 257,\n",
    "263, 269, 271, 277, 281, 283, 293, 307, 311, 313,\n",
    "317, 331, 337, 347, 349, 353, 359, 367]\n",
    ">>> sieve(32)\n",
    "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "10. Implement function triangleArea(a,b,c) that takes as input the lengths of the 3\n",
    "sides of a triangle and returns the area of the triangle. By Heron's formula, the area\n",
    "of a triangle with side lengths a, b, and c is\n",
    "s(s - a)(s -b)(s -c)\n",
    ", where\n",
    "s = (a+b+c)/2.\n",
    ">>> triangleArea(2,2,2)\n",
    "1.7320508075688772\n",
    "\n",
    "\n",
    "import math\n",
    "def triangleArea(a, b, c):\n",
    "    s = (a+b+c)//2\n",
    "    return math.sqrt(s*(s-a)*(s-b)*(s-c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

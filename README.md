Some letters may have more than one translation, and others may have no translation. 
By repeatedly applying some of these translations to individual letters in the gibberish documents, she might be able to decipher them.
You are given the possible translations of letters and a list of pairs of original and deciphered words. 
Your task is to verify whether the words in each pair match. 
Two words match if they have the same length and if each letter of the first word can be turned into the corresponding letter of the second word 
by using the available translations zero or more times. 
Check the attached document for a hint on input and output values with a sample provided on both.

Initial data:
The first line of input contains two integers m (1 ≤ m ≤ 500) and n (1 ≤ n ≤ 50), where m is the number of translations of letters and n is the number of word pairs.
Each of the next m lines contains two distinct space-separated letters a and b, indicating that the letter a can be translated to the letter b. 
Each ordered pair of letters (a, b) appears at most once. Following this are n lines, each containing a word pair to check. 
Translations and words use only lowercase letters ‘a’–‘z’, and each word contains at least 1 and at most 50 letters.
Result:
For each pair of words, display yes if the two words match, and no otherwise.

Test 1
input
3 3 
a c 
b a 
a b 
aaa abc
abc aaa
acm bcm

output
yes 
no 
yes

Test 2
input
9 5 
c t 
i r 
k p 
o c 
r o 
t e 
t f 
u h 
w p 
we we 
can the 
work people 
it of 
out the

output
yes 
no 
no 
yes 
yes

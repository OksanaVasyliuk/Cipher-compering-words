from itertools import permutations

with open("tasks.txt") as file:
    lines = file.read()
result = list(lines)

def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

result[:] = [''.join(result[:])]
string = "".join(result)
list_of_elements = string.split("\n")

# extracting numbers that signifies m line and n line
n_line = int(list_of_elements[0][0])
m_line = int(list_of_elements[0][2])

smth = []
for element in list_of_elements:
    one = element.strip()
    smth.append(one)

# getting separate lists with letters and words
translation_rules = smth[1:(n_line + 1)]
word_pairs = smth[(n_line + 1):-1]

# separating lists with original letters
# and their corresponding meaning within translation rules
orr_letter = []
corr_letter = []
for element in translation_rules:
    orr_letter.append(element[0])
    corr_letter.append(element[2])

pairs = []
for pair in word_pairs:
    line = pair.split()
    pairs.append(line)

for line in pairs:
    # if length of words do not match - result "no"
    if len(line[0]) != len(line[1]):
        print("no")
    else:
        possible_letters = []
        poss_comb = []
        for letter in line[0]:
            # creating lists of all possible letters from first word
            # if letter is not mentioned in translation rules, we add this letter as it is in list possible_letters
            possible_letters.append(letter)
            # if letter from first word is in translation list -
            # we find it's all indexes and add to possible_letters its translaton counterparts
            #  eg, "we" --> ['w', 'p', 'p', 'e', 'p']; "can" --> ['c', 't', 't', 'e', 'f', 'e', 'f', 'a', 't', 'e', 'f', 'e', 'f', 'e', 'f', 'n', 't', 'e', 'f', 'e', 'f', 'e', 'f', 'e', 'f']
            if letter in orr_letter:
                index = indices(orr_letter, letter)
                for i in index:
                    possible_letters.append(corr_letter[i])
            for p_let in possible_letters:
                if p_let in orr_letter:
                    index = indices(orr_letter, p_let)
                    for i in index:
                        possible_letters.append(corr_letter[i])
            # with list of all possible letters we create all possible variations with length of the second word add to list poss_comb
            # eg. ['w', 'p', 'p', 'e', 'p'] --> ['wp', 'wp', 'pw', 'pp', 'pw', 'pp', 'wp', 'wp', 'we', 'wp', 'pw', 'pp', 'pe', 'pp', 'pw', 'pp', 'pe', 'pp', 'ew', 'ep', 'ep', 'ep', 'pw', 'pp', 'pp', 'pe']
            pos = permutations(possible_letters, len(line[1]))
            for i in pos:
                combination = "".join(i)
                poss_comb.append(combination)
        # we check if second word exists in lit of possible combinations of letters received from first word
        # eg from letters "['c', 't', 't', 'e', 'f', 'e', 'f', 'a', 't', 'e', 'f', 'e', 'f', 'e', 'f', 'n', 't', 'e', 'f', 'e', 'f', 'e', 'f', 'e', 'f']" we can't create word "the", answer is "no"
        if line[1] in poss_comb:
            print("yes")
        else:
            print("no")

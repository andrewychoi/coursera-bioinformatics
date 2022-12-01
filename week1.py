"""
Where in the genome does replication begin? Lesson 1
"""


def PatternCount(Text, Pattern):
    # fill in your function here
    count = 0
    for i in range(0, len(Text) - len(Pattern) + 1):
        if Pattern == Text[i:i + len(Pattern)]:
            count += 1
    return count

# =================================

# Copy your PatternCount function from the previous step below this line


def PatternCount(Text, Pattern):
    # fill in your function here
    count = 0
    for i in range(0, len(Text) - len(Pattern) + 1):
        if Pattern == Text[i:i + len(Pattern)]:
            count += 1
    return count


# Now, set Text equal to the ori of Vibrio cholerae and Pattern equal to "TGATCA"
ori = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

pattern = "TGATCA"

# Finally, print the result of calling PatternCount on Text and Pattern.
# Don't forget to use the notation print() with parentheses included!

print(PatternCount(ori, pattern))

# =================================

# Insert your completed FrequencyMap() function here.


def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0
    for i in range(n - k + 1):
        freq[Text[i:i + k]] += 1
    return freq
# =================================

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text


def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
        # add each key to words whose corresponding frequency value is equal to m
    return words


# Copy your FrequencyMap() function here.
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0
    for i in range(n - k + 1):
        freq[Text[i:i + k]] += 1
    return freq


# =================================
# Copy your updated FrequentWords function (along with all required subroutines) below this line

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
        # add each key to words whose corresponding frequency value is equal to m
    return words

# Copy your FrequencyMap() function here.


def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0
    for i in range(n - k + 1):
        freq[Text[i:i + k]] += 1
    return freq
# Now set Text equal to the Vibrio cholerae oriC and k equal to 10


Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k = 10

print(FrequentWords(Text, k))

# Finally, print the result of calling FrequentWords on Text and k.

# =================================

# Input:  A string Pattern
# Output: The reverse of Pattern


def Reverse(Pattern):
    return Pattern[::-1]

# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).


def Complement(Pattern):
    replace = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([replace[i] for i in Pattern])

# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern


def ReverseComplement(Pattern):
    return Reverse(Complement(Pattern))

# fill in your PatternMatching() function along with any subroutines that you need.


def PatternMatching(Pattern, Genome):
    positions = []  # output variable
    for i in range(len(Genome) - len(Pattern) + 1):
        if Pattern == Genome[i:i + len(Pattern)]:
            positions.append(i)
    # your code here
    return positions

# Copy your PatternMatching function below this line.


def PatternMatching(Pattern, Genome):
    positions = []  # output variable
    for i in range(len(Genome) - len(Pattern) + 1):
        if Pattern == Genome[i:i + len(Pattern)]:
            positions.append(i)
    # your code here
    return positions


# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
positions = PatternMatching("CTTGATCAT", v_cholerae)


# print the positions variable
print(positions)

# Copy your PatternCount function below here


def PatternMatching(Pattern, Genome):
    positions = []  # output variable
    for i in range(len(Genome) - len(Pattern) + 1):
        if Pattern == Genome[i:i + len(Pattern)]:
            positions.append(i)
    # your code here
    return positions


# On the following line, create a variable called Text that is equal to the oriC region from T petrophila
Text = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"

# On the following line, create a variable called count_1 that is equal to the number of times
# that "ATGATCAAG" occurs in Text.
count_1 = len(PatternMatching("ATGATCAAG", Text))

# On the following line, create a variable called count_2 that is equal to the number of times
# that "CTTGATCAT" occurs in Text.
count_2 = len(PatternMatching("CTTGATCAT", Text))

# Finally, print the sum of count_1 and count_2
print(count_1 + count_2)

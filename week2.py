
# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    # type your code here
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n // 2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i + (n // 2)])
    return array

# Reproduce the PatternCount function here.


def PatternCount(Pattern, Text):
    count = 0
    for i in range(0, len(Text) - len(Pattern) + 1):
        if Pattern == Text[i:i + len(Pattern)]:
            count += 1
    return count

# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n // 2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n // 2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i - 1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i - 1] == symbol:
            array[i] = array[i] - 1
        if ExtendedGenome[i + (n // 2) - 1] == symbol:
            array[i] = array[i] + 1
    return array

# Input:  Strings Text and Pattern
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount


def PatternCount(Pattern, Text):
    count = 0  # output variable
    for i in range(0, len(Text) - len(Pattern) + 1):
        if Pattern == Text[i:i + len(Pattern)]:
            count += 1
    return count


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
# lines = sys.stdin.read().splitlines()
# print(FasterSymbolArray(lines[0], lines[1]))

# ====================

# Input:  A String Genome
# Output: The skew array of Genome as a list.


def SkewArray(Genome):
    counter = 0
    return_list = [0]
    for i in Genome:
        if i == "G":
            counter += 1
            return_list.append(counter)
        elif i == "C":
            counter -= 1
            return_list.append(counter)
        else:
            return_list.append(counter)
    return return_list


# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = []  # output variable
    skew_array = SkewArray(Genome)
    min_skew = min(skew_array.values())
    for k, v in skew_array.items():
        if v == min_skew:
            positions.append(k)
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.


def SkewArray(Genome):
    counter = 0
    skew = {0: 0}
    for i, base in enumerate(Genome):
        if base == "G":
            counter += 1
            skew[i + 1] = counter
        elif base == "C":
            counter -= 1
            skew[i + 1] = counter
        else:
            skew[i + 1] = counter
    return skew

# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.


def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches


def ApproximatePatternMatching(Text, Pattern, d):
    positions = []  # initializing list of positions
    for i in range(0, len(Text) - len(Pattern) + 1):
        distance = HammingDistance(Text[i:i + len(Pattern)], Pattern)
        if distance <= d:
            positions.append(i)
    return positions


# Insert your Hamming distance function on the following line.
def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance

# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches


def ApproximatePatternCount(Pattern, Text, d):

    positions = []  # initializing list of positions
    for i in range(0, len(Text) - len(Pattern) + 1):
        distance = HammingDistance(Text[i:i + len(Pattern)], Pattern)
        if distance <= d:
            positions.append(i)
    return len(positions)


def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
# lines = sys.stdin.read().splitlines()
# print(ApproximatePatternCount(lines[0], lines[1], int(lines[2])))

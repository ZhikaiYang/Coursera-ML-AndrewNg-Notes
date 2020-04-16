def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d


alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def has_duplicates(s):

    count = dict()
    count = histogram(s)
    for ss in s:
        if count[ss] > 1:
            return True
        else:
            result = False

    return result



for element in test_dups:
    if has_duplicates(element):
        print(element, " has duplicates")

    else:
        print(element, "has no duplicates")



def missing_letters(s):
    count = dict()
    count = histogram(s)
    t = list()
    i = 0
    global alphabet
    for letter in alphabet:
        if not(letter in s):
            t.append(i)

        i = i +1
    return t

miss = ""
for element in test_miss:
    if len(missing_letters(element)) > 0:
        for l in missing_letters(element):
            miss = miss + alphabet[l]
        print(element, "is missing letters ", miss)
    else:
        print(element, "uses all the letters")

    miss = ""

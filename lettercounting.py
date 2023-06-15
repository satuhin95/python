import pprint as pp
text = 'Comillla Victoria Govt College'

letter = {}

for i in text:
    letter.setdefault(i,0)
    letter[i] = letter[i]+1

pp.pprint(letter)
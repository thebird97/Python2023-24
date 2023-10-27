alphabet = "abcdefghijklmnopqrstuvwxyz"
#del alphabet[0]
#alphabet.append("A")
#alphabet.insert(0, "A")

# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))
# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')
t = [0, 1, 2]
print(min(t))

# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))
# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')
t = [0, 1, 2]
print(max(t))


# Demonstrating the list() function:
print(list("abcabc"))


# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))


# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
# Demonstrating the list() function:
print(list("abcabc"))
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))
# Demonstrating the capitalize() method:
print('aBcD'.capitalize())
# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s
or earlier, when it was popularized by advertisements
for Letraset transfer sheets. It was introduced to
the Information Age in the mid-1980s by the Aldus Corporation,
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
"""
while fnd != -1:
    print(fnd)
    find = the_text.find('the', fnd + 1)
    
"""

print('alpha' == 'alpha')
print('alpha' != 'Alpha')
print('alpha' < 'alphabet')
print('beta' > 'Beta')


# Demonstrating the sorted() function:
print('sorted')
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)
print()
# Demonstrating the sort() method:

print('sort')
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
second_greek.sort()
print(second_greek)

for ch in "abc":
    print(chr(ord(ch) + 1), end='')
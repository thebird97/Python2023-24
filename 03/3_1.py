#n = int(input("szam "))
#print(n>=100)


n = 3

while n > 0:
    print(n +1)
    n-= 1
else:
    print(n)
print("---------")
n = range(4)
for num in n:
    print(num-1)
else :
    print(num)

print("---------")
#del num
#print(num)


print("---------")

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle! |
| Enter an integer number |
| and guess what number I've |
| picked for you. |
| So, what is the secret number? |
+================================+
""")

#guess game
print("😀😀")

word = "hello"
vowels = "aeiou"
result = ""

for ch in word:
    if ch not in vowels:
        #print(ch.upper())
        result += ch.upper()
        #result.append(str(ch.upper()))

print(str(result))





def collatz(number):
    while number != 1:
        print(number)
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    print(number)

# Get user input
number = int(input("Enter a number: "))

# Call the function with the input
collatz(number)
